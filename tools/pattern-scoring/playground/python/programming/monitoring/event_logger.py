"""
Structured event logger with rotation capabilities.

This module provides a complete logging solution that outputs structured
events in JSONL format with automatic log rotation based on file size.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import json
import os
import time
from abc import ABC, abstractmethod
from datetime import datetime
from typing import Any, Dict, List, Optional
from pathlib import Path


class LogFilter(ABC):
    """Abstract base class for log filters."""
    
    @abstractmethod
    def should_log(self, event: Dict[str, Any]) -> bool:
        """Determine if an event should be logged.
        
        Args:
            event: The event dictionary to evaluate
            
        Returns:
            True if the event should be logged, False otherwise
        """
        pass


class LevelFilter(LogFilter):
    """Filter events based on their log level."""
    
    def __init__(self, min_level: str = "INFO"):
        """Initialize the level filter.
        
        Args:
            min_level: Minimum level to log (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        """
        self.levels = {
            "DEBUG": 0,
            "INFO": 1,
            "WARNING": 2,
            "ERROR": 3,
            "CRITICAL": 4
        }
        self.min_level_value = self.levels.get(min_level.upper(), 1)
    
    def should_log(self, event: Dict[str, Any]) -> bool:
        """Check if event level meets minimum requirement.
        
        Args:
            event: Event dictionary with 'level' key
            
        Returns:
            True if event level is at or above minimum level
        """
        level = event.get("level", "INFO").upper()
        level_value = self.levels.get(level, 1)
        return level_value >= self.min_level_value


class KeywordFilter(LogFilter):
    """Filter events based on keywords in message."""
    
    def __init__(self, keywords: List[str], exclude: bool = False):
        """Initialize the keyword filter.
        
        Args:
            keywords: List of keywords to match
            exclude: If True, exclude matching events; if False, include only matching
        """
        self.keywords = [kw.lower() for kw in keywords]
        self.exclude = exclude
    
    def should_log(self, event: Dict[str, Any]) -> bool:
        """Check if event message contains specified keywords.
        
        Args:
            event: Event dictionary with 'message' key
            
        Returns:
            True if event should be logged based on keyword matching
        """
        message = event.get("message", "").lower()
        has_keyword = any(kw in message for kw in self.keywords)
        return not has_keyword if self.exclude else has_keyword


class LogRotator:
    """Handles log file rotation based on size."""
    
    def __init__(self, max_size_mb: int = 10, backup_count: int = 5):
        """Initialize the log rotator.
        
        Args:
            max_size_mb: Maximum file size in MB before rotation
            backup_count: Number of backup files to keep
        """
        self.max_size_bytes = max_size_mb * 1024 * 1024
        self.backup_count = backup_count
    
    def should_rotate(self, filepath: str) -> bool:
        """Check if log file should be rotated.
        
        Args:
            filepath: Path to the log file
            
        Returns:
            True if file should be rotated, False otherwise
        """
        if not os.path.exists(filepath):
            return False
        
        return os.path.getsize(filepath) >= self.max_size_bytes
    
    def rotate(self, filepath: str) -> None:
        """Perform log rotation.
        
        Args:
            filepath: Path to the log file to rotate
        """
        if not os.path.exists(filepath):
            return
        
        # Remove oldest backup if we have too many
        for i in range(self.backup_count, 0, -1):
            old_file = f"{filepath}.{i}"
            if os.path.exists(old_file):
                if i == self.backup_count:
                    os.remove(old_file)
                else:
                    os.rename(old_file, f"{filepath}.{i+1}")
        
        # Move current file to .1
        if os.path.exists(filepath):
            os.rename(filepath, f"{filepath}.1")


class EventLogger:
    """Structured event logger with filtering and rotation capabilities."""
    
    def __init__(
        self,
        filepath: str,
        filters: Optional[List[LogFilter]] = None,
        rotator: Optional[LogRotator] = None,
        auto_timestamp: bool = True
    ):
        """Initialize the event logger.
        
        Args:
            filepath: Path to the log file
            filters: List of filters to apply to events
            rotator: Log rotator instance
            auto_timestamp: Whether to automatically add timestamps
        """
        self.filepath = filepath
        self.filters = filters or []
        self.rotator = rotator or LogRotator()
        self.auto_timestamp = auto_timestamp
        
        # Ensure directory exists
        Path(filepath).parent.mkdir(parents=True, exist_ok=True)
    
    def _apply_filters(self, event: Dict[str, Any]) -> bool:
        """Apply all filters to determine if event should be logged.
        
        Args:
            event: Event dictionary to filter
            
        Returns:
            True if event passes all filters, False otherwise
        """
        return all(f.should_log(event) for f in self.filters)
    
    def log(self, event: Dict[str, Any]) -> None:
        """Log an event to the file.
        
        Args:
            event: Dictionary containing event data
        """
        # Add timestamp if requested
        if self.auto_timestamp and "timestamp" not in event:
            event["timestamp"] = datetime.utcnow().isoformat() + "Z"
        
        # Apply filters
        if not self._apply_filters(event):
            return
        
        # Check if rotation is needed
        if self.rotator.should_rotate(self.filepath):
            self.rotator.rotate(self.filepath)
        
        # Write event to file
        try:
            with open(self.filepath, "a", encoding="utf-8") as f:
                f.write(json.dumps(event, separators=(',', ':')) + "\n")
        except Exception as e:
            # In a production system, you might want to handle this differently
            print(f"Failed to write log entry: {e}")


def main():
    """Self-test: level filtering exact, JSONL round-trip, keyword filters
    both directions, rotation actually rotates with bounded backups."""
    import tempfile
    tmpdir = tempfile.mkdtemp(prefix="evlog_")
    log_file = os.path.join(tmpdir, "events.log")

    # Level filter INFO+: DEBUG dropped, the other four written.
    logger = EventLogger(filepath=log_file, filters=[LevelFilter(min_level="INFO")],
                         rotator=LogRotator(max_size_mb=1, backup_count=3),
                         auto_timestamp=True)
    events = [
        {"level": "DEBUG", "message": "debug msg", "component": "demo"},
        {"level": "INFO", "message": "started", "component": "main"},
        {"level": "WARNING", "message": "low disk", "available_gb": 2.5},
        {"level": "ERROR", "message": "db down", "error_code": 500},
        {"level": "INFO", "message": "login", "user_id": "user123"},
    ]
    for e in events:
        logger.log(dict(e))

    with open(log_file) as f:
        written = [json.loads(line) for line in f]
    assert len(written) == 4, f"INFO+ filter must keep 4 of 5 events, kept {len(written)}"
    assert all(w["level"] != "DEBUG" for w in written), "DEBUG leaked past the filter"

    # JSONL round-trip preserves fields and types exactly.
    err = next(w for w in written if w["level"] == "ERROR")
    assert err["error_code"] == 500 and isinstance(err["error_code"], int)
    warn = next(w for w in written if w["level"] == "WARNING")
    assert warn["available_gb"] == 2.5
    assert all("timestamp" in w for w in written), "auto_timestamp missing"

    # Keyword filter, include and exclude directions.
    inc = KeywordFilter(["error", "warning"])
    assert inc.should_log({"message": "an ERROR happened"}) is True
    assert inc.should_log({"message": "all fine"}) is False
    exc = KeywordFilter(["heartbeat"], exclude=True)
    assert exc.should_log({"message": "heartbeat ok"}) is False
    assert exc.should_log({"message": "real event"}) is True

    # Multiple filters AND together.
    both = EventLogger(filepath=os.path.join(tmpdir, "both.log"),
                       filters=[LevelFilter("INFO"), inc], auto_timestamp=False)
    both.log({"level": "ERROR", "message": "error in db"})     # passes both
    both.log({"level": "ERROR", "message": "quiet failure"})   # fails keyword
    both.log({"level": "DEBUG", "message": "error detail"})    # fails level
    with open(os.path.join(tmpdir, "both.log")) as f:
        kept = [json.loads(l) for l in f]
    assert len(kept) == 1 and kept[0]["message"] == "error in db", \
        f"AND-filtering wrong: {[k['message'] for k in kept]}"

    # ROTATION: tiny threshold; each oversized write rotates the file.
    rot_file = os.path.join(tmpdir, "rot.log")
    rot = LogRotator(max_size_mb=1, backup_count=2)
    rot.max_size_bytes = 200  # tighten for the test
    rlog = EventLogger(filepath=rot_file, rotator=rot, auto_timestamp=False)
    for i in range(6):
        rlog.log({"level": "INFO", "message": f"entry {i}", "pad": "x" * 200})
    backups = sorted(os.path.basename(p) for p in Path(tmpdir).glob("rot.log.*"))
    assert backups == ["rot.log.1", "rot.log.2"], \
        f"backup_count=2 must leave exactly .1 and .2, got {backups}"
    assert os.path.exists(rot_file), "active log missing after rotation"
    # The newest backup (.1) holds the previous generation — content rotated, not lost.
    with open(os.path.join(tmpdir, "rot.log.1")) as f:
        assert "entry" in f.read(), "rotated backup lost its content"

    for p in Path(tmpdir).rglob("*"):
        if p.is_file():
            p.unlink()
    print("event_logger: 4/5 kept (DEBUG dropped), types survive JSONL, "
          "AND-filters exact, rotation bounded at 2 backups — PASS")


if __name__ == "__main__":
    main()