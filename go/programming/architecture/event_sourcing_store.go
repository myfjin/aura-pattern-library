package main

import (
	"fmt"
	"os"
	"sort"
	"time"
)

// Event-sourced aggregate store: appends versioned domain events per aggregate,
// rebuilds state by replaying events from the nearest snapshot forward, and
// auto-snapshots every N versions; supports export/import of the full event log.
// Use when state must be derived from an auditable, replayable history of events.
// Guarantees: replay is exact at every version, versions must strictly increase,
// snapshots agree with the replayed truth, export/import rebuilds identically, and
// aggregates stay isolated so one never pollutes another's state.
// Event represents a domain event in the event store.
// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
var _auraMark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
type Event struct {
	EventID     string
	EventType   string
	AggregateID string
	Version     int
	Timestamp   time.Time
	Payload     map[string]interface{}
}

func (e Event) toDict() map[string]interface{} {
	return map[string]interface{}{
		"event_id":     e.EventID,
		"event_type":   e.EventType,
		"aggregate_id": e.AggregateID,
		"version":      e.Version,
		"timestamp":    e.Timestamp.Format(time.RFC3339Nano),
		"payload":      e.Payload,
	}
}

func eventFromDict(data map[string]interface{}) Event {
	ts, _ := time.Parse(time.RFC3339Nano, data["timestamp"].(string))
	payload := map[string]interface{}{}
	if p, ok := data["payload"].(map[string]interface{}); ok {
		payload = p
	}
	version := 0
	switch v := data["version"].(type) {
	case float64:
		version = int(v)
	case int:
		version = v
	}
	return Event{
		EventID:     data["event_id"].(string),
		EventType:   data["event_type"].(string),
		AggregateID: data["aggregate_id"].(string),
		Version:     version,
		Timestamp:   ts,
		Payload:     payload,
	}
}

// Snapshot represents a snapshot of an aggregate state.
type Snapshot struct {
	AggregateID string
	Version     int
	State       map[string]interface{}
	Timestamp   time.Time
}

func (s Snapshot) toDict() map[string]interface{} {
	return map[string]interface{}{
		"aggregate_id": s.AggregateID,
		"version":      s.Version,
		"state":        s.State,
		"timestamp":    s.Timestamp.Format(time.RFC3339Nano),
	}
}

func snapshotFromDict(data map[string]interface{}) Snapshot {
	ts, _ := time.Parse(time.RFC3339Nano, data["timestamp"].(string))
	state := map[string]interface{}{}
	if st, ok := data["state"].(map[string]interface{}); ok {
		state = st
	}
	return Snapshot{
		AggregateID: data["aggregate_id"].(string),
		Version:     int(data["version"].(float64)),
		State:       state,
		Timestamp:   ts,
	}
}

// EventStore is an event store with snapshot optimization.
type EventStore struct {
	events            []Event
	snapshots         map[string]Snapshot
	snapshotInterval  int
	aggregateVersions map[string]int
	applier           func(map[string]interface{}, Event) map[string]interface{}
}

func newEventStore(snapshotInterval int, applier func(map[string]interface{}, Event) map[string]interface{}) *EventStore {
	return &EventStore{
		events:            []Event{},
		snapshots:         map[string]Snapshot{},
		snapshotInterval:  snapshotInterval,
		aggregateVersions: map[string]int{},
		applier:           applier,
	}
}

func (s *EventStore) appendEvent(event Event) {
	if current, ok := s.aggregateVersions[event.AggregateID]; ok {
		if event.Version <= current {
			fmt.Fprintf(os.Stderr, "Event version %d is not greater than current version %d\n", event.Version, current)
			os.Exit(1)
		}
	}
	s.events = append(s.events, event)
	s.aggregateVersions[event.AggregateID] = event.Version
	if event.Version%s.snapshotInterval == 0 {
		s.createSnapshot(event.AggregateID)
	}
}

