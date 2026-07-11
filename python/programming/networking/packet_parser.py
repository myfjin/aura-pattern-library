#!/usr/bin/env python3
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import struct
from typing import List, Dict, Any, Optional, Tuple
from dataclasses import dataclass
from enum import Enum
import hashlib


class PacketType(Enum):
    """Enumeration of supported packet types."""
    DATA = 0x01
    ACK = 0x02
    NACK = 0x03
    CONTROL = 0x04


@dataclass
class Field:
    """Represents a field in a packet with its metadata."""
    name: str
    format: str
    offset: int
    size: int


class ChecksumError(Exception):
    """Raised when packet checksum validation fails."""
    pass


class Packet:
    """Represents a network packet with header and payload."""
    
    def __init__(self, data: bytes):
        """Initialize packet with raw data."""
        if not isinstance(data, bytes):
            raise TypeError("Packet data must be bytes")
        if len(data) < 8:  # Minimum packet size (header only)
            raise ValueError("Packet data too short")
        self._data = data
        self._fields: Dict[str, Any] = {}
        self._parsed = False
    
    def __len__(self) -> int:
        """Return packet length."""
        return len(self._data)
    
    def __bytes__(self) -> bytes:
        """Return raw packet data."""
        return self._data
    
    @property
    def data(self) -> bytes:
        """Get raw packet data."""
        return self._data
    
    @property
    def fields(self) -> Dict[str, Any]:
        """Get parsed fields."""
        if not self._parsed:
            raise RuntimeError("Packet not parsed yet")
        return self._fields
    
    def get_field(self, name: str) -> Any:
        """Get a specific field value."""
        if not self._parsed:
            raise RuntimeError("Packet not parsed yet")
        return self._fields.get(name)
    
    def validate_checksum(self) -> bool:
        """Validate packet checksum."""
        if len(self._data) < 8:
            return False
        
        # Simple checksum: sum of all bytes except last 2 (checksum field)
        calculated = sum(self._data[:-2]) & 0xFFFF
        stored = struct.unpack(">H", self._data[-2:])[0]
        return calculated == stored


class Parser:
    """Parser for network packets with configurable field definitions."""
    
    def __init__(self):
        """Initialize parser with default field definitions."""
        self._field_definitions: Dict[PacketType, List[Field]] = {
            PacketType.DATA: [
                Field("sync", "B", 0, 1),
                Field("type", "B", 1, 1),
                Field("length", ">H", 2, 2),
                Field("sequence", ">H", 4, 2),
                Field("payload", None, 6, -2),  # runs to the checksum trailer
                Field("checksum", ">H", -2, 2)
            ],
            PacketType.ACK: [
                Field("sync", "B", 0, 1),
                Field("type", "B", 1, 1),
                Field("length", ">H", 2, 2),
                Field("sequence", ">H", 4, 2),
                Field("checksum", ">H", -2, 2)
            ],
            PacketType.NACK: [
                Field("sync", "B", 0, 1),
                Field("type", "B", 1, 1),
                Field("length", ">H", 2, 2),
                Field("sequence", ">H", 4, 2),
                Field("checksum", ">H", -2, 2)
            ],
            PacketType.CONTROL: [
                Field("sync", "B", 0, 1),
                Field("type", "B", 1, 1),
                Field("length", ">H", 2, 2),
                Field("command", "B", 4, 1),
                Field("payload", None, 5, -2),
                Field("checksum", ">H", -2, 2)
            ]
        }
    
    def add_field_definition(self, packet_type: PacketType, fields: List[Field]) -> None:
        """Add or update field definitions for a packet type."""
        if not isinstance(packet_type, PacketType):
            raise TypeError("packet_type must be a PacketType")
        if not isinstance(fields, list):
            raise TypeError("fields must be a list")
        self._field_definitions[packet_type] = fields
    
    def parse(self, packet: Packet) -> Packet:
        """Parse packet fields according to its type."""
        if len(packet.data) < 2:
            raise ValueError("Packet too short to determine type")
        
        # Extract packet type
        packet_type_value = packet.data[1]
        try:
            packet_type = PacketType(packet_type_value)
        except ValueError:
            raise ValueError(f"Unknown packet type: {packet_type_value}")
        
        # Get field definitions for this packet type
        if packet_type not in self._field_definitions:
            raise ValueError(f"No field definitions for packet type: {packet_type}")
        
        fields = self._field_definitions[packet_type]
        parsed_fields = {}
        
        # Parse each field
        for field in fields:
            if field.name == "payload" and field.size == -1:
                # Variable length field - calculate from length field
                length = parsed_fields.get("length", 0)
                header_size = 6  # sync + type + length + sequence + checksum
                payload_length = length - header_size
                if payload_length > 0:
                    start = field.offset
                    end = start + payload_length
                    if end <= len(packet.data) - 2:  # -2 for checksum
                        parsed_fields[field.name] = packet.data[start:end]
                    else:
                        parsed_fields[field.name] = b""
                else:
                    parsed_fields[field.name] = b""
            elif field.format:
                # Fixed size field
                start = field.offset if field.offset >= 0 else len(packet.data) + field.offset
                end = start + field.size
                if end <= len(packet.data):
                    value = struct.unpack(field.format, packet.data[start:end])[0]
                    parsed_fields[field.name] = value
                else:
                    raise ValueError(f"Field {field.name} extends beyond packet boundary")
            else:
                # Raw bytes field
                start = field.offset
                end = start + field.size if field.size > 0 else len(packet.data) + field.size
                if start < len(packet.data) and end <= len(packet.data):
                    parsed_fields[field.name] = packet.data[start:end]
                else:
                    parsed_fields[field.name] = b""
        
        packet._fields = parsed_fields
        packet._parsed = True
        return packet
    
    def create_packet(self, packet_type: PacketType, **kwargs) -> Packet:
        """Create a new packet with specified fields."""
        if packet_type == PacketType.DATA:
            sequence = kwargs.get("sequence", 0)
            payload = kwargs.get("payload", b"")
            length = 6 + len(payload)  # header + payload

            # Header + payload, checksum appended as a 2-byte trailer
            data = struct.pack(">BBHH", 0xAA, packet_type.value, length, sequence)
            data += payload
            data += struct.pack(">H", sum(data) & 0xFFFF)

        elif packet_type in (PacketType.ACK, PacketType.NACK):
            sequence = kwargs.get("sequence", 0)
            length = 6  # header only

            data = struct.pack(">BBHH", 0xAA, packet_type.value, length, sequence)
            data += struct.pack(">H", sum(data) & 0xFFFF)

        elif packet_type == PacketType.CONTROL:
            command = kwargs.get("command", 0)
            payload = kwargs.get("payload", b"")
            length = 5 + len(payload)  # header + command + payload

            data = struct.pack(">BBHB", 0xAA, packet_type.value, length, command)
            data += payload
            data += struct.pack(">H", sum(data) & 0xFFFF)

        else:
            raise ValueError(f"Unsupported packet type: {packet_type}")
        
        return Packet(data)


