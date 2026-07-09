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
    # Demo: Encode and decode messages with different versions
    print("Message Encoder/Decoder Demo")
    print("=" * 40)
    
    # Test data
    test_messages = [
        "Hello, World!",
        "Python encoding demo",
        b"Binary data test",
        "Special chars: !@#$%^&*()"
    ]
    
    # Test V1 encoding/decoding
    print("\nTesting V1 Protocol:")
    encoder_v1 = Encoder(MessageFormat.V1)
    decoder_v1 = Decoder({MessageFormat.V1})
    
    for msg in test_messages:
        try:
            encoded = encoder_v1.encode(msg)
            version, decoded = decoder_v1.decode(encoded)
            original = msg.encode('utf-8') if isinstance(msg, str) else msg
            status = "✓ PASS" if original == decoded else "✗ FAIL"
            print(f"  {status} | {msg} -> V{version} -> {decoded}")
        except Exception as e:
            print(f"  ✗ ERROR | {msg} -> {e}")
    
    # Test V2 encoding/decoding
    print("\nTesting V2 Protocol:")
    encoder_v2 = Encoder(MessageFormat.V2)
    decoder_v2 = Decoder({MessageFormat.V1, MessageFormat.V2})
    
    for msg in test_messages:
        try:
            encoded = encoder_v2.encode(msg)
            version, decoded = decoder_v2.decode(encoded)
            original = msg.encode('utf-8') if isinstance(msg, str) else msg
            status = "✓ PASS" if original == decoded else "✗ FAIL"
            print(f"  {status} | {msg} -> V{version} -> {decoded}")
        except Exception as e:
            print(f"  ✗ ERROR | {msg} -> {e}")
    
    # Test version negotiation
    print("\nTesting Version Negotiation:")
    compatible, negotiated = negotiate_version(MessageFormat.V2, {MessageFormat.V1})
    print(f"  V2 with V1-only decoder: Compatible={compatible}, Negotiated={negotiated}")
    
    compatible, negotiated = negotiate_version(MessageFormat.V1, {MessageFormat.V1, MessageFormat.V2})
    print(f"  V1 with V1/V2 decoder: Compatible={compatible}, Negotiated={negotiated}")
    
    # Test error cases
    print("\nTesting Error Handling:")
    
    # Test checksum failure
    try:
        encoder = Encoder(MessageFormat.V2)
        encoded = encoder.encode("test")
        # Corrupt the checksum
        corrupted = encoded[:5] + b'\x00' * 16 + encoded[21:]
        decoder = Decoder()
        decoder.decode(corrupted)
        print("  ✗ FAIL | Checksum corruption not detected")
    except ValueError as e:
        print(f"  ✓ PASS | Checksum error detected: {e}")
    
    # Test unsupported version
    try:
        decoder = Decoder({MessageFormat.V1})
        encoder = Encoder(MessageFormat.V2)
        encoded = encoder.encode("test")
        decoder.decode(encoded)
        print("  ✗ FAIL | Unsupported version not detected")
    except NotImplementedError as e:
        print(f"  ✓ PASS | Unsupported version error: {e}")
    
    print("\nDemo completed successfully!")