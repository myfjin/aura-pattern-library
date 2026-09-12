"""Leaked secret scan: detect secrets in code blobs via regex patterns.
Failure simulated: blob contains "password = 'hunter2'" and API key patterns;
scan detects and reports exact matches and line numbers.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import re
import tempfile
import os
from pathlib import Path

def leaked_secret_scan(blob, patterns=None):
    """Scan blob for leaked secrets matching patterns. Return list of matches."""
    if patterns is None:
        patterns = [
            r'password\s*=\s*["\']([^"\']+)["\']',
            r'api[_-]?key\s*[:=]\s*["\']?([a-zA-Z0-9_\-]+)["\']?',
            r'token\s*[:=]\s*["\']?([a-zA-Z0-9_\-]+)["\']?',
            r'secret\s*[:=]\s*["\']([^"\']+)["\']',
        ]

    matches = []
    lines = blob.split('\n')
    for line_num, line in enumerate(lines, start=1):
        for pattern in patterns:
            for match in re.finditer(pattern, line, re.IGNORECASE):
                secret_value = match.group(1) if match.groups() else match.group(0)
                matches.append({
                    'line': line_num,
                    'pattern': pattern,
                    'secret': secret_value,
                    'full_match': match.group(0),
                })
    return matches

if __name__ == "__main__":
    import random
    random.seed(42)

    with tempfile.TemporaryDirectory() as tmpdir:
        # Code blob with leaked secrets
        code_blob = """
def connect_database():
    host = "localhost"
    user = "admin"
    password = 'hunter2_secret_pass_123'
    return connect(host, user, password)

def get_api_client():
    api_key = 'sk_live_test_abcdef1234567890'
    client = APIClient(api_key=api_key)
    return client

def oauth_flow():
    token = 'ghp_token_xyz_secret_value'
    secret = 'secret_oauth_code_12345'
    return validate(token, secret)
"""

        # FAILURE SIM: scan for leaked secrets
        matches = leaked_secret_scan(code_blob)

        # RECOVERY ASSERT 1: found all secrets
        assert len(matches) >= 4, f"Expected at least 4 secrets, found {len(matches)}"

        # RECOVERY ASSERT 2: password pattern detected
        password_matches = [m for m in matches if 'password' in m['pattern'].lower()]
        assert len(password_matches) > 0, "Password pattern not detected"
        assert any('hunter2' in m['secret'] for m in password_matches), \
            "hunter2 password not found"

        # RECOVERY ASSERT 3: API key pattern detected
        api_matches = [m for m in matches if 'api' in m['pattern'].lower()]
        assert len(api_matches) > 0, "API key pattern not detected"
        assert any('sk_live' in m['secret'] for m in api_matches), \
            "sk_live API key not found"

        # RECOVERY ASSERT 4: line numbers are correct
        for match in matches:
            assert 'line' in match, "Match missing line number"
            assert match['line'] > 0, f"Invalid line number: {match['line']}"

        # RECOVERY ASSERT 5: secret values are extracted (not None)
        for match in matches:
            assert match['secret'], f"Secret value is empty: {match}"
            assert len(match['secret']) > 0, f"Secret has zero length: {match}"

        # RECOVERY ASSERT 6: full_match contains secret
        for match in matches:
            assert match['secret'] in match['full_match'], \
                f"Secret '{match['secret']}' not in full_match '{match['full_match']}'"

        print("leaked_secret_scan PASS")
