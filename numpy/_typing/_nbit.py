from __future__ import annotations
"""A module with the precisions of platform-specific `~numpy.number`s."""


try:
    from typing import TypeAlias
except ImportError:
    from typing_extensions import TypeAlias
from typing import Union

from ._nbit_base import _8Bit, _16Bit, _32Bit, _64Bit, _96Bit, _128Bit

# To-be replaced with a `npt.NBitBase` subclass by numpy's mypy plugin
_NBitByte: TypeAlias = _8Bit
_NBitShort: TypeAlias = _16Bit
_NBitIntC: TypeAlias = _32Bit
_NBitIntP: TypeAlias = Union[_32Bit, _64Bit]
_NBitInt: TypeAlias = _NBitIntP
_NBitLong: TypeAlias = Union[_32Bit, _64Bit]
_NBitLongLong: TypeAlias = _64Bit

_NBitHalf: TypeAlias = _16Bit
_NBitSingle: TypeAlias = _32Bit
_NBitDouble: TypeAlias = _64Bit
_NBitLongDouble: TypeAlias = Union[_64Bit, _96Bit, _128Bit]
