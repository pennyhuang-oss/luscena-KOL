"""TASK-002 modeling pack field checks.

Field and string evidence only. A clean run does not prove the pages are
semantically right; read the pages. Anomalies are printed; the exit code is
always 0, so read the output.

R2 (T2-F06): L04 side marks added; the [R2] block at the end checks only the
listed strings and file existence. It does not validate whole prompts.
"""
import hashlib
import os
import re
import sys

R = sys.argv[1] if len(sys.argv) > 1 else '.'
M = os.path.join(R, 'production', 'modeling_pack_v1')
P = os.path.join(R, 'persona_pack_v1')


def rd(path):
    return open(path, encoding='utf-8').read()


# name, age, height (cm), (zh mark, en mark) or a list of them, or None
CANON = {
    'L01': ('簡予安', 29, 168, ('左眉尾', 'left eyebrow')),
    'L02': ('凜', 25, 163, ('右眼下', 'right eye')),
    'L03': ('周以晨', 27, 170, ('左頰', 'left cheek')),
    'L04': ('林可妮', 31, 158, [('略偏她本人的右側', 'slightly toward her own right side'),
                                 ('左手腕', 'on her own left wrist')]),
    'L05': ('陳柏凱', 24, 172, ('左耳', 'left ear')),
    'L06': ('黃子翔', 34, 175, ('右前臂', 'right forearm')),
    'L07': ('程翊', 28, 178, None),
    'L08': ('蔡沛岑', 26, 165, None),
    'L09': ('方士哲', 36, 180, ('右手中指', 'middle finger of his own right hand')),
    'L10': ('邱雅雯', 32, 160, ('右耳', 'right ear')),
}
HEADS = ['## A.', '## B.', '## C.', '## D.', '## E.', '## F.', '## G.', '## H.', '## I.']
PROMPT_KEYS = ['BASE_IDENTITY', 'NEUTRAL_CASTING', 'IDENTITY_CHECK', 'SIGNATURE_PORTRAIT']
BANNED = ['已核准', '客戶已選', '客戶選定 B', '一律不用標示', '同一個團隊做的', 'same team',
          'celebrity look', 'look like a famous']
out = []
ov = rd(os.path.join(P, '00_OVERVIEW.md'))
for lid, (name, age, height, mark) in CANON.items():
    path = os.path.join(M, lid + '.md')
    if not os.path.exists(path):
        out.append(f'{lid} MISSING')
        continue
    s = rd(path)
    issues = []
    pos = -1
    for h in HEADS:
        i = s.find(h)
        if i < 0:
            issues.append('missing heading ' + h)
        elif i < pos:
            issues.append('heading order ' + h)
        else:
            pos = i
    for k in PROMPT_KEYS:
        if k not in s:
            issues.append('missing prompt key ' + k)
    blocks = re.findall(r'```text\n(.*?)```', s, re.S)
    if len(blocks) < 4:
        issues.append(f'text blocks={len(blocks)}')
    if name not in s:
        issues.append('name missing ' + name)
    if f'{age} 歲' not in s and f'{age}／' not in s:
        issues.append(f'age {age} not found in Chinese text')
    en = '\n'.join(blocks)
    if not re.search(rf'\b{age}[- ]year', en) and lid != 'L08':
        issues.append(f'age {age} not found in English prompts')
    if f'{height} cm' not in s:
        issues.append(f'height {height} cm not found')
    if not re.search(r'adult', en, re.I):
        issues.append('English prompts never say adult')
    if 'Original fictional' not in en and 'original fictional' not in en:
        issues.append('English prompts never say original fictional')
    if 'PROPOSED' not in s[:600]:
        issues.append('PROPOSED not in header')
    if '待選' not in s:
        issues.append('no 待選 label')
    for zh, enk in ([mark] if isinstance(mark, tuple) else (mark or [])):
        if zh not in s:
            issues.append('zh mark missing ' + zh)
        if enk not in en:
            issues.append('en mark missing ' + enk)
    for b in BANNED:
        for m in re.finditer(re.escape(b), s):
            before = s[max(0, m.start() - 12):m.start()]
            if any(neg in before for neg in ('不是', '未', '沒有', '不等於', '不能寫成')):
                continue  # negated mention, e.g. 「不是 Penny 已核准」
            line = s[s.rfind('\n', 0, m.start()) + 1:s.find('\n', m.start())]
            issues.append(f'banned "{b}": {line.strip()[:100]}')
    # overview row consistency (age)
    row = [l for l in ov.split('\n') if l.startswith(f'| {lid} |')]
    if row and f'| {age}／' not in row[0]:
        issues.append('overview age differs')
    out.append(f'{lid} text_blocks={len(blocks)} ' + ('OK' if not issues else ''))
    out += ['   - ' + i for i in issues]

