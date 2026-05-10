#!/usr/bin/env python3
"""
NumPy Python 3.8 Backport Test Script
======================================
Tests all numpy submodules for import correctness and runs basic
functional tests on key modules to verify the backport works properly.

Usage:
    python test_numpy_full.py
"""

import sys
import pkgutil
import importlib


SKIP_MODULES = {
    "numpy.f2py",
    "numpy._core.cversions",
    "numpy._pyinstaller",
}


def test_submodule_imports():
    import numpy as np

    print(f"numpy version: {np.__version__}")
    print(f"numpy location: {np.__file__}")
    print()

    modules_to_test = []
    for importer, modname, ispkg in pkgutil.walk_packages(np.__path__, np.__name__ + "."):
        if modname not in SKIP_MODULES and not modname.startswith("numpy.f2py."):
            modules_to_test.append(modname)

    print(f"Found {len(modules_to_test)} numpy submodules (skipping f2py)")
    print("--- Submodule Import Tests ---")

    failed = []
    passed = 0
    for mod in modules_to_test:
        try:
            importlib.import_module(mod)
            print(f"  OK: {mod}")
            passed += 1
        except Exception as e:
            err = str(e)[:120]
            print(f"  FAIL: {mod} -> {err}")
            failed.append((mod, err))

    print(f"\nSubmodule Import: {passed}/{len(modules_to_test)} passed")
    return failed


def test_functional():
    import numpy as np

    print("\n--- Functional Tests ---")
    results = []

    tests = [
        ("np.array", lambda: np.array([1, 2, 3])),
        ("np.zeros", lambda: np.zeros((3, 3))),
        ("np.ones", lambda: np.ones((3, 3))),
        ("np.arange", lambda: np.arange(10)),
        ("np.linspace", lambda: np.linspace(0, 1, 5)),
        ("np.dot", lambda: np.dot([1, 2, 3], [4, 5, 6])),
        ("np.linalg.eig", lambda: np.linalg.eig(np.array([[1, 2], [3, 4]]))),
        ("np.linalg.svd", lambda: np.linalg.svd(np.array([[1, 2], [3, 4]]))),
        ("np.linalg.det", lambda: np.linalg.det(np.array([[1, 2], [3, 4]]))),
        ("np.fft.fft", lambda: np.fft.fft(np.array([1, 2, 3, 4]))),
        ("np.random.rand", lambda: np.random.rand(3)),
        ("np.random.normal", lambda: np.random.normal(0, 1, 100)),
        ("np.ma.array", lambda: np.ma.array([1, 2, 3], mask=[0, 1, 0])),
        ("np.polynomial.Polynomial", lambda: np.polynomial.Polynomial([1, 2, 3])),
        ("np.testing.assert_almost_equal", lambda: np.testing.assert_almost_equal(1.0, 1.0)),
        ("np.typing.ArrayLike", lambda: np.typing.ArrayLike),
        ("np.sin", lambda: np.sin(0)),
        ("np.cos", lambda: np.cos(0)),
        ("np.exp", lambda: np.exp(1)),
        ("np.log", lambda: np.log(np.e)),
        ("np.sort", lambda: np.sort([3, 1, 2])),
        ("np.unique", lambda: np.unique([1, 2, 2, 3])),
        ("np.concatenate", lambda: np.concatenate([[1, 2], [3, 4]])),
        ("np.reshape", lambda: np.arange(6).reshape(2, 3)),
        ("np.mean", lambda: np.mean([1, 2, 3])),
        ("np.std", lambda: np.std([1, 2, 3])),
        ("np.corrcoef", lambda: np.corrcoef([1, 2, 3], [4, 5, 6])),
    ]

    for name, fn in tests:
        try:
            fn()
            print(f"  OK: {name}")
            results.append((name, True))
        except Exception as e:
            err = str(e)[:120]
            print(f"  FAIL: {name} -> {err}")
            results.append((name, False))

    passed = sum(1 for _, ok in results if ok)
    print(f"\nFunctional Tests: {passed}/{len(results)} passed")
    return results


def main():
    print("=" * 60)
    print("NumPy Python 3.8 Backport - Comprehensive Test")
    print("=" * 60)
    print(f"Python version: {sys.version}")
    print()

    import_failed = test_submodule_imports()
    func_results = test_functional()

    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)

    real_import_failed = [
        (mod, err) for mod, err in import_failed
        if "pytest" not in err and "hypothesis" not in err and "PyInstaller" not in err
    ]

    if not real_import_failed and all(ok for _, ok in func_results):
        print("ALL TESTS PASSED!")
        return 0
    else:
        if real_import_failed:
            print(f"  {len(real_import_failed)} module import(s) failed (excluding test-only deps):")
            for mod, err in real_import_failed:
                print(f"    - {mod}: {err}")
        func_failed = sum(1 for _, ok in func_results if not ok)
        if func_failed:
            print(f"  {func_failed} functional test(s) failed")
        return 1


if __name__ == "__main__":
    sys.exit(main())
