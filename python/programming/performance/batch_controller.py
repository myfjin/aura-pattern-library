"""
Adaptive Batch Size Controller

A module for dynamically adjusting batch sizes based on throughput metrics
to optimize processing performance.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import time
from typing import List, Optional, Tuple
from dataclasses import dataclass
from collections import deque


@dataclass
class Metrics:
    """Performance metrics for batch processing."""
    batch_size: int
    processing_time: float  # seconds
    items_processed: int
    timestamp: float

    @property
    def throughput(self) -> float:
        """Calculate throughput in items per second."""
        if self.processing_time <= 0:
            return 0.0
        return self.items_processed / self.processing_time


class BatchController:
    """
    Adaptive batch size controller that adjusts batch sizes based on throughput metrics.
    
    Implements a slow start algorithm similar to TCP congestion control to find
    optimal batch sizes while detecting and responding to performance degradation.
    """
    
    def __init__(
        self,
        initial_batch_size: int = 1,
        max_batch_size: int = 1000,
        min_batch_size: int = 1,
        slow_start_threshold: int = 32,
        congestion_window_multiplier: float = 2.0,
        decay_factor: float = 0.5,
        metrics_window_size: int = 10
    ):
        """
        Initialize the batch controller.
        
        Args:
            initial_batch_size: Starting batch size
            max_batch_size: Maximum allowed batch size
            min_batch_size: Minimum allowed batch size
            slow_start_threshold: Threshold to switch from slow start to congestion avoidance
            congestion_window_multiplier: Multiplier for batch size increase during slow start
            decay_factor: Factor to reduce batch size when congestion is detected
            metrics_window_size: Number of recent metrics to consider for throughput analysis
        """
        if initial_batch_size < 1:
            raise ValueError("Initial batch size must be positive")
        if max_batch_size < initial_batch_size:
            raise ValueError("Max batch size must be >= initial batch size")
        if min_batch_size < 1:
            raise ValueError("Min batch size must be positive")
        if slow_start_threshold < 1:
            raise ValueError("Slow start threshold must be positive")
        if congestion_window_multiplier <= 1.0:
            raise ValueError("Congestion window multiplier must be > 1.0")
        if not 0 < decay_factor < 1:
            raise ValueError("Decay factor must be between 0 and 1")
        if metrics_window_size < 1:
            raise ValueError("Metrics window size must be positive")
            
        self.initial_batch_size = initial_batch_size
        self.max_batch_size = max_batch_size
        self.min_batch_size = min_batch_size
        self.slow_start_threshold = slow_start_threshold
        self.congestion_window_multiplier = congestion_window_multiplier
        self.decay_factor = decay_factor
        self.metrics_window_size = metrics_window_size
        
        # State variables
        self.current_batch_size = initial_batch_size
        self.in_slow_start = True
        self.previous_throughput = 0.0
        self.metrics_history: deque[Metrics] = deque(maxlen=metrics_window_size)
        
    def record_metrics(self, metrics: Metrics) -> None:
        """
        Record processing metrics for throughput analysis.
        
        Args:
            metrics: Metrics from a completed batch processing operation
        """
        if metrics.batch_size <= 0:
            raise ValueError("Batch size must be positive")
        if metrics.processing_time < 0:
            raise ValueError("Processing time cannot be negative")
        if metrics.items_processed < 0:
            raise ValueError("Items processed cannot be negative")
            
        self.metrics_history.append(metrics)
        
    def _calculate_average_throughput(self) -> float:
        """Calculate average throughput from recent metrics."""
        if not self.metrics_history:
            return 0.0
        return sum(m.throughput for m in self.metrics_history) / len(self.metrics_history)
        
    def _detect_congestion(self) -> bool:
        """
        Detect if system performance is degrading.
        
        Returns:
            True if congestion is detected, False otherwise
        """
        if len(self.metrics_history) < 2:
            return False
            
        # Compare recent throughput with historical average
        recent_metrics = list(self.metrics_history)[-2:]
        recent_avg = sum(m.throughput for m in recent_metrics) / len(recent_metrics)
        historical_avg = self._calculate_average_throughput()
        
        # Congestion if recent throughput is significantly worse than historical
        if historical_avg > 0 and recent_avg < 0.8 * historical_avg:
            return True
            
        # Also check if the most recent batch was much slower than previous
        if len(recent_metrics) == 2:
            prev_throughput = recent_metrics[0].throughput
            current_throughput = recent_metrics[1].throughput
            if prev_throughput > 0 and current_throughput < 0.7 * prev_throughput:
                return True
                
        return False
        
    def adjust_batch_size(self) -> int:
        """
        Adjust the batch size based on performance metrics.
        
        Returns:
            The new recommended batch size
        """
        # If we don't have enough metrics, continue with current strategy
        if len(self.metrics_history) < 2:
            if self.in_slow_start:
                # Slow start: exponentially increase batch size
                new_size = min(
                    int(self.current_batch_size * self.congestion_window_multiplier),
                    self.max_batch_size
                )
                if new_size > self.slow_start_threshold:
                    self.in_slow_start = False
                self.current_batch_size = new_size
            return self.current_batch_size
            
        # Check for congestion
        if self._detect_congestion():
            # Congestion detected: reduce batch size
            self.current_batch_size = max(
                int(self.current_batch_size * self.decay_factor),
                self.min_batch_size
            )
            self.in_slow_start = False  # Exit slow start on congestion
            return self.current_batch_size
            
        # No congestion, adjust based on phase
        if self.in_slow_start:
            # Slow start: exponentially increase
            new_size = min(
                int(self.current_batch_size * self.congestion_window_multiplier),
                self.max_batch_size
            )
            if new_size > self.slow_start_threshold:
                self.in_slow_start = False
            self.current_batch_size = new_size
        else:
            # Congestion avoidance: linearly increase
            self.current_batch_size = min(
                self.current_batch_size + 1,
                self.max_batch_size
            )
            
        return self.current_batch_size
        
    def reset(self) -> None:
        """Reset the controller to initial state."""
        self.current_batch_size = self.initial_batch_size
        self.in_slow_start = True
        self.previous_throughput = 0.0
        self.metrics_history.clear()


def simulate_processing(batch_size: int, baseline_time_per_item: float = 0.01) -> Metrics:
    """
    Simulate batch processing with some variability.
    
    Args:
        batch_size: Number of items to process
        baseline_time_per_item: Base processing time per item in seconds
        
    Returns:
        Metrics for the processing operation
    """
    # Add some variability to simulate real-world conditions
    variability = 0.2 * (hash(str(time.time())) % 100) / 100 - 0.1  # -10% to +10%
    
    # Simulate degradation with larger batches
    degradation_factor = 1.0 + (batch_size / 1000.0) * 0.5
    
    processing_time = batch_size * baseline_time_per_item * (1 + variability) * degradation_factor
    timestamp = time.time()
    
    return Metrics(
        batch_size=batch_size,
        processing_time=processing_time,
        items_processed=batch_size,
        timestamp=timestamp
    )


def main():
    """Demo the adaptive batch controller."""
    print("Adaptive Batch Size Controller Demo")
    print("=" * 40)
    
    # Create controller
    controller = BatchController(
        initial_batch_size=1,
        max_batch_size=128,
        min_batch_size=1,
        slow_start_threshold=16,
        congestion_window_multiplier=2.0,
        decay_factor=0.5,
        metrics_window_size=5
    )
    
    # Simulate processing batches
    for i in range(50):
        batch_size = controller.current_batch_size
        print(f"Iteration {i+1:2d}: Batch size = {batch_size:3d}", end="")
        
        # Simulate processing
        metrics = simulate_processing(batch_size)
        controller.record_metrics(metrics)
        
        throughput = metrics.throughput
        print(f" | Throughput = {throughput:6.1f} items/sec", end="")
        
        # Adjust batch size
        new_batch_size = controller.adjust_batch_size()
        
        if new_batch_size != batch_size:
            print(f" | Adjusted to {new_batch_size}")
        else:
            print()
            
        # Add some random variation to make it interesting
        if i % 7 == 0:
            time.sleep(0.001)  # Small delay to simulate system load
    
    print("\nFinal state:")
    print(f"Batch size: {controller.current_batch_size}")
    print(f"In slow start: {controller.in_slow_start}")
    print(f"Metrics recorded: {len(controller.metrics_history)}")


if __name__ == "__main__":
    main()