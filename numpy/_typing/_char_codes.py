from __future__ import annotations

from typing import Literal

_BoolCodes = Literal["bool", "bool_", "?", "b1", "|b1", "=b1", "<b1", ">b1"]

_Int8Codes = Literal["int8", "byte", "b", "i1", "|i1", "=i1", "<i1", ">i1"]
_Int16Codes = Literal["int16", "short", "h", "i2", "|i2", "=i2", "<i2", ">i2"]
_Int32Codes = Literal["int32", "i4", "|i4", "=i4", "<i4", ">i4"]
_Int64Codes = Literal["int64", "i8", "|i8", "=i8", "<i8", ">i8"]

_UInt8Codes = Literal["uint8", "ubyte", "B", "u1", "|u1", "=u1", "<u1", ">u1"]
_UInt16Codes = Literal["uint16", "ushort", "H", "u2", "|u2", "=u2", "<u2", ">u2"]
_UInt32Codes = Literal["uint32", "u4", "|u4", "=u4", "<u4", ">u4"]
_UInt64Codes = Literal["uint64", "u8", "|u8", "=u8", "<u8", ">u8"]

_IntCCodes = Literal["intc", "i", "|i", "=i", "<i", ">i"]
_LongCodes = Literal["long", "l", "|l", "=l", "<l", ">l"]
_LongLongCodes = Literal["longlong", "q", "|q", "=q", "<q", ">q"]
_IntPCodes = Literal["intp", "int", "int_", "n", "|n", "=n", "<n", ">n"]

_UIntCCodes = Literal["uintc", "I", "|I", "=I", "<I", ">I"]
_ULongCodes = Literal["ulong", "L", "|L", "=L", "<L", ">L"]
_ULongLongCodes = Literal["ulonglong", "Q", "|Q", "=Q", "<Q", ">Q"]
_UIntPCodes = Literal["uintp", "uint", "N", "|N", "=N", "<N", ">N"]

_Float16Codes = Literal["float16", "half", "e", "f2", "|f2", "=f2", "<f2", ">f2"]
_Float32Codes = Literal["float32", "single", "f", "f4", "|f4", "=f4", "<f4", ">f4"]
_Float64Codes = Literal[
    "float64", "float", "double", "d", "f8", "|f8", "=f8", "<f8", ">f8"
]

_LongDoubleCodes = Literal["longdouble", "g", "|g", "=g", "<g", ">g"]

_Complex64Codes = Literal[
    "complex64", "csingle", "F", "c8", "|c8", "=c8", "<c8", ">c8"
]

_Complex128Codes = Literal[
    "complex128", "complex", "cdouble", "D", "c16", "|c16", "=c16", "<c16", ">c16"
]

_CLongDoubleCodes = Literal["clongdouble", "G", "|G", "=G", "<G", ">G"]

_StrCodes = Literal["str", "str_", "unicode", "U", "|U", "=U", "<U", ">U"]
_BytesCodes = Literal["bytes", "bytes_", "S", "|S", "=S", "<S", ">S"]
_VoidCodes = Literal["void", "V", "|V", "=V", "<V", ">V"]
_ObjectCodes = Literal["object", "object_", "O", "|O", "=O", "<O", ">O"]

_DT64Codes_any = Literal["datetime64", "M", "M8", "|M8", "=M8", "<M8", ">M8"]
_DT64Codes_date = Literal[
    "datetime64[Y]", "M8[Y]", "|M8[Y]", "=M8[Y]", "<M8[Y]", ">M8[Y]",
    "datetime64[M]", "M8[M]", "|M8[M]", "=M8[M]", "<M8[M]", ">M8[M]",
    "datetime64[W]", "M8[W]", "|M8[W]", "=M8[W]", "<M8[W]", ">M8[W]",
    "datetime64[D]", "M8[D]", "|M8[D]", "=M8[D]", "<M8[D]", ">M8[D]",
]
_DT64Codes_datetime = Literal[
    "datetime64[h]", "M8[h]", "|M8[h]", "=M8[h]", "<M8[h]", ">M8[h]",
    "datetime64[m]", "M8[m]", "|M8[m]", "=M8[m]", "<M8[m]", ">M8[m]",
    "datetime64[s]", "M8[s]", "|M8[s]", "=M8[s]", "<M8[s]", ">M8[s]",
    "datetime64[ms]", "M8[ms]", "|M8[ms]", "=M8[ms]", "<M8[ms]", ">M8[ms]",
    "datetime64[us]", "M8[us]", "|M8[us]", "=M8[us]", "<M8[us]", ">M8[us]",
    "datetime64[\u03bcs]", "M8[\u03bcs]", "|M8[\u03bcs]", "=M8[\u03bcs]", "<M8[\u03bcs]", ">M8[\u03bcs]",
]
_DT64Codes_int = Literal[
    "datetime64[ns]", "M8[ns]", "|M8[ns]", "=M8[ns]", "<M8[ns]", ">M8[ns]",
    "datetime64[ps]", "M8[ps]", "|M8[ps]", "=M8[ps]", "<M8[ps]", ">M8[ps]",
    "datetime64[fs]", "M8[fs]", "|M8[fs]", "=M8[fs]", "<M8[fs]", ">M8[fs]",
    "datetime64[as]", "M8[as]", "|M8[as]", "=M8[as]", "<M8[as]", ">M8[as]",
]
_DT64Codes = Literal[
    _DT64Codes_any,
    _DT64Codes_date,
    _DT64Codes_datetime,
    _DT64Codes_int,
]

