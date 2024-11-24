# """
# Manually created file that defines XML Schema types for UCO.
# """

import base64
import re
from typing import Any, Optional

# # Mapping of XSD datatypes to Python types or classes with constraints

# # String types
# xsd_string = str
# xsd_normalizedString = str
# xsd_token = str
# xsd_language = str
# xsd_Name = str
# xsd_NCName = str
# xsd_URI = str
# xsd_ID = str
# xsd_IDREF = str
# xsd_IDREFS = List["xsd_IDREF"]  # List of xsd_IDREF
# xsd_ENTITY = str
# xsd_ENTITIES = List["xsd_ENTITY"]  # List of xsd_ENTITY
# xsd_NMTOKEN = str
# xsd_NMTOKENS = List["xsd_NMTOKEN"]  # List of xsd_NMTOKEN

# # Boolean type
# xsd_boolean = bool

# # Numeric types
# xsd_decimal = decimal.Decimal
# xsd_float = float
# xsd_double = float


# # Integer types with constraints
# class xsd_integer(int):
#     """Represents xsd:integer"""


# class xsd_nonPositiveInteger(int):
#     """Represents xsd:nonPositiveInteger (<= 0)"""

#     def __new__(cls, value: Any) -> "xsd_nonPositiveInteger":
#         value = int(value)
#         if value > 0:
#             raise ValueError("Value must be non-positive (<= 0)")
#         return super().__new__(cls, value)


# class xsd_negativeInteger(int):
#     """Represents xsd:negativeInteger (< 0)"""

#     def __new__(cls, value: Any) -> "xsd_negativeInteger":
#         value = int(value)
#         if value >= 0:
#             raise ValueError("Value must be negative (< 0)")
#         return super().__new__(cls, value)


# class xsd_long(int):
#     """Represents xsd:long (-9223372036854775808 to 9223372036854775807)"""

#     def __new__(cls, value: Any) -> "xsd_long":
#         value = int(value)
#         if not (-(2**63) <= value < 2**63):
#             raise ValueError("Value out of range for xsd:long")
#         return super().__new__(cls, value)


# class xsd_int(int):
#     """Represents xsd:int (-2147483648 to 2147483647)"""

#     def __new__(cls, value: Any) -> "xsd_int":
#         value = int(value)
#         if not (-(2**31) <= value < 2**31):
#             raise ValueError("Value out of range for xsd:int")
#         return super().__new__(cls, value)


# class xsd_short(int):
#     """Represents xsd:short (-32768 to 32767)"""

#     def __new__(cls, value: Any) -> "xsd_short":
#         value = int(value)
#         if not (-(2**15) <= value < 2**15):
#             raise ValueError("Value out of range for xsd:short")
#         return super().__new__(cls, value)


class xsd_byte(int):
    """Represents xsd:byte (-128 to 127)"""

    def __new__(cls, value: Any) -> "xsd_byte":
        value = int(value)
        if not (-(2**7) <= value < 2**7):
            raise ValueError("Value out of range for xsd:byte")
        return super().__new__(cls, value)


# class xsd_nonNegativeInteger(int):
#     """Represents xsd:nonNegativeInteger (>= 0)"""

#     def __new__(cls, value: Any) -> "xsd_nonNegativeInteger":
#         value = int(value)
#         if value < 0:
#             raise ValueError("Value must be non-negative (>= 0)")
#         return super().__new__(cls, value)


# class xsd_unsignedLong(int):
#     """Represents xsd:unsignedLong (0 to 18446744073709551615)"""

#     def __new__(cls, value: Any) -> "xsd_unsignedLong":
#         value = int(value)
#         if not (0 <= value < 2**64):
#             raise ValueError("Value out of range for xsd:unsignedLong")
#         return super().__new__(cls, value)


class xsd_unsignedInt(int):
    """Represents xsd:unsignedInt (0 to 4294967295)"""

    def __new__(cls, value: Any) -> "xsd_unsignedInt":
        value = int(value)
        if not (0 <= value < 2**32):
            raise ValueError("Value out of range for xsd:unsignedInt")
        return super().__new__(cls, value)


class xsd_unsignedShort(int):
    """Represents xsd:unsignedShort (0 to 65535)"""

    def __new__(cls, value: Any) -> "xsd_unsignedShort":
        value = int(value)
        if not (0 <= value < 2**16):
            raise ValueError("Value out of range for xsd:unsignedShort")
        return super().__new__(cls, value)


