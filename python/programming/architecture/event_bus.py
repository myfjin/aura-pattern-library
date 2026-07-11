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


async def main():
    """Self-test: fan-out to every subscriber in order, channel isolation,
    type enforcement, unsubscribe stops delivery."""
    bus = EventBus()
    bus.create_channel("strings", str)
    bus.create_channel("integers", int)
    bus.create_channel("dictionaries", dict)

    received = {"s1": [], "s2": [], "i": [], "d": []}

    def make_handler(name):
        async def handler(event):
            received[name].append(event.payload)
        return handler

    sub_s1 = Subscriber("s1", make_handler("s1"))
    sub_s2 = Subscriber("s2", make_handler("s2"))
    bus.subscribe("strings", sub_s1)
    bus.subscribe("strings", sub_s2)
    bus.subscribe("integers", Subscriber("i", make_handler("i")))
    bus.subscribe("dictionaries", Subscriber("d", make_handler("d")))

    # Publish concurrently from three producers.
    async def produce(channel, payloads):
        for p in payloads:
            await bus.publish(channel, p)
    await asyncio.gather(
        produce("strings", [f"Hello {i}" for i in range(5)]),
        produce("integers", [i * 10 for i in range(5)]),
        produce("dictionaries", [{"id": i} for i in range(3)]),
    )
    await asyncio.sleep(0.1)   # let handlers drain

    # FAN-OUT: both string subscribers got all 5, in publish order.
    assert received["s1"] == [f"Hello {i}" for i in range(5)], \
        f"s1 missed or reordered events: {received['s1']}"
    assert received["s2"] == received["s1"], "fan-out delivered different streams"

    # CHANNEL ISOLATION: ints only to the int subscriber, exact values.
    assert received["i"] == [0, 10, 20, 30, 40], f"int channel wrong: {received['i']}"
    assert sum(received["i"]) == 100, "0+10+20+30+40 must be 100"
    assert received["d"] == [{"id": 0}, {"id": 1}, {"id": 2}]
    assert not any(isinstance(x, int) for x in received["s1"]), \
        "integer leaked into the string channel"

    # TYPE ENFORCEMENT: wrong payload type refused, channel must exist.
    try:
        await bus.publish("strings", 123)
        assert False, "int accepted on a str channel"
    except TypeError:
        pass
    try:
        await bus.publish("nonexistent", "x")
        assert False, "publish to a missing channel accepted"
    except (ValueError, KeyError):
        pass

    # UNSUBSCRIBE: s2 stops receiving; s1 continues.
    bus.unsubscribe("strings", sub_s2)
    await bus.publish("strings", "after-unsub")
    await asyncio.sleep(0.05)
    assert received["s1"][-1] == "after-unsub", "s1 lost delivery after s2 unsubscribed"
    assert "after-unsub" not in received["s2"], "unsubscribed s2 still receives"

    await bus.close()
    print("event_bus: fan-out 5+5 in order, channels isolated (ints sum 100), "
          "type+missing-channel refused, unsubscribe honored — PASS")


if __name__ == "__main__":
    asyncio.run(main())