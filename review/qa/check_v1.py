import re, sys, os
root = sys.argv[1]
canon = {
 'L01': dict(name='簡予安', age='29', city='中山', bday='11 月 16|11/16|11-16', sign='天蠍'),
 'L02': dict(name='凜', age='25', city='西屯', bday='1 月 29|1/29|01-29', sign='水瓶'),
 'L03': dict(name='周以晨', age='27', city='苓雅', bday='4 月 12|4/12|04-12', sign='牡羊'),
 'L04': dict(name='林可妮', age='31', city='萬華', bday='9 月 5|9/5|09-05', sign='處女'),
 'L05': dict(name='陳柏凱', age='24', city='新莊', bday='6 月 5|6/5|06-05', sign='雙子'),
 'L06': dict(name='黃子翔', age='34', city='台南', bday='3 月 28|3/28|03-28', sign='牡羊'),
 'L07': dict(name='程翊', age='28', city='新竹', bday='9 月 15|9/15|09-15', sign='處女'),
 'L08': dict(name='蔡沛岑', age='26', city='中壢', bday='8 月 3|8/3|08-03', sign='獅子'),
 'L09': dict(name='方士哲', age='36', city='基隆', bday='1 月 15|1/15|01-15', sign='摩羯'),
 'L10': dict(name='邱雅雯', age='32', city='板橋', bday='6 月 12|6/12|06-12', sign='雙子'),
}
heads = ['一眼看懂','## 1. 基本設定','## 2. 個性','## 3. 說話方式','## 4. 外型方向','## 5. 代表場景','## 6. 四張形象照','## 7. 三條可延續','## 8. 和其餘九人','## 9. 需要 Penny 選擇','## 10. 製作或公開內容的限制','## 11. 相對 v0 的修改']
banned = [r'LUSCENA', r'導流', r'落地頁', r'UTM', r'合作文', r'BLOCKED', r'撰寫中', r'尚未建立', r'待 ?THREADS_RESEARCH', r'現在沒有合作', r'這不是廣告', r'不是業配', r'每週\s*\d+\s*(則|篇)', r'2026-1[0-2]-\d\d', r'雙十一', r'選舉週', r'營運計畫']
for lid, c in canon.items():
    p = os.path.join(root, 'persona_pack_v1', lid + '.md')
    if not os.path.exists(p): print(lid, 'MISSING'); continue
    s = open(p, encoding='utf-8').read()
    iss = []
    for k in ('name','age','city','sign'):
        if not re.search(c[k], s): iss.append('missing %s=%s' % (k, c[k]))
    if not re.search(c['bday'], s): iss.append('birthday not found ' + c['bday'])
    pos = -1
    for h in heads:
        i = s.find(h)
        if i < 0: iss.append('heading missing: ' + h)
        elif i < pos: iss.append('heading order: ' + h)
        else: pos = i
    for b in banned:
        for m in re.finditer(b, s):
            line = s[s.rfind('\n',0,m.start())+1:s.find('\n',m.end())]
            if lid in ('L02','L08') and '## 11' in s[:m.start()] : pass
            # allow in section 11 (change log) and 10 limits
            sec11 = s.find('## 11.')
            if sec11 >= 0 and m.start() > sec11: continue
            iss.append('banned "%s": %s' % (b, line.strip()[:110]))
    n_portraits = len(re.findall(r'^\|\s*[1-4]\s*\|', s[s.find('## 6.'):s.find('## 7.')], re.M)) if '## 6.' in s else 0
    if n_portraits < 4: iss.append('portrait rows=%d' % n_portraits)
    ch = re.findall(r'C-%s-\d' % lid, s)
    if len(set(ch)) < 2: iss.append('choices=%d' % len(set(ch)))
    nposts = len(re.findall(r'貼文\s*[A-Z]?-?[1-3１-３]', s[s.find('### 三則'):s.find('## 4.')])) if '### 三則' in s else 0
    print('%s lines=%d posts~%d choices=%d %s' % (lid, s.count('\n'), nposts, len(set(ch)), 'OK' if not iss else ''))
    for i in iss: print('   -', i)
