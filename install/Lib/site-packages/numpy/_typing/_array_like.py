from __future__ import annotations

from collections.abc import Callable, Collection
try:
    from collections.abc import Buffer
except ImportError:
    try:
        from typing import Buffer, Type
    except ImportError:
        from typing import Any as Buffer
from typing import TYPE_CHECKING, Any, Protocol, runtime_checkable, Generic, TypeVar, Union, Tuple, Dict
try:
    from typing import TypeAlias
except ImportError:
    from typing_extensions import TypeAlias

import numpy as np

if TYPE_CHECKING:
    from numpy.dtypes import StringDType
else:
    from numpy._core.multiarray import StringDType

from ._nbit_base import _32Bit, _64Bit
from ._nested_sequence import _NestedSequence
from ._shape import _AnyShape

ScalarT = TypeVar('ScalarT', bound=np.generic)
DTypeT = TypeVar('DTypeT', bound=np.dtype)
BuiltinT = TypeVar('BuiltinT')

NDArray: TypeAlias = np.ndarray[_AnyShape, np.dtype[ScalarT]]

# The `_SupportsArray` protocol only cares about the default dtype
# (i.e. `dtype=None` or no `dtype` parameter at all) of the to-be returned
# array.
# Concrete implementations of the protocol are responsible for adding
# any and all remaining overloads
@runtime_checkable
class _SupportsArray(Protocol, Generic[DTypeT]):
    def __array__(self) -> np.ndarray[Any, DTypeT]: ...


@runtime_checkable
class _SupportsArrayFunc(Protocol):
    """A protocol class representing `~class.__array_function__`."""
    def __array_function__(
        self,
        func: Callable[..., Any],
        types: Collection[Type[Any]],
        args: Tuple[Any, ...],
        kwargs: Dict[str, Any],
    ) -> object: ...


# A subset of `npt.ArrayLike` that can be parametrized w.r.t. `np.generic`
_ArrayLike: TypeAlias = Union[_SupportsArray[np.dtype[ScalarT]], _NestedSequence[_SupportsArray[np.dtype[ScalarT]]]]

# A union representing array-like objects; consists of two typevars:
# One representing types that can be parametrized w.r.t. `np.dtype`
# and another one for the rest
_DualArrayLike: TypeAlias = Union[_SupportsArray[DTypeT], _NestedSequence[_SupportsArray[DTypeT]], BuiltinT, _NestedSequence[BuiltinT]]

ArrayLike: TypeAlias = Union[Buffer, _DualArrayLike[np.dtype, Union[complex, bytes, str]]]

# `ArrayLike<X>_co`: array-like objects that can be coerced into `X`
# given the casting rules `same_kind`
_ArrayLikeBool_co: TypeAlias = _DualArrayLike[np.dtype[np.bool], bool]
_ArrayLikeUInt_co: TypeAlias = _DualArrayLike[np.dtype[Union[np.bool, np.unsignedinteger]], bool]
_ArrayLikeInt_co: TypeAlias = _DualArrayLike[np.dtype[Union[np.bool, np.integer]], int]
_ArrayLikeFloat_co: TypeAlias = _DualArrayLike[
    np.dtype[Union[np.bool, np.integer, np.floating]],
    float,
]
_ArrayLikeComplex_co: TypeAlias = _DualArrayLike[np.dtype[Union[np.bool, np.number]], complex]
_ArrayLikeNumber_co: TypeAlias = _ArrayLikeComplex_co
_ArrayLikeTD64_co: TypeAlias = _DualArrayLike[
    np.dtype[Union[np.bool, np.integer, np.timedelta64]],
    int,
]
_ArrayLikeDT64_co: TypeAlias = _ArrayLike[np.datetime64]
_ArrayLikeObject_co: TypeAlias = _ArrayLike[np.object_]

_ArrayLikeVoid_co: TypeAlias = _ArrayLike[np.void]
_ArrayLikeBytes_co: TypeAlias = _DualArrayLike[np.dtype[np.bytes_], bytes]
_ArrayLikeStr_co: TypeAlias = _DualArrayLike[np.dtype[np.str_], str]
_ArrayLikeString_co: TypeAlias = _DualArrayLike[StringDType, str]
_ArrayLikeAnyString_co: TypeAlias = _DualArrayLike[
    Union[np.dtype[np.character], StringDType],
    Union[bytes, str],
]

__Float64_co: TypeAlias = Union[np.floating[_64Bit], np.float32, np.float16, np.integer, np.bool]
__Complex128_co: TypeAlias = Union[np.number[_64Bit], np.number[_32Bit], np.float16, np.integer, np.bool]
_ArrayLikeFloat64_co: TypeAlias = _DualArrayLike[np.dtype[__Float64_co], float]
_ArrayLikeComplex128_co: TypeAlias = _DualArrayLike[np.dtype[__Complex128_co], complex]

# NOTE: This includes `builtins.bool`, but not `numpy.bool`.
_ArrayLikeInt: TypeAlias = _DualArrayLike[np.dtype[np.integer], int]
