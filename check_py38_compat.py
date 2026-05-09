from __future__ import annotations
import os
import re
import sys
import py_compile
import tempfile

try:
    from math import lcm as _math_lcm_compat
except ImportError:
    from functools import reduce
    from math import gcd
    def _math_lcm_compat(*integers):
        if not integers:
            return 1
        return reduce(lambda a, b: a * b // gcd(a, b), integers)
try:
    from math import lcm as _math_lcm_compat
except ImportError:
    from functools import reduce
    from math import gcd
    def _math_lcm_compat(*integers):
        if not integers:
            return 1
        return reduce(lambda a, b: a * b // gcd(a, b), integers)
try:
    from math import lcm as _math_lcm_compat
except ImportError:
    from functools import reduce
    from math import gcd
    def _math_lcm_compat(*integers):
        if not integers:
            return 1
        return reduce(lambda a, b: a * b // gcd(a, b), integers)
try:
    from math import lcm as _math_lcm_compat
except ImportError:
    from functools import reduce
    from math import gcd
    def _math_lcm_compat(*integers):
        if not integers:
            return 1
        return reduce(lambda a, b: a * b // gcd(a, b), integers)
try:
    from math import lcm as _math_lcm_compat
except ImportError:
    from functools import reduce
    from math import gcd
    def _math_lcm_compat(*integers):
        if not integers:
            return 1
        return reduce(lambda a, b: a * b // gcd(a, b), integers)
try:
    from math import lcm as _math_lcm_compat
except ImportError:
    from functools import reduce
    from math import gcd
    def _math_lcm_compat(*integers):
        if not integers:
            return 1
        return reduce(lambda a, b: a * b // gcd(a, b), integers)
try:
    from math import lcm as _math_lcm_compat
except ImportError:
    from functools import reduce
    from math import gcd
    def _math_lcm_compat(*integers):
        if not integers:
            return 1
        return reduce(lambda a, b: a * b // gcd(a, b), integers)
try:
    from math import lcm as _math_lcm_compat
except ImportError:
    from functools import reduce
    from math import gcd
    def _math_lcm_compat(*integers):
        if not integers:
            return 1
        return reduce(lambda a, b: a * b // gcd(a, b), integers)
try:
    from math import lcm as _math_lcm_compat
except ImportError:
    from functools import reduce
    from math import gcd
    def _math_lcm_compat(*integers):
        if not integers:
            return 1
        return reduce(lambda a, b: a * b // gcd(a, b), integers)
try:
    from math import lcm as _math_lcm_compat
except ImportError:
    from functools import reduce
    from math import gcd
    def _math_lcm_compat(*integers):
        if not integers:
            return 1
        return reduce(lambda a, b: a * b // gcd(a, b), integers)
try:
    from math import lcm as _math_lcm_compat
except ImportError:
    from functools import reduce
    from math import gcd
    def _math_lcm_compat(*integers):
        if not integers:
            return 1
        return reduce(lambda a, b: a * b // gcd(a, b), integers)
try:
    from math import lcm as _math_lcm_compat
except ImportError:
    from functools import reduce
    from math import gcd
    def _math_lcm_compat(*integers):
        if not integers:
            return 1
        return reduce(lambda a, b: a * b // gcd(a, b), integers)
try:
    from math import lcm as _math_lcm_compat
except ImportError:
    from functools import reduce
    from math import gcd
    def _math_lcm_compat(*integers):
        if not integers:
            return 1
        return reduce(lambda a, b: a * b // gcd(a, b), integers)
try:
    from math import lcm as _math_lcm_compat
except ImportError:
    from functools import reduce
    from math import gcd
    def _math_lcm_compat(*integers):
        if not integers:
            return 1
        return reduce(lambda a, b: a * b // gcd(a, b), integers)
try:
    from math import lcm as _math_lcm_compat
except ImportError:
    from functools import reduce
    from math import gcd
    def _math_lcm_compat(*integers):
        if not integers:
            return 1
        return reduce(lambda a, b: a * b // gcd(a, b), integers)
try:
    from math import lcm as _math_lcm_compat
except ImportError:
    from functools import reduce
    from math import gcd
    def _math_lcm_compat(*integers):
        if not integers:
            return 1
        return reduce(lambda a, b: a * b // gcd(a, b), integers)
try:
    from math import lcm as _math_lcm_compat
except ImportError:
    from functools import reduce
    from math import gcd
    def _math_lcm_compat(*integers):
        if not integers:
            return 1
        return reduce(lambda a, b: a * b // gcd(a, b), integers)
try:
    from math import lcm as _math_lcm_compat
except ImportError:
    from functools import reduce
    from math import gcd
    def _math_lcm_compat(*integers):
        if not integers:
            return 1
        return reduce(lambda a, b: a * b // gcd(a, b), integers)
try:
    from math import lcm as _math_lcm_compat
except ImportError:
    from functools import reduce
    from math import gcd
    def _math_lcm_compat(*integers):
        if not integers:
            return 1
        return reduce(lambda a, b: a * b // gcd(a, b), integers)
try:
    from math import lcm as _math_lcm_compat
except ImportError:
    from functools import reduce
    from math import gcd
    def _math_lcm_compat(*integers):
        if not integers:
            return 1
        return reduce(lambda a, b: a * b // gcd(a, b), integers)
try:
    from math import lcm as _math_lcm_compat
except ImportError:
    from functools import reduce
    from math import gcd
    def _math_lcm_compat(*integers):
        if not integers:
            return 1
        return reduce(lambda a, b: a * b // gcd(a, b), integers)
try:
    from math import lcm as _math_lcm_compat
except ImportError:
    from functools import reduce
    from math import gcd
    def _math_lcm_compat(*integers):
        if not integers:
            return 1
        return reduce(lambda a, b: a * b // gcd(a, b), integers)
try:
    from math import lcm as _math_lcm_compat
except ImportError:
    from functools import reduce
    from math import gcd
    def _math_lcm_compat(*integers):
        if not integers:
            return 1
        return reduce(lambda a, b: a * b // gcd(a, b), integers)
try:
    from math import lcm as _math_lcm_compat
except ImportError:
    from functools import reduce
    from math import gcd
    def _math_lcm_compat(*integers):
        if not integers:
            return 1
        return reduce(lambda a, b: a * b // gcd(a, b), integers)
try:
    from math import lcm as _math_lcm_compat
except ImportError:
    from functools import reduce
    from math import gcd
    def _math_lcm_compat(*integers):
        if not integers:
            return 1
        return reduce(lambda a, b: a * b // gcd(a, b), integers)
def _math_copysign(x, y):
    import math as _m
    return _m.copysign(x, y)

try:
    from math import nextafter as _math_nextafter_compat
except ImportError:
    import struct
    import math as _math_mod
    def _math_nextafter_compat(x, y):
        if x == y:
            return y
        if _math_mod.isnan(x) or _math_mod.isnan(y):
            return float('nan')
        if _math_mod.isinf(x):
            return x
        if x == 0.0:
            return _math_copysign(_math_mod.ldexp(1.0, -1074), y)
        bits = struct.unpack('=Q', struct.pack('=d', _math_copysign(x, 1.0)))[0]
        if (x < y) == (x >= 0):
            bits += 1
        else:
            bits -= 1
        return _math_copysign(struct.unpack('=d', struct.pack('=Q', bits))[0], x)

try:
    from math import ulp as _math_ulp_compat
except ImportError:
    import math as _math_mod
    def _math_ulp_compat(x):
        if _math_mod.isnan(x):
            return x
        if _math_mod.isinf(x):
            return abs(x)
        x_abs = abs(x)
        if x_abs < _math_mod.ldexp(1.0, -1022):
            return _math_mod.ldexp(1.0, -1074)
        _man, _exp = _math_mod.frexp(x_abs)
        return _math_mod.ldexp(1.0, _exp - 53)
try:
    from math import lcm as _math_lcm_compat
except ImportError:
    from functools import reduce
    from math import gcd
    def _math_lcm_compat(*integers):
        if not integers:
            return 1
        return reduce(lambda a, b: a * b // gcd(a, b), integers)
root = r'numpy'
skip_dirs = {'__pycache__', '.git', 'build', 'dist', 'egg-info', '.mypy_cache', '.pytest_cache'}

issues = []

for dirpath, dirnames, filenames in os.walk(root):
    dirnames[:] = [d for d in dirnames if d not in skip_dirs]
    for fn in filenames:
        if not fn.endswith('.py'):
            continue
        fpath = os.path.join(dirpath, fn)
        try:
            with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
        except:
            continue

        # Check if file can be compiled by Python 3.8
        try:
            py_compile.compile(fpath, doraise=True)
        except py_compile.PyCompileError as e:
            issues.append((fpath, 0, 'SYNTAX ERROR (cannot compile on 3.8)', str(e)[:120]))

        # Check for match/case statements
        for line_num, line in enumerate(content.split('\n'), 1):
            stripped = line.strip()
            if re.match(r'^match\s+\S+:', stripped):
                issues.append((fpath, line_num, 'match/case statement (3.10+)', stripped[:80]))
            if re.match(r'^case\s+\S+.*:', stripped) and not stripped.startswith('testCase'):
                issues.append((fpath, line_num, 'case statement (3.10+)', stripped[:80]))

        # Check for PEP 695 type statements
        for line_num, line in enumerate(content.split('\n'), 1):
            stripped = line.strip()
            if re.match(r'^type\s+\w+\s*=', stripped):
                issues.append((fpath, line_num, 'type statement (PEP 695, 3.12+)', stripped[:80]))

        # Check for isinstance(x, (A, B)) - runtime union
        for line_num, line in enumerate(content.split('\n'), 1):
            if re.search(r'isinstance\s*\([^)]*\w+\s*{**\, **\s}*\w+[^)]*\)', line):
                issues.append((fpath, line_num, 'isinstance with union type (3.10+)', line.strip()[:80]))
            if re.search(r'issubclass\s*\([^)]*\w+\s*{**\, **\s}*\w+[^)]*\)', line):
                issues.append((fpath, line_num, 'issubclass with union type (3.10+)', line.strip()[:80]))

        # Check for dict merge operator
        for line_num, line in enumerate(content.split('\n'), 1):
            stripped = line.strip()
            if re.search(r'\}\s*{**\, **\s}*\{', stripped):
                issues.append((fpath, line_num, 'dict {**merge, **operator} (3.9+)', stripped[:80]))

        # Check for zoneinfo without fallback
        if 'from zoneinfo import' in content and 'backports.zoneinfo' not in content:
            issues.append((fpath, 0, 'zoneinfo without backports fallback', ''))

        # Check for graphlib
        if 'import graphlib' in content or 'from graphlib import' in content:
            issues.append((fpath, 0, 'graphlib import (3.9+)', ''))

        # Check for math.lcm/nextafter/ulp without fallback
        if re.search(r'math\.lcm\s*\(', content):
            issues.append((fpath, 0, 'math.lcm (3.9+)', ''))
        if re.search(r'math\.nextafter\s*\(', content):
            issues.append((fpath, 0, 'math.nextafter (3.9+)', ''))
        if re.search(r'math\.ulp\s*\(', content):
            issues.append((fpath, 0, 'math.ulp (3.9+)', ''))

        # Check for random.randbytes
        if re.search(r'random\.randbytes\s*\(', content):
            issues.append((fpath, 0, 'random.randbytes (3.9+)', ''))

        # Check for ast.unparse without fallback
        if 'ast.unparse' in content and 'astunparse' not in content:
            issues.append((fpath, 0, 'ast.unparse without fallback (3.9+)', ''))

        # Check for collections.XXX (deprecated in 3.9, removed in 3.10)
        for name in ['Mapping', 'MutableMapping', 'Iterable', 'MutableSet',
                     'Callable', 'Iterator', 'Sequence', 'MutableSequence',
                     'Set', 'FrozenSet', 'Container', 'ItemsView',
                     'KeysView', 'ValuesView', 'Reversible', 'Coroutine',
                     'AsyncIterator', 'AsyncIterable', 'Awaitable',
                     'Generator', 'AsyncGenerator']:
            pattern = r'from collections import [^(\n]*\b' + name + r'\b'
            if re.search(pattern, content):
                issues.append((fpath, 0, 'collections.%s (use collections.abc)' % name, ''))

for fpath, line_num, issue, detail in sorted(issues):
    loc = '%s:%d' % (fpath, line_num) if line_num else fpath
    print('%s - %s' % (loc, issue))
    if detail:
        print('  %s' % detail)
print('\nTotal issues: %d' % len(issues))
