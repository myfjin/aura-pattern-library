"""
Time-Based One-Time Password (TOTP) generator and validator.

This module implements RFC 6238 TOTP and RFC 4226 HOTP algorithms for generating
and validating time-based one-time passwords. It includes functionality for
generating secrets, creating QR code URIs, and validating tokens with drift tolerance.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import hashlib
import hmac
import struct
import time
import base64
import secrets
import urllib.parse
from typing import Optional, Tuple


class HOTP:
    """HMAC-based One-Time Password (RFC 4226) generator and validator."""
    
    def __init__(self, secret: str, digits: int = 6):
        """
        Initialize HOTP instance.
        
        Args:
            secret: Base32 encoded secret key
            digits: Number of digits in the OTP (default: 6)
        """
        self.secret = secret
        self.digits = digits
        if not 6 <= digits <= 10:
            raise ValueError("Digits must be between 6 and 10")
    
    def _base32_decode(self, secret: str) -> bytes:
        """Decode a base32 encoded string to bytes."""
        # Normalize the secret (remove spaces, pad to 8-character boundaries)
        secret = secret.upper().replace(" ", "")
        padding = '=' * ((8 - len(secret) % 8) % 8)
        return base64.b32decode(secret + padding)
    
    def _hotp(self, counter: int) -> str:
        """
        Generate HOTP for a given counter value.
        
        Args:
            counter: Counter value
            
        Returns:
            HOTP token as string
        """
        # Convert counter to 8-byte big-endian representation
        counter_bytes = struct.pack(">Q", counter)
        
        # Decode secret
        key = self._base32_decode(self.secret)
        
        # Generate HMAC-SHA1
        h = hmac.new(key, counter_bytes, hashlib.sha1).digest()
        
        # Dynamic truncation
        offset = h[-1] & 0x0F
        binary = ((h[offset] & 0x7F) << 24 |
                  (h[offset + 1] & 0xFF) << 16 |
                  (h[offset + 2] & 0xFF) << 8 |
                  (h[offset + 3] & 0xFF))
        
        # Generate OTP
        otp = str(binary % (10 ** self.digits)).zfill(self.digits)
        return otp
    
    def generate(self, counter: int) -> str:
        """
        Generate HOTP token for given counter.
        
        Args:
            counter: Counter value
            
        Returns:
            HOTP token
        """
        return self._hotp(counter)
    
    def validate(self, token: str, counter: int) -> bool:
        """
        Validate HOTP token against given counter.
        
        Args:
            token: Token to validate
            counter: Counter value
            
        Returns:
            True if valid, False otherwise
        """
        return token == self.generate(counter)


class TOTP:
    """Time-Based One-Time Password (RFC 6238) generator and validator."""
    
    def __init__(self, secret: str, digits: int = 6, interval: int = 30):
        """
        Initialize TOTP instance.
        
        Args:
            secret: Base32 encoded secret key
            digits: Number of digits in the OTP (default: 6)
            interval: Time interval in seconds (default: 30)
        """
        self.secret = secret
        self.digits = digits
        self.interval = interval
        self.hotp = HOTP(secret, digits)
        if not 6 <= digits <= 10:
            raise ValueError("Digits must be between 6 and 10")
        if interval <= 0:
            raise ValueError("Interval must be positive")
    
    @staticmethod
    def generate_secret() -> str:
        """
        Generate a random base32-encoded secret.
        
        Returns:
            Base32 encoded secret key
        """
        # Generate 20 random bytes (160 bits) as recommended by RFC 4226
        random_bytes = secrets.token_bytes(20)
        # Encode to base32 and remove padding
        secret = base64.b32encode(random_bytes).decode('utf-8').rstrip('=')
        return secret
    
    def _timecode(self, timestamp: Optional[float] = None) -> int:
        """
        Calculate timecode for given timestamp.
        
        Args:
            timestamp: Unix timestamp (default: current time)
            
        Returns:
            Timecode value
        """
        if timestamp is None:
            timestamp = time.time()
        return int(timestamp // self.interval)
    
    def generate(self, timestamp: Optional[float] = None) -> str:
        """
        Generate TOTP token for given timestamp.
        
        Args:
            timestamp: Unix timestamp (default: current time)
            
        Returns:
            TOTP token
        """
        timecode = self._timecode(timestamp)
        return self.hotp.generate(timecode)
    
    def validate(self, token: str, timestamp: Optional[float] = None, 
                 window: int = 1) -> Tuple[bool, int]:
        """
        Validate TOTP token with drift tolerance.
        
        Args:
            token: Token to validate
            timestamp: Unix timestamp (default: current time)
            window: Number of intervals to check before/after (default: 1)
            
        Returns:
            Tuple of (is_valid, counter_offset)
        """
        if timestamp is None:
            timestamp = time.time()
            
        timecode = self._timecode(timestamp)
        
        # Check current and surrounding timecodes
        for i in range(-window, window + 1):
            counter = timecode + i
            if self.hotp.validate(token, counter):
                return True, i
                
        return False, 0
    
    def provisioning_uri(self, name: str, issuer: Optional[str] = None) -> str:
        """
        Generate provisioning URI for QR code.
        
        Args:
            name: Account name
            issuer: Issuer name (optional)
            
        Returns:
            Provisioning URI
        """
        # URL encode parameters
        name = urllib.parse.quote(name, safe='')
        secret = self.secret
        
        # Build URI
        uri = f"otpauth://totp/{name}?secret={secret}"
        if issuer:
            issuer = urllib.parse.quote(issuer, safe='')
            uri += f"&issuer={issuer}"
            
        uri += f"&digits={self.digits}&period={self.interval}"
        return uri


def main():
    """Self-test against the RFC 4226 / RFC 6238 published test vectors —
    the strongest oracle a OTP implementation can face."""
    # RFC 4226 Appendix D: secret is the ASCII "12345678901234567890".
    rfc_secret = base64.b32encode(b"12345678901234567890").decode().rstrip("=")
    hotp = HOTP(rfc_secret, digits=6)

    rfc4226_truth = ["755224", "287082", "359152", "969429", "338314",
                     "254676", "287922", "162583", "399871", "520489"]
    for counter, expected in enumerate(rfc4226_truth):
        got = hotp.generate(counter)
        assert got == expected, \
            f"RFC 4226 vector failed at counter {counter}: got {got}, want {expected}"

    # validate() agrees with the vectors and refuses wrong tokens.
    assert hotp.validate("755224", 0) is True
    assert hotp.validate("755224", 1) is False, "token for counter 0 accepted at counter 1"
    assert hotp.validate("000000", 0) is False

    # RFC 6238 TOTP (SHA-1, 8 digits, 30s): published time/token pairs.
    totp8 = TOTP(rfc_secret, digits=8, interval=30)
    rfc6238_truth = [(59, "94287082"), (1111111109, "07081804"),
                     (1111111111, "14050471"), (1234567890, "89005924"),
                     (2000000000, "69279037")]
    for ts, expected in rfc6238_truth:
        got = totp8.generate(ts)
        assert got == expected, \
            f"RFC 6238 vector failed at t={ts}: got {got}, want {expected}"

    # Drift window: a token from one interval ago validates with window=1
    # at offset -1; a token from 3 intervals ago must NOT validate.
    totp = TOTP(rfc_secret, digits=6, interval=30)
    t = 1_111_111_109
    prev_token = totp.generate(t - 30)
    ok, offset = totp.validate(prev_token, timestamp=t, window=1)
    assert ok and offset == -1, f"1-interval drift must validate at offset -1, got {ok}/{offset}"
    stale = totp.generate(t - 90)
    ok, _ = totp.validate(stale, timestamp=t, window=1)
    assert ok is False, "3-interval-old token accepted inside window=1"

    # Determinism within an interval; change across intervals.
    assert totp.generate(990) == totp.generate(1019), "same interval, different tokens"
    assert totp.generate(990) != totp.generate(1020), "interval boundary did not rotate token"

    # Provisioning URI carries the exact secret and parameters.
    uri = totp.provisioning_uri("user@example.com", "DemoApp")
    assert f"secret={rfc_secret}" in uri and "issuer=DemoApp" in uri
    assert "digits=6" in uri and "period=30" in uri
    assert uri.startswith("otpauth://totp/user%40example.com")

    # Generated secrets are valid base32 and long enough.
    s = TOTP.generate_secret()
    assert len(s) >= 16
    HOTP(s).generate(0)  # must not raise

    print("hotp_totp: 10/10 RFC 4226 vectors, 5/5 RFC 6238 vectors, drift "
          "window -1 exact, stale refused, URI complete — PASS")


if __name__ == "__main__":
    main()