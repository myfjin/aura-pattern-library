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
        """Get all currently active, non-suppressed alerts. (Suppressed
        alerts are tracked in the same store; returning them as 'active'
        would page on exactly the alerts suppression exists to silence.)"""
        return [alert for alert in self.active_alerts.values()
                if alert.id not in self.suppressed_alerts]

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


def _mk_alert(title, severity, source, tags, ts):
    # timestamp passed explicitly: the dataclass default_factory bound the
    # real time.time at class definition, so a patched clock can't reach it.
    return Alert(title=title, description=title, severity=severity,
                 source=source, tags=tags, rule_id="service_rule", timestamp=ts)


def main():
    """Self-test on a fake clock: dedup inside the window, re-alert after it,
    tag suppression, resolve lifecycle — all exact."""
    _now = [50_000.0]
    _real_time = time.time
    time.time = lambda: _now[0]
    try:
        manager = AlertManager()
        manager.add_rule(Rule(id="service_rule", name="Service Alert Rule",
                              dedup_window_seconds=10.0,
                              suppression_tags={"maintenance"},
                              max_escalation_count=2,
                              escalation_interval_seconds=30.0))

        # First alert accepted; identical fingerprint inside 10s deduped.
        a1 = _mk_alert("High CPU", AlertSeverity.HIGH, "server01", {"prod", "cpu"}, _now[0])
        assert manager.process_alert(a1) is True, "first alert rejected"
        _now[0] += 1.0
        dup = _mk_alert("High CPU", AlertSeverity.HIGH, "server01", {"prod", "cpu"}, _now[0])
        assert manager.process_alert(dup) is False, "duplicate inside window accepted"

        # Different fingerprint is NOT deduped.
        a3 = _mk_alert("High Memory", AlertSeverity.CRITICAL, "server01", {"prod"}, _now[0])
        assert manager.process_alert(a3) is True, "distinct alert wrongly deduped"

        # PAST the window the same fingerprint alerts again.
        _now[0] += 11.0
        again = _mk_alert("High CPU", AlertSeverity.HIGH, "server01", {"prod", "cpu"}, _now[0])
        assert manager.process_alert(again) is True, \
            "re-alert after the dedup window was swallowed"

        # Suppression: maintenance-tagged alert is accepted but SUPPRESSED.
        supp = _mk_alert("Disk Warning", AlertSeverity.MEDIUM, "server02",
                         {"maintenance", "disk"}, _now[0])
        assert manager.process_alert(supp) is True
        suppressed = manager.get_suppressed_alerts()
        assert [s.title for s in suppressed] == ["Disk Warning"], \
            f"suppressed set wrong: {[s.title for s in suppressed]}"
        active_titles = sorted(a.title for a in manager.get_active_alerts())
        assert "Disk Warning" not in active_titles, "suppressed alert is active"

        # Resolve removes from active, reports honestly.
        n_active_before = len(manager.get_active_alerts())
        assert n_active_before == 3, \
            f"exactly 3 alerts must be active (cpu, memory, cpu-again), got {n_active_before}"
        assert manager.resolve_alert(a1.id) is True
        assert manager.resolve_alert(a1.id) is False, "double resolve reported success"
        assert manager.resolve_alert("ghost-id") is False
        assert len(manager.get_active_alerts()) == n_active_before - 1, \
            "resolve did not shrink the active set by exactly 1"

        # Dedup applies per-fingerprint: 4 rapid repeats → 1 accepted, 3 deduped.
        accepted = 0
        for i in range(4):
            e = _mk_alert("Recurring Error", AlertSeverity.MEDIUM, "serviceA", {"error"}, _now[0])
            if manager.process_alert(e):
                accepted += 1
            _now[0] += 0.5
        assert accepted == 1, f"4 repeats in 2s must accept exactly 1, accepted {accepted}"
    finally:
        time.time = _real_time

    print("alert_manager: dedup in-window, re-alert at +11s, maintenance "
          "suppressed, resolve exact, 4 repeats → 1 accepted — PASS")

if __name__ == "__main__":
    main()
