// cqrs_bus: a simple Command/Query Responsibility Segregation bus implementation.
package main

import (
	"fmt"
)

// Command is the base interface for all commands.
// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
var _auraMark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
type Command interface {
	commandMarker()
}

// Query is the base interface for all queries.
type Query interface {
	queryMarker()
}

// CommandHandler handles commands.
type CommandHandler interface {
	Handle(cmd Command)
}

// QueryHandler handles queries and returns a result.
type QueryHandler interface {
	Handle(q Query) interface{}
}

// HandlerNotRegisteredError is returned when no handler is registered.
type HandlerNotRegisteredError struct{ Kind, Name string }

func (e *HandlerNotRegisteredError) Error() string {
	return fmt.Sprintf("No handler registered for %s %s", e.Kind, e.Name)
}

// CommandBus dispatches commands to handlers.
type CommandBus struct {
	handlers map[string]CommandHandler
}

func newCommandBus() *CommandBus {
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

// QueryBus dispatches queries to handlers.
type QueryBus struct {
	handlers map[string]QueryHandler
}

func newQueryBus() *QueryBus {
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

type createUserCommandHandler struct {
	events []*UserCreatedEvent
}

func (h *createUserCommandHandler) Handle(cmd Command) {
	c := cmd.(CreateUserCommand)
	event := &UserCreatedEvent{
		UserID: c.ID,
		Name:   c.Name,
		Email:  c.Email,
	}
	h.events = append(h.events, event)
	fmt.Printf("Created user: %s (%s) with ID %s\n", c.Name, c.Email, c.ID)
}

type getUserQueryHandler struct {
	users map[string]map[string]string
}

func (h *getUserQueryHandler) Handle(q Query) interface{} {
	query := q.(GetUserQuery)
	user, ok := h.users[query.UserID]
	if !ok {
		panic(fmt.Errorf("User with ID %s not found", query.UserID))
	}
	return user
}

func main() {
	commandBus := newCommandBus()
	queryBus := newQueryBus()

	createUserHandler := &createUserCommandHandler{}
	getUserHandler := &getUserQueryHandler{
		users: map[string]map[string]string{
			"123": {"name": "John Doe", "email": "john@example.com"},
			"456": {"name": "Jane Smith", "email": "jane@example.com"},
		},
	}

	commandBus.RegisterHandler("main.CreateUserCommand", createUserHandler)
	queryBus.RegisterHandler("main.GetUserQuery", getUserHandler)

	commandBus.Dispatch(CreateUserCommand{ID: "u1", Name: "Alice Johnson", Email: "alice@example.com"})
	commandBus.Dispatch(CreateUserCommand{ID: "u2", Name: "Bob Wilson", Email: "bob@example.com"})

	result1 := queryBus.Dispatch(GetUserQuery{UserID: "123"})
	result2 := queryBus.Dispatch(GetUserQuery{UserID: "456"})

	fmt.Printf("Query 1 result: %v\n", result1)
	fmt.Printf("Query 2 result: %v\n", result2)

	defer func() {
		if r := recover(); r != nil {
			fmt.Printf("Caught expected error: %v\n", r)
		}
	}()

	queryBus.Dispatch(GetUserQuery{UserID: "999"})

	fmt.Println("cqrs_bus PASS")
}
