"""從 Chrome 的 Local Storage leveldb 讀出 threads.com 的 __lus_* 值（純 Python：sstable + log + snappy）。"""
import json, struct, sys
from pathlib import Path

def varint(b, i):
    r = s = 0
    while True:
        c = b[i]; i += 1
        r |= (c & 0x7F) << s; s += 7
        if c < 0x80: return r, i

def snappy(b):
    n, i = varint(b, 0); out = bytearray()
    while i < len(b):
        t = b[i]; k = t & 3; i += 1
        if k == 0:
            ln = t >> 2
            if ln >= 60:
                nb = ln - 59; ln = int.from_bytes(b[i:i+nb], 'little'); i += nb
            ln += 1; out += b[i:i+ln]; i += ln; continue
        if k == 1:
            ln = ((t >> 2) & 7) + 4; off = ((t >> 5) << 8) | b[i]; i += 1
        elif k == 2:
            ln = (t >> 2) + 1; off = int.from_bytes(b[i:i+2], 'little'); i += 2
        else:
            ln = (t >> 2) + 1; off = int.from_bytes(b[i:i+4], 'little'); i += 4
        for _ in range(ln): out.append(out[-off])
    assert len(out) == n
    return bytes(out)

def block_entries(blk):
    nr = struct.unpack('<I', blk[-4:])[0]; end = len(blk) - 4 - 4 * nr
    i = 0; key = b''
    while i < end:
        sh, i = varint(blk, i); ns, i = varint(blk, i); vl, i = varint(blk, i)
        key = key[:sh] + blk[i:i+ns]; i += ns
        yield key, blk[i:i+vl]; i += vl

def read_block(data, off, size):
    raw = data[off:off+size]; typ = data[off+size]
    return snappy(raw) if typ == 1 else raw

def sst(path):
    d = path.read_bytes(); f = d[-48:]
    _, i = varint(f, 0); _, i = varint(f, i)
    io, i = varint(f, i); isz, i = varint(f, i)
    for _, h in block_entries(read_block(d, io, isz)):
        o, j = varint(h, 0); s, j = varint(h, j)
        for k, v in block_entries(read_block(d, o, s)):
            tag = int.from_bytes(k[-8:], 'little')
            yield k[:-8], tag >> 8, tag & 0xFF, v

def logf(path):
    d = path.read_bytes(); recs = []; buf = b''; pos = 0
    while pos + 7 <= len(d):
        blk_left = 32768 - pos % 32768
        if blk_left < 7: pos += blk_left; continue
        ln, typ = struct.unpack('<HB', d[pos+4:pos+7]); pay = d[pos+7:pos+7+ln]; pos += 7 + ln
        if typ == 0 and ln == 0: continue
        if typ == 1: recs.append(pay)
        elif typ == 2: buf = pay
        elif typ == 3: buf += pay
        elif typ == 4: recs.append(buf + pay); buf = b''
    for r in recs:
        seq = int.from_bytes(r[:8], 'little'); cnt = struct.unpack('<I', r[8:12])[0]; i = 12
        for n in range(cnt):
            t = r[i]; i += 1
            kl, i = varint(r, i); k = r[i:i+kl]; i += kl
            if t == 1:
                vl, i = varint(r, i); v = r[i:i+vl]; i += vl
            else:
                v = None
            yield k, seq + n, t, v

def decode(v):
    return v[1:].decode('utf-16-le') if v[0] == 0 else v[1:].decode('latin-1')

def main(src, out):
    best = {}
    for p in Path(src).iterdir():
        it = sst(p) if p.suffix == '.ldb' else (logf(p) if p.suffix == '.log' else ())
        try:
            for k, seq, t, v in it:
                if b'threads.com' in k and b'__lus' in k:
                    if k not in best or seq > best[k][0]: best[k] = (seq, t, v)
        except Exception as e:
            print('skip', p.name, e)
    Path(out).mkdir(parents=True, exist_ok=True)
    for k, (seq, t, v) in best.items():
        name = k.split(b'__lus')[-1].decode('latin-1')
        if t != 1 or v is None: print(name, 'deleted'); continue
        obj = json.loads(decode(v))
        (Path(out) / f'{name}.json').write_text(json.dumps(obj, ensure_ascii=False), encoding='utf-8')
        print(name, 'seq', seq, len(obj['rows'].split('\n')) if 'rows' in obj else len(obj))

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
