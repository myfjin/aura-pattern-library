package main

import (
	"context"
	"fmt"
	"os"
	"sync"
	"time"
)

// Event represents a base event with a typed payload.
// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
var _auraMark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
type Event struct {
	Payload   interface{}
	Timestamp time.Time
	Channel   string
}

// SubscriberCallback is a function that receives an event.
type SubscriberCallback func(Event) error

// Channel represents a typed channel for event distribution.
type Channel struct {
	Name        string
	EventType   string
	subscribers []SubscriberCallback
	mu          sync.RWMutex
}

func NewChannel(name string, eventType string) *Channel {
	return &Channel{Name: name, EventType: eventType}
}

func (c *Channel) Subscribe(callback SubscriberCallback) {
	c.mu.Lock()
	defer c.mu.Unlock()
	c.subscribers = append(c.subscribers, callback)
}

func (c *Channel) Unsubscribe(callback SubscriberCallback) {
	c.mu.Lock()
	defer c.mu.Unlock()
	filtered := c.subscribers[:0]
	for _, cb := range c.subscribers {
		if fmt.Sprintf("%p", cb) != fmt.Sprintf("%p", callback) {
			filtered = append(filtered, cb)
		}
	}
	c.subscribers = filtered
}

func (c *Channel) SubscriberCount() int {
	c.mu.RLock()
	defer c.mu.RUnlock()
	return len(c.subscribers)
}

func (c *Channel) String() string {
	return fmt.Sprintf("Channel<%s>(name='%s')", c.EventType, c.Name)
}

// Subscriber wraps a named callback.
type Subscriber struct {
	Name     string
	Callback func(Event) error
}

func (s *Subscriber) HandleEvent(event Event) error {
	if s.Callback != nil {
		return s.Callback(event)
	}
	return nil
}

// EventBus is the central event bus managing channels and message routing.
type EventBus struct {
	channels    map[string]*Channel
	subscribers map[string][]*Subscriber
	mu          sync.RWMutex
}

func NewEventBus() *EventBus {
	return &EventBus{
		channels:    make(map[string]*Channel),
		subscribers: make(map[string][]*Subscriber),
	}
}

func (bus *EventBus) CreateChannel(name string, eventType string) *Channel {
	bus.mu.Lock()
	defer bus.mu.Unlock()
	if _, exists := bus.channels[name]; exists {
		panic(fmt.Sprintf("Channel '%s' already exists", name))
	}
	ch := NewChannel(name, eventType)
	bus.channels[name] = ch
	bus.subscribers[name] = nil
	return ch
}

func (bus *EventBus) GetChannel(name string) (*Channel, bool) {
	bus.mu.RLock()
	defer bus.mu.RUnlock()
	ch, ok := bus.channels[name]
	return ch, ok
}

func (bus *EventBus) Subscribe(channelName string, sub *Subscriber) {
	bus.mu.Lock()
	defer bus.mu.Unlock()
	ch, ok := bus.channels[channelName]
	if !ok {
		panic(fmt.Sprintf("Channel '%s' does not exist", channelName))
	}
	bus.subscribers[channelName] = append(bus.subscribers[channelName], sub)
	ch.Subscribe(func(event Event) error { return sub.HandleEvent(event) })
}

func (bus *EventBus) Publish(channelName string, payload interface{}) error {
	bus.mu.RLock()
	ch, ok := bus.channels[channelName]
	bus.mu.RUnlock()
	if !ok {
		return fmt.Errorf("Channel '%s' does not exist", channelName)
	}

	// Type verification using the registered type name.
	if ch.EventType != "interface{}" && fmt.Sprintf("%T", payload) != ch.EventType {
		return fmt.Errorf("Payload type %T does not match channel type %s", payload, ch.EventType)
	}

	event := Event{
		Payload:   payload,
		Timestamp: time.Now(),
		Channel:   channelName,
	}

	bus.mu.RLock()
	subs := make([]*Subscriber, len(bus.subscribers[channelName]))
	copy(subs, bus.subscribers[channelName])
	bus.mu.RUnlock()

	var wg sync.WaitGroup
	errCh := make(chan error, len(subs))
	for _, sub := range subs {
		wg.Add(1)
		go func(s *Subscriber) {
			defer wg.Done()
			if err := s.HandleEvent(event); err != nil {
				errCh <- err
			}
		}(sub)
	}
	wg.Wait()
	close(errCh)
	for err := range errCh {
		if err != nil {
			return err
		}
	}
	return nil
}

