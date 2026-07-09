"""
Dead Letter Queue Handler Module

This module provides a complete implementation of a Dead Letter Queue system
with retry policies, exponential backoff, and poison pill detection.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import time
import json
import uuid
from typing import Dict, List, Optional, Callable, Any
from dataclasses import dataclass, asdict
from enum import Enum
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class MessageStatus(Enum):
    """Enumeration of possible message statuses."""
    PENDING = "pending"
    PROCESSING = "processing"
    FAILED = "failed"
    COMPLETED = "completed"
    DEAD_LETTER = "dead_letter"


@dataclass
class DLQMessage:
    """Data class representing a message in the Dead Letter Queue system."""
    id: str
    payload: Dict[str, Any]
    status: MessageStatus = MessageStatus.PENDING
    attempt_count: int = 0
    created_at: float = None
    updated_at: float = None
    error_message: Optional[str] = None
    next_retry_at: Optional[float] = None

    def __post_init__(self):
        """Initialize timestamps if not provided."""
        if self.created_at is None:
            self.created_at = time.time()
        if self.updated_at is None:
            self.updated_at = self.created_at

    def to_dict(self) -> Dict[str, Any]:
        """Convert message to dictionary representation."""
        return {
            "id": self.id,
            "payload": self.payload,
            "status": self.status.value,
            "attempt_count": self.attempt_count,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "error_message": self.error_message,
            "next_retry_at": self.next_retry_at
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'DLQMessage':
        """Create DLQMessage from dictionary representation."""
        data_copy = data.copy()
        if 'status' in data_copy:
            data_copy['status'] = MessageStatus(data_copy['status'])
        return cls(**data_copy)


class RetryPolicy:
    """Defines retry policy with exponential backoff for message processing."""

    def __init__(self, max_retries: int = 3, base_delay: float = 1.0, max_delay: float = 300.0):
        """
        Initialize retry policy.

        Args:
            max_retries: Maximum number of retry attempts
            base_delay: Base delay in seconds for exponential backoff
            max_delay: Maximum delay in seconds between retries
        """
        self.max_retries = max_retries
        self.base_delay = base_delay
        self.max_delay = max_delay

    def calculate_delay(self, attempt: int) -> float:
        """
        Calculate delay for given attempt using exponential backoff.

        Args:
            attempt: Current attempt number (0-indexed)

        Returns:
            Delay in seconds
        """
        if attempt < 0:
            raise ValueError("Attempt must be non-negative")
        
        # Exponential backoff: base_delay * (2 ^ attempt)
        delay = self.base_delay * (2 ** attempt)
        return min(delay, self.max_delay)

    def should_retry(self, attempt_count: int) -> bool:
        """
        Determine if message should be retried based on attempt count.

        Args:
            attempt_count: Number of attempts made so far

        Returns:
            True if should retry, False otherwise
        """
        return attempt_count < self.max_retries


class DeadLetterQueue:
    """Dead Letter Queue handler with retry management and poison pill detection."""

    def __init__(self, retry_policy: Optional[RetryPolicy] = None):
        """
        Initialize Dead Letter Queue.

        Args:
            retry_policy: Retry policy to use, defaults to RetryPolicy()
        """
        self.retry_policy = retry_policy or RetryPolicy()
        self.pending_queue: List[DLQMessage] = []
        self.processing_queue: List[DLQMessage] = []
        self.dead_letter_queue: List[DLQMessage] = []
        self.processed_messages: List[DLQMessage] = []

    def enqueue(self, payload: Dict[str, Any]) -> DLQMessage:
        """
        Add a new message to the pending queue.

        Args:
            payload: Message payload as dictionary

        Returns:
            Created DLQMessage
        """
        message = DLQMessage(
            id=str(uuid.uuid4()),
            payload=payload
        )
        self.pending_queue.append(message)
        logger.info(f"Enqueued message {message.id}")
        return message

    def process_message(self, message: DLQMessage, processor: Callable[[DLQMessage], bool]) -> bool:
        """
        Process a single message with retry logic.

        Args:
            message: Message to process
            processor: Function that processes the message and returns True on success

        Returns:
            True if message was processed successfully, False otherwise
        """
        try:
            message.status = MessageStatus.PROCESSING
            message.updated_at = time.time()
            
            success = processor(message)
            
            if success:
                message.status = MessageStatus.COMPLETED
                message.updated_at = time.time()
                self.processed_messages.append(message)
                logger.info(f"Successfully processed message {message.id}")
                return True
            else:
                raise Exception("Processor returned False")
                
        except Exception as e:
            message.error_message = str(e)
            message.attempt_count += 1
            message.updated_at = time.time()
            
            if self.retry_policy.should_retry(message.attempt_count):
                # Schedule for retry with exponential backoff
                delay = self.retry_policy.calculate_delay(message.attempt_count - 1)
                message.next_retry_at = time.time() + delay
                message.status = MessageStatus.FAILED
                self.pending_queue.append(message)
                logger.warning(f"Failed to process message {message.id}, retrying in {delay:.2f}s "
                             f"(attempt {message.attempt_count}/{self.retry_policy.max_retries})")
            else:
                # Move to dead letter queue - poison pill detected
                message.status = MessageStatus.DEAD_LETTER
                self.dead_letter_queue.append(message)
                logger.error(f"Message {message.id} moved to dead letter queue after {message.attempt_count} attempts")
            
            return False

    def process_queue(self, processor: Callable[[DLQMessage], bool]) -> Dict[str, int]:
        """
        Process all pending messages in the queue.

        Args:
            processor: Function that processes messages

        Returns:
            Dictionary with processing statistics
        """
        stats = {"processed": 0, "failed": 0, "dead_letter": 0}
        
        # Move pending messages that are ready for retry to processing queue
        current_time = time.time()
        ready_messages = []
        remaining_pending = []
        
        for message in self.pending_queue:
            if message.next_retry_at is None or message.next_retry_at <= current_time:
                ready_messages.append(message)
            else:
                remaining_pending.append(message)
        
        self.pending_queue = remaining_pending
        self.processing_queue.extend(ready_messages)
        
        # Process all ready messages
        while self.processing_queue:
            message = self.processing_queue.pop(0)
            success = self.process_message(message, processor)
            
            if success:
                stats["processed"] += 1
            elif message.status == MessageStatus.DEAD_LETTER:
                stats["dead_letter"] += 1
            else:
                stats["failed"] += 1
        
        return stats

    def get_queue_stats(self) -> Dict[str, int]:
        """Get statistics about all queues."""
        return {
            "pending": len(self.pending_queue),
            "processing": len(self.processing_queue),
            "dead_letter": len(self.dead_letter_queue),
            "processed": len(self.processed_messages)
        }

    def get_dead_letter_messages(self) -> List[DLQMessage]:
        """Get all messages in the dead letter queue."""
        return self.dead_letter_queue.copy()

    def retry_dead_letter_message(self, message_id: str) -> bool:
        """
        Move a dead letter message back to pending queue for retry.

        Args:
            message_id: ID of message to retry

        Returns:
            True if message was found and moved, False otherwise
        """
        for i, message in enumerate(self.dead_letter_queue):
            if message.id == message_id:
                message.attempt_count = 0
                message.error_message = None
                message.status = MessageStatus.PENDING
                message.next_retry_at = None
                message.updated_at = time.time()
                
                self.pending_queue.append(self.dead_letter_queue.pop(i))
                logger.info(f"Retrying dead letter message {message_id}")
                return True
        return False


def demo_processor(message: DLQMessage) -> bool:
    """
    Demo message processor that fails for certain messages.
    
    Args:
        message: Message to process
        
    Returns:
        True if processed successfully, False otherwise
    """
    # Simulate processing time
    time.sleep(0.1)
    
    # Fail messages with 'fail' in payload
    if message.payload.get('should_fail', False):
        raise Exception(f"Simulated failure for message {message.id}")
    
    # Fail messages with specific IDs to demonstrate poison pill detection
    if 'poison' in message.payload.get('data', ''):
        raise Exception("Poison pill detected")
    
    return True


def main():
    """Demo the Dead Letter Queue functionality."""
    print("=== Dead Letter Queue Demo ===\n")
    
    # Create DLQ with custom retry policy
    retry_policy = RetryPolicy(max_retries=3, base_delay=1.0)
    dlq = DeadLetterQueue(retry_policy)
    
    # Enqueue some test messages
    messages = [
        {"data": "normal message 1", "should_fail": False},
        {"data": "failing message 1", "should_fail": True},
        {"data": "normal message 2", "should_fail": False},
        {"data": "poison pill message", "should_fail": False},  # Will fail due to content
        {"data": "failing message 2", "should_fail": True},
    ]
    
    for msg_data in messages:
        dlq.enqueue(msg_data)
    
    print(f"Initial queue stats: {dlq.get_queue_stats()}\n")
    
    # Process messages multiple times to demonstrate retries
    for i in range(5):
        print(f"--- Processing Round {i+1} ---")
        stats = dlq.process_queue(demo_processor)
        print(f"Round stats: {stats}")
        print(f"Queue stats: {dlq.get_queue_stats()}\n")
        
        if dlq.get_queue_stats()["pending"] == 0:
            print("No more pending messages.")
            break
        
        # Wait a bit to allow retry delays to pass
        time.sleep(1.5)
    
    # Show dead letter queue contents
    print("=== Dead Letter Queue Contents ===")
    dead_letters = dlq.get_dead_letter_messages()
    for msg in dead_letters:
        print(f"ID: {msg.id}")
        print(f"Payload: {msg.payload}")
        print(f"Attempts: {msg.attempt_count}")
        print(f"Error: {msg.error_message}")
        print("---")
    
    # Demonstrate retrying a dead letter message
    if dead_letters:
        print("\n=== Retrying Dead Letter Message ===")
        message_to_retry = dead_letters[0]
        success = dlq.retry_dead_letter_message(message_to_retry.id)
        print(f"Retry initiated for {message_to_retry.id}: {success}")
        print(f"Queue stats after retry: {dlq.get_queue_stats()}")
    
    print("\n=== Final Queue Statistics ===")
    final_stats = dlq.get_queue_stats()
    for queue_name, count in final_stats.items():
        print(f"{queue_name.capitalize()}: {count}")


if __name__ == "__main__":
    main()