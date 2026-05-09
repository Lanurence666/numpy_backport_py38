#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
# Copyright 2012-2019 The Meson development team

# some simple checks on the file format of:
# - python code
# - code samples in tests
# - markdown documentation
#
# checks are:
# - no use of tabs
# - no use of DOS line endings

import os
import re
from pathlib import Path

def _pathlib_walk_compat(path, top_down=True, on_error=None, follow_symlinks=False):
    import os
    try:
        from pathlib import Path
    except ImportError:
        Path = None
    if Path is not None and hasattr(Path, 'walk'):
        yield from _pathlib_walk_compat(path, top_down=top_down, on_error=on_error, follow_symlinks=follow_symlinks)
        return
    dirs = []
    nondirs = []
    walk_dir = str(path)
    try:
        scandir_it = os.scandir(walk_dir)
    except OSError as e:
        if on_error is not None:
            on_error(e)
        return
    with scandir_it:
        while True:
            try:
                entry = next(scandir_it)
            except StopIteration:
                break
            try:
                is_dir = entry.is_dir()
            except OSError:
                is_dir = False
            if is_dir:
                dirs.append(entry.name)
            else:
                nondirs.append(entry.name)
    if top_down:
        yield walk_dir, dirs, nondirs
    for dirname in dirs:
        new_path = os.path.join(walk_dir, dirname)
        if follow_symlinks:
            pass
        else:
            if os.path.islink(new_path):
                continue
        yield from _pathlib_walk_compat(new_path, top_down=top_down, on_error=on_error, follow_symlinks=follow_symlinks)
    if not top_down:
        yield walk_dir, dirs, nondirs
def check_file(file: Path) -> None:
    lines = file.read_bytes().split(b'\n')
    tabdetector = re.compile(br' *\t')
    for i, line in enumerate(lines):
        if re.match(tabdetector, line):
            raise SystemExit("File {} contains a tab indent on line {:d}. Only spaces are permitted.".format(file, i + 1))
        if line.endswith(b'\r'):
            raise SystemExit("File {} contains DOS line ending on line {:d}. Only unix-style line endings are permitted.".format(file, i + 1))

def check_format() -> None:
    check_suffixes = {'.c',
                      '.cpp',
                      '.cxx',
                      '.cc',
                      '.rs',
                      '.f90',
                      '.vala',
                      '.d',
                      '.s',
                      '.m',
                      '.mm',
                      '.asm',
                      '.java',
                      '.txt',
                      '.py',
                      '.swift',
                      '.build',
                      '.md',
                      }
    skip_dirs = {
        '.dub',                         # external deps are here
        '.pytest_cache',
        'meson-logs', 'meson-private',
        'work area',
        '.eggs', '_cache',              # e.g. .mypy_cache
        'venv',                         # virtualenvs have DOS line endings
        '120 rewrite',                  # we explicitly test for tab in meson.build file
        '3 editorconfig',
    }
    for (root, _, filenames) in _pathlib_walk_compat(os, '.'):
        if any([x in root for x in skip_dirs]):
            continue
        for fname in filenames:
            file = Path(fname)
            if file.suffix.lower() in check_suffixes:
                if file.name in ('sitemap.txt', 'meson-test-run.txt'):
                    continue
                check_file(root / file)

def check_symlinks():
    # Test data must NOT contain symlinks. setup.py
    # butchers them. If you need symlinks, they need
    # to be created on the fly.
    for f in Path('test cases').glob('**/*'):
        if f.is_symlink():
            if 'boost symlinks/boost/lib' in str(f):
                continue
            raise SystemExit(f'Test data dir contains symlink: {f}.')


if __name__ == '__main__':
    script_dir = os.path.split(__file__)[0]
    if script_dir != '':
        os.chdir(script_dir)
    check_format()
    check_symlinks()
