"""
Message Format Encoder/Decoder Module

This module provides classes for encoding and decoding messages with:
- Length-prefix framing
- Checksum validation
- Version negotiation
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import struct
import hashlib
from typing import Optional, Tuple, Union
from enum import IntEnum


class MessageFormat(IntEnum):
    """Supported message format versions"""
    V1 = 1
    V2 = 2


class Encoder:
    """Encodes messages with length-prefix framing, checksum, and version info"""
    
    def __init__(self, version: MessageFormat = MessageFormat.V2):
        self.version = version
    
    def encode(self, data: Union[str, bytes]) -> bytes:
        """
        Encode data into a framed message
        
        Args:
            data: String or bytes to encode
            
        Returns:
            Encoded message as bytes
            
        Raises:
            TypeError: If data is not string or bytes
        """
        if isinstance(data, str):
            payload = data.encode('utf-8')
        elif isinstance(data, bytes):
            payload = data
        else:
            raise TypeError("Data must be string or bytes")
        
        # Create message based on version
        if self.version == MessageFormat.V1:
            # V1: [version][length][payload]
            version_bytes = struct.pack('!B', self.version)
            length_bytes = struct.pack('!I', len(payload))
            message = version_bytes + length_bytes + payload
        else:  # V2
            # V2: [version][length][checksum][payload]
            version_bytes = struct.pack('!B', self.version)
            length_bytes = struct.pack('!I', len(payload))
            checksum = hashlib.md5(payload).digest()
            message = version_bytes + length_bytes + checksum + payload
        
        return message


class Decoder:
    """Decodes framed messages with checksum validation and version support"""
    
    def __init__(self, supported_versions: Optional[set] = None):
        if supported_versions is None:
            self.supported_versions = {MessageFormat.V1, MessageFormat.V2}
        else:
            self.supported_versions = supported_versions
    
    def decode(self, message: bytes) -> Tuple[MessageFormat, bytes]:
        """
        Decode a framed message
        
        Args:
            message: Encoded message bytes
            
        Returns:
            Tuple of (version, payload)
            
        Raises:
            ValueError: If message format is invalid or checksum fails
            NotImplementedError: If message version is not supported
        """
        if len(message) < 5:  # Minimum: version(1) + length(4)
            raise ValueError("Message too short")
        
        # Extract version
        version = MessageFormat(struct.unpack('!B', message[0:1])[0])
        if version not in self.supported_versions:
            raise NotImplementedError(f"Unsupported version: {version}")
        
        # Extract length
        length = struct.unpack('!I', message[1:5])[0]
        
        # Process based on version
        if version == MessageFormat.V1:
            if len(message) < 5 + length:
                raise ValueError("Incomplete message")
            payload = message[5:5 + length]
        else:  # V2
            if len(message) < 5 + 16 + length:  # version(1) + length(4) + checksum(16)
                raise ValueError("Incomplete message")
            
            checksum = message[5:21]
            payload = message[21:21 + length]
            
            # Validate checksum
            expected_checksum = hashlib.md5(payload).digest()
            if checksum != expected_checksum:
                raise ValueError("Checksum validation failed")
        
        return version, payload


def negotiate_version(encoder_version: MessageFormat, 
                     decoder_supported: set) -> Tuple[bool, Optional[MessageFormat]]:
    """
    Negotiate compatible message format version
    
    Args:
        encoder_version: Version preferred by encoder
        decoder_supported: Set of versions supported by decoder
        
    Returns:
        Tuple of (compatible, negotiated_version)
    """
    if encoder_version in decoder_supported:
        return True, encoder_version
    return False, None


if __name__ == "__main__":
    # Self-test: byte-exact round-trips on both protocol versions,
    # corruption caught, version negotiation exact, unsupported refused.
    test_messages = ["Hello, World!", "Python encoding demo",
                     b"Binary data test \x00\xff", "Special chars: !@#$%^&*()"]

    # V1 and V2: every message round-trips byte-exactly, version echoed.
    for fmt, decoder in ((MessageFormat.V1, Decoder({MessageFormat.V1})),
                         (MessageFormat.V2, Decoder({MessageFormat.V1,
                                                     MessageFormat.V2}))):
        encoder = Encoder(fmt)
        for msg in test_messages:
            encoded = encoder.encode(msg)
            version, decoded = decoder.decode(encoded)
            original = msg.encode("utf-8") if isinstance(msg, str) else msg
            assert decoded == original, \
                f"{fmt} round-trip corrupted {msg!r} -> {decoded!r}"
            assert version == fmt.value, f"decoder reported version {version}"
        # The wire form differs from the plaintext (it IS an encoding).
        assert encoder.encode("test") != b"test"

    # A V2 message decodes in a V1+V2 decoder as V2, not V1.
    v2_blob = Encoder(MessageFormat.V2).encode("check")
    version, _ = Decoder({MessageFormat.V1, MessageFormat.V2}).decode(v2_blob)
    assert version == MessageFormat.V2.value

    # THE DISASTER: corrupt the checksum region — must be caught, not decoded.
    encoded = Encoder(MessageFormat.V2).encode("test")
    corrupted = encoded[:5] + b"\x00" * 16 + encoded[21:]
    try:
        Decoder().decode(corrupted)
        assert False, "checksum corruption decoded successfully"
    except ValueError:
        pass

    # Unsupported version: a V1-only decoder must refuse V2 frames.
    v2_frame = Encoder(MessageFormat.V2).encode("test")
    try:
        Decoder({MessageFormat.V1}).decode(v2_frame)
        assert False, "V1-only decoder accepted a V2 frame"
    except NotImplementedError:
        pass

    # Version negotiation: exact tuples.
    assert negotiate_version(MessageFormat.V2, {MessageFormat.V1}) == (False, None)
    assert negotiate_version(MessageFormat.V1,
                             {MessageFormat.V1, MessageFormat.V2}) == \
        (True, MessageFormat.V1)
    assert negotiate_version(MessageFormat.V2,
                             {MessageFormat.V2}) == (True, MessageFormat.V2)

    n_ok = len(test_messages) * 2
    assert n_ok == 8, "4 messages x 2 versions must be 8 round-trips"
    print("message_encoder: 8/8 round-trips byte-exact (incl. binary), "
          "checksum corruption caught, V1-only refused V2, negotiation exact — PASS")
