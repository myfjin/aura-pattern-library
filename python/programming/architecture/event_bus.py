"""
Event Bus with Typed Channels

A lightweight event bus implementation supporting typed channels, asynchronous
delivery, and type-safe message passing.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import asyncio
import logging
from typing import (
    Any,
    Awaitable,
    Callable,
    Dict,
    Generic,
    List,
    Optional,
    Set,
    Type,
    TypeVar,
    Union,
)
from collections import defaultdict
from dataclasses import dataclass
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Type variables for generic typing
T = TypeVar("T")
EventType = TypeVar("EventType")

# Type alias for subscriber callbacks
SubscriberCallback = Callable[[Any], Union[None, Awaitable[None]]]


@dataclass
class Event(Generic[T]):
    """Base event class with typed payload."""

    payload: T
    timestamp: datetime
    channel: str


class Channel(Generic[T]):
    """Typed channel for event distribution."""

    def __init__(self, name: str, event_type: Type[T]):
        self.name = name
        self.event_type = event_type
        self._subscribers: Set[SubscriberCallback] = set()

    def subscribe(self, callback: SubscriberCallback) -> None:
        """Subscribe a callback to this channel."""
        self._subscribers.add(callback)

    def unsubscribe(self, callback: SubscriberCallback) -> None:
        """Unsubscribe a callback from this channel."""
        self._subscribers.discard(callback)

    @property
    def subscriber_count(self) -> int:
        """Get the number of subscribers."""
        return len(self._subscribers)

    def __str__(self) -> str:
        return f"Channel<{self.event_type.__name__}>(name='{self.name}')"


class Subscriber(Generic[T]):
    """Subscriber that handles events of a specific type."""

    def __init__(
        self,
        name: str,
        callback: Callable[[Event[T]], Union[None, Awaitable[None]]],
    ):
        self.name = name
        self.callback = callback

    async def handle_event(self, event: Event[T]) -> None:
        """Handle an incoming event."""
        try:
            result = self.callback(event)
            if asyncio.iscoroutine(result):
                await result
        except Exception as e:
            logger.error(f"Subscriber {self.name} failed to handle event: {e}")


class EventBus:
    """Central event bus managing channels and message routing."""

    def __init__(self):
        self._channels: Dict[str, Channel[Any]] = {}
        self._subscribers: Dict[str, List[Subscriber[Any]]] = defaultdict(list)
        self._lock = asyncio.Lock()

    def create_channel(self, name: str, event_type: Type[T]) -> Channel[T]:
        """Create a new typed channel."""
        if name in self._channels:
            raise ValueError(f"Channel '{name}' already exists")

        channel = Channel(name, event_type)
        self._channels[name] = channel
        return channel

    def get_channel(self, name: str) -> Optional[Channel[Any]]:
        """Get a channel by name."""
        return self._channels.get(name)

    def subscribe(
        self,
        channel_name: str,
        subscriber: Subscriber[Any],
    ) -> None:
        """Subscribe to a channel."""
        if channel_name not in self._channels:
            raise ValueError(f"Channel '{channel_name}' does not exist")

        self._subscribers[channel_name].append(subscriber)
        self._channels[channel_name].subscribe(subscriber.handle_event)

    async def publish(self, channel_name: str, payload: Any) -> None:
        """Publish an event to a channel."""
        if channel_name not in self._channels:
            raise ValueError(f"Channel '{channel_name}' does not exist")

        channel = self._channels[channel_name]
        event = Event(
            payload=payload,
            timestamp=datetime.now(),
            channel=channel_name,
        )

        # Verify payload type matches channel type
        if not isinstance(payload, channel.event_type):
            raise TypeError(
                f"Payload type {type(payload)} does not match "
                f"channel type {channel.event_type}"
            )

        # Deliver to all subscribers
        subscribers = self._subscribers[channel_name]
        if not subscribers:
            logger.debug(f"No subscribers for channel '{channel_name}'")
            return

        tasks = [
            asyncio.create_task(sub.handle_event(event)) for sub in subscribers
        ]
        
        if tasks:
            await asyncio.gather(*tasks, return_exceptions=True)

    def unsubscribe(self, channel_name: str, subscriber: Subscriber[Any]) -> None:
        """Unsubscribe from a channel."""
        if channel_name not in self._channels:
            raise ValueError(f"Channel '{channel_name}' does not exist")

        if subscriber in self._subscribers[channel_name]:
            self._subscribers[channel_name].remove(subscriber)
            self._channels[channel_name].unsubscribe(subscriber.handle_event)

    async def close(self) -> None:
        """Close the event bus and clean up resources."""
        self._channels.clear()
        self._subscribers.clear()


# Demo section
async def main():
    """Demo producer-consumer flow with typed channels."""
    # Create event bus
    bus = EventBus()

    # Create typed channels
    string_channel = bus.create_channel("strings", str)
    int_channel = bus.create_channel("integers", int)
    dict_channel = bus.create_channel("dictionaries", dict)

    # Track received events
    received_events = {
        "string_consumer1": [],
        "string_consumer2": [],
        "int_consumer": [],
        "dict_consumer": [],
    }

    # Create subscribers
    def make_string_handler(name: str):
        async def handler(event: Event[str]) -> None:
            logger.info(f"{name} received: {event.payload}")
            received_events[name].append(event.payload)
            # Simulate async work
            await asyncio.sleep(0.01)
        return handler

    def make_int_handler(name: str):
        async def handler(event: Event[int]) -> None:
            logger.info(f"{name} received: {event.payload}")
            received_events[name].append(event.payload)
            await asyncio.sleep(0.01)
        return handler

    def make_dict_handler(name: str):
        async def handler(event: Event[dict]) -> None:
            logger.info(f"{name} received: {event.payload}")
            received_events[name].append(event.payload)
            await asyncio.sleep(0.01)
        return handler

    string_sub1 = Subscriber("string_consumer1", make_string_handler("string_consumer1"))
    string_sub2 = Subscriber("string_consumer2", make_string_handler("string_consumer2"))
    int_sub = Subscriber("int_consumer", make_int_handler("int_consumer"))
    dict_sub = Subscriber("dict_consumer", make_dict_handler("dict_consumer"))

    # Subscribe to channels
    bus.subscribe("strings", string_sub1)
    bus.subscribe("strings", string_sub2)
    bus.subscribe("integers", int_sub)
    bus.subscribe("dictionaries", dict_sub)

    # Producer tasks
    async def produce_strings():
        for i in range(5):
            await bus.publish("strings", f"Hello {i}")
            await asyncio.sleep(0.05)

    async def produce_ints():
        for i in range(5):
            await bus.publish("integers", i * 10)
            await asyncio.sleep(0.05)

    async def produce_dicts():
        for i in range(3):
            await bus.publish("dictionaries", {"id": i, "value": f"data_{i}"})
            await asyncio.sleep(0.07)

    # Run producers concurrently
    await asyncio.gather(
        produce_strings(),
        produce_ints(),
        produce_dicts(),
    )

    # Allow time for all events to be processed
    await asyncio.sleep(0.2)

    # Print summary
    print("\n=== Event Bus Demo Summary ===")
    for consumer, events in received_events.items():
        print(f"{consumer}: {len(events)} events received")
        if events:
            print(f"  Sample: {events[:3]}{'...' if len(events) > 3 else ''}")

    # Test error handling
    print("\n=== Error Handling Demo ===")
    try:
        await bus.publish("strings", 123)  # Wrong type
    except TypeError as e:
        print(f"Type error caught: {e}")

    try:
        await bus.publish("nonexistent", "test")  # Nonexistent channel
    except ValueError as e:
        print(f"Value error caught: {e}")

    # Clean up
    await bus.close()
    print("\nDemo completed successfully!")


if __name__ == "__main__":
    asyncio.run(main())