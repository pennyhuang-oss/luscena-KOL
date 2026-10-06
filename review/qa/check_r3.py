import re, os, sys
R = sys.argv[1]
P = os.path.join(R, 'persona_pack_v1')
def rd(f): return open(os.path.join(P, f), encoding='utf-8').read()
L = {f'L{i:02d}': rd(f'L{i:02d}.md') for i in range(1, 11)}
def body(s):  # sections before §11 change log
    i = s.find('## 11.'); return s if i < 0 else s[:i]
ov, ch, pr, se = rd('00_OVERVIEW.md'), rd('PENNY_CHOICES.md'), rd('PRODUCER_REFERENCE_NEEDS.md'), rd('SHARED_EVENTS.md')
out = []
# 1 SE cross-reference
se_ids = sorted(set(re.findall(r'^### (SE-\d\d)', se, re.M)))
tbl = sorted(set(re.findall(r'^\| (SE-\d\d) \|', se, re.M)))
out.append(f'[SE] defined steps={len(se_ids)} table rows={len(tbl)} match={se_ids==tbl}')
part = {}
for row in re.findall(r'^\| (SE-\d\d) \|[^|]*\|([^|]*)\|([^|]*)\|', se, re.M):
    part[row[0]] = set(re.findall(r'L\d\d', row[1] + row[2]))
used = {}
for lid, s in L.items():
    for sid in set(re.findall(r'SE-\d\d', s)):
        used.setdefault(sid, set()).add(lid)
for f in ('00_OVERVIEW.md', 'PENNY_CHOICES.md'):
    for sid in set(re.findall(r'SE-\d\d', rd(f))): pass
undefined = sorted(set(used) - set(se_ids))
out.append(f'[SE] referenced in Lxx but undefined: {undefined or "none"}')
for sid in se_ids:
    miss = sorted(part.get(sid, set()) - used.get(sid, set()))
    out.append(f'[SE] {sid} participants={sorted(part.get(sid,set()))} referenced_in={sorted(used.get(sid,set()))} missing_ref={miss or "none"}')
# 2 W numbers near SE tags on the same line: candidate matches only, judged by hand.
# The regex stops at ｜ or |, allows 40 (W→SE) / 10 (SE→W) chars, and can pair an
# unrelated W with a later SE, so it neither finds every case nor proves a dependency.
cand, cand_lines = 0, set()
for lid, s in L.items():
    for no, ln in enumerate(body(s).split('\n'), 1):
        if 'SE-' in ln:
            for m in re.finditer(r'(W\d+)[^｜|]{0,40}SE-\d\d|SE-\d\d[^｜|]{0,10}(W\d+)', ln):
                cand += 1; cand_lines.add((lid, no))
                out.append(f'[W+SE] {lid} line {no}: match="{m.group(0)[:60]}"')
out.append(f'[W+SE] candidate matches={cand} distinct source lines={len(cand_lines)} (manual judgement required)')
# 3 leftover phrases (body only)
bad = ['最貼客戶', '不同縣市', '先用尺度 1 做候選', 'VISUAL_BRIEF', '矩陣', '視覺規格', '弱光', '兩邊差多少', '莊家', '賭一句', '我的心痛是真的', '真實流程', '懂球的女生本來就稀有', '太常見', '押哪', '一律標 AI', '全部 AI 生成', '卡關點：一直在等', '同團隊互相留言為什麼不算刷留言', '表演日的真實時間表']
for name, s in list(L.items()) + [('00_OVERVIEW', ov), ('PENNY_CHOICES', ch), ('PRODUCER', pr), ('SHARED_EVENTS', se)]:
    b = body(s) if name.startswith('L') else s
    for w in bad:
        for m in re.finditer(re.escape(w), b):
            ln = b[b.rfind('\n', 0, m.start())+1:b.find('\n', m.end())]
            out.append(f'[LEFTOVER] {name} "{w}": {ln.strip()[:140]}')
# 4 one-liner consistency
for lid, s in L.items():
    m = re.search(r'^\| 一句話定位 \| (.+?) \|$', s, re.M)
    one = m.group(1)
    row = [l for l in ov.split('\n') if l.startswith(f'| {lid} |')][0]
    if lid == 'L08':
        parts = [p.replace('**', '').split('：', 1)[1] for p in one.split('<br>')]
        ok = all(p in row for p in parts)
    else:
        ok = one in row
    out.append(f'[ONE-LINER] {lid} {"OK" if ok else "MISMATCH"}')
# 5 choice IDs: Lxx §9 vs PENNY_CHOICES
for lid, s in L.items():
    sec9 = s[s.find('## 9.'):s.find('## 10.')]
    ids = sorted(set(re.findall(rf'C-{lid}-\d', sec9)))
    missing = [i for i in ids if i not in ch]
    out.append(f'[CHOICES] {lid} §9 ids={ids} missing_in_PENNY_CHOICES={missing or "none"}')
def sec9(s): return s[s.find('## 9.'):s.find('## 10.')]
extra = sorted(i for i in set(re.findall(r'C-L\d\d-\d', ch)) if i not in sec9(L[i[2:5]]))
out.append(f'[CHOICES] ids in PENNY_CHOICES not found in Lxx §9: {extra or "none"}')
# 6 posts per file
for lid, s in L.items():
    sec3 = s[s.find('## 3.'):s.find('## 4.')]
    n = len(re.findall(r'^\*\*(#\d|貼文 ?[A-Z]?-?\d)', sec3, re.M))
    out.append(f'[POSTS] {lid} post headings in §3={n}')
# 7 producer composition rows and pairs
out.append(f'[PRODUCER] 構圖（情境照） rows={pr.count("| 構圖（情境照） |")} legacy 構圖 rows={pr.count(chr(10)+"| 構圖 |")}')
pairs_ov = re.findall(r'\| (L\d\d ↔ L\d\d)', ov); pairs_pr = re.findall(r'\| (L\d\d ↔ L\d\d)', pr)
out.append(f'[PAIRS] overview={pairs_ov}')
out.append(f'[PAIRS] producer={pairs_pr} same_order={pairs_ov==pairs_pr}')
# 8 PROPOSED header in each L file
for lid, s in L.items():
    out.append(f'[PROPOSED] {lid} {"OK" if "PROPOSED" in s[:300] else "MISSING"}')
print('\n'.join(out))