# pack-level files
for f in ['00_START_HERE.md', 'CLIENT_FEEDBACK_2026-10-07.md', 'MODEL_AND_WORKFLOW_OPTIONS.md',
          'REFERENCE_AND_ACCEPTANCE.md', 'PRODUCER_CLAUDE_HANDOFF_PROMPT.md']:
    p = os.path.join(M, f)
    out.append(f'[file] {f}: ' + ('exists' if os.path.exists(p) else 'MISSING'))

# relative links in 00_START_HERE resolve
sh = os.path.join(M, '00_START_HERE.md')
if os.path.exists(sh):
    bad = []
    for link in re.findall(r'\]\(([^)#]+)\)', rd(sh)):
        if link.startswith('http'):
            continue
        if not os.path.exists(os.path.normpath(os.path.join(M, link))):
            bad.append(link)
    out.append('[links] 00_START_HERE unresolved: ' + (', '.join(bad) if bad else 'none'))

# client feedback tags in persona pack
tag_no = '依客戶回饋不採用'
n_no = sum(rd(os.path.join(P, f)).count(tag_no) for f in os.listdir(P) if f.endswith('.md'))
heads = [f for f in sorted(os.listdir(P)) if re.match(r'L\d\d\.md', f)
         and '2026-10-07 客戶回饋' in rd(os.path.join(P, f))[:1500]]
out.append(f'[feedback] "{tag_no}" occurrences in persona_pack_v1: {n_no}')
out.append(f'[feedback] Lxx files with 2026-10-07 header note: {len(heads)}/10')
left = []
for f in sorted(os.listdir(P)):
    if not f.endswith('.md'):
        continue
    body = rd(os.path.join(P, f))
    cut = body.find('## 11.')  # §11 change logs describe history; exempt
    if cut > 0:
        body = body[:cut]
    for i, l in enumerate(body.split('\n'), 1):
        if ('同一個團隊' in l or '同團隊' in l or '我們這群' in l or '規格書' in l) and '2026-10-07' not in l:
            left.append(f'{f}:{i}: {l.strip()[:90]}')
out.append('[feedback] same-team lines without a 2026-10-07 note: ' + (str(len(left)) if left else 'none'))
out += ['   - ' + x for x in left]
print('\n'.join(out))

# [R2] residual strings and handoff must-read files (field checks only)
r2 = []
R1_PATTERNS = ['5–20', '5-20', 'T1–T8 通過之後再做', '把服裝與髮型那一句換成', '把服裝、髮型或表情那一句換成',
               '把服裝、髮型與妝那一句換成', '把服裝、髮型、眼鏡與妝那一句換成', '目前允許的尺度', '只做尺度 1']
for f in sorted(os.listdir(M)):
    if not f.endswith('.md'):
        continue
    s = rd(os.path.join(M, f))
    for pat in R1_PATTERNS:
        if pat in s and not (f == 'MODEL_AND_WORKFLOW_OPTIONS.md' and pat.startswith('5')):
            r2.append(f'{f}: residual "{pat}"')
    if re.match(r'L\d\d\.md', f):
        if 'T6–T8 的角度依' not in s:
            r2.append(f'{f}: no T6–T8 view mapping')
        if 'identity reference image A; keep' not in s:
            r2.append(f'{f}: full-body B not tied to reference A')
        if 'REFERENCE_AND_ACCEPTANCE.md` §7' not in s:
            r2.append(f'{f}: no pointer to REFERENCE_AND_ACCEPTANCE §7')