# class xsd_unsignedByte(int):
#     """Represents xsd:unsignedByte (0 to 255)"""

#     def __new__(cls, value: Any) -> "xsd_unsignedByte":
#         value = int(value)
#         if not (0 <= value < 2**8):
#             raise ValueError("Value out of range for xsd:unsignedByte")
#         return super().__new__(cls, value)


class xsd_positiveInteger(int):
    """Represents xsd:positiveInteger (> 0)"""

    def __new__(cls, value: Any) -> "xsd_positiveInteger":
        value = int(value)
        if value <= 0:
            raise ValueError("Value must be positive (> 0)")
        return super().__new__(cls, value)


# # Date and time types
# class xsd_dateTime(datetime.datetime):
#     """Represents xsd:dateTime"""

#     @classmethod
#     def from_string(cls, value: str) -> "xsd_dateTime":
#         return cls.fromisoformat(value)


# class xsd_date(datetime.date):
#     """Represents xsd:date"""

#     @classmethod
#     def from_string(cls, value: str) -> "xsd_date":
#         return cls.fromisoformat(value)


# class xsd_time(datetime.time):
#     """Represents xsd:time"""

#     @classmethod
#     def from_string(cls, value: str) -> "xsd_time":
#         return cls.fromisoformat(value)


class xsd_duration:
    """Represents xsd:duration (ISO 8601 duration)"""

    def __init__(self, value: str):
        # Simplified parsing; for full support, use an ISO 8601 duration parser
        pattern = (
            r"^P(?:(\d+)Y)?(?:(\d+)M)?(?:(\d+)D)?"
            r"(?:T(?:(\d+)H)?(?:(\d+)M)?(?:(\d+(?:\.\d+)?)S)?)?$"
        )
        match = re.match(pattern, value)
        if not match:
            raise ValueError("Invalid xsd:duration format")
        self.years: Optional[int] = int(match.group(1)) if match.group(1) else None
        self.months: Optional[int] = int(match.group(2)) if match.group(2) else None
        self.days: Optional[int] = int(match.group(3)) if match.group(3) else None
        self.hours: Optional[int] = int(match.group(4)) if match.group(4) else None
        self.minutes: Optional[int] = int(match.group(5)) if match.group(5) else None
        self.seconds: Optional[float] = (
            float(match.group(6)) if match.group(6) else None
        )


# class xsd_gYear:
#     """Represents xsd:gYear"""

#     def __init__(self, value: str):
#         try:
#             self.year: int = int(value)
#         except ValueError:
#             raise ValueError("Invalid xsd:gYear format")


# class xsd_gMonth:
#     """Represents xsd:gMonth"""

#     def __init__(self, value: str):
#         if not value.startswith("--"):
#             raise ValueError("Invalid xsd:gMonth format")
#         try:
#             self.month: int = int(value[2:])
#             if not (1 <= self.month <= 12):
#                 raise ValueError("Invalid month in xsd:gMonth")
#         except ValueError:
#             raise ValueError("Invalid xsd:gMonth format")


# class xsd_gDay:
#     """Represents xsd:gDay"""

#     def __init__(self, value: str):
#         if not value.startswith("---"):
#             raise ValueError("Invalid xsd:gDay format")
#         try:
#             self.day: int = int(value[3:])
#             if not (1 <= self.day <= 31):
#                 raise ValueError("Invalid day in xsd:gDay")
#         except ValueError:
#             raise ValueError("Invalid xsd:gDay format")


# class xsd_gYearMonth:
#     """Represents xsd:gYearMonth"""

#     def __init__(self, value: str):
#         try:
#             self.date: datetime.datetime = datetime.datetime.strptime(value, "%Y-%m")
#         except ValueError:
#             raise ValueError("Invalid xsd:gYearMonth format")


# class xsd_gMonthDay:
#     """Represents xsd:gMonthDay"""

#     def __init__(self, value: str):
#         if not value.startswith("--"):
#             raise ValueError("Invalid xsd:gMonthDay format")
#         try:
#             self.month_day: datetime.datetime = datetime.datetime.strptime(
#                 value, "--%m-%d"
#             )
#         except ValueError:
#             raise ValueError("Invalid xsd:gMonthDay format")


