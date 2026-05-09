import os
import py_compile
import sys

root = r'numpy'
skip_dirs = {'__pycache__', '.git', 'build', 'dist', 'egg-info', '.mypy_cache', '.pytest_cache'}

errors = []
success = 0

for dirpath, dirnames, filenames in os.walk(root):
    dirnames[:] = [d for d in dirnames if d not in skip_dirs]
    for fn in filenames:
        if not fn.endswith('.py'):
            continue
        fpath = os.path.join(dirpath, fn)
        try:
            py_compile.compile(fpath, doraise=True)
            success += 1
        except py_compile.PyCompileError as e:
            errors.append((fpath, str(e)[:200]))

print('Successfully compiled: %d files' % success)
print('Failed to compile: %d files' % len(errors))
for fpath, err in errors:
    print('\nFAILED: %s' % fpath)
    print('  %s' % err)