func (s *EventStore) getEvents(aggregateID string, fromVersion int) []Event {
	var result []Event
	for _, event := range s.events {
		if event.AggregateID == aggregateID && event.Version > fromVersion {
			result = append(result, event)
		}
	}
	return result
}

func (s *EventStore) getLatestVersion(aggregateID string) int {
	if v, ok := s.aggregateVersions[aggregateID]; ok {
		return v
	}
	return 0
}

func (s *EventStore) saveSnapshot(snapshot Snapshot) {
	s.snapshots[snapshot.AggregateID] = snapshot
}

func (s *EventStore) getSnapshot(aggregateID string) (Snapshot, bool) {
	snapshot, ok := s.snapshots[aggregateID]
	return snapshot, ok
}

func (s *EventStore) replayToVersion(aggregateID string, version int, applier func(map[string]interface{}, Event) map[string]interface{}) map[string]interface{} {
	state := map[string]interface{}{}
	startVersion := 0
	if snapshot, ok := s.getSnapshot(aggregateID); ok && snapshot.Version <= version {
		for k, v := range snapshot.State {
			state[k] = v
		}
		startVersion = snapshot.Version
	}
	for _, event := range s.getEvents(aggregateID, startVersion) {
		if event.Version > version {
			break
		}
		state = applier(state, event)
	}
	return state
}

func (s *EventStore) createSnapshot(aggregateID string) {
	if s.applier == nil {
		return
	}
	version := s.aggregateVersions[aggregateID]
	state := map[string]interface{}{}
	for _, event := range s.getEvents(aggregateID, 0) {
		if event.Version > version {
			break
		}
		state = s.applier(state, event)
	}
	s.saveSnapshot(Snapshot{
		AggregateID: aggregateID,
		Version:     version,
		State:       state,
		Timestamp:   time.Now(),
	})
}

func (s *EventStore) exportEvents() []map[string]interface{} {
	result := make([]map[string]interface{}, len(s.events))
	for i, event := range s.events {
		result[i] = event.toDict()
	}
	return result
}

func (s *EventStore) importEvents(eventsData []map[string]interface{}) {
	s.events = make([]Event, len(eventsData))
	for i, data := range eventsData {
		s.events[i] = eventFromDict(data)
	}
	s.aggregateVersions = map[string]int{}
	for _, event := range s.events {
		s.aggregateVersions[event.AggregateID] = event.Version
	}
	s.snapshots = map[string]Snapshot{}
	// Deterministic snapshot rebuild order.
	ids := make([]string, 0, len(s.aggregateVersions))
	for id := range s.aggregateVersions {
		ids = append(ids, id)
	}
	sort.Strings(ids)
	for _, aggregateID := range ids {
		if s.aggregateVersions[aggregateID]%s.snapshotInterval == 0 {
			s.createSnapshot(aggregateID)
		}
	}
}

// BankAccount applies events to account state.
func applyToState(state map[string]interface{}, event Event) map[string]interface{} {
	newState := map[string]interface{}{}
	for k, v := range state {
		newState[k] = v
	}
	switch event.EventType {
	case "AccountCreated":
		newState["owner"] = event.Payload["owner"]
		newState["balance"] = event.Payload["initial_balance"]
	case "MoneyDeposited":
		balance := 0
		if b, ok := newState["balance"].(int); ok {
			balance = b
		}
		newState["balance"] = balance + event.Payload["amount"].(int)
	case "MoneyWithdrawn":
		balance := 0
		if b, ok := newState["balance"].(int); ok {
			balance = b
		}
		newState["balance"] = balance - event.Payload["amount"].(int)
	}
	newState["version"] = event.Version
	return newState
}

var eventCounter int

func newEventID() string {
	eventCounter++
	return fmt.Sprintf("evt-%d", eventCounter)
}

