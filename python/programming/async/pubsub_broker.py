#!/usr/bin/env python3
"""
A simple pub-sub message broker implementation with wildcard topic matching.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import re
import uuid
from typing import Dict, List, Callable, Any, Optional
from collections import defaultdict


class Subscriber:
    """Represents a subscriber to topics in the message broker."""
    
    def __init__(self, name: str, callback: Callable[[str, Any], None]):
        """
        Initialize a subscriber.
        
        Args:
            name: Unique identifier for the subscriber
            callback: Function to call when a message is received
        """
        self.id = str(uuid.uuid4())
        self.name = name
        self.callback = callback
    
    def notify(self, topic: str, message: Any) -> None:
        """
        Notify the subscriber of a new message.
        
        Args:
            topic: The topic the message was published to
            message: The message content
        """
        try:
            self.callback(topic, message)
        except Exception as e:
            print(f"Error in subscriber {self.name} callback: {e}")


class Topic:
    """Represents a topic in the message broker."""
    
    def __init__(self, name: str):
        """
        Initialize a topic.
        
        Args:
            name: Name of the topic
        """
        self.name = name
        self.subscribers: Dict[str, Subscriber] = {}
    
    def add_subscriber(self, subscriber: Subscriber) -> None:
        """
        Add a subscriber to this topic.
        
        Args:
            subscriber: The subscriber to add
        """
        self.subscribers[subscriber.id] = subscriber
    
    def remove_subscriber(self, subscriber_id: str) -> bool:
        """
        Remove a subscriber from this topic.
        
        Args:
            subscriber_id: ID of the subscriber to remove
            
        Returns:
            True if subscriber was removed, False if not found
        """
        if subscriber_id in self.subscribers:
            del self.subscribers[subscriber_id]
            return True
        return False
    
    def publish(self, message: Any) -> None:
        """
        Publish a message to all subscribers of this topic.
        
        Args:
            message: The message to publish
        """
        for subscriber in list(self.subscribers.values()):
            subscriber.notify(self.name, message)


class Broker:
    """Main message broker that manages topics and subscribers."""
    
    def __init__(self):
        """Initialize the broker."""
        self.topics: Dict[str, Topic] = {}
        self.subscriber_topics: Dict[str, List[str]] = defaultdict(list)
    
    def _match_topic(self, pattern: str, topic: str) -> bool:
        """
        Check if a topic matches a pattern with wildcards.
        
        Args:
            pattern: Pattern with wildcards (* for single level, # for multi-level)
            topic: Actual topic name
            
        Returns:
            True if topic matches pattern, False otherwise
        """
        # Convert pattern to regex
        # Replace # (multi-level wildcard) with .*
        # Replace * (single-level wildcard) with [^.]*
        regex_pattern = pattern.replace(r'.', r'\.')
        regex_pattern = regex_pattern.replace(r'#', r'.*')
        regex_pattern = regex_pattern.replace(r'*', r'[^.]*')
        regex_pattern = f"^{regex_pattern}$"
        
        return bool(re.match(regex_pattern, topic))
    
    def create_topic(self, name: str) -> Topic:
        """
        Create a new topic.
        
        Args:
            name: Name of the topic to create
            
        Returns:
            The created topic
            
        Raises:
            ValueError: If topic already exists
        """
        if name in self.topics:
            raise ValueError(f"Topic '{name}' already exists")
        
        topic = Topic(name)
        self.topics[name] = topic
        return topic
    
    def get_topic(self, name: str) -> Optional[Topic]:
        """
        Get a topic by name.
        
        Args:
            name: Name of the topic
            
        Returns:
            The topic or None if not found
        """
        return self.topics.get(name)
    
    def subscribe(self, subscriber: Subscriber, topic_pattern: str) -> None:
        """
        Subscribe a subscriber to topics matching a pattern.
        
        Args:
            subscriber: The subscriber
            topic_pattern: Topic pattern to subscribe to (supports wildcards)
        """
        # Add to subscriber tracking
        if topic_pattern not in self.subscriber_topics[subscriber.id]:
            self.subscriber_topics[subscriber.id].append(topic_pattern)
        
        # Add to existing matching topics
        for topic_name, topic in self.topics.items():
            if self._match_topic(topic_pattern, topic_name):
                topic.add_subscriber(subscriber)
    
    def unsubscribe(self, subscriber: Subscriber, topic_pattern: str) -> None:
        """
        Unsubscribe a subscriber from topics matching a pattern.
        
        Args:
            subscriber: The subscriber
            topic_pattern: Topic pattern to unsubscribe from
        """
        # Remove from subscriber tracking
        if subscriber.id in self.subscriber_topics:
            if topic_pattern in self.subscriber_topics[subscriber.id]:
                self.subscriber_topics[subscriber.id].remove(topic_pattern)
        
        # Remove from matching topics
        for topic_name, topic in self.topics.items():
            if self._match_topic(topic_pattern, topic_name):
                topic.remove_subscriber(subscriber.id)
    
    def publish(self, topic_name: str, message: Any) -> None:
        """
        Publish a message to a topic.
        
        Args:
            topic_name: Name of the topic to publish to
            message: Message to publish
        """
        # Create topic if it doesn't exist
        if topic_name not in self.topics:
            self.create_topic(topic_name)
        
        # Publish to the topic
        topic = self.topics[topic_name]
        topic.publish(message)
        
        # Also publish to subscribers of matching wildcard topics
        for subscriber_id, patterns in self.subscriber_topics.items():
            for pattern in patterns:
                if self._match_topic(pattern, topic_name):
                    # Find the subscriber
                    for t in self.topics.values():
                        if subscriber_id in [s.id for s in t.subscribers.values()]:
                            subscriber = t.subscribers[subscriber_id]
                            subscriber.notify(topic_name, message)
                            break
    
    def get_subscribers(self, topic_name: str) -> List[Subscriber]:
        """
        Get all subscribers for a topic.
        
        Args:
            topic_name: Name of the topic
            
        Returns:
            List of subscribers
        """
        if topic_name in self.topics:
            return list(self.topics[topic_name].subscribers.values())
        return []


def main():
    """Demo the message broker functionality."""
    # Create broker
    broker = Broker()
    
    # Create topics
    broker.create_topic("news/sports")
    broker.create_topic("news/politics")
    broker.create_topic("weather/local")
    
    # Create subscribers
    def callback1(topic: str, message: Any) -> None:
        print(f"Subscriber 1 received on '{topic}': {message}")
    
    def callback2(topic: str, message: Any) -> None:
        print(f"Subscriber 2 received on '{topic}': {message}")
    
    def callback3(topic: str, message: Any) -> None:
        print(f"Subscriber 3 received on '{topic}': {message}")
    
    sub1 = Subscriber("Sports Fan", callback1)
    sub2 = Subscriber("News Enthusiast", callback2)
    sub3 = Subscriber("Weather Watcher", callback3)
    
    # Subscribe to topics
    broker.subscribe(sub1, "news/sports")  # Exact match
    broker.subscribe(sub2, "news/#")       # Wildcard for all news
    broker.subscribe(sub3, "weather/#")    # Wildcard for all weather
    
    # Publish messages
    print("Publishing messages...")
    broker.publish("news/sports", "Football game tonight!")
    broker.publish("news/politics", "Election results coming in")
    broker.publish("weather/local", "Sunny with chance of rain")
    
    # Test wildcard subscription
    print("\nTesting wildcard subscriptions...")
    broker.publish("news/technology", "New smartphone released")
    broker.publish("weather/national", "Hurricane approaching")
    
    # Test unsubscribing
    print("\nUnsubscribing News Enthusiast from news topics...")
    broker.unsubscribe(sub2, "news/#")
    broker.publish("news/sports", "Basketball playoffs start soon")
    
    # Show subscriber counts
    print("\nSubscriber counts per topic:")
    for topic_name in ["news/sports", "news/politics", "weather/local"]:
        subscribers = broker.get_subscribers(topic_name)
        print(f"  {topic_name}: {len(subscribers)} subscribers")


if __name__ == "__main__":
    main()