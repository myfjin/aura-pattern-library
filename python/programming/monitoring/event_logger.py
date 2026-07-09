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
    """Demo of the structured event logger functionality."""
    # Create a temporary log file for demo
    log_file = "demo_logs/events.log"
    
    # Create filters
    level_filter = LevelFilter(min_level="INFO")
    keyword_filter = KeywordFilter(["error", "warning"], exclude=False)
    
    # Create rotator (small size for demo)
    rotator = LogRotator(max_size_mb=1, backup_count=3)
    
    # Create logger
    logger = EventLogger(
        filepath=log_file,
        filters=[level_filter],
        rotator=rotator,
        auto_timestamp=True
    )
    
    print("Logging demo events...")
    
    # Log various events
    logger.log({
        "level": "DEBUG",
        "message": "This is a debug message",
        "component": "demo"
    })
    
    logger.log({
        "level": "INFO",
        "message": "Application started successfully",
        "component": "main",
        "version": "1.0.0"
    })
    
    logger.log({
        "level": "WARNING",
        "message": "Low disk space detected",
        "component": "monitor",
        "available_gb": 2.5
    })
    
    logger.log({
        "level": "ERROR",
        "message": "Failed to connect to database",
        "component": "database",
        "error_code": 500
    })
    
    logger.log({
        "level": "INFO",
        "message": "User login successful",
        "component": "auth",
        "user_id": "user123"
    })
    
    # Show log contents
    print(f"\nContents of {log_file}:")
    if os.path.exists(log_file):
        with open(log_file, "r") as f:
            for i, line in enumerate(f, 1):
                event = json.loads(line.strip())
                print(f"{i:2d}. {event}")
    else:
        print("Log file not found")
    
    # Demo rotation by creating a large entry
    print("\nDemonstrating log rotation...")
    large_event = {
        "level": "INFO",
        "message": "Large data entry",
        "component": "demo",
        "data": "A" * 1024 * 1024  # 1MB of data
    }
    
    # This will likely trigger rotation due to the large size
    logger.log(large_event)
    
    print("Demo completed. Check the demo_logs directory for output files.")


if __name__ == "__main__":
    main()