"""
Secure Envelope Module

This module provides a secure envelope implementation using HMAC-SHA256 for
message authentication and integrity verification. It includes key rotation
capabilities and tamper detection.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import hmac
import hashlib
import secrets
import json
import base64
from typing import Dict, List, Optional, Tuple, Any
from datetime import datetime, timedelta


class KeyRing:
    """Manages a collection of cryptographic keys with rotation support."""
    
    def __init__(self, max_keys: int = 5):
        """
        Initialize the KeyRing.
        
        Args:
            max_keys: Maximum number of keys to keep in rotation
        """
        self._keys: Dict[str, bytes] = {}
        self._key_ids: List[str] = []
        self._max_keys = max_keys
        self._current_key_id: Optional[str] = None
        
    def add_key(self, key_id: str, key: bytes) -> None:
        """
        Add a key to the keyring.
        
        Args:
            key_id: Unique identifier for the key
            key: The key bytes
        """
        if not isinstance(key, bytes):
            raise TypeError("Key must be bytes")
        
        if len(key) < 32:
            raise ValueError("Key must be at least 32 bytes")
            
        self._keys[key_id] = key
        self._key_ids.append(key_id)
        
        if self._current_key_id is None:
            self._current_key_id = key_id
            
        # Rotate out old keys if we exceed max_keys
        while len(self._key_ids) > self._max_keys:
            old_key_id = self._key_ids.pop(0)
            del self._keys[old_key_id]
            if self._current_key_id == old_key_id:
                self._current_key_id = self._key_ids[0] if self._key_ids else None
    
    def generate_key(self, key_id: Optional[str] = None) -> str:
        """
        Generate a new secure key and add it to the keyring.
        
        Args:
            key_id: Optional key identifier, auto-generated if None
            
        Returns:
            The key identifier of the generated key
        """
        if key_id is None:
            key_id = secrets.token_urlsafe(16)
            
        key = secrets.token_bytes(32)
        self.add_key(key_id, key)
        self._current_key_id = key_id
        return key_id
    
    def get_key(self, key_id: str) -> Optional[bytes]:
        """
        Retrieve a key by its identifier.
        
        Args:
            key_id: The key identifier
            
        Returns:
            The key bytes or None if not found
        """
        return self._keys.get(key_id)
    
    def get_current_key_id(self) -> Optional[str]:
        """
        Get the current key identifier.
        
        Returns:
            Current key identifier or None if no keys
        """
        return self._current_key_id
    
    def rotate_key(self) -> str:
        """
        Generate and set a new key as current.
        
        Returns:
            The new key identifier
        """
        new_key_id = self.generate_key()
        self._current_key_id = new_key_id
        return new_key_id


class Envelope:
    """Secure envelope for sealing and opening messages with HMAC-SHA256."""
    
    def __init__(self, keyring: KeyRing):
        """
        Initialize the Envelope with a KeyRing.
        
        Args:
            keyring: KeyRing instance to use for sealing/opening
        """
        if not isinstance(keyring, KeyRing):
            raise TypeError("keyring must be a KeyRing instance")
        self._keyring = keyring
    
    def seal(self, message: bytes, metadata: Optional[Dict[str, Any]] = None) -> str:
        """
        Seal a message with HMAC-SHA256 authentication.
        
        Args:
            message: The message to seal
            metadata: Optional metadata to include
            
        Returns:
            Base64-encoded sealed envelope
            
        Raises:
            ValueError: If no current key is available
        """
        if not isinstance(message, bytes):
            raise TypeError("Message must be bytes")
            
        current_key_id = self._keyring.get_current_key_id()
        if current_key_id is None:
            raise ValueError("No current key available for sealing")
            
        key = self._keyring.get_key(current_key_id)
        if key is None:
            raise ValueError("Current key not found")
        
        # Prepare envelope data
        envelope_data = {
            "key_id": current_key_id,
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "message": base64.b64encode(message).decode('utf-8')
        }
        
        if metadata:
            envelope_data["metadata"] = metadata
            
        # Create JSON payload
        payload = json.dumps(envelope_data, separators=(',', ':'))
        payload_bytes = payload.encode('utf-8')
        
        # Generate HMAC signature
        signature = hmac.new(key, payload_bytes, hashlib.sha256).digest()
        
        # Create final envelope with signature
        sealed_envelope = {
            "payload": payload,
            "signature": base64.b64encode(signature).decode('utf-8')
        }
        
        # Return as base64-encoded JSON
        return base64.b64encode(
            json.dumps(sealed_envelope, separators=(',', ':')).encode('utf-8')
        ).decode('utf-8')
    
    def open(self, sealed_envelope: str) -> Tuple[bytes, Dict[str, Any], str]:
        """
        Open and verify a sealed envelope.
        
        Args:
            sealed_envelope: Base64-encoded sealed envelope
            
        Returns:
            Tuple of (message, metadata, key_id)
            
        Raises:
            ValueError: If envelope is tampered or malformed
            KeyError: If key is not found
        """
        try:
            # Decode the envelope
            envelope_bytes = base64.b64decode(sealed_envelope.encode('utf-8'))
            envelope = json.loads(envelope_bytes.decode('utf-8'))
            
            payload = envelope["payload"]
            signature = base64.b64decode(envelope["signature"].encode('utf-8'))
            
            # Parse payload
            payload_data = json.loads(payload)
            key_id = payload_data["key_id"]
            timestamp = payload_data["timestamp"]
            encoded_message = payload_data["message"]
            
            # Get the key
            key = self._keyring.get_key(key_id)
            if key is None:
                raise KeyError(f"Key with ID '{key_id}' not found")
            
            # Verify signature
            expected_signature = hmac.new(
                key, payload.encode('utf-8'), hashlib.sha256
            ).digest()
            
            if not hmac.compare_digest(signature, expected_signature):
                raise ValueError("HMAC verification failed - possible tampering")
            
            # Decode message
            message = base64.b64decode(encoded_message.encode('utf-8'))
            metadata = payload_data.get("metadata", {})
            
            return message, metadata, key_id
            
        except (json.JSONDecodeError, KeyError, base64.binascii.Error) as e:
            raise ValueError(f"Invalid envelope format: {e}")
        except Exception as e:
            raise ValueError(f"Failed to open envelope: {e}")


def main():
    """Self-test: seal→open round-trip byte-exact, THE ATTACKS actually run
    (payload tampering, wrong keyring, garbage) and every one is refused."""
    keyring = KeyRing(max_keys=3)
    key_id1 = keyring.generate_key("initial-key")
    envelope = Envelope(keyring)

    # Round-trip: bytes and metadata come back exactly.
    messages = [b"Hello, World!", b"Secret message for Alice", b"\x00\xff binary \x7f"]
    sealed_messages = []
    for i, msg in enumerate(messages):
        sealed = envelope.seal(msg, {"sender": "user1", "n": i})
        sealed_messages.append(sealed)
    opened = [envelope.open(s) for s in sealed_messages]
    for i, (message, metadata, key_id) in enumerate(opened):
        assert message == messages[i], f"message {i} corrupted in round-trip"
        assert metadata == {"sender": "user1", "n": i}, f"metadata {i} corrupted"
        assert key_id == key_id1
    assert sum(m[1]["n"] for m in opened) == 3, "metadata n-values 0+1+2 must sum to 3"
    assert opened[2][0] == b"\x00\xff binary \x7f", "binary payload mangled"

    # Two seals of the same message differ (timestamped envelopes)
    # but both open to the same plaintext.
    s1, s2 = envelope.seal(b"same"), envelope.seal(b"same")
    assert envelope.open(s1)[0] == envelope.open(s2)[0] == b"same"

    # Key rotation: new seals use the new key; OLD envelopes still open
    # while the old key remains on the ring.
    key_id2 = keyring.rotate_key()
    assert key_id2 != key_id1
    new_sealed = envelope.seal(b"with new key")
    message, _, key_id = envelope.open(new_sealed)
    assert message == b"with new key" and key_id == key_id2, "seal not using rotated key"
    assert envelope.open(sealed_messages[0])[0] == messages[0], \
        "rotation broke old envelopes while their key is still on the ring"

    # ATTACK 1: wrong keyring — must refuse, not decrypt garbage.
    stranger = Envelope(KeyRing())
    stranger._keyring.generate_key("wrong-key")
    try:
        stranger.open(sealed_messages[0])
        assert False, "envelope opened by a keyring that never held the key"
    except (ValueError, KeyError):
        pass

    # ATTACK 2: modify the payload, keep the old signature — HMAC must catch it.
    env_data = json.loads(base64.b64decode(sealed_messages[0]))
    payload = json.loads(env_data["payload"])
    payload["message"] = base64.b64encode(b"Tampered message").decode()
    env_data["payload"] = json.dumps(payload, separators=(",", ":"))
    tampered = base64.b64encode(json.dumps(env_data, separators=(",", ":")).encode()).decode()
    try:
        envelope.open(tampered)
        assert False, "TAMPERED payload opened successfully"
    except ValueError as e:
        assert "tamper" in str(e).lower() or "HMAC" in str(e), \
            f"tampering error must say why: {e}"

    # ATTACK 3: flip one character of the sealed blob.
    flipped = sealed_messages[0][:-2] + ("A" if sealed_messages[0][-2] != "A" else "B") \
        + sealed_messages[0][-1]
    try:
        envelope.open(flipped)
        assert False, "bit-flipped envelope opened"
    except ValueError:
        pass

    # ATTACK 4: plain garbage.
    try:
        envelope.open("bm90IGFuIGVudmVsb3Bl")
        assert False, "garbage accepted as an envelope"
    except ValueError:
        pass

    print("secure_envelope: 3 round-trips byte-exact (incl. binary), rotation "
          "keeps old envelopes, 4/4 attacks refused — PASS")


if __name__ == "__main__":
    main()