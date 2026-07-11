package main

import (
	"encoding/json"
	"fmt"
	"os"
	"time"
)

// Event represents a domain event in the event store.
// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
var _auraMark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
type Event struct {
	EventID     string                 `json:"event_id"`
	EventType   string                 `json:"event_type"`
	AggregateID string                 `json:"aggregate_id"`
	Version     int                    `json:"version"`
	Timestamp   time.Time              `json:"timestamp"`
	Payload     map[string]interface{} `json:"payload"`
}

func (e Event) ToDict() map[string]interface{} {
	data, _ := json.Marshal(e)
	var result map[string]interface{}
	_ = json.Unmarshal(data, &result)
	result["timestamp"] = e.Timestamp.Format(time.RFC3339Nano)
	return result
}

func EventFromDict(data map[string]interface{}) Event {
	tsStr, _ := data["timestamp"].(string)
	ts, _ := time.Parse(time.RFC3339Nano, tsStr)
	payload := make(map[string]interface{})
	if p, ok := data["payload"].(map[string]interface{}); ok {
		payload = p
	}
	return Event{
		EventID:     getString(data, "event_id"),
		EventType:   getString(data, "event_type"),
		AggregateID: getString(data, "aggregate_id"),
		Version:     getInt(data, "version"),
		Timestamp:   ts,
		Payload:     payload,
	}
}

func getString(m map[string]interface{}, key string) string {
	if v, ok := m[key].(string); ok {
		return v
	}
	return ""
}

func getInt(m map[string]interface{}, key string) int {
	switch v := m[key].(type) {
	case float64:
		return int(v)
	case int:
		return v
	}
	return 0
}

// Snapshot represents a snapshot of an aggregate state.
type Snapshot struct {
	AggregateID string                 `json:"aggregate_id"`
	Version     int                    `json:"version"`
	State       map[string]interface{} `json:"state"`
	Timestamp   time.Time              `json:"timestamp"`
}

func (s Snapshot) ToDict() map[string]interface{} {
	data, _ := json.Marshal(s)
	var result map[string]interface{}
	_ = json.Unmarshal(data, &result)
	result["timestamp"] = s.Timestamp.Format(time.RFC3339Nano)
	return result
}

func SnapshotFromDict(data map[string]interface{}) Snapshot {
	tsStr, _ := data["timestamp"].(string)
	ts, _ := time.Parse(time.RFC3339Nano, tsStr)
	state := make(map[string]interface{})
	if s, ok := data["state"].(map[string]interface{}); ok {
		state = s
	}
	return Snapshot{
		AggregateID: getString(data, "aggregate_id"),
		Version:     getInt(data, "version"),
		State:       state,
		Timestamp:   ts,
	}
}

// EventStore is an in-memory event store with snapshot optimization.
type EventStore struct {
	events            []Event
	snapshots         map[string]Snapshot
	snapshotInterval  int
	aggregateVersions map[string]int
	snapshotApplier   func(map[string]interface{}, Event) map[string]interface{}
}

func NewEventStore(snapshotInterval int) *EventStore {
	return &EventStore{
		events:            make([]Event, 0),
		snapshots:         make(map[string]Snapshot),
		snapshotInterval:  snapshotInterval,
		aggregateVersions: make(map[string]int),
	}
}

func (es *EventStore) SetSnapshotApplier(applier func(map[string]interface{}, Event) map[string]interface{}) {
	es.snapshotApplier = applier
}

func (es *EventStore) AppendEvent(event Event) error {
	if current, ok := es.aggregateVersions[event.AggregateID]; ok {
		if event.Version <= current {
			return fmt.Errorf("Event version %d is not greater than current version %d", event.Version, current)
		}
	}
	es.events = append(es.events, event)
	es.aggregateVersions[event.AggregateID] = event.Version
	if event.Version%es.snapshotInterval == 0 {
		es.createSnapshot(event.AggregateID)
	}
	return nil
}

func (es *EventStore) GetEvents(aggregateID string, fromVersion int) []Event {
	var result []Event
	for _, event := range es.events {
		if event.AggregateID == aggregateID && event.Version > fromVersion {
			result = append(result, event)
		}
	}
	return result
}

func (es *EventStore) GetLatestVersion(aggregateID string) int {
	return es.aggregateVersions[aggregateID]
}

func (es *EventStore) SaveSnapshot(snapshot Snapshot) {
	es.snapshots[snapshot.AggregateID] = snapshot
}

