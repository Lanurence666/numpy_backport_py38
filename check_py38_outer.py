import os
import re
import sys
import py_compile

root = r'.'
skip_dirs = {'__pycache__', '.git', 'build', 'dist', 'egg-info', '.mypy_cache', '.pytest_cache',
             'numpy', 'vendored-meson', 'numpy-main', 'check_py38_compat.py'}

issues = []

for dirpath, dirnames, filenames in os.walk(root):
    dirnames[:] = [d for d in dirnames if d not in skip_dirs]
    for fn in filenames:
        if not fn.endswith('.py'):
            continue
        fpath = os.path.join(dirpath, fn)
        if fpath.startswith('.\\fix_py38') or fpath.startswith('.\\check_py38'):
            continue
        try:
            with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
        except:
            continue

        try:
            py_compile.compile(fpath, doraise=True)
        except py_compile.PyCompileError as e:
            issues.append((fpath, 0, 'SYNTAX ERROR (cannot compile on 3.8)', str(e)[:150]))

        for line_num, line in enumerate(content.split('\n'), 1):
            stripped = line.strip()
            if re.match(r'^match\s+\S+:', stripped):
                issues.append((fpath, line_num, 'match/case statement (3.10+)', stripped[:80]))

        for line_num, line in enumerate(content.split('\n'), 1):
            stripped = line.strip()
            if re.match(r'^type\s+\w+\s*=', stripped):
                issues.append((fpath, line_num, 'type statement (PEP 695, 3.12+)', stripped[:80]))

        if re.search(r'^\s+with\s*\(', content, re.MULTILINE):
            for line_num, line in enumerate(content.split('\n'), 1):
                if re.match(r'^\s+with\s*\(', line):
                    if 'as ' in line or 'as ' in content.split('\n')[min(line_num, len(content.split('\n'))-1)]:
                        issues.append((fpath, line_num, 'parenthesized context manager (3.10+)', line.strip()[:80]))

for fpath, line_num, issue, detail in sorted(issues):
    loc = '%s:%d' % (fpath, line_num) if line_num else fpath
    print('%s - %s' % (loc, issue))
    if detail:
        print('  %s' % detail)
print('\nTotal issues: %d' % len(issues))
