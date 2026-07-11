#!/usr/bin/env python3
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import re
from typing import Dict, List, Optional, Tuple, Any
from collections import defaultdict, Counter


class PatternMatcher:
    """A class to manage regex patterns with named groups for log parsing."""
    
    def __init__(self, pattern: str, name: str):
        """
        Initialize a PatternMatcher.
        
        Args:
            pattern: A regex pattern with named groups
            name: A name to identify this pattern
        """
        self.pattern = pattern
        self.name = name
        try:
            self.compiled_pattern = re.compile(pattern)
        except re.error as e:
            raise ValueError(f"Invalid regex pattern: {pattern}") from e
    
    def match(self, text: str) -> Optional[Dict[str, str]]:
        """
        Match text against the pattern and extract named groups.
        
        Args:
            text: Text to match against the pattern
            
        Returns:
            Dictionary of named groups if match found, None otherwise
        """
        match = self.compiled_pattern.match(text)
        if match:
            return match.groupdict()
        return None


class LogParser:
    """A log parser that uses pattern matchers to extract structured data."""
    
    def __init__(self):
        """Initialize the LogParser with an empty list of patterns."""
        self.patterns: List[PatternMatcher] = []
        self.match_counts: Dict[str, int] = defaultdict(int)
    
    def add_pattern(self, pattern: str, name: str) -> None:
        """
        Add a pattern to the parser.
        
        Args:
            pattern: A regex pattern with named groups
            name: A name to identify this pattern
        """
        self.patterns.append(PatternMatcher(pattern, name))
    
    def parse_line(self, line: str) -> Tuple[Optional[str], Optional[Dict[str, str]]]:
        """
        Parse a single log line using registered patterns.
        
        Args:
            line: A log line to parse
            
        Returns:
            Tuple of (pattern_name, extracted_data) if match found, (None, None) otherwise
        """
        for pattern_matcher in self.patterns:
            result = pattern_matcher.match(line)
            if result is not None:
                self.match_counts[pattern_matcher.name] += 1
                return (pattern_matcher.name, result)
        return (None, None)
    
    def parse_lines(self, lines: List[str]) -> List[Tuple[Optional[str], Optional[Dict[str, str]]]]:
        """
        Parse multiple log lines.
        
        Args:
            lines: List of log lines to parse
            
        Returns:
            List of parsed results
        """
        return [self.parse_line(line) for line in lines]
    
    def get_match_counts(self) -> Dict[str, int]:
        """
        Get counts of matches for each pattern.
        
        Returns:
            Dictionary mapping pattern names to match counts
        """
        return dict(self.match_counts)
    
    def reset_counts(self) -> None:
        """Reset all match counts to zero."""
        self.match_counts.clear()


def main():
    """Self-test: exact field extraction per format, unmatched lines report
    (None, None), match counts exact, first-pattern-wins ordering."""
    parser = LogParser()
    parser.add_pattern(
        r'(?P<ip>\d+\.\d+\.\d+\.\d+) - - \[(?P<timestamp>[^\]]+)\] "(?P<method>\w+) (?P<path>\S+) HTTP/[\d.]+" (?P<status>\d+) (?P<size>\d+)',
        "apache_common")
    parser.add_pattern(
        r'(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) \[(?P<level>\w+)\] (?P<message>.*)',
        "app_log")
    parser.add_pattern(
        r'(?P<user>\w+) logged in from (?P<ip>\d+\.\d+\.\d+\.\d+)',
        "login_event")

    log_lines = [
        '192.168.1.1 - - [10/Oct/2023:13:55:36 +0000] "GET /index.html HTTP/1.1" 200 2326',
        '192.168.1.2 - - [10/Oct/2023:13:55:37 +0000] "POST /api/login HTTP/1.1" 401 123',
        '2023-10-10 13:55:38 [INFO] Application started successfully',
        '2023-10-10 13:55:39 [ERROR] Database connection failed',
        'john logged in from 192.168.1.3',
        '2023-10-10 13:55:40 [DEBUG] Processing user request',
        'jane logged in from 192.168.1.4',
        'invalid log line that does not match any pattern',
        '192.168.1.5 - - [10/Oct/2023:13:55:41 +0000] "GET /favicon.ico HTTP/1.1" 404 0',
    ]
    results = parser.parse_lines(log_lines)

    # Exact field extraction for each format.
    name, data = results[0]
    assert name == "apache_common"
    assert data == {"ip": "192.168.1.1", "timestamp": "10/Oct/2023:13:55:36 +0000",
                    "method": "GET", "path": "/index.html", "status": "200",
                    "size": "2326"}, f"apache fields wrong: {data}"
    assert int(data["status"]) + int(data["size"]) == 2526, "200+2326 must be 2526"
    name, data = results[3]
    assert name == "app_log" and data["level"] == "ERROR"
    assert data["message"] == "Database connection failed"
    name, data = results[4]
    assert name == "login_event"
    assert data == {"user": "john", "ip": "192.168.1.3"}

    # Unmatched lines are honestly (None, None) — not force-fit.
    assert results[7] == (None, None), f"garbage line matched: {results[7]}"

    # Counts are exact per pattern.
    assert parser.get_match_counts() == {"apache_common": 3, "app_log": 3,
                                         "login_event": 2}, \
        f"match counts wrong: {parser.get_match_counts()}"

    # First-pattern-wins: a line matching two patterns credits the first.
    dual = LogParser()
    dual.add_pattern(r'(?P<word>\w+)', "greedy_first")
    dual.add_pattern(r'(?P<word>hello)', "specific_second")
    name, _ = dual.parse_line("hello world")
    assert name == "greedy_first", "pattern priority order not respected"

    # reset_counts really zeroes.
    parser.reset_counts()
    assert parser.get_match_counts() == {}

    # Invalid regex is refused at registration, not at match time.
    try:
        parser.add_pattern(r'(?P<broken', "bad")
        assert False, "invalid regex accepted"
    except ValueError:
        pass

    print("log_pattern_matcher: 3 formats extracted exactly (status+size 2526), "
          "counts 3/3/2, first-wins order, bad regex refused — PASS")


if __name__ == "__main__":
    main()