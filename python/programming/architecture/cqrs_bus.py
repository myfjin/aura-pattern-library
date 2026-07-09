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
        print(f"Created user: {command.name} ({command.email}) with ID {command.id}")


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
    """Demo the CQRS implementation"""
    # Create buses
    command_bus = CommandBus()
    query_bus = QueryBus()
    
    # Create and register handlers
    create_user_handler = CreateUserCommandHandler()
    get_user_handler = GetUserQueryHandler()
    
    command_bus.register_handler(CreateUserCommand, create_user_handler)
    query_bus.register_handler(GetUserQuery, get_user_handler)
    
    # Dispatch commands
    command1 = CreateUserCommand("Alice Johnson", "alice@example.com")
    command2 = CreateUserCommand("Bob Wilson", "bob@example.com")
    
    command_bus.dispatch(command1)
    command_bus.dispatch(command2)
    
    # Dispatch queries
    query1 = GetUserQuery("123")
    query2 = GetUserQuery("456")
    
    result1 = query_bus.dispatch(query1)
    result2 = query_bus.dispatch(query2)
    
    print(f"Query 1 result: {result1}")
    print(f"Query 2 result: {result2}")
    
    # Test error handling
    try:
        query_bus.dispatch(GetUserQuery("999"))  # Non-existent user
    except ValueError as e:
        print(f"Caught expected error: {e}")
    
    try:
        command_bus.dispatch(Query())  # Not a registered command
    except HandlerNotRegisteredException as e:
        print(f"Caught expected error: {e}")


if __name__ == "__main__":
    main()