_TD64Codes_any = Literal["timedelta64", "m", "m8", "|m8", "=m8", "<m8", ">m8"]
_TD64Codes_int = Literal[
    "timedelta64[Y]", "m8[Y]", "|m8[Y]", "=m8[Y]", "<m8[Y]", ">m8[Y]",
    "timedelta64[M]", "m8[M]", "|m8[M]", "=m8[M]", "<m8[M]", ">m8[M]",
    "timedelta64[ns]", "m8[ns]", "|m8[ns]", "=m8[ns]", "<m8[ns]", ">m8[ns]",
    "timedelta64[ps]", "m8[ps]", "|m8[ps]", "=m8[ps]", "<m8[ps]", ">m8[ps]",
    "timedelta64[fs]", "m8[fs]", "|m8[fs]", "=m8[fs]", "<m8[fs]", ">m8[fs]",
    "timedelta64[as]", "m8[as]", "|m8[as]", "=m8[as]", "<m8[as]", ">m8[as]",
]
_TD64Codes_timedelta = Literal[
    "timedelta64[W]", "m8[W]", "|m8[W]", "=m8[W]", "<m8[W]", ">m8[W]",
    "timedelta64[D]", "m8[D]", "|m8[D]", "=m8[D]", "<m8[D]", ">m8[D]",
    "timedelta64[h]", "m8[h]", "|m8[h]", "=m8[h]", "<m8[h]", ">m8[h]",
    "timedelta64[m]", "m8[m]", "|m8[m]", "=m8[m]", "<m8[m]", ">m8[m]",
    "timedelta64[s]", "m8[s]", "|m8[s]", "=m8[s]", "<m8[s]", ">m8[s]",
    "timedelta64[ms]", "m8[ms]", "|m8[ms]", "=m8[ms]", "<m8[ms]", ">m8[ms]",
    "timedelta64[us]", "m8[us]", "|m8[us]", "=m8[us]", "<m8[us]", ">m8[us]",
    "timedelta64[\u03bcs]", "m8[\u03bcs]", "|m8[\u03bcs]", "=m8[\u03bcs]", "<m8[\u03bcs]", ">m8[\u03bcs]",
]
_TD64Codes = Literal[_TD64Codes_any, _TD64Codes_int, _TD64Codes_timedelta]

_StringCodes = Literal["T", "|T", "=T", "<T", ">T"]

_SignedIntegerCodes = Literal[
    _Int8Codes,
    _Int16Codes,
    _Int32Codes,
    _Int64Codes,
    _IntCCodes,
    _LongCodes,
    _LongLongCodes,
    _IntPCodes,
]
_UnsignedIntegerCodes = Literal[
    _UInt8Codes,
    _UInt16Codes,
    _UInt32Codes,
    _UInt64Codes,
    _UIntCCodes,
    _ULongCodes,
    _ULongLongCodes,
    _UIntPCodes,
]
_FloatingCodes = Literal[
    _Float16Codes,
    _Float32Codes,
    _Float64Codes,
    _LongDoubleCodes,
]
_ComplexFloatingCodes = Literal[
    _Complex64Codes,
    _Complex128Codes,
    _CLongDoubleCodes,
]
_IntegerCodes = Literal[_UnsignedIntegerCodes, _SignedIntegerCodes]
_InexactCodes = Literal[_FloatingCodes, _ComplexFloatingCodes]
_NumberCodes = Literal[_IntegerCodes, _InexactCodes]

_CharacterCodes = Literal[_BytesCodes, _StrCodes]
_FlexibleCodes = Literal[_CharacterCodes, _VoidCodes]

_GenericCodes = Literal[
    _BoolCodes,
    _NumberCodes,
    _FlexibleCodes,
    _DT64Codes,
    _TD64Codes,
    _ObjectCodes,
]