l07 = rd(os.path.join(M, 'L07.md'))
for l in l07.split('\n'):
    if 'pushed up onto his forehead' in l and 'Avoid:' not in l:
        r2.append('L07.md: glasses-pushed-up line has no Avoid replacement')
g3 = rd(os.path.join(M, 'L09.md')).split('### G-3')[1].split('### G-4')[0]
if '[HAIR]' not in re.findall(r'```text\n(.*?)```', g3, re.S)[0]:
    r2.append('L09.md: G-3 template has no [HAIR]')
if '## 7.' not in rd(os.path.join(M, 'REFERENCE_AND_ACCEPTANCE.md')):
    r2.append('REFERENCE_AND_ACCEPTANCE.md: no §7')
if '替團隊算' in ov:
    r2.append('00_OVERVIEW.md: residual "替團隊算"')
se12 = [l for l in rd(os.path.join(P, 'SHARED_EVENTS.md')).split('\n') if l.startswith('| SE-12 |')]
if not se12 or '要在第 1 步之後' in se12[0]:
    r2.append('SHARED_EVENTS.md: SE-12 row still depends on step 1')
r2.insert(0, 'string/structure anomalies: ' + (str(len(r2)) if r2 else 'none'))
MUST = (['production/modeling_pack_v1/' + x for x in
         ['00_START_HERE.md'] + [f'L{i:02d}.md' for i in range(1, 11)] +
         ['MODEL_AND_WORKFLOW_OPTIONS.md', 'REFERENCE_AND_ACCEPTANCE.md', 'CLIENT_FEEDBACK_2026-10-07.md']] +
        [f'persona_pack_v1/L{i:02d}.md' for i in range(1, 11)] +
        ['persona_pack_v1/00_OVERVIEW.md', 'persona_pack_v1/PRODUCER_REFERENCE_NEEDS.md',
         'review/REVIEW_RESPONSE_TASK_002_MODELING_PACK_R1.md', 'review/CORRECTION_TASK_002_MODELING_PACK_R2.md'])
ho = rd(os.path.join(M, 'PRODUCER_CLAUDE_HANDOFF_PROMPT.md'))
miss = [x for x in MUST if not os.path.exists(os.path.join(R, x))]
unlisted = [x for x in MUST if os.path.basename(x) not in ho]
r2.append(f'handoff must-read files: {len(MUST)} listed in script; missing on disk: '
          + (', '.join(miss) if miss else 'none') + '; basename not in handoff: '
          + (', '.join(unlisted) if unlisted else 'none'))
BLOBS = {'REVIEW_RESPONSE_TASK_001_R1.md': '0163fc243b1145c0c9e9c68a095fc4390b084fe5',
         'REVIEW_RESPONSE_TASK_001_R2_PERSONA.md': '778e0095afe41866977d4e81c373df34b98017c7',
         'REVIEW_RESPONSE_TASK_001_R3.md': '221e461aaa580ee357ab6859dfc28ed250836920',
         'REVIEW_RESPONSE_TASK_001_R3_F01-F06.md': 'cc4706bc98d1b39db9706a7468f594e7abac1843',
         'REVIEW_RESPONSE_TASK_001_R3_F01_FINAL.md': '742a03d2ad2dc720a233ef652b5b4eb833be9b75',
         'REVIEW_RESPONSE_TASK_001_MERGE_MAIN.md': '6e915d243025764a467b6133799856f4130f99f7',
         'REVIEW_RESPONSE_TASK_002_MODELING_PACK_R1.md': '11d897b48a3c0594de27212024f031ce023a3c4f'}
for f, want in BLOBS.items():
    b = open(os.path.join(R, 'review', f), 'rb').read()
    got = hashlib.sha1(b'blob %d\0' % len(b) + b).hexdigest()
    r2.append(f'blob {f}: ' + ('same' if got == want else 'CHANGED ' + got))
print('\n'.join('[R2] ' + x for x in r2))
