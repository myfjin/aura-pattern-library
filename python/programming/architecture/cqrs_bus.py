"""
Simple CQRS Command/Query Splitter Module

This module implements a basic Command Query Responsibility Segregation (CQRS) pattern
with separate buses for commands and queries, handler registration, and dispatch mechanisms.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

from typing import Any, Callable, Dict, Type, TypeVar, Generic
from abc import ABC, abstractmethod
import uuid


T = TypeVar('T')


class Command(ABC):
    """Base class for all commands"""
    def __init__(self) -> None:
        self.id = str(uuid.uuid4())


class Query(ABC):
    """Base class for all queries"""
    def __init__(self) -> None:
        self.id = str(uuid.uuid4())


class Handler(ABC, Generic[T]):
    """Base handler interface"""
    @abstractmethod
    def handle(self, message: T) -> Any:
        pass


class CommandHandler(Handler[Command], ABC):
    """Base command handler"""
    pass


class QueryHandler(Handler[Query], ABC):
    """Base query handler"""
    @abstractmethod
    def handle(self, query: Query) -> Any:
        pass


class HandlerNotRegisteredException(Exception):
    """Raised when no handler is registered for a command or query"""
    pass


class CommandBus:
    """Dispatches commands to their registered handlers"""
    
    def __init__(self) -> None:
        self._handlers: Dict[Type[Command], CommandHandler] = {}
    
    def register_handler(self, command_type: Type[Command], handler: CommandHandler) -> None:
        """
        Register a handler for a specific command type
        
        Args:
            command_type: The command class to handle
            handler: The handler instance
        """
        self._handlers[command_type] = handler
    
    def dispatch(self, command: Command) -> None:
        """
        Dispatch a command to its registered handler
        
        Args:
            command: The command to dispatch
            
        Raises:
            HandlerNotRegisteredException: If no handler is registered for the command
        """
        handler = self._handlers.get(type(command))
        if handler is None:
            raise HandlerNotRegisteredException(f"No handler registered for command {type(command).__name__}")
        handler.handle(command)


class QueryBus:
    """Dispatches queries to their registered handlers"""
    
    def __init__(self) -> None:
        self._handlers: Dict[Type[Query], QueryHandler] = {}
    
    def register_handler(self, query_type: Type[Query], handler: QueryHandler) -> None:
        """
        Register a handler for a specific query type
        
        Args:
            query_type: The query class to handle
            handler: The handler instance
        """
        self._handlers[query_type] = handler
    
    def dispatch(self, query: Query) -> Any:
        """
        Dispatch a query to its registered handler
        
        Args:
            query: The query to dispatch
            
        Returns:
            The result from the query handler
            
        Raises:
            HandlerNotRegisteredException: If no handler is registered for the query
        """
        handler = self._handlers.get(type(query))
        if handler is None:
            raise HandlerNotRegisteredException(f"No handler registered for query {type(query).__name__}")
        return handler.handle(query)


# Demo classes
class CreateUserCommand(Command):
    """Command to create a user"""
    def __init__(self, name: str, email: str) -> None:
        super().__init__()
        self.name = name
        self.email = email


class GetUserQuery(Query):
    """Query to get user information"""
    def __init__(self, user_id: str) -> None:
        super().__init__()
        self.user_id = user_id


class UserCreatedEvent:
    """Event representing a created user"""
    def __init__(self, user_id: str, name: str, email: str) -> None:
        self.user_id = user_id
        self.name = name
        self.email = email


class CreateUserCommandHandler(CommandHandler):
    """Handler for creating users"""
    
    def __init__(self) -> None:
        self._events: list = []
    
    def handle(self, command: CreateUserCommand) -> None:
        # In a real system, this would save to a database
        event = UserCreatedEvent(
            user_id=command.id,
            name=command.name,
            email=command.email
        )
        self._events.append(event)
        print(f"Created user: {command.name} ({command.email})")


class GetUserQueryHandler(QueryHandler):
    """Handler for getting user information"""
    
    def __init__(self) -> None:
        # In a real system, this would fetch from a database
        self._users = {
            "123": {"name": "John Doe", "email": "john@example.com"},
            "456": {"name": "Jane Smith", "email": "jane@example.com"}
        }
    
    def handle(self, query: GetUserQuery) -> Dict[str, str]:
        user = self._users.get(query.user_id)
        if user is None:
            raise ValueError(f"User with ID {query.user_id} not found")
        return user


def main() -> None:
    """Self-test: commands route to their handler and produce events with the
    exact payloads; queries return exact data; unregistered types refused."""
    command_bus = CommandBus()
    query_bus = QueryBus()
    create_user_handler = CreateUserCommandHandler()
    command_bus.register_handler(CreateUserCommand, create_user_handler)
    query_bus.register_handler(GetUserQuery, GetUserQueryHandler())

    # Commands: each dispatch produces exactly one event carrying the payload.
    c1 = CreateUserCommand("Alice Johnson", "alice@example.com")
    c2 = CreateUserCommand("Bob Wilson", "bob@example.com")
    command_bus.dispatch(c1)
    command_bus.dispatch(c2)
    events = create_user_handler._events
    assert len(events) == 2, f"2 commands must yield 2 events, got {len(events)}"
    assert events[0].name == "Alice Johnson" and events[0].email == "alice@example.com"
    assert events[1].name == "Bob Wilson"
    assert sum(1 for e in events if "@" in e.email) == 2, \
        "both events must carry the command's email payload"
    assert events[0].user_id == c1.id and events[1].user_id == c2.id, \
        "event user_id does not trace back to its command"
    assert c1.id != c2.id, "commands share an id"

    # Queries: exact stored data returned.
    r1 = query_bus.dispatch(GetUserQuery("123"))
    assert r1 == {"name": "John Doe", "email": "john@example.com"}, f"query wrong: {r1}"
    r2 = query_bus.dispatch(GetUserQuery("456"))
    assert r2["name"] == "Jane Smith"

    # Handler errors surface (missing user).
    try:
        query_bus.dispatch(GetUserQuery("999"))
        assert False, "missing user returned a result"
    except ValueError:
        pass

    # Unregistered message types are refused by the right bus.
    try:
        command_bus.dispatch(Query())
        assert False, "unregistered command dispatched"
    except HandlerNotRegisteredException:
        pass
    try:
        query_bus.dispatch(Command())
        assert False, "unregistered query dispatched"
    except HandlerNotRegisteredException:
        pass

    # Registration replaces cleanly: a second handler takes over.
    fresh_handler = CreateUserCommandHandler()
    command_bus.register_handler(CreateUserCommand, fresh_handler)
    command_bus.dispatch(CreateUserCommand("Cara", "cara@example.com"))
    assert len(fresh_handler._events) == 1 and len(events) == 2, \
        "re-registration did not switch handlers"

    print("cqrs_bus: 2 commands → 2 traced events, queries exact, unregistered "
          "refused on both buses, re-registration switches — PASS")


if __name__ == "__main__":
    main()