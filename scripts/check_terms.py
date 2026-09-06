#!/usr/bin/env python3
"""Term gate for docs/ and repo/ text files. Rules switch on book.json "lang".
zh: no vendor-narrative words, "客户" only in whitelisted phrases (policyholder sense).
en: no em dash, no non-ASCII outside a small allowlist, no romanized or near-miss names (term-gate/en-banned.txt).
Both: "FDE" only in the designated files. Usage: python3 scripts/check_terms.py [files...]; no args scans everything."""
import glob
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GATE = os.path.join(ROOT, 'scripts', 'term-gate')
BOOK = json.load(open(os.path.join(ROOT, 'book.json'), encoding='utf-8'))
LANG = BOOK['lang']
TEXT_EXT = ('.md', '.py', '.sql', '.yaml', '.json', '.jsonl', '.csv', '.svg', '.css', '.txt')
EXCLUDE = ('llms.txt', 'llms-full.txt', '__pycache__')
FDE = re.compile(r'\bFDE\b')
FDE_ALLOWED = ('ch02-inheritance.md', 'internal-fde-mapping.md', 'template-03-capability.md', 'template-02-role-charter.md')

FORBIDDEN = re.compile(r'乙方|甲方|我方|你方|续约|报价|人天|利润率|离场|退场|账号回收|(?<!赔)付款|尾款|采购|合同|客户工程师|客户侧|客户方|内部 FDE')
VENDOR_EXEMPT = ('ch02-inheritance.md', 'internal-fde-mapping.md')

EM_DASH = re.compile(r'[—―]')
NON_ASCII = re.compile(r'[^\x00-\x7f]')
EN_ALLOWED = set('–·’‘“”…→↔↑↓×≤≥≠∈§©✓✗☐☑📋🗂🚧')  # en dash (ranges), middot (H1 / Part titles), curly quotes, arrows, math


def load(name):
    p = os.path.join(GATE, name)
    return [l.strip() for l in open(p, encoding='utf-8') if l.strip() and not l.startswith('#')] if os.path.exists(p) else []


def vendor_block_lines(lines):
    s = set(); on = False
    for i, l in enumerate(lines, 1):
        if l.startswith(BOOK['vendor_block']):
            on = True; s.add(i); continue
        if on:
            if l.startswith('    ') or not l.strip():
                s.add(i); continue
            on = False
    return s


def check_zh(base, l, wl):
    out = []
    if base not in VENDOR_EXEMPT:
        out += [f'banned term "{m.group(0)}"' for m in FORBIDDEN.finditer(l)]
    if base in VENDOR_EXEMPT and base != 'ch02-inheritance.md':
        return out
    for m in re.finditer('客户', l):
        w = l[max(0, m.start() - 6):m.end() + 6]
        if not any(x in w for x in wl):
            out.append(f'"客户" not in whitelist: …{l[max(0, m.start()-12):m.end()+12]}…')
    return out


def check_en(base, l, banned):
    out = [f'em dash U+{ord(m.group(0)):04X}, rewrite with period, comma or parentheses' for m in EM_DASH.finditer(l)]
    out += [f"non-ASCII U+{ord(c):04X} '{c}'" for c in dict.fromkeys(NON_ASCII.findall(l))
           if c not in EN_ALLOWED and not EM_DASH.match(c) and not (0x2460 <= ord(c) <= 0x2473 or 0x2500 <= ord(c) <= 0x25FF)]  # circled digits, box drawing, shapes
    low = l.lower()
    out += [f'banned name "{b}"' for b in banned if b.lower() in low]
    return out


def main():
    files = sys.argv[1:] or sorted(glob.glob(os.path.join(ROOT, 'docs', '**', '*'), recursive=True)
                                   + glob.glob(os.path.join(ROOT, 'repo', '**', '*'), recursive=True)
                                   + [os.path.join(ROOT, 'repo', 'LICENSE')])
    files = [p for p in files if os.path.isfile(p) and (p.endswith(TEXT_EXT) or os.path.basename(p) == 'LICENSE')
             and not any(x in p for x in EXCLUDE)]
    wl, banned = load('customer-whitelist.txt'), load('en-banned.txt')
    allow = load('vendor-allow.txt' if LANG == 'zh' else 'en-allow.txt')  # lines containing these skip the gate
    bad = 0
    for path in files:
        base = os.path.basename(path)
        lines = open(path, encoding='utf-8').read().split('\n')
        skip = vendor_block_lines(lines)
        for i, l in enumerate(lines, 1):
            if i in skip or any(a in l for a in allow):
                continue
            problems = check_zh(base, l, wl) if LANG == 'zh' else check_en(base, l, banned)
            if base not in FDE_ALLOWED and FDE.search(l):
                problems.append('FDE outside the allowed files')
            for msg in problems:
                bad += 1; print(f'{os.path.relpath(path, ROOT)}:{i}: {msg}  {l.strip()[:60]}')
    print(f'{"FAIL" if bad else "OK"}: {bad} problem(s)')
    sys.exit(1 if bad else 0)


if __name__ == '__main__':
    main()