func createAccountCreatedEvent(accountID, owner string, initialBalance, version int) Event {
	return Event{
		EventID:     newEventID(),
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
		EventID:     newEventID(),
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
		EventID:     newEventID(),
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
	store := newEventStore(3, applyToState)
	accountID := "account-123"

	store.appendEvent(createAccountCreatedEvent(accountID, "John Doe", 1000, 1))
	store.appendEvent(createMoneyDepositedEvent(accountID, 500, 2))
	store.appendEvent(createMoneyWithdrawnEvent(accountID, 200, 3))
	store.appendEvent(createMoneyDepositedEvent(accountID, 300, 4))

	truths := map[int]int{1: 1000, 2: 1500, 3: 1300, 4: 1600}
	for version, expected := range truths {
		state := store.replayToVersion(accountID, version, applyToState)
		balance := state["balance"].(int)
		if !(balance == expected) {
			fmt.Fprintf(os.Stderr, "balance at v%d must be %d, got %d\n", version, expected, balance)
			os.Exit(1)
		}
		v := state["version"].(int)
		if !(v == version) {
			fmt.Fprintf(os.Stderr, "replayed version must be %d, got %d\n", version, v)
			os.Exit(1)
		}
	}
	owner := store.replayToVersion(accountID, 4, applyToState)["owner"].(string)
	if !(owner == "John Doe") {
		fmt.Fprintf(os.Stderr, "owner lost in replay\n")
		os.Exit(1)
	}

	snapshot, ok := store.getSnapshot(accountID)
	if !ok {
		fmt.Fprintf(os.Stderr, "no snapshot despite crossing the interval\n")
		os.Exit(1)
	}
	if !(snapshot.AggregateID == accountID) {
		fmt.Fprintf(os.Stderr, "snapshot aggregate id mismatch\n")
		os.Exit(1)
	}
	if !(snapshot.Version >= 3) {
		fmt.Fprintf(os.Stderr, "snapshot version %d below interval\n", snapshot.Version)
		os.Exit(1)
	}
	expected := truths[snapshot.Version]
	bal := snapshot.State["balance"].(int)
	if !(bal == expected) {
		fmt.Fprintf(os.Stderr, "snapshot state disagrees with the replayed truth at its version\n")
		os.Exit(1)
	}

	exported := store.exportEvents()
	nExported := len(exported)
	if !(nExported == 4) {
		fmt.Fprintf(os.Stderr, "4 events must export, got %d\n", nExported)
		os.Exit(1)
	}
	newStore := newEventStore(3, nil)
	newStore.importEvents(exported)
	imported := newStore.replayToVersion(accountID, 4, applyToState)
	importedBalance := imported["balance"].(int)
	if !(importedBalance == 1600) {
		fmt.Fprintf(os.Stderr, "imported store replayed %d, want 1600\n", importedBalance)
		os.Exit(1)
	}
	importedOwner := imported["owner"].(string)
	if !(importedOwner == "John Doe") {
		fmt.Fprintf(os.Stderr, "imported owner mismatch\n")
		os.Exit(1)
	}

	store.appendEvent(createAccountCreatedEvent("account-999", "Jane", 50, 1))
	a2 := store.replayToVersion("account-999", 1, applyToState)
	a2Balance := a2["balance"].(int)
	if !(a2Balance == 50) {
		fmt.Fprintf(os.Stderr, "second account balance mismatch\n")
		os.Exit(1)
	}
	a2Owner := a2["owner"].(string)
	if !(a2Owner == "Jane") {
		fmt.Fprintf(os.Stderr, "second account owner mismatch\n")
		os.Exit(1)
	}
	a1 := store.replayToVersion(accountID, 4, applyToState)
	a1Balance := a1["balance"].(int)
	if !(a1Balance == 1600) {
		fmt.Fprintf(os.Stderr, "second aggregate polluted the first\n")
		os.Exit(1)
	}

	fmt.Println("event_sourcing_store: replay exact at v1..v4 (1000/1500/1300/1600), " +
		"snapshot at v>=3 agrees, export/import rebuilt 1600, isolation — PASS")
}
