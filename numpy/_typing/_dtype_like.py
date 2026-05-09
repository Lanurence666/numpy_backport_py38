from __future__ import annotations

from collections.abc import Sequence
from typing import Any, Protocol, TypedDict, runtime_checkable, Generic, TypeVar, Union, Tuple, List, Type
try:
    from typing import TypeAlias
except ImportError:
    from typing_extensions import TypeAlias
try:
    from typing import NotRequired
except ImportError:
    from typing_extensions import NotRequired

import numpy as np

from ._char_codes import (
    _BoolCodes,
    _BytesCodes,
    _ComplexFloatingCodes,
    _DT64Codes,
    _FloatingCodes,
    _NumberCodes,
    _ObjectCodes,
    _SignedIntegerCodes,
    _StrCodes,
    _TD64Codes,
    _UnsignedIntegerCodes,
    _VoidCodes,
)

DTypeT = TypeVar('DTypeT', bound=np.dtype)
ScalarT = TypeVar('ScalarT', bound=np.generic)

_DTypeLikeNested: TypeAlias = Any  # TODO: wait for support for recursive types


class _DTypeDict(TypedDict):
    names: Sequence[str]
    formats: Sequence[_DTypeLikeNested]
    # Only `str` elements are usable as indexing aliases,
    # but `titles` can in principle accept any object
    offsets: NotRequired[Sequence[int]]
    titles: NotRequired[Sequence[Any]]
    itemsize: NotRequired[int]
    aligned: NotRequired[bool]


# A protocol for anything with the dtype attribute
@runtime_checkable
class _HasDType(Protocol, Generic[DTypeT]):
    @property
    def dtype(self) -> DTypeT: ...


class _HasNumPyDType(Protocol, Generic[DTypeT]):
    @property
    def __numpy_dtype__(self, /) -> DTypeT: ...


_SupportsDType: TypeAlias = Union[_HasDType[DTypeT], _HasNumPyDType[DTypeT]]


# A subset of `npt.DTypeLike` that can be parametrized w.r.t. `np.generic`
_DTypeLike: TypeAlias = Union[Type[ScalarT], np.dtype[ScalarT], _SupportsDType[np.dtype[ScalarT]]]


# Would create a dtype[np.void]
_VoidDTypeLike: TypeAlias = Union[
    # If a tuple, then it can be either:
    # - (flexible_dtype, itemsize)
    # - (fixed_dtype, shape)
    # - (base_dtype, new_dtype)
    # But because `_DTypeLikeNested = Any`, the first two cases are redundant

    # Tuple[_DTypeLikeNested, int] | Tuple[_DTypeLikeNested, _ShapeLike] |
    Tuple[_DTypeLikeNested, _DTypeLikeNested],

    # [(field_name, field_dtype, field_shape), ...]
    # The type here is quite broad because NumPy accepts quite a wide
    # range of inputs inside the list; see the tests for some examples.
    List[Any],

    # {'names': ..., 'formats': ..., 'offsets': ..., 'titles': ..., 'itemsize': ...}
    _DTypeDict,
]

# Aliases for commonly used dtype-like objects.
# Note that the precision of `np.number` subclasses is ignored herein.
_DTypeLikeBool: TypeAlias = Union[Type[bool], _DTypeLike[np.bool], _BoolCodes]
_DTypeLikeInt: TypeAlias = Union[Type[int], _DTypeLike[np.signedinteger], _SignedIntegerCodes]
_DTypeLikeUInt: TypeAlias = Union[_DTypeLike[np.unsignedinteger], _UnsignedIntegerCodes]
_DTypeLikeFloat: TypeAlias = Union[Type[float], _DTypeLike[np.floating], _FloatingCodes]
_DTypeLikeComplex: TypeAlias = Union[Type[complex], _DTypeLike[np.complexfloating], _ComplexFloatingCodes]
_DTypeLikeComplex_co: TypeAlias = Union[Type[complex], _DTypeLike[Union[np.bool, np.number]], _BoolCodes, _NumberCodes]
_DTypeLikeDT64: TypeAlias = Union[_DTypeLike[np.timedelta64], _TD64Codes]
_DTypeLikeTD64: TypeAlias = Union[_DTypeLike[np.datetime64], _DT64Codes]
_DTypeLikeBytes: TypeAlias = Union[Type[bytes], _DTypeLike[np.bytes_], _BytesCodes]
_DTypeLikeStr: TypeAlias = Union[Type[str], _DTypeLike[np.str_], _StrCodes]
_DTypeLikeVoid: TypeAlias = Union[Type[memoryview], _DTypeLike[np.void], _VoidDTypeLike, _VoidCodes]
_DTypeLikeObject: TypeAlias = Union[Type[object], _DTypeLike[np.object_], _ObjectCodes]


# Anything that can be coerced into numpy.dtype.
# Reference: https://docs.scipy.org/doc/numpy/reference/arrays.dtypes.html
DTypeLike: TypeAlias = Union[type, str, np.dtype, _SupportsDType[np.dtype], _VoidDTypeLike]

# NOTE: while it is possible to provide the dtype as a dict of
# dtype-like objects (e.g. `{'field1': ..., 'field2': ..., ...}`),
# this syntax is officially discouraged and
# therefore not included in the type-union defining `DTypeLike`.
#
# See https://github.com/numpy/numpy/issues/16891 for more details.
