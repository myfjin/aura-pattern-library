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
    """Demo of TOTP functionality."""
    print("=== TOTP Generator and Validator Demo ===\n")
    
    # Generate a secret
    secret = TOTP.generate_secret()
    print(f"Generated secret: {secret}")
    
    # Create TOTP instance
    totp = TOTP(secret, digits=6, interval=30)
    print(f"TOTP configuration: {totp.digits} digits, {totp.interval}s interval\n")
    
    # Generate current token
    current_token = totp.generate()
    print(f"Current TOTP token: {current_token}")
    
    # Validate current token
    is_valid, offset = totp.validate(current_token)
    print(f"Token validation: {'Valid' if is_valid else 'Invalid'} (offset: {offset})")
    
    # Test invalid token
    is_valid, offset = totp.validate("123456")
    print(f"Invalid token validation: {'Valid' if is_valid else 'Invalid'}")
    
    # Generate provisioning URI
    uri = totp.provisioning_uri("user@example.com", "DemoApp")
    print(f"\nProvisioning URI: {uri}")
    print("You can use this URI to generate a QR code for authenticator apps")
    
    # Test with time drift
    print("\n=== Testing with time drift ===")
    future_time = time.time() + 60  # 1 minute in the future
    future_token = totp.generate(future_time)
    print(f"Future token (60s): {future_token}")
    
    # Validate with window
    is_valid, offset = totp.validate(future_token, window=2)
    print(f"Future token validation with window=2: {'Valid' if is_valid else 'Invalid'} (offset: {offset})")
    
    # Show token changes over time
    print("\n=== Token changes over time ===")
    for i in range(5):
        token = totp.generate()
        print(f"{time.strftime('%H:%M:%S')}: {token}")
        time.sleep(5)


if __name__ == "__main__":
    main()