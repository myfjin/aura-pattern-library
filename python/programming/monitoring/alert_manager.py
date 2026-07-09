#!/usr/bin/env python3
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import time
import uuid
from typing import Dict, List, Optional, Set
from dataclasses import dataclass, field
from collections import defaultdict
from enum import Enum


class AlertSeverity(Enum):
    """Enumeration of alert severity levels."""
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    CRITICAL = 4


class AlertStatus(Enum):
    """Enumeration of alert statuses."""
    FIRING = "firing"
    RESOLVED = "resolved"
    SUPPRESSED = "suppressed"


@dataclass
class Alert:
    """Represents an alert with all its properties."""
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    title: str = ""
    description: str = ""
    severity: AlertSeverity = AlertSeverity.MEDIUM
    status: AlertStatus = AlertStatus.FIRING
    source: str = ""
    tags: Set[str] = field(default_factory=set)
    timestamp: float = field(default_factory=time.time)
    escalation_count: int = 0
    rule_id: Optional[str] = None

    def __hash__(self) -> int:
        """Make Alert hashable based on its ID."""
        return hash(self.id)

    def __eq__(self, other) -> bool:
        """Compare alerts based on their ID."""
        if not isinstance(other, Alert):
            return False
        return self.id == other.id

    def fingerprint(self) -> str:
        """Generate a fingerprint for deduplication based on key attributes."""
        return f"{self.title}:{self.source}:{':'.join(sorted(self.tags))}"


@dataclass
class Rule:
    """Represents an alert rule with suppression and escalation settings."""
    id: str
    name: str
    dedup_window_seconds: float = 300.0  # 5 minutes default
    suppression_tags: Set[str] = field(default_factory=set)
    max_escalation_count: int = 3
    escalation_interval_seconds: float = 3600.0  # 1 hour default


class AlertManager:
    """Manages alerts with deduplication, suppression, and escalation."""

    def __init__(self) -> None:
        """Initialize the AlertManager."""
        self.rules: Dict[str, Rule] = {}
        self.active_alerts: Dict[str, Alert] = {}  # alert_id -> Alert
        self.alert_history: Dict[str, List[Alert]] = defaultdict(list)  # fingerprint -> alerts
        self.suppressed_alerts: Set[str] = set()  # alert IDs that are suppressed

    def add_rule(self, rule: Rule) -> None:
        """Add a rule to the manager."""
        if not isinstance(rule, Rule):
            raise TypeError("Rule must be an instance of Rule class")
        self.rules[rule.id] = rule

    def process_alert(self, alert: Alert) -> bool:
        """
        Process an incoming alert.
        
        Returns:
            bool: True if alert was processed (not deduplicated), False if deduplicated
        """
        if not isinstance(alert, Alert):
            raise TypeError("Alert must be an instance of Alert class")
            
        # Assign rule if not already assigned
        if not alert.rule_id and len(self.rules) == 1:
            alert.rule_id = next(iter(self.rules))
        elif not alert.rule_id:
            raise ValueError("Alert must have a rule_id or exactly one rule must exist")

        rule = self.rules.get(alert.rule_id)
        if not rule:
            raise ValueError(f"Rule with ID {alert.rule_id} not found")

        # Check for suppression
        if self._is_suppressed(alert, rule):
            alert.status = AlertStatus.SUPPRESSED
            self.suppressed_alerts.add(alert.id)
            self.active_alerts[alert.id] = alert
            return True

        # Check for deduplication
        duplicate_id = self._find_duplicate(alert, rule)
        if duplicate_id:
            # Update the existing alert
            existing_alert = self.active_alerts[duplicate_id]
            existing_alert.timestamp = alert.timestamp
            existing_alert.description = alert.description
            existing_alert.escalation_count = alert.escalation_count
            return False

        # New alert - check for escalation
        if self._should_escalate(alert, rule):
            alert.escalation_count += 1

        # Add to active alerts
        self.active_alerts[alert.id] = alert
        self.alert_history[alert.fingerprint()].append(alert)
        return True

    def resolve_alert(self, alert_id: str) -> bool:
        """
        Resolve an active alert.
        
        Returns:
            bool: True if alert was resolved, False if not found
        """
        if alert_id not in self.active_alerts:
            return False
            
        alert = self.active_alerts[alert_id]
        alert.status = AlertStatus.RESOLVED
        alert.timestamp = time.time()
        del self.active_alerts[alert_id]
        return True

    def get_active_alerts(self) -> List[Alert]:
        """Get all currently active alerts."""
        return list(self.active_alerts.values())

    def get_suppressed_alerts(self) -> List[Alert]:
        """Get all currently suppressed alerts."""
        return [alert for alert in self.active_alerts.values() 
                if alert.id in self.suppressed_alerts]

    def _is_suppressed(self, alert: Alert, rule: Rule) -> bool:
        """Check if an alert should be suppressed based on rule tags."""
        return bool(rule.suppression_tags & alert.tags)

    def _find_duplicate(self, alert: Alert, rule: Rule) -> Optional[str]:
        """
        Find a duplicate alert within the deduplication window.
        
        Returns:
            str or None: ID of duplicate alert if found, None otherwise
        """
        fingerprint = alert.fingerprint()
        current_time = time.time()
        
        # Check recent alerts with same fingerprint
        for historical_alert in reversed(self.alert_history[fingerprint]):
            # Only consider active alerts
            if historical_alert.id not in self.active_alerts:
                continue
                
            # Check if within dedup window
            if current_time - historical_alert.timestamp <= rule.dedup_window_seconds:
                return historical_alert.id
            else:
                # Since we're going backwards in time, no need to check further
                break
                
        return None

    def _should_escalate(self, alert: Alert, rule: Rule) -> bool:
        """
        Determine if an alert should be escalated.
        
        Returns:
            bool: True if alert should be escalated
        """
        if rule.max_escalation_count <= 0:
            return False
            
        fingerprint = alert.fingerprint()
        current_time = time.time()
        
        # Count recent alerts with same fingerprint
        recent_count = 0
        for historical_alert in reversed(self.alert_history[fingerprint]):
            if current_time - historical_alert.timestamp <= rule.escalation_interval_seconds:
                recent_count += 1
            else:
                break
                
        return recent_count >= rule.max_escalation_count