func (bus *EventBus) Unsubscribe(channelName string, sub *Subscriber) {
	bus.mu.Lock()
	defer bus.mu.Unlock()
	if _, ok := bus.channels[channelName]; !ok {
		panic(fmt.Sprintf("Channel '%s' does not exist", channelName))
	}
	filtered := bus.subscribers[channelName][:0]
	for _, s := range bus.subscribers[channelName] {
		if s != sub {
			filtered = append(filtered, s)
		}
	}
	bus.subscribers[channelName] = filtered
}

func (bus *EventBus) Close() {
	bus.mu.Lock()
	defer bus.mu.Unlock()
	for k := range bus.channels {
		delete(bus.channels, k)
	}
	for k := range bus.subscribers {
		delete(bus.subscribers, k)
	}
}

func main() {
	bus := NewEventBus()

	bus.CreateChannel("strings", "string")
	bus.CreateChannel("integers", "int")
	bus.CreateChannel("dictionaries", "map[string]interface {}")

	received := map[string][]interface{}{
		"string_consumer1": {},
		"string_consumer2": {},
		"int_consumer":     {},
		"dict_consumer":    {},
	}
	var mu sync.Mutex

	makeStringHandler := func(name string) func(Event) error {
		return func(event Event) error {
			mu.Lock()
			received[name] = append(received[name], event.Payload)
			mu.Unlock()
			time.Sleep(10 * time.Millisecond)
			return nil
		}
	}
	makeIntHandler := func(name string) func(Event) error {
		return func(event Event) error {
			mu.Lock()
			received[name] = append(received[name], event.Payload)
			mu.Unlock()
			time.Sleep(10 * time.Millisecond)
			return nil
		}
	}
	makeDictHandler := func(name string) func(Event) error {
		return func(event Event) error {
			mu.Lock()
			received[name] = append(received[name], event.Payload)
			mu.Unlock()
			time.Sleep(10 * time.Millisecond)
			return nil
		}
	}

	stringSub1 := &Subscriber{Name: "string_consumer1", Callback: makeStringHandler("string_consumer1")}
	stringSub2 := &Subscriber{Name: "string_consumer2", Callback: makeStringHandler("string_consumer2")}
	intSub := &Subscriber{Name: "int_consumer", Callback: makeIntHandler("int_consumer")}
	dictSub := &Subscriber{Name: "dict_consumer", Callback: makeDictHandler("dict_consumer")}

	bus.Subscribe("strings", stringSub1)
	bus.Subscribe("strings", stringSub2)
	bus.Subscribe("integers", intSub)
	bus.Subscribe("dictionaries", dictSub)

	ctx := context.Background()
	produceStrings := func() error {
		for i := 0; i < 5; i++ {
			if err := bus.Publish("strings", fmt.Sprintf("Hello %d", i)); err != nil {
				return err
			}
			time.Sleep(50 * time.Millisecond)
		}
		return nil
	}
	produceInts := func() error {
		for i := 0; i < 5; i++ {
			if err := bus.Publish("integers", i*10); err != nil {
				return err
			}
			time.Sleep(50 * time.Millisecond)
		}
		return nil
	}
	produceDicts := func() error {
		for i := 0; i < 3; i++ {
			if err := bus.Publish("dictionaries", map[string]interface{}{
				"id":    i,
				"value": fmt.Sprintf("data_%d", i),
			}); err != nil {
				return err
			}
			time.Sleep(70 * time.Millisecond)
		}
		return nil
	}

	_ = ctx
	if err := produceStrings(); err != nil {
		fmt.Fprintf(os.Stderr, "produce strings: %v\n", err)
		os.Exit(1)
	}
	if err := produceInts(); err != nil {
		fmt.Fprintf(os.Stderr, "produce ints: %v\n", err)
		os.Exit(1)
	}
	if err := produceDicts(); err != nil {
		fmt.Fprintf(os.Stderr, "produce dicts: %v\n", err)
		os.Exit(1)
	}

	time.Sleep(200 * time.Millisecond)

	fmt.Println("\n=== Event Bus Demo Summary ===")
	for consumer, events := range received {
		fmt.Printf("%s: %d events received\n", consumer, len(events))
		if len(events) > 0 {
			end := 3
			if len(events) < end {
				end = len(events)
			}
			fmt.Printf("  Sample: %v", events[:end])
			if len(events) > 3 {
				fmt.Print("...")
			}
			fmt.Println()
		}
	}

	fmt.Println("\n=== Error Handling Demo ===")
	if err := bus.Publish("strings", 123); err != nil {
		fmt.Printf("Type error caught: %v\n", err)
	}
	if err := bus.Publish("nonexistent", "test"); err != nil {
		fmt.Printf("Value error caught: %v\n", err)
	}

	bus.Close()
	fmt.Println("\nDemo completed successfully!")
}
