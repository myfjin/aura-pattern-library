#!/usr/bin/env python3
"""
Anomaly Detection Sampler Module

This module provides classes for detecting anomalies in time-series data using
statistical methods with adaptive baselines and windowed sampling.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import math
from typing import List, Optional, Tuple, Union
from collections import deque
import statistics


class WindowSampler:
    """
    A sliding window sampler that maintains a fixed-size buffer of recent values.
    
    This class efficiently manages a rolling window of data points, automatically
    removing old values as new ones are added.
    """
    
    def __init__(self, window_size: int) -> None:
        """
        Initialize the WindowSampler.
        
        Args:
            window_size: The maximum number of values to keep in the window
            
        Raises:
            ValueError: If window_size is not a positive integer
        """
        if not isinstance(window_size, int) or window_size <= 0:
            raise ValueError("Window size must be a positive integer")
        
        self.window_size = window_size
        self._values = deque(maxlen=window_size)
    
    def add(self, value: Union[int, float]) -> None:
        """
        Add a new value to the window.
        
        Args:
            value: The numeric value to add
            
        Raises:
            TypeError: If value is not numeric
        """
        if not isinstance(value, (int, float)) or math.isnan(value):
            raise TypeError("Value must be a numeric type")
        
        self._values.append(float(value))
    
    def get_values(self) -> List[float]:
        """
        Get all current values in the window.
        
        Returns:
            A list of all values currently in the window
        """
        return list(self._values)
    
    def is_full(self) -> bool:
        """
        Check if the window is at full capacity.
        
        Returns:
            True if the window has reached its maximum size, False otherwise
        """
        return len(self._values) == self.window_size
    
    def size(self) -> int:
        """
        Get the current number of values in the window.
        
        Returns:
            The number of values currently in the window
        """
        return len(self._values)
    
    def clear(self) -> None:
        """Clear all values from the window."""
        self._values.clear()


class AnomalyDetector:
    """
    Anomaly detector using z-score analysis with adaptive baseline.
    
    This detector uses statistical z-score analysis to identify anomalies
    while maintaining an adaptive baseline that adjusts to changes in the data.
    """
    
    def __init__(
        self, 
        window_size: int = 100, 
        z_threshold: float = 2.0,
        baseline_window_factor: float = 0.5
    ) -> None:
        """
        Initialize the AnomalyDetector.
        
        Args:
            window_size: Size of the sliding window for recent values
            z_threshold: Z-score threshold for anomaly detection
            baseline_window_factor: Factor for baseline window size (relative to main window)
            
        Raises:
            ValueError: If parameters are invalid
        """
        if window_size <= 0:
            raise ValueError("Window size must be positive")
        if z_threshold <= 0:
            raise ValueError("Z-score threshold must be positive")
        if not 0 < baseline_window_factor <= 1:
            raise ValueError("Baseline window factor must be between 0 and 1")
        
        self.window_size = window_size
        self.z_threshold = z_threshold
        self.baseline_window_factor = baseline_window_factor
        
        # Main window for recent values
        self._recent_values = WindowSampler(window_size)
        
        # Baseline window for computing statistics
        baseline_size = max(1, int(window_size * baseline_window_factor))
        self._baseline_values = WindowSampler(baseline_size)
        
        # Alert state tracking
        self._last_alert_time = -1
        self._alert_cooldown = window_size // 10  # Cooldown period
    
    def add_value(self, value: Union[int, float]) -> Tuple[bool, Optional[float]]:
        """
        Add a new value and check for anomalies.
        
        Args:
            value: The new value to analyze
            
        Returns:
            A tuple containing:
                - Boolean indicating if an anomaly was detected
                - Z-score of the value (None if baseline is insufficient)
                
        Raises:
            TypeError: If value is not numeric
        """
        if not isinstance(value, (int, float)) or math.isnan(value):
            raise TypeError("Value must be a numeric type")
        
        # Add to both windows
        self._recent_values.add(value)
        self._baseline_values.add(value)
        
        # Check for anomaly if we have enough data
        if self._baseline_values.is_full():
            z_score = self._calculate_z_score(value)
            if z_score is not None:
                is_anomaly = abs(z_score) > self.z_threshold
                if is_anomaly and self._can_trigger_alert():
                    self._last_alert_time = self._recent_values.size()
                    return True, z_score
                return is_anomaly, z_score
        
        return False, None
    
    def _calculate_z_score(self, value: float) -> Optional[float]:
        """
        Calculate the z-score for a value based on baseline statistics.
        
        Args:
            value: The value to calculate z-score for
            
        Returns:
            The z-score, or None if calculation is not possible
        """
        baseline_data = self._baseline_values.get_values()
        
        if len(baseline_data) < 2:
            return None
            
        try:
            mean = statistics.mean(baseline_data)
            # Use population standard deviation for consistency
            std_dev = statistics.pstdev(baseline_data, mean)
            
            if std_dev == 0:
                return 0.0 if value == mean else (float('inf') if value > mean else float('-inf'))
                
            return (value - mean) / std_dev
        except statistics.StatisticsError:
            return None
    
    def _can_trigger_alert(self) -> bool:
        """
        Check if an alert can be triggered based on cooldown period.
        
        Returns:
            True if an alert can be triggered, False otherwise
        """
        if self._last_alert_time < 0:
            return True
        return (self._recent_values.size() - self._last_alert_time) >= self._alert_cooldown
    
    def get_baseline_stats(self) -> Tuple[Optional[float], Optional[float]]:
        """
        Get current baseline statistics.
        
        Returns:
            A tuple of (mean, standard_deviation) or (None, None) if insufficient data
        """
        if not self._baseline_values.is_full():
            return None, None
            
        baseline_data = self._baseline_values.get_values()
        try:
            mean = statistics.mean(baseline_data)
            std_dev = statistics.pstdev(baseline_data, mean)
            return mean, std_dev
        except statistics.StatisticsError:
            return None, None
    
    def reset(self) -> None:
        """Reset the detector to its initial state."""
        self._recent_values.clear()
        self._baseline_values.clear()
        self._last_alert_time = -1


def main() -> None:
    """Demo of the anomaly detection sampler functionality."""
    print("Anomaly Detection Sampler Demo")
    print("=" * 40)
    
    # Create detector with default parameters
    detector = AnomalyDetector(window_size=50, z_threshold=2.0)
    
    # Generate normal data (mean=100, std=10)
    import random
    random.seed(42)
    
    print("Feeding normal data...")
    normal_count = 0
    anomaly_count = 0
    
    # Feed 100 normal values
    for i in range(100):
        value = random.gauss(100, 10)
        is_anomaly, z_score = detector.add_value(value)
        
        if is_anomaly:
            anomaly_count += 1
            print(f"  Anomaly detected at step {i}: value={value:.2f}, z-score={z_score:.2f}")
        else:
            normal_count += 1
    
    print(f"Normal data summary: {normal_count} normal points, {anomaly_count} anomalies")
    
    # Feed some obvious anomalies
    print("\nFeeding obvious anomalies...")
    anomalies = [150, 160, 50, 175, 30]
    
    for i, value in enumerate(anomalies):
        is_anomaly, z_score = detector.add_value(value)
        if is_anomaly:
            anomaly_count += 1
            print(f"  Anomaly detected: value={value}, z-score={z_score:.2f}")
        else:
            print(f"  Value {value} not flagged as anomaly (z-score={z_score:.2f})")
    
    # Show baseline statistics
    mean, std_dev = detector.get_baseline_stats()
    if mean is not None and std_dev is not None:
        print(f"\nCurrent baseline: mean={mean:.2f}, std_dev={std_dev:.2f}")
    
    # Demonstrate parameter validation
    print("\nTesting error handling...")
    try:
        detector.add_value("invalid")
    except TypeError as e:
        print(f"  Caught expected error: {e}")
    
    try:
        AnomalyDetector(window_size=-1)
    except ValueError as e:
        print(f"  Caught expected error: {e}")
    
    # Test window sampler directly
    print("\nTesting WindowSampler...")
    sampler = WindowSampler(5)
    for i in range(7):
        sampler.add(i)
        print(f"  After adding {i}: {sampler.get_values()}")
    
    print(f"  Window full: {sampler.is_full()}")
    print(f"  Current size: {sampler.size()}")


if __name__ == "__main__":
    main()