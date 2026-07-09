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
    
    def __init__(self, snapshot_interval: int = 10):
        """
        Initialize the event store.
        
        Args:
            snapshot_interval: Number of events between snapshots
        """
        self._events: List[Event] = []
        self._snapshots: Dict[str, Snapshot] = {}
        self._snapshot_interval = snapshot_interval
        self._aggregate_versions: Dict[str, int] = {}
    
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
        # In a real implementation, this would use a registered applier function
        # For this example, we'll create a simple snapshot
        version = self._aggregate_versions[aggregate_id]
        events = self.get_events(aggregate_id)
        
        # Simple state reconstruction (in practice, you'd use the aggregate's apply methods)
        state = {"version": version}
        if events:
            # This is a simplified example - in practice you'd reconstruct actual state
            state["last_event_type"] = events[-1].event_type
        
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
    """Demonstrate the event sourcing store with bank account events."""
    print("=== Event Sourcing Store Demo ===\n")
    
    # Create event store
    store = EventStore(snapshot_interval=3)
    
    # Create account
    account_id = "account-123"
    print(f"1. Creating account {account_id}")
    event1 = create_account_created_event(account_id, "John Doe", 1000, 1)
    store.append_event(event1)
    print(f"   Created account for {event1.payload['owner']} with initial balance ${event1.payload['initial_balance']}")
    
    # Deposit money
    print(f"2. Depositing $500 to {account_id}")
    event2 = create_money_deposited_event(account_id, 500, 2)
    store.append_event(event2)
    print(f"   Deposited ${event2.payload['amount']}")
    
    # Withdraw money
    print(f"3. Withdrawing $200 from {account_id}")
    event3 = create_money_withdrawn_event(account_id, 200, 3)
    store.append_event(event3)
    print(f"   Withdrew ${event3.payload['amount']}")
    
    # Another deposit (this will trigger a snapshot)
    print(f"4. Depositing $300 to {account_id} (triggers snapshot)")
    event4 = create_money_deposited_event(account_id, 300, 4)
    store.append_event(event4)
    print(f"   Deposited ${event4.payload['amount']}")
    
    # Check current state
    print(f"5. Current state of {account_id}:")
    current_state = store.replay_to_version(account_id, 4, BankAccount.apply_to_state)
    print(f"   Owner: {current_state.get('owner', 'Unknown')}")
    print(f"   Balance: ${current_state.get('balance', 0)}")
    print(f"   Version: {current_state.get('version', 0)}")
    
    # Replay to previous version
    print(f"6. State of {account_id} at version 2:")
    version_2_state = store.replay_to_version(account_id, 2, BankAccount.apply_to_state)
    print(f"   Owner: {version_2_state.get('owner', 'Unknown')}")
    print(f"   Balance: ${version_2_state.get('balance', 0)}")
    print(f"   Version: {version_2_state.get('version', 0)}")
    
    # Show snapshots
    print("7. Available snapshots:")
    snapshot = store.get_snapshot(account_id)
    if snapshot:
        print(f"   Account {snapshot.aggregate_id}: version {snapshot.version}")
        print(f"   State: {snapshot.state}")
    else:
        print("   No snapshots available")
    
    # Export and import demonstration
    print("8. Exporting events:")
    exported_events = store.export_events()
    print(f"   Exported {len(exported_events)} events")
    
    # Create new store and import
    print("9. Importing events to new store:")
    new_store = EventStore()
    new_store.import_events(exported_events)
    imported_state = new_store.replay_to_version(account_id, 4, BankAccount.apply_to_state)
    print(f"   Imported state: Balance ${imported_state.get('balance', 0)}")
    
    print("\n=== Demo Complete ===")


if __name__ == "__main__":
    main()