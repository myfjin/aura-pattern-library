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
        
        # Publish to the topic's attached subscribers
        topic = self.topics[topic_name]
        topic.publish(message)

        # Also deliver to pattern subscribers NOT yet attached to this topic
        # (e.g. wildcards that predate the topic). Skipping the already-
        # attached prevents the double delivery the former code produced —
        # every attached subscriber was notified by BOTH paths. Attach them
        # so future publishes go through the fast path exactly once.
        already_attached = set(topic.subscribers.keys())
        for subscriber_id, patterns in list(self.subscriber_topics.items()):
            if subscriber_id in already_attached:
                continue
            if any(self._match_topic(p, topic_name) for p in patterns):
                for t in self.topics.values():
                    if subscriber_id in t.subscribers:
                        subscriber = t.subscribers[subscriber_id]
                        subscriber.notify(topic_name, message)
                        topic.add_subscriber(subscriber)
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
    """Self-test: exact-topic and wildcard delivery verified message-by-
    message, cross-topic isolation, unsubscribe stops delivery."""
    broker = Broker()
    broker.create_topic("news/sports")
    broker.create_topic("news/politics")
    broker.create_topic("weather/local")

    inbox = {"sports": [], "news": [], "weather": []}
    sub_sports = Subscriber("sports-fan", lambda t, m: inbox["sports"].append((t, m)))
    sub_news = Subscriber("news-all", lambda t, m: inbox["news"].append((t, m)))
    sub_weather = Subscriber("weather", lambda t, m: inbox["weather"].append((t, m)))

    broker.subscribe(sub_sports, "news/sports")   # exact
    broker.subscribe(sub_news, "news/#")          # wildcard
    broker.subscribe(sub_weather, "weather/#")    # wildcard

    broker.publish("news/sports", "football")
    broker.publish("news/politics", "election")
    broker.publish("weather/local", "sunny")

    # Exact subscriber: only its topic, exactly once.
    assert inbox["sports"] == [("news/sports", "football")], \
        f"exact subscription wrong: {inbox['sports']}"

    # Wildcard subscriber: BOTH news topics, neither weather.
    assert ("news/sports", "football") in inbox["news"]
    assert ("news/politics", "election") in inbox["news"]
    assert not any(t.startswith("weather") for t, _ in inbox["news"]), \
        "news/# received weather traffic"
    assert inbox["weather"] == [("weather/local", "sunny")]

    # Wildcards catch topics created AFTER subscription.
    broker.publish("news/technology", "gadget")
    assert ("news/technology", "gadget") in inbox["news"], \
        "wildcard missed a newly created topic"
    assert not any(t == "news/technology" for t, _ in inbox["sports"]), \
        "exact subscriber received a foreign topic"

    # No duplicate delivery to the wildcard subscriber per publish.
    n_sports_msgs = sum(1 for t, _ in inbox["news"] if t == "news/sports")
    assert n_sports_msgs == 1, f"wildcard received news/sports {n_sports_msgs} times"

    # UNSUBSCRIBE: the wildcard subscriber goes silent; exact one continues.
    broker.unsubscribe(sub_news, "news/#")
    n_news = len(inbox["news"])
    broker.publish("news/sports", "basketball")
    assert len(inbox["news"]) == n_news, "unsubscribed wildcard still receives"
    assert ("news/sports", "basketball") in inbox["sports"], \
        "exact subscriber lost delivery after another's unsubscribe"

    # Subscriber accounting.
    assert len(broker.get_subscribers("weather/local")) == 1
    assert broker.get_subscribers("ghost/topic") == []
    total = sum(len(v) for v in inbox.values())
    assert total == 6, f"exactly 6 deliveries expected in the whole run, got {total}"

    print("pubsub_broker: exact 1:1, wildcard caught 3 news topics (incl. "
          "late-created), no dupes, unsubscribe silent, 6 total deliveries — PASS")


if __name__ == "__main__":
    main()