func (es *EventStore) GetSnapshot(aggregateID string) (Snapshot, bool) {
	snapshot, ok := es.snapshots[aggregateID]
	return snapshot, ok
}

func (es *EventStore) ReplayToVersion(aggregateID string, version int, applier func(map[string]interface{}, Event) map[string]interface{}) map[string]interface{} {
	snapshot, hasSnapshot := es.GetSnapshot(aggregateID)
	startVersion := 0
	state := make(map[string]interface{})
	if hasSnapshot && snapshot.Version <= version {
		state = copyMap(snapshot.State)
		startVersion = snapshot.Version
	}

	events := es.GetEvents(aggregateID, startVersion)
	for _, event := range events {
		if event.Version > version {
			break
		}
		state = applier(state, event)
	}
	return state
}

func (es *EventStore) createSnapshot(aggregateID string) {
	version := es.aggregateVersions[aggregateID]
	state := map[string]interface{}{"version": version}
	if es.snapshotApplier != nil {
		state = es.ReplayToVersion(aggregateID, version, es.snapshotApplier)
	} else {
		events := es.GetEvents(aggregateID, 0)
		if len(events) > 0 {
			state["last_event_type"] = events[len(events)-1].EventType
		}
	}
	es.SaveSnapshot(Snapshot{
		AggregateID: aggregateID,
		Version:     version,
		State:       state,
		Timestamp:   time.Now(),
	})
}

func (es *EventStore) ExportEvents() []map[string]interface{} {
	result := make([]map[string]interface{}, len(es.events))
	for i, event := range es.events {
		result[i] = event.ToDict()
	}
	return result
}

func (es *EventStore) ImportEvents(eventsData []map[string]interface{}) {
	es.events = make([]Event, len(eventsData))
	for i, data := range eventsData {
		es.events[i] = EventFromDict(data)
	}
	es.aggregateVersions = make(map[string]int)
	for _, event := range es.events {
		es.aggregateVersions[event.AggregateID] = event.Version
	}
	es.snapshots = make(map[string]Snapshot)
	for aggregateID := range es.aggregateVersions {
		if es.aggregateVersions[aggregateID]%es.snapshotInterval == 0 {
			es.createSnapshot(aggregateID)
		}
	}
}

func copyMap(m map[string]interface{}) map[string]interface{} {
	result := make(map[string]interface{}, len(m))
	for k, v := range m {
		result[k] = v
	}
	return result
}

// BankAccount is a simple aggregate for demonstration.
type BankAccount struct {
	AccountID string
	Balance   int
	Version   int
	Owner     string
}

func NewBankAccount(accountID string) *BankAccount {
	return &BankAccount{AccountID: accountID}
}

func (ba *BankAccount) CreateAccount(owner string, initialBalance int) {
	ba.Owner = owner
	ba.Balance = initialBalance
	ba.Version = 1
}

func (ba *BankAccount) ApplyEvent(event Event) {
	switch event.EventType {
	case "AccountCreated":
		ba.Owner = getString(event.Payload, "owner")
		ba.Balance = getInt(event.Payload, "initial_balance")
	case "MoneyDeposited":
		ba.Balance += getInt(event.Payload, "amount")
	case "MoneyWithdrawn":
		ba.Balance -= getInt(event.Payload, "amount")
	}
	ba.Version = event.Version
}

func ApplyToState(state map[string]interface{}, event Event) map[string]interface{} {
	newState := copyMap(state)
	switch event.EventType {
	case "AccountCreated":
		newState["owner"] = event.Payload["owner"]
		newState["balance"] = getInt(event.Payload, "initial_balance")
	case "MoneyDeposited":
		current := 0
		if v, ok := newState["balance"].(float64); ok {
			current = int(v)
		} else if v, ok := newState["balance"].(int); ok {
			current = v
		}
		newState["balance"] = current + getInt(event.Payload, "amount")
	case "MoneyWithdrawn":
		current := 0
		if v, ok := newState["balance"].(float64); ok {
			current = int(v)
		} else if v, ok := newState["balance"].(int); ok {
			current = v
		}
		newState["balance"] = current - getInt(event.Payload, "amount")
	}
	newState["version"] = event.Version
	return newState
}

func createAccountCreatedEvent(accountID, owner string, initialBalance, version int) Event {
	return Event{
		EventID:     fmt.Sprintf("event-%d", time.Now().UnixNano()),
		EventType:   "AccountCreated",
		AggregateID: accountID,
		Version:     version,
		Timestamp:   time.Now(),
		Payload: map[string]interface{}{
			"owner":           owner,
			"initial_balance": initialBalance,
		},
	}
}