def main():
    """Self-test: create→parse round-trip field-exact for all 3 packet types,
    corruption caught by the checksum, unknown type refused."""
    parser = Parser()

    # DATA round-trip: every field comes back exactly.
    data_packet = parser.create_packet(PacketType.DATA, sequence=42,
                                       payload=b"Hello, World!")
    parsed = parser.parse(data_packet).fields
    assert parsed["sequence"] == 42, f"sequence lost: {parsed['sequence']}"
    assert parsed["payload"] == b"Hello, World!", f"payload corrupted: {parsed['payload']}"
    assert parsed["length"] == 6 + 13, f"length must be header 6 + payload 13, got {parsed['length']}"
    assert data_packet.validate_checksum() is True, "fresh packet failed its own checksum"
    # Wire format: magic byte and type on the wire are exact.
    assert data_packet.data[0] == 0xAA and data_packet.data[1] == PacketType.DATA.value

    # ACK: header-only, sequence exact.
    ack = parser.create_packet(PacketType.ACK, sequence=1000)
    ack_fields = parser.parse(ack).fields
    assert ack_fields["sequence"] == 1000
    assert ack.validate_checksum() is True
    assert len(ack.data) == 8, f"ACK wire size must be 8 bytes, got {len(ack.data)}"

    # CONTROL: command + payload.
    ctrl = parser.create_packet(PacketType.CONTROL, command=0x05, payload=b"config")
    ctrl_fields = parser.parse(ctrl).fields
    assert ctrl_fields["command"] == 5, f"command lost: {ctrl_fields['command']}"
    assert ctrl_fields["payload"] == b"config"
    assert ctrl.validate_checksum() is True

    # THE DISASTER: flip bits anywhere — the checksum must catch it.
    caught = 0
    for byte_idx in (1, 3, 8):
        corrupted = bytearray(data_packet.data)
        corrupted[byte_idx] ^= 0xFF
        if Packet(bytes(corrupted)).validate_checksum() is False:
            caught += 1
    assert caught == 3, f"checksum caught only {caught}/3 corruptions"

    # Empty payload is legal and round-trips.
    empty = parser.create_packet(PacketType.DATA, sequence=0, payload=b"")
    assert parser.parse(empty).fields["payload"] == b""
    assert empty.validate_checksum() is True

    # Binary payload with checksum-relevant bytes survives.
    blob = bytes(range(256))[:50]
    binp = parser.create_packet(PacketType.DATA, sequence=7, payload=blob)
    assert parser.parse(binp).fields["payload"] == blob, "binary payload mangled"

    # Unknown packet type is refused at parse.
    unknown = Packet(struct.pack(">BBHHH", 0xAA, 0xFF, 6, 42, 0x1234))
    try:
        parser.parse(unknown)
        assert False, "unknown packet type parsed"
    except (ValueError, KeyError):
        pass
    try:
        parser.create_packet(PacketType.HEARTBEAT if hasattr(PacketType, "HEARTBEAT") else None)  # type: ignore[arg-type]
        assert False, "unsupported type accepted by create_packet"
    except (ValueError, AttributeError, TypeError):
        pass

    print("packet_parser: DATA/ACK/CONTROL round-trips exact (len 19, ACK 8B), "
          "3/3 corruptions caught, binary payload safe, unknown type refused — PASS")


if __name__ == "__main__":
    main()