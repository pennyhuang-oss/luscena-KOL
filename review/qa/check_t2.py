"""TASK-002 modeling pack field checks.

Field and string evidence only. A clean run does not prove the pages are
semantically right; read the pages. Anomalies are printed; the exit code is
always 0, so read the output.
"""
import os
import re
import sys

R = sys.argv[1] if len(sys.argv) > 1 else '.'
M = os.path.join(R, 'production', 'modeling_pack_v1')
P = os.path.join(R, 'persona_pack_v1')


def rd(path):
    return open(path, encoding='utf-8').read()


# name, age, height (cm), (zh mark keyword, en mark keyword) or None
CANON = {
    'L01': ('簡予安', 29, 168, ('左眉尾', 'left eyebrow')),
    'L02': ('凜', 25, 163, ('右眼下', 'right eye')),
    'L03': ('周以晨', 27, 170, ('左頰', 'left cheek')),
    'L04': ('林可妮', 31, 158, None),
    'L05': ('陳柏凱', 24, 172, ('左耳', 'left ear')),
    'L06': ('黃子翔', 34, 175, ('右前臂', 'right forearm')),
    'L07': ('程翊', 28, 178, None),
    'L08': ('蔡沛岑', 26, 165, None),
    'L09': ('方士哲', 36, 180, ('右手中指', 'right middle finger')),
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
    if mark:
        zh, enk = mark
        if zh not in s:
            issues.append('zh mark missing ' + zh)
        if enk not in en:
            issues.append('en mark missing ' + enk)
    for b in BANNED:
        if b in s:
            line = s[s.rfind('\n', 0, s.find(b)) + 1:s.find('\n', s.find(b))]
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
    for i, l in enumerate(rd(os.path.join(P, f)).split('\n'), 1):
        if ('同一個團隊' in l or '同團隊' in l or '我們這群' in l or '規格書' in l) and '2026-10-07' not in l:
            left.append(f'{f}:{i}: {l.strip()[:90]}')
out.append('[feedback] same-team lines without a 2026-10-07 note: ' + (str(len(left)) if left else 'none'))
out += ['   - ' + x for x in left]
print('\n'.join(out))