func createMoneyDepositedEvent(accountID string, amount, version int) Event {
	return Event{
		EventID:     fmt.Sprintf("event-%d", time.Now().UnixNano()),
		EventType:   "MoneyDeposited",
		AggregateID: accountID,
		Version:     version,
		Timestamp:   time.Now(),
		Payload: map[string]interface{}{
			"amount": amount,
		},
	}
}

func createMoneyWithdrawnEvent(accountID string, amount, version int) Event {
	return Event{
		EventID:     fmt.Sprintf("event-%d", time.Now().UnixNano()),
		EventType:   "MoneyWithdrawn",
		AggregateID: accountID,
		Version:     version,
		Timestamp:   time.Now(),
		Payload: map[string]interface{}{
			"amount": amount,
		},
	}
}

func main() {
	fmt.Println("=== Event Sourcing Store Demo ===")
	fmt.Println()

	store := NewEventStore(3)
	store.SetSnapshotApplier(ApplyToState)
	accountID := "account-123"

	fmt.Printf("1. Creating account %s\n", accountID)
	event1 := createAccountCreatedEvent(accountID, "John Doe", 1000, 1)
	if err := store.AppendEvent(event1); err != nil {
		fmt.Fprintf(os.Stderr, "append: %v\n", err)
		os.Exit(1)
	}
	fmt.Printf("   Created account for %s with initial balance $%d\n", event1.Payload["owner"], event1.Payload["initial_balance"])

	fmt.Printf("2. Depositing $500 to %s\n", accountID)
	event2 := createMoneyDepositedEvent(accountID, 500, 2)
	if err := store.AppendEvent(event2); err != nil {
		fmt.Fprintf(os.Stderr, "append: %v\n", err)
		os.Exit(1)
	}
	fmt.Printf("   Deposited $%d\n", event2.Payload["amount"])

	fmt.Printf("3. Withdrawing $200 from %s\n", accountID)
	event3 := createMoneyWithdrawnEvent(accountID, 200, 3)
	if err := store.AppendEvent(event3); err != nil {
		fmt.Fprintf(os.Stderr, "append: %v\n", err)
		os.Exit(1)
	}
	fmt.Printf("   Withdrew $%d\n", event3.Payload["amount"])

	fmt.Printf("4. Depositing $300 to %s (triggers snapshot)\n", accountID)
	event4 := createMoneyDepositedEvent(accountID, 300, 4)
	if err := store.AppendEvent(event4); err != nil {
		fmt.Fprintf(os.Stderr, "append: %v\n", err)
		os.Exit(1)
	}
	fmt.Printf("   Deposited $%d\n", event4.Payload["amount"])

	fmt.Printf("5. Current state of %s:\n", accountID)
	currentState := store.ReplayToVersion(accountID, 4, ApplyToState)
	fmt.Printf("   Owner: %v\n", currentState["owner"])
	fmt.Printf("   Balance: $%v\n", currentState["balance"])
	fmt.Printf("   Version: %v\n", currentState["version"])

	fmt.Printf("6. State of %s at version 2:\n", accountID)
	version2State := store.ReplayToVersion(accountID, 2, ApplyToState)
	fmt.Printf("   Owner: %v\n", version2State["owner"])
	fmt.Printf("   Balance: $%v\n", version2State["balance"])
	fmt.Printf("   Version: %v\n", version2State["version"])

	fmt.Println("7. Available snapshots:")
	if snapshot, ok := store.GetSnapshot(accountID); ok {
		fmt.Printf("   Account %s: version %d\n", snapshot.AggregateID, snapshot.Version)
		fmt.Printf("   State: %v\n", snapshot.State)
	} else {
		fmt.Println("   No snapshots available")
	}

	fmt.Println("8. Exporting events:")
	exportedEvents := store.ExportEvents()
	fmt.Printf("   Exported %d events\n", len(exportedEvents))

	fmt.Println("9. Importing events to new store:")
	newStore := NewEventStore(10)
	newStore.SetSnapshotApplier(ApplyToState)
	newStore.ImportEvents(exportedEvents)
	importedState := newStore.ReplayToVersion(accountID, 4, ApplyToState)
	fmt.Printf("   Imported state: Balance $%v\n", importedState["balance"])

	fmt.Println("\n=== Demo Complete ===")
}