# # Binary types
class xsd_hexBinary:
    """Represents xsd:hexBinary (hexadecimal string)"""

    def __init__(self, value: str):
        if not re.fullmatch(r"([0-9a-fA-F]{2})*", value):
            raise ValueError("Invalid xsd:hexBinary value")
        self.value: bytes = bytes.fromhex(value)

    def __bytes__(self) -> bytes:
        return self.value

    def __str__(self) -> str:
        return self.value.hex()


class xsd_base64Binary:
    """Represents xsd:base64Binary (base64 encoded data)"""

    def __init__(self, value: str):
        try:
            self.value: bytes = base64.b64decode(value, validate=True)
        except ValueError:
            raise ValueError("Invalid xsd:base64Binary value")

    def __bytes__(self) -> bytes:
        return self.value

    def __str__(self) -> str:
        return base64.b64encode(self.value).decode("ascii")


# AnyURI type
class xsd_anyURI(str):
    """Represents xsd:anyURI"""

    # Optionally, add URI validation


# # QName type
# class xsd_QName(str):
#     """Represents xsd:QName"""

#     # QName parsing requires namespace context; handled as string here


# # NOTATION type
# class xsd_NOTATION(str):
#     """Represents xsd:NOTATION"""


# # String types with patterns and constraints
# class xsd_normalizedString(str):
#     """Represents xsd:normalizedString (disallows line breaks and tabs)"""

#     def __new__(cls, value: str) -> "xsd_normalizedString":
#         if any(c in value for c in ["\r", "\n", "\t"]):
#             raise ValueError("Invalid character in xsd:normalizedString")
#         return super().__new__(cls, value)


# class xsd_token(str):
#     """Represents xsd:token (normalizedString without leading/trailing spaces and collapsing sequences of spaces)"""

#     def __new__(cls, value: str) -> "xsd_token":
#         value = " ".join(value.strip().split())
#         return super().__new__(cls, value)


# class xsd_language(str):
#     """Represents xsd:language (language codes as per RFC 3066)"""

#     def __new__(cls, value: str) -> "xsd_language":
#         if not re.fullmatch(r"[a-zA-Z]{1,8}(-[a-zA-Z0-9]{1,8})*", value):
#             raise ValueError("Invalid xsd:language value")
#         return super().__new__(cls, value)


# class xsd_Name(str):
#     """Represents xsd:Name (valid XML name)"""

#     def __new__(cls, value: str) -> "xsd_Name":
#         pattern = r"^[A-Za-z_:][A-Za-z0-9._:-]*$"
#         if not re.match(pattern, value):
#             raise ValueError("Invalid xsd:Name value")
#         return super().__new__(cls, value)


# class xsd_NCName(xsd_Name):
#     """Represents xsd:NCName (Name without colon)"""

#     def __new__(cls, value: str) -> "xsd_NCName":
#         if ":" in value:
#             raise ValueError("Invalid xsd:NCName value (contains ':')")
#         return super().__new__(cls, value)


# class xsd_ID(xsd_NCName):
#     """Represents xsd:ID"""


# class xsd_IDREF(xsd_NCName):
#     """Represents xsd:IDREF"""


# class xsd_IDREFS(List[xsd_IDREF]):
#     """Represents xsd:IDREFS (list of IDREFs)"""

#     def __init__(self, value: Union[str, List[str]]):
#         items = value.strip().split() if isinstance(value, str) else value
#         super().__init__(xsd_IDREF(item) for item in items)


# class xsd_ENTITY(xsd_NCName):
#     """Represents xsd:ENTITY"""


# class xsd_ENTITIES(List[xsd_ENTITY]):
#     """Represents xsd:ENTITIES (list of ENTITY)"""

#     def __init__(self, value: Union[str, List[str]]):
#         items = value.strip().split() if isinstance(value, str) else value
#         super().__init__(xsd_ENTITY(item) for item in items)


# class xsd_NMTOKEN(str):
#     """Represents xsd:NMTOKEN (tokens without spaces)"""

#     def __new__(cls, value: str) -> "xsd_NMTOKEN":
#         pattern = r"^\w+$"
#         if not re.match(pattern, value):
#             raise ValueError("Invalid xsd:NMTOKEN value")
#         return super().__new__(cls, value)


# class xsd_NMTOKENS(List[xsd_NMTOKEN]):
#     """Represents xsd:NMTOKENS (list of NMTOKEN)"""

#     def __init__(self, value: Union[str, List[str]]):
#         items = value.strip().split() if isinstance(value, str) else value
#         super().__init__(xsd_NMTOKEN(item) for item in items)
