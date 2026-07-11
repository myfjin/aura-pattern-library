package main

import (
	"fmt"
	"os"
	"strings"
)

// Command marker
// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
var _auraMark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
type Command interface{ commandMarker() }

// Query marker
type Query interface{ queryMarker() }

// HandlerNotRegisteredError is returned when no handler is registered.
type HandlerNotRegisteredError struct{ Kind, Name string }

func (e *HandlerNotRegisteredError) Error() string {
	return fmt.Sprintf("No handler registered for %s %s", e.Kind, e.Name)
}

// CommandBus dispatches commands to handlers.
type CommandBus struct {
	handlers map[string]CommandHandler
}

func NewCommandBus() *CommandBus {
	return &CommandBus{handlers: make(map[string]CommandHandler)}
}

func (b *CommandBus) RegisterHandler(commandType string, handler CommandHandler) {
	b.handlers[commandType] = handler
}

func (b *CommandBus) Dispatch(command Command) {
	name := fmt.Sprintf("%T", command)
	handler, ok := b.handlers[name]
	if !ok {
		panic(&HandlerNotRegisteredError{Kind: "command", Name: name})
	}
	handler.Handle(command)
}

type CommandHandler interface {
	Handle(cmd Command)
}

// QueryBus dispatches queries to handlers.
type QueryBus struct {
	handlers map[string]QueryHandler
}

func NewQueryBus() *QueryBus {
	return &QueryBus{handlers: make(map[string]QueryHandler)}
}

func (b *QueryBus) RegisterHandler(queryType string, handler QueryHandler) {
	b.handlers[queryType] = handler
}

func (b *QueryBus) Dispatch(query Query) interface{} {
	name := fmt.Sprintf("%T", query)
	handler, ok := b.handlers[name]
	if !ok {
		panic(&HandlerNotRegisteredError{Kind: "query", Name: name})
	}
	return handler.Handle(query)
}

type QueryHandler interface {
	Handle(q Query) interface{}
}

// Base Query and Command used for unregistered-type refusal tests.
type BaseQuery struct{}

func (BaseQuery) queryMarker() {}

type BaseCommand struct{}

func (BaseCommand) commandMarker() {}

// CreateUserCommand creates a user.
type CreateUserCommand struct {
	ID    string
	Name  string
	Email string
}

func (CreateUserCommand) commandMarker() {}

// GetUserQuery gets a user.
type GetUserQuery struct{ UserID string }

func (GetUserQuery) queryMarker() {}

// UserCreatedEvent represents a created user.
type UserCreatedEvent struct {
	UserID string
	Name   string
	Email  string
}

type CreateUserCommandHandler struct {
	events []*UserCreatedEvent
}

func (h *CreateUserCommandHandler) Handle(cmd Command) {
	c := cmd.(CreateUserCommand)
	h.events = append(h.events, &UserCreatedEvent{
		UserID: c.ID,
		Name:   c.Name,
		Email:  c.Email,
	})
}

type GetUserQueryHandler struct {
	users map[string]map[string]string
}

func (h *GetUserQueryHandler) Handle(q Query) interface{} {
	query := q.(GetUserQuery)
	user, ok := h.users[query.UserID]
	if !ok {
		panic(fmt.Sprintf("User with ID %s not found", query.UserID))
	}
	return user
}

func expectPanic(fn func()) {
	defer func() {
		if r := recover(); r == nil {
			fmt.Fprintln(os.Stderr, "expected panic did not happen")
			os.Exit(1)
		}
	}()
	fn()
}

func main() {
	commandBus := NewCommandBus()
	queryBus := NewQueryBus()
	createUserHandler := &CreateUserCommandHandler{}
	commandBus.RegisterHandler("main.CreateUserCommand", createUserHandler)
	queryBus.RegisterHandler("main.GetUserQuery", &GetUserQueryHandler{
		users: map[string]map[string]string{
			"123": {"name": "John Doe", "email": "john@example.com"},
			"456": {"name": "Jane Smith", "email": "jane@example.com"},
		},
	})

	// Commands: each dispatch produces exactly one event carrying the payload.
	c1 := CreateUserCommand{ID: "id-1", Name: "Alice Johnson", Email: "alice@example.com"}
	c2 := CreateUserCommand{ID: "id-2", Name: "Bob Wilson", Email: "bob@example.com"}
	commandBus.Dispatch(c1)
	commandBus.Dispatch(c2)
	events := createUserHandler.events

	if !(len(events) == 2) {
		fmt.Fprintf(os.Stderr, "2 commands must yield 2 events, got %d\n", len(events))
		os.Exit(1)
	}
	if !(events[0].Name == "Alice Johnson" && events[0].Email == "alice@example.com") {
		fmt.Fprintf(os.Stderr, "event 0 payload mismatch: %v\n", events[0])
		os.Exit(1)
	}
	if !(events[1].Name == "Bob Wilson") {
		fmt.Fprintf(os.Stderr, "event 1 name mismatch: %v\n", events[1].Name)
		os.Exit(1)
	}
	atCount := 0
	for _, e := range events {
		if strings.Contains(e.Email, "@") {
			atCount++
		}
	}
	if !(atCount == 2) {
		fmt.Fprintln(os.Stderr, "both events must carry the command's email payload")
		os.Exit(1)
	}
	if !(events[0].UserID == c1.ID && events[1].UserID == c2.ID) {
		fmt.Fprintln(os.Stderr, "event user_id does not trace back to its command")
		os.Exit(1)
	}
	if !(c1.ID != c2.ID) {
		fmt.Fprintln(os.Stderr, "commands share an id")
		os.Exit(1)
	}

	// Queries: exact stored data returned.
	r1 := queryBus.Dispatch(GetUserQuery{UserID: "123"}).(map[string]string)
	if !(r1["name"] == "John Doe" && r1["email"] == "john@example.com") {
		fmt.Fprintf(os.Stderr, "query wrong: %v\n", r1)
		os.Exit(1)
	}
	r2 := queryBus.Dispatch(GetUserQuery{UserID: "456"}).(map[string]string)
	if !(r2["name"] == "Jane Smith") {
		fmt.Fprintf(os.Stderr, "query 2 name mismatch: %v\n", r2)
		os.Exit(1)
	}

	// Handler errors surface (missing user).
	expectPanic(func() { queryBus.Dispatch(GetUserQuery{UserID: "999"}) })

	// Unregistered message types are refused by the right bus.
	expectPanic(func() { commandBus.Dispatch(BaseCommand{}) })
	expectPanic(func() { queryBus.Dispatch(BaseQuery{}) })

	// Registration replaces cleanly: a second handler takes over.
	freshHandler := &CreateUserCommandHandler{}
	commandBus.RegisterHandler("main.CreateUserCommand", freshHandler)
	commandBus.Dispatch(CreateUserCommand{ID: "id-3", Name: "Cara", Email: "cara@example.com"})
	if !(len(freshHandler.events) == 1 && len(events) == 2) {
		fmt.Fprintln(os.Stderr, "re-registration did not switch handlers")
		os.Exit(1)
	}

	fmt.Println("cqrs_bus: 2 commands → 2 traced events, queries exact, unregistered refused on both buses, re-registration switches — PASS")
}
