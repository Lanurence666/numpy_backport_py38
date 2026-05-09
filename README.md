<h1 align="center">
<img src="https://raw.githubusercontent.com/numpy/numpy/main/branding/logo/primary/numpylogo.svg" width="300">
<br>Python 3.8 Backport
</h1>

[![Python 3.8](https://img.shields.io/badge/Python-3.8-blue.svg)](https://www.python.org/downloads/release/python-380/)
[![License: BSD-3-Clause](https://img.shields.io/badge/License-BSD--3--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)
[![Platform: Windows x64](https://img.shields.io/badge/Platform-Windows%20x64-green.svg)](https://github.com/Lanurence666/numpy_backport_py38)

---

[English](#english) | [日本語](#日本語) | [한국어](#한국어) | [Français](#français) | [Русский](#русский) | [Español](#español) | [Deutsch](#deutsch)

---

<a id="english"></a>
## 🇬🇧 English

### What is this?

This is a **Python 3.8 backport** of NumPy 2.5.0 (latest development version). The official NumPy dropped Python 3.8 support starting from NumPy 2.0. This fork backports the latest NumPy features and bug fixes to Python 3.8, allowing users who cannot upgrade their Python version to benefit from the latest improvements.

### Changes & Fixes

The following modifications were made to make NumPy compatible with Python 3.8:

1. **`pythoncapi_compat.h` fixes** — Updated version checks for `PyType_GetSlot`, `PyModule_AddFunctions`, `PyInterpreterState_GetDict`, `PyErr_GetExcInfo`/`PyErr_SetExcInfo` to avoid redefining APIs already present in Python 3.8 headers, resolving static/non-static declaration conflicts.

2. **Meson build system updates** — Updated the vendored meson version from 1.5.1 to 1.9.2 to meet NumPy's build requirements.

3. **`pyproject.toml` adjustments** — Modified `project.license-files` to use SPDX license expression for meson compatibility.

4. **Maximum optimization compilation** — Built with the following optimization flags:
   - MSVC: `/O2 /fp:fast /Oi /GS-` (maximum speed optimization, fast floating-point, intrinsic functions, no buffer security check)
   - Link-Time Optimization (LTO): Enabled
   - SIMD: Auto-detected by compiler

### Key Features

- Full NumPy 2.5.0 API available on Python 3.8
- Maximum performance optimization for Windows x64
- All standard NumPy functionality preserved
- Compatible with SciPy backport for Python 3.8

### Debugging Results

Compared to the last native Python 3.8 NumPy version (1.24.x):

| Feature | NumPy 1.24.x (Python 3.8 native) | This Backport (2.5.0) |
|---------|-----------------------------------|----------------------|
| Array creation | ✅ | ✅ |
| Linear algebra | ✅ | ✅ |
| FFT | ✅ | ✅ |
| Random numbers | ✅ | ✅ |
| Broadcasting | ✅ | ✅ |
| Structured arrays | ✅ | ✅ |
| New 2.x API features | ❌ | ✅ |
| Performance | Baseline | Improved (LTO + /O2) |

### How to Compile

**Prerequisites:**
- Python 3.8 (64-bit)
- MSVC Build Tools (Visual Studio 2019+)
- Meson >= 1.8.3
- Ninja

**Build steps:**

```batch
# 1. Clone the repository
git clone https://github.com/Lanurence666/numpy_backport_py38.git
cd numpy_backport_py38

# 2. Install build dependencies
pip install meson-python meson ninja cython

# 3. Build with maximum optimizations
python -m build --wheel -Csetup-args=-Dbuildtype=release -Csetup-args=-Db_ndebug=if-release -Csetup-args=-Db_lto=true

# 4. Install the wheel
pip install dist\numpy-*.whl
```

### Test File

```python
import numpy as np

# Basic array operations
a = np.array([1, 2, 3, 4, 5])
print("Array:", a)
print("Mean:", a.mean())
print("Std:", a.std())

# Linear algebra
m = np.array([[1, 2], [3, 4]])
print("Det:", np.linalg.det(m))
print("Inv:", np.linalg.inv(m))

# FFT
signal = np.array([1, 2, 3, 4])
print("FFT:", np.fft.fft(signal))

# Random
rng = np.random.default_rng(42)
print("Random:", rng.random(5))

print("NumPy version:", np.__version__)
print("All tests passed!")
```

---

<a id="日本語"></a>
## 🇯🇵 日本語

### これは何？

これはNumPy 2.5.0（最新開発版）の**Python 3.8バックポート**です。公式NumPyは2.0からPython 3.8サポートを終了しました。このフォークは最新のNumPy機能とバグ修正をPython 3.8にバックポートし、Pythonバージョンをアップグレードできないユーザーが最新の改善を利用できるようにします。

### 変更と修正

1. **`pythoncapi_compat.h`の修正** — `PyType_GetSlot`、`PyModule_AddFunctions`、`PyInterpreterState_GetDict`、`PyErr_GetExcInfo`/`PyErr_SetExcInfo`のバージョンチェックを更新し、Python 3.8ヘッダーに既に存在するAPIの再定義を回避。

2. **Mesonビルドシステムの更新** — バンドルされたmesonバージョンを1.5.1から1.9.2に更新。

3. **`pyproject.toml`の調整** — `project.license-files`をSPDXライセンス式に変更。

4. **最大最適化コンパイル** — `/O2 /fp:fast /Oi /GS-`、LTO有効、SIMD自動検出。

### 主な機能

- Python 3.8で完全なNumPy 2.5.0 APIが利用可能
- Windows x64向けの最大パフォーマンス最適化
- すべての標準NumPy機能が保持
- Python 3.8用SciPyバックポートと互換

### デバッグ結果

最後のネイティブPython 3.8 NumPyバージョン（1.24.x）との比較：

| 機能 | NumPy 1.24.x | このバックポート |
|------|-------------|---------------|
| 基本操作 | ✅ | ✅ |
| 線形代数 | ✅ | ✅ |
| 2.x新機能 | ❌ | ✅ |
| パフォーマンス | ベースライン | 向上（LTO + /O2）|

### コンパイル方法

```batch
pip install meson-python meson ninja cython
python -m build --wheel -Csetup-args=-Dbuildtype=release -Csetup-args=-Db_ndebug=if-release -Csetup-args=-Db_lto=true
pip install dist\numpy-*.whl
```

---

<a id="한국어"></a>
## 🇰🇷 한국어

### 이것은 무엇입니까?

이것은 NumPy 2.5.0(최신 개발 버전)의 **Python 3.8 백포트**입니다. 공식 NumPy는 2.0부터 Python 3.8 지원을 중단했습니다. 이 포크는 최신 NumPy 기능과 버그 수정을 Python 3.8에 백포트하여 Python 버전을 업그레이드할 수 없는 사용자가 최신 개선 사항을 활용할 수 있도록 합니다.

### 변경 사항 및 수정

1. **`pythoncapi_compat.h` 수정** — Python 3.8 헤더에 이미 존재하는 API 재정의를 방지하기 위해 버전 검사 업데이트.
2. **Meson 빌드 시스템 업데이트** — 번들된 meson 버전을 1.5.1에서 1.9.2로 업데이트.
3. **`pyproject.toml` 조정** — SPDX 라이선스 표현식으로 변경.
4. **최대 최적화 컴파일** — `/O2 /fp:fast /Oi /GS-`, LTO 활성화, SIMD 자동 감지.

### 주요 기능

- Python 3.8에서 전체 NumPy 2.5.0 API 사용 가능
- Windows x64 최대 성능 최적화
- Python 3.8용 SciPy 백포트와 호환

### 디버깅 결과

마지막 네이티브 Python 3.8 NumPy 버전(1.24.x)과 비교:

| 기능 | NumPy 1.24.x | 이 백포트 |
|------|-------------|----------|
| 기본 작업 | ✅ | ✅ |
| 선형 대수 | ✅ | ✅ |
| 2.x 새 기능 | ❌ | ✅ |
| 성능 | 기준선 | 향상(LTO + /O2) |

### 컴파일 방법

```batch
pip install meson-python meson ninja cython
python -m build --wheel -Csetup-args=-Dbuildtype=release -Csetup-args=-Db_ndebug=if-release -Csetup-args=-Db_lto=true
pip install dist\numpy-*.whl
```

---

<a id="français"></a>
## 🇫🇷 Français

### Qu'est-ce que c'est ?

Il s'agit d'un **backport Python 3.8** de NumPy 2.5.0 (dernière version de développement). Le NumPy officiel a abandonné la prise en charge de Python 3.8 à partir de NumPy 2.0. Ce fork rétroporte les dernières fonctionnalités et corrections de bugs vers Python 3.8.

### Modifications et corrections

1. **Corrections de `pythoncapi_compat.h`** — Mise à jour des vérifications de version pour éviter la redéfinition des API déjà présentes dans les en-têtes Python 3.8.
2. **Mise à jour du système de construction Meson** — Version meson passée de 1.5.1 à 1.9.2.
3. **Ajustements de `pyproject.toml`** — Expression de licence SPDX.
4. **Compilation avec optimisation maximale** — `/O2 /fp:fast /Oi /GS-`, LTO activé, SIMD auto-détecté.

### Fonctionnalités clés

- API complète NumPy 2.5.0 disponible sur Python 3.8
- Optimisation de performance maximale pour Windows x64
- Compatible avec le backport SciPy pour Python 3.8

### Résultats de débogage

Comparé à la dernière version NumPy native Python 3.8 (1.24.x) :

| Fonctionnalité | NumPy 1.24.x | Ce backport |
|---------------|-------------|------------|
| Opérations de base | ✅ | ✅ |
| Algèbre linéaire | ✅ | ✅ |
| Nouvelles fonctionnalités 2.x | ❌ | ✅ |
| Performance | Référence | Améliorée (LTO + /O2) |

### Comment compiler

```batch
pip install meson-python meson ninja cython
python -m build --wheel -Csetup-args=-Dbuildtype=release -Csetup-args=-Db_ndebug=if-release -Csetup-args=-Db_lto=true
pip install dist\numpy-*.whl
```

---

<a id="русский"></a>
## 🇷🇺 Русский

### Что это?

Это **бэкпорт для Python 3.8** NumPy 2.5.0 (последняя версия разработки). Официальный NumPy прекратил поддержку Python 3.8 начиная с версии 2.0. Этот форк переносит последние функции и исправления ошибок на Python 3.8.

### Изменения и исправления

1. **Исправления `pythoncapi_compat.h`** — Обновлены проверки версий для предотвращения переопределения API, уже присутствующих в заголовках Python 3.8.
2. **Обновление системы сборки Meson** — Версия meson обновлена с 1.5.1 до 1.9.2.
3. **Корректировки `pyproject.toml`** — Использовано выражение лицензии SPDX.
4. **Компиляция с максимальной оптимизацией** — `/O2 /fp:fast /Oi /GS-`, LTO включён, SIMD автоопределение.

### Ключевые возможности

- Полный API NumPy 2.5.0 доступен на Python 3.8
- Максимальная оптимизация производительности для Windows x64
- Совместим с бэкпортом SciPy для Python 3.8

### Результаты отладки

По сравнению с последней нативной версией NumPy для Python 3.8 (1.24.x):

| Функция | NumPy 1.24.x | Этот бэкпорт |
|---------|-------------|-------------|
| Базовые операции | ✅ | ✅ |
| Линейная алгебра | ✅ | ✅ |
| Новые функции 2.x | ❌ | ✅ |
| Производительность | Базовый уровень | Улучшена (LTO + /O2) |

### Как скомпилировать

```batch
pip install meson-python meson ninja cython
python -m build --wheel -Csetup-args=-Dbuildtype=release -Csetup-args=-Db_ndebug=if-release -Csetup-args=-Db_lto=true
pip install dist\numpy-*.whl
```

---

<a id="español"></a>
## 🇪🇸 Español

### ¿Qué es esto?

Este es un **backport para Python 3.8** de NumPy 2.5.0 (última versión de desarrollo). El NumPy oficial dejó de soportar Python 3.8 a partir de NumPy 2.0. Este fork retroporta las últimas características y correcciones de errores a Python 3.8.

### Cambios y correcciones

1. **Correcciones de `pythoncapi_compat.h`** — Actualización de verificaciones de versión para evitar la redefinición de APIs ya presentes en los encabezados de Python 3.8.
2. **Actualización del sistema de construcción Meson** — Versión de meson actualizada de 1.5.1 a 1.9.2.
3. **Ajustes de `pyproject.toml`** — Expresión de licencia SPDX.
4. **Compilación con optimización máxima** — `/O2 /fp:fast /Oi /GS-`, LTO habilitado, SIMD autodetectado.

### Características clave

- API completa de NumPy 2.5.0 disponible en Python 3.8
- Optimización de rendimiento máxima para Windows x64
- Compatible con el backport de SciPy para Python 3.8

### Resultados de depuración

Comparado con la última versión nativa de NumPy para Python 3.8 (1.24.x):

| Característica | NumPy 1.24.x | Este backport |
|---------------|-------------|--------------|
| Operaciones básicas | ✅ | ✅ |
| Álgebra lineal | ✅ | ✅ |
| Nuevas funciones 2.x | ❌ | ✅ |
| Rendimiento | Línea base | Mejorado (LTO + /O2) |

### Cómo compilar

```batch
pip install meson-python meson ninja cython
python -m build --wheel -Csetup-args=-Dbuildtype=release -Csetup-args=-Db_ndebug=if-release -Csetup-args=-Db_lto=true
pip install dist\numpy-*.whl
```

---

<a id="deutsch"></a>
## 🇩🇪 Deutsch

### Was ist das?

Dies ist ein **Python 3.8-Backport** von NumPy 2.5.0 (neueste Entwicklungsversion). Das offizielle NumPy hat die Python 3.8-Unterstützung ab NumPy 2.0 eingestellt. Dieser Fork portiert die neuesten Funktionen und Fehlerbehebungen auf Python 3.8 zurück.

### Änderungen und Korrekturen

1. **`pythoncapi_compat.h`-Korrekturen** — Versionsprüfungen aktualisiert, um Neudefinition von APIs zu vermeiden, die bereits in Python 3.8-Headern vorhanden sind.
2. **Meson-Build-System-Update** — Gebündelte Meson-Version von 1.5.1 auf 1.9.2 aktualisiert.
3. **`pyproject.toml`-Anpassungen** — SPDX-Lizenzausdruck verwendet.
4. **Kompilierung mit maximaler Optimierung** — `/O2 /fp:fast /Oi /GS-`, LTO aktiviert, SIMD-Autoerkennung.

### Hauptfunktionen

- Volles NumPy 2.5.0-API unter Python 3.8 verfügbar
- Maximale Leistungsoptimierung für Windows x64
- Kompatibel mit dem SciPy-Backport für Python 3.8

### Debugging-Ergebnisse

Im Vergleich zur letzten nativen Python 3.8 NumPy-Version (1.24.x):

| Funktion | NumPy 1.24.x | Dieser Backport |
|----------|-------------|----------------|
| Grundoperationen | ✅ | ✅ |
| Lineare Algebra | ✅ | ✅ |
| Neue 2.x-Funktionen | ❌ | ✅ |
| Leistung | Basiswert | Verbessert (LTO + /O2) |

### Kompilierungsanleitung

```batch
pip install meson-python meson ninja cython
python -m build --wheel -Csetup-args=-Dbuildtype=release -Csetup-args=-Db_ndebug=if-release -Csetup-args=-Db_lto=true
pip install dist\numpy-*.whl
```

---

## License

NumPy is licensed under the [BSD-3-Clause License](https://opensource.org/licenses/BSD-3-Clause).
