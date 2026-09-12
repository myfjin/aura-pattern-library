#!/usr/bin/env python3
"""
logline_parse: Parse syslog-style log lines (timestamp priority host process message).
THE ONE LAW: Parse messy real-world log data, assert exact extraction.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import re
import tempfile
import os

def parse_syslog_line(line):
    """
    Parse syslog format: "timestamp priority host process: message"
    Example: "Jul 10 12:34:56 myhost kernel[1234]: Out of memory"
    Return dict {timestamp, priority, host, process, pid, message} or None if unparseable.
    """
    # Syslog pattern: month day time host process[pid]: message
    pattern = r'^(\w+\s+\d+\s+[\d:]+)\s+(\S+)\s+(\S+)\[(\d+)\]:\s*(.*)$'
    match = re.match(pattern, line)
    if not match:
        return None

    timestamp, host, process, pid, message = match.groups()
    return {
        'timestamp': timestamp,
        'host': host,
        'process': process,
        'pid': int(pid),
        'message': message
    }

def parse_log_file(file_path):
    """Read log file and parse all lines. Return list of parsed dicts."""
    result = []
    try:
        with open(file_path) as f:
            for line in f:
                parsed = parse_syslog_line(line.rstrip('\n'))
                if parsed:
                    result.append(parsed)
    except IOError:
        return None
    return result

def main():
    # Synthetic syslog data.
    log_data = """Jul 10 12:34:56 myhost kernel[1234]: Out of memory
Jul 10 12:35:01 myhost sshd[5678]: Accepted publickey for user from 192.168.1.1 port 22 ssh2
Jul 10 12:35:15 myhost systemd[1]: Starting System Logging Service..."""

    lines = log_data.strip().split('\n')
    parsed_lines = [parse_syslog_line(line) for line in lines]

    # Verify first log line.
    assert parsed_lines[0] is not None, "First line should parse"
    assert parsed_lines[0]['host'] == 'myhost', "Host should be myhost"
    assert parsed_lines[0]['process'] == 'kernel', "Process should be kernel"
    assert parsed_lines[0]['pid'] == 1234, "PID should be 1234"
    assert 'memory' in parsed_lines[0]['message'].lower(), "Message should contain memory"

    # Verify second line.
    assert parsed_lines[1]['process'] == 'sshd', "Should parse sshd"
    assert parsed_lines[1]['pid'] == 5678, "PID should be 5678"
    assert 'publickey' in parsed_lines[1]['message'], "Message should contain publickey"

    # FAILURE SIMULATION: Malformed line (no pid in brackets).
    broken = "Jul 10 12:34:56 myhost kernel: Out of memory"
    assert parse_syslog_line(broken) is None, "Malformed line should return None"

    # Malformed: missing colon before message.
    broken2 = "Jul 10 12:34:56 myhost kernel[1234] Out of memory"
    assert parse_syslog_line(broken2) is None, "Missing colon should fail"

    # Test file parsing with temp file.
    with tempfile.NamedTemporaryFile(mode='w', suffix='.log', delete=False) as f:
        f.write(log_data)
        temp_file = f.name

    try:
        parsed = parse_log_file(temp_file)
        assert parsed is not None, "File should parse"
        assert len(parsed) == 3, f"Expected 3 lines, got {len(parsed)}"
        assert parsed[0]['host'] == 'myhost', "First entry host should match"
    finally:
        os.unlink(temp_file)

    # Edge case: Very long message.
    long_msg = "Jul 10 12:34:56 myhost systemd[1]: " + "x" * 1000
    long_parsed = parse_syslog_line(long_msg)
    assert long_parsed is not None, "Should handle long message"
    assert len(long_parsed['message']) == 1000, "Message should preserve length"

    print("✓ logline_parse passed")

if __name__ == '__main__':
    main()
