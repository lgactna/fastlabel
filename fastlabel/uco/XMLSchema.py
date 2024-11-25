"""
Manually created file that defines XML Schema types for UCO.
"""

import base64
import re
from typing import Any, Optional

from pydantic import GetCoreSchemaHandler
from pydantic_core import core_schema


class xsd_byte(int):
    """Represents xsd:byte (-128 to 127)"""

    def __new__(cls, value: Any) -> "xsd_byte":
        value = int(value)
        if not (-(2**7) <= value < 2**7):
            raise ValueError("Value out of range for xsd:byte")
        return super().__new__(cls, value)

    @classmethod
    def __get_pydantic_core_schema__(
        cls, source_type: type, handler: GetCoreSchemaHandler
    ) -> core_schema.CoreSchema:
        return core_schema.int_schema(
            ge=-128,
            lt=128,
            serialization=core_schema.to_string_ser_schema(),
        )


class xsd_unsignedInt(int):
    """Represents xsd:unsignedInt (0 to 4294967295)"""

    def __new__(cls, value: Any) -> "xsd_unsignedInt":
        value = int(value)
        if not (0 <= value < 2**32):
            raise ValueError("Value out of range for xsd:unsignedInt")
        return super().__new__(cls, value)

    @classmethod
    def __get_pydantic_core_schema__(
        cls, source_type: type, handler: GetCoreSchemaHandler
    ) -> core_schema.CoreSchema:
        return core_schema.int_schema(
            ge=0,
            lt=2**32,
            serialization=core_schema.to_string_ser_schema(),
        )


class xsd_unsignedShort(int):
    """Represents xsd:unsignedShort (0 to 65535)"""

    def __new__(cls, value: Any) -> "xsd_unsignedShort":
        value = int(value)
        if not (0 <= value < 2**16):
            raise ValueError("Value out of range for xsd:unsignedShort")
        return super().__new__(cls, value)

    @classmethod
    def __get_pydantic_core_schema__(
        cls, source_type: type, handler: GetCoreSchemaHandler
    ) -> core_schema.CoreSchema:
        return core_schema.int_schema(
            ge=0,
            lt=2**16,
            serialization=core_schema.to_string_ser_schema(),
        )


class xsd_positiveInteger(int):
    """Represents xsd:positiveInteger (> 0)"""

    def __new__(cls, value: Any) -> "xsd_positiveInteger":
        value = int(value)
        if value <= 0:
            raise ValueError("Value must be positive (> 0)")
        return super().__new__(cls, value)

    @classmethod
    def __get_pydantic_core_schema__(
        cls, source_type: type, handler: GetCoreSchemaHandler
    ) -> core_schema.CoreSchema:
        return core_schema.int_schema(
            gt=0,
            serialization=core_schema.to_string_ser_schema(),
        )


# Duration type


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

    @classmethod
    def __get_pydantic_core_schema__(
        cls, source_type: type, handler: GetCoreSchemaHandler
    ) -> core_schema.CoreSchema:
        # Use regex validator to match ISO 8601 duration format
        return core_schema.no_info_plain_validator_function(
            cls._validate_duration,
            serialization=core_schema.to_string_ser_schema(),
        )

    @classmethod
    def _validate_duration(cls, value: Any) -> "xsd_duration":
        if isinstance(value, cls):
            return value
        if not isinstance(value, str):
            raise TypeError("xsd_duration must be a string")
        return cls(value)


# Binary types


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

    @classmethod
    def __get_pydantic_core_schema__(
        cls, source_type: type, handler: GetCoreSchemaHandler
    ) -> core_schema.CoreSchema:
        # Use validator function to ensure correct hexBinary format
        return core_schema.no_info_plain_validator_function(
            cls._validate_hex_binary,
            serialization=core_schema.to_string_ser_schema(),
        )

    @classmethod
    def _validate_hex_binary(cls, value: Any) -> "xsd_hexBinary":
        if isinstance(value, cls):
            return value
        if not isinstance(value, str):
            raise TypeError("xsd_hexBinary must be a string")
        return cls(value)


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

    @classmethod
    def __get_pydantic_core_schema__(
        cls, source_type: type, handler: GetCoreSchemaHandler
    ) -> core_schema.CoreSchema:
        # Use validator function to ensure correct base64Binary format
        return core_schema.no_info_plain_validator_function(
            cls._validate_base64_binary,
            serialization=core_schema.to_string_ser_schema(),
        )

    @classmethod
    def _validate_base64_binary(cls, value: Any) -> "xsd_base64Binary":
        if isinstance(value, cls):
            return value
        if not isinstance(value, str):
            raise TypeError("xsd_base64Binary must be a string")
        return cls(value)


# AnyURI type


class xsd_anyURI(str):
    """Represents xsd:anyURI"""

    # Optionally, add URI validation

    @classmethod
    def __get_pydantic_core_schema__(
        cls, source_type: type, handler: GetCoreSchemaHandler
    ) -> core_schema.CoreSchema:
        # Simple string schema; can add URI validation if desired
        return core_schema.str_schema(
            serialization=core_schema.to_string_ser_schema(),
        )
