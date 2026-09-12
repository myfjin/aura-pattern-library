"""
Event Sourcing Store Implementation

This module provides a complete event sourcing system with:
- Event and Snapshot classes
- Append-only event log storage
- Snapshot optimization for performance
- Replay to any version capability
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import json
import uuid
from typing import Any, Dict, List, Optional, Callable
from datetime import datetime
from dataclasses import dataclass, asdict


@dataclass
class Event:
    """Represents a domain event in the event store."""
    event_id: str
    event_type: str
    aggregate_id: str
    version: int
    timestamp: datetime
    payload: Dict[str, Any]

    def to_dict(self) -> Dict[str, Any]:
        """Convert event to dictionary representation."""
        result = asdict(self)
        result['timestamp'] = self.timestamp.isoformat()
        return result

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Event':
        """Create event from dictionary representation."""
        data['timestamp'] = datetime.fromisoformat(data['timestamp'])
        return cls(**data)


@dataclass
class Snapshot:
    """Represents a snapshot of an aggregate state."""
    aggregate_id: str
    version: int
    state: Dict[str, Any]
    timestamp: datetime

    def to_dict(self) -> Dict[str, Any]:
        """Convert snapshot to dictionary representation."""
        result = asdict(self)
        result['timestamp'] = self.timestamp.isoformat()
        return result

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Snapshot':
        """Create snapshot from dictionary representation."""
        data['timestamp'] = datetime.fromisoformat(data['timestamp'])
        return cls(**data)


class EventStore:
    """Event store implementation with snapshot optimization."""
    
    def __init__(self, snapshot_interval: int = 10,
                 applier: Optional[Callable[[Dict[str, Any], Event], Dict[str, Any]]] = None):
        """
        Initialize the event store.

        Args:
            snapshot_interval: Number of events between snapshots
            applier: Function used to reconstruct real state for snapshots.
                Without it, NO snapshots are taken — a missing snapshot only
                costs a full replay, whereas the former placeholder snapshot
                ({"version", "last_event_type"}) was TRUSTED by
                replay_to_version and corrupted every read past it.
        """
        self._events: List[Event] = []
        self._snapshots: Dict[str, Snapshot] = {}
        self._snapshot_interval = snapshot_interval
        self._aggregate_versions: Dict[str, int] = {}
        self._applier = applier
    
    def append_event(self, event: Event) -> None:
        """
        Append an event to the event store.
        
        Args:
            event: The event to append
        """
        if event.aggregate_id in self._aggregate_versions:
            if event.version <= self._aggregate_versions[event.aggregate_id]:
                raise ValueError(f"Event version {event.version} is not greater than current version {self._aggregate_versions[event.aggregate_id]}")
        
        self._events.append(event)
        self._aggregate_versions[event.aggregate_id] = event.version
        
        # Create snapshot if needed
        if event.version % self._snapshot_interval == 0:
            self._create_snapshot(event.aggregate_id)
    
    def get_events(self, aggregate_id: str, from_version: int = 0) -> List[Event]:
        """
        Get events for an aggregate from a specific version.
        
        Args:
            aggregate_id: The aggregate ID
            from_version: The version to start from (inclusive)
            
        Returns:
            List of events
        """
        return [
            event for event in self._events
            if event.aggregate_id == aggregate_id and event.version > from_version
        ]
    
    def get_latest_version(self, aggregate_id: str) -> int:
        """
        Get the latest version for an aggregate.
        
        Args:
            aggregate_id: The aggregate ID
            
        Returns:
            Latest version number
        """
        return self._aggregate_versions.get(aggregate_id, 0)
    
    def save_snapshot(self, snapshot: Snapshot) -> None:
        """
        Save a snapshot.
        
        Args:
            snapshot: The snapshot to save
        """
        self._snapshots[snapshot.aggregate_id] = snapshot
    
    def get_snapshot(self, aggregate_id: str) -> Optional[Snapshot]:
        """
        Get the latest snapshot for an aggregate.
        
        Args:
            aggregate_id: The aggregate ID
            
        Returns:
            The snapshot or None if not found
        """
        return self._snapshots.get(aggregate_id)
    
    def replay_to_version(self, aggregate_id: str, version: int, 
                         applier: Callable[[Dict[str, Any], Event], Dict[str, Any]]) -> Dict[str, Any]:
        """
        Replay events to a specific version and apply them to state.
        
        Args:
            aggregate_id: The aggregate ID
            version: The version to replay to
            applier: Function to apply events to state
            
        Returns:
            The state at the specified version
        """
        # Start with snapshot if available
        snapshot = self.get_snapshot(aggregate_id)
        start_version = 0
        state = {}
        
        if snapshot and snapshot.version <= version:
            state = snapshot.state.copy()
            start_version = snapshot.version
        
        # Apply events from snapshot version to target version
        events = self.get_events(aggregate_id, start_version)
        for event in events:
            if event.version > version:
                break
            state = applier(state, event)
        
        return state
    
    def _create_snapshot(self, aggregate_id: str) -> None:
        """
        Create a snapshot for an aggregate.
        
        Args:
            aggregate_id: The aggregate ID
        """
        # Only snapshot when we can reconstruct REAL state; a hollow
        # snapshot is worse than none because replay_to_version trusts it.
        if self._applier is None:
            return

        version = self._aggregate_versions[aggregate_id]
        state: Dict[str, Any] = {}
        for event in self.get_events(aggregate_id):
            if event.version > version:
                break
            state = self._applier(state, event)

        snapshot = Snapshot(
            aggregate_id=aggregate_id,
            version=version,
            state=state,
            timestamp=datetime.now()
        )
        self.save_snapshot(snapshot)
    
    def export_events(self) -> List[Dict[str, Any]]:
        """Export all events as dictionaries."""
        return [event.to_dict() for event in self._events]
    
    def import_events(self, events_data: List[Dict[str, Any]]) -> None:
        """Import events from dictionaries."""
        self._events = [Event.from_dict(data) for data in events_data]
        # Rebuild aggregate versions
        self._aggregate_versions = {}
        for event in self._events:
            self._aggregate_versions[event.aggregate_id] = event.version
        # Rebuild snapshots
        self._snapshots = {}
        for aggregate_id in self._aggregate_versions:
            if self._aggregate_versions[aggregate_id] % self._snapshot_interval == 0:
                self._create_snapshot(aggregate_id)


class BankAccount:
    """A simple bank account aggregate for demonstration."""
    
    def __init__(self, account_id: str):
        """
        Initialize a bank account.
        
        Args:
            account_id: The account ID
        """
        self.account_id = account_id
        self.balance = 0
        self.version = 0
        self.owner = ""
    
    @classmethod
    def create_account(cls, account_id: str, owner: str, initial_balance: int = 0) -> 'BankAccount':
        """
        Create a new bank account.
        
        Args:
            account_id: The account ID
            owner: The account owner
            initial_balance: The initial balance
            
        Returns:
            A new bank account
        """
        account = cls(account_id)
        account.owner = owner
        account.balance = initial_balance
        account.version = 1
        return account
    
    def apply_event(self, event: Event) -> None:
        """
        Apply an event to the account.
        
        Args:
            event: The event to apply
        """
        if event.event_type == "AccountCreated":
            self.owner = event.payload["owner"]
            self.balance = event.payload["initial_balance"]
        elif event.event_type == "MoneyDeposited":
            self.balance += event.payload["amount"]
        elif event.event_type == "MoneyWithdrawn":
            self.balance -= event.payload["amount"]
        
        self.version = event.version
    
    @staticmethod
    def apply_to_state(state: Dict[str, Any], event: Event) -> Dict[str, Any]:
        """
        Apply an event to a state dictionary.
        
        Args:
            state: The current state
            event: The event to apply
            
        Returns:
            The new state
        """
        new_state = state.copy()
        
        if event.event_type == "AccountCreated":
            new_state["owner"] = event.payload["owner"]
            new_state["balance"] = event.payload["initial_balance"]
        elif event.event_type == "MoneyDeposited":
            new_state["balance"] = new_state.get("balance", 0) + event.payload["amount"]
        elif event.event_type == "MoneyWithdrawn":
            new_state["balance"] = new_state.get("balance", 0) - event.payload["amount"]
        
        new_state["version"] = event.version
        return new_state


def create_account_created_event(account_id: str, owner: str, initial_balance: int, version: int) -> Event:
    """Create an AccountCreated event."""
    return Event(
        event_id=str(uuid.uuid4()),
        event_type="AccountCreated",
        aggregate_id=account_id,
        version=version,
        timestamp=datetime.now(),
        payload={
            "owner": owner,
            "initial_balance": initial_balance
        }
    )


def create_money_deposited_event(account_id: str, amount: int, version: int) -> Event:
    """Create a MoneyDeposited event."""
    return Event(
        event_id=str(uuid.uuid4()),
        event_type="MoneyDeposited",
        aggregate_id=account_id,
        version=version,
        timestamp=datetime.now(),
        payload={
            "amount": amount
        }
    )


def create_money_withdrawn_event(account_id: str, amount: int, version: int) -> Event:
    """Create a MoneyWithdrawn event."""
    return Event(
        event_id=str(uuid.uuid4()),
        event_type="MoneyWithdrawn",
        aggregate_id=account_id,
        version=version,
        timestamp=datetime.now(),
        payload={
            "amount": amount
        }
    )


def main():
    """Self-test: replay arithmetic exact at every version (time travel),
    snapshots taken at the interval, export→import reproduces the state."""
    store = EventStore(snapshot_interval=3, applier=BankAccount.apply_to_state)
    account_id = "account-123"

    # History: create(1000) → +500 → -200 → +300.
    store.append_event(create_account_created_event(account_id, "John Doe", 1000, 1))
    store.append_event(create_money_deposited_event(account_id, 500, 2))
    store.append_event(create_money_withdrawn_event(account_id, 200, 3))
    store.append_event(create_money_deposited_event(account_id, 300, 4))

    # TIME TRAVEL: the balance at every version is exact arithmetic.
    truths = {1: 1000, 2: 1500, 3: 1300, 4: 1600}
    for version, expected in truths.items():
        state = store.replay_to_version(account_id, version, BankAccount.apply_to_state)
        assert state.get("balance") == expected, \
            f"balance at v{version} must be {expected}, got {state.get('balance')}"
        assert state.get("version") == version, \
            f"replayed version must be {version}, got {state.get('version')}"
    assert state.get("owner") == "John Doe", "owner lost in replay"

    # SNAPSHOT: interval 3 means a snapshot exists at (or after) version 3.
    snapshot = store.get_snapshot(account_id)
    assert snapshot is not None, "no snapshot despite crossing the interval"
    assert snapshot.aggregate_id == account_id
    assert snapshot.version >= 3, f"snapshot version {snapshot.version} below interval"
    assert snapshot.state.get("balance") == truths[snapshot.version], \
        "snapshot state disagrees with the replayed truth at its version"

    # EXPORT → IMPORT: a fresh store rebuilds the identical final state.
    exported = store.export_events()
    n_exported = len(exported)
    assert n_exported == 4, f"4 events must export, got {n_exported}"
    new_store = EventStore()
    new_store.import_events(exported)
    imported = new_store.replay_to_version(account_id, 4, BankAccount.apply_to_state)
    assert imported.get("balance") == 1600, \
        f"imported store replayed {imported.get('balance')}, want 1600"
    assert imported.get("owner") == "John Doe"

    # Aggregate isolation: a second account's events don't leak.
    store.append_event(create_account_created_event("account-999", "Jane", 50, 1))
    a2 = store.replay_to_version("account-999", 1, BankAccount.apply_to_state)
    assert a2.get("balance") == 50 and a2.get("owner") == "Jane"
    a1 = store.replay_to_version(account_id, 4, BankAccount.apply_to_state)
    assert a1.get("balance") == 1600, "second aggregate polluted the first"

    print("event_sourcing_store: replay exact at v1..v4 (1000/1500/1300/1600), "
          "snapshot at v>=3 agrees, export/import rebuilt 1600, isolation — PASS")


if __name__ == "__main__":
    main()