def main():
    """Demo the AlertManager functionality."""
    # Create alert manager
    manager = AlertManager()
    
    # Create a rule
    rule = Rule(
        id="service_rule",
        name="Service Alert Rule",
        dedup_window_seconds=10.0,
        suppression_tags={"maintenance"},
        max_escalation_count=2,
        escalation_interval_seconds=30.0
    )
    manager.add_rule(rule)
    
    # Create some alerts
    alert1 = Alert(
        title="High CPU Usage",
        description="CPU usage exceeded 90%",
        severity=AlertSeverity.HIGH,
        source="server01",
        tags={"production", "cpu"},
        rule_id="service_rule"
    )
    
    alert2 = Alert(
        title="High CPU Usage",
        description="CPU usage still high",
        severity=AlertSeverity.HIGH,
        source="server01",
        tags={"production", "cpu"},
        rule_id="service_rule"
    )
    
    alert3 = Alert(
        title="High Memory Usage",
        description="Memory usage exceeded 95%",
        severity=AlertSeverity.CRITICAL,
        source="server01",
        tags={"production", "memory"},
        rule_id="service_rule"
    )
    
    suppressed_alert = Alert(
        title="Disk Warning",
        description="Disk usage at 85%",
        severity=AlertSeverity.MEDIUM,
        source="server02",
        tags={"maintenance", "disk"},
        rule_id="service_rule"
    )
    
    # Process alerts
    print("Processing alerts...")
    result1 = manager.process_alert(alert1)
    print(f"Alert 1 processed: {result1}")  # Should be True (new)
    
    time.sleep(0.1)  # Small delay
    
    result2 = manager.process_alert(alert2)
    print(f"Alert 2 processed: {result2}")  # Should be False (duplicate)
    
    result3 = manager.process_alert(alert3)
    print(f"Alert 3 processed: {result3}")  # Should be True (new)
    
    suppressed_result = manager.process_alert(suppressed_alert)
    print(f"Suppressed alert processed: {suppressed_result}")  # Should be True
    
    # Check active alerts
    active = manager.get_active_alerts()
    print(f"\nActive alerts: {len(active)}")
    for alert in active:
        print(f"  - {alert.title} ({alert.status.value})")
    
    # Check suppressed alerts
    suppressed = manager.get_suppressed_alerts()
    print(f"\nSuppressed alerts: {len(suppressed)}")
    for alert in suppressed:
        print(f"  - {alert.title}")
    
    # Resolve an alert
    resolved = manager.resolve_alert(alert1.id)
    print(f"\nAlert 1 resolved: {resolved}")
    
    active_after_resolve = manager.get_active_alerts()
    print(f"Active alerts after resolve: {len(active_after_resolve)}")
    
    # Test escalation
    print("\nTesting escalation...")
    for i in range(4):
        escalation_test = Alert(
            title="Recurring Error",
            description=f"Error occurred {i+1} times",
            severity=AlertSeverity.MEDIUM,
            source="serviceA",
            tags={"error"},
            rule_id="service_rule"
        )
        processed = manager.process_alert(escalation_test)
        print(f"Escalation test {i+1} processed: {processed}")
        if not processed and i > 0:  # Should be deduplicated after first
            print(f"  Alert was deduplicated")
        time.sleep(0.1)


if __name__ == "__main__":
    main()