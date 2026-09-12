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
    """Self-test: window eviction exact, z-scores on a PLANTED baseline,
    the anomaly is caught and the normal point is not."""
    # WindowSampler: fixed capacity, oldest evicted first.
    sampler = WindowSampler(5)
    for i in range(7):
        sampler.add(i)
    assert sampler.get_values() == [2, 3, 4, 5, 6], \
        f"window must keep the newest 5: {sampler.get_values()}"
    assert sampler.is_full() and sampler.size() == 5
    assert sum(sampler.get_values()) == 20, "2+3+4+5+6 must be 20"

    # AnomalyDetector with baseline == full window (factor 1.0). The z-score
    # is computed against a baseline INCLUDING the new value, so a single
    # outlier v after 9 zeros gives exactly z = (v - v/10)/(3v/10) = 3.0.
    det = AnomalyDetector(window_size=10, z_threshold=2.5,
                          baseline_window_factor=1.0)
    for _ in range(9):
        det.add_value(0.0)
    is_anom, z = det.add_value(100.0)
    assert z == 3.0, f"single outlier in a 10-window flat baseline must be z=3, got {z}"
    assert is_anom, "a 3-sigma value was not flagged at threshold 2.5"
    mean, std = det.get_baseline_stats()
    assert mean == 10.0, f"baseline mean must be 100/10 = 10, got {mean}"
    assert std == 30.0, f"baseline pstdev must be 30, got {std}"

    # A value AT the flat baseline is exactly z=0 and not flagged.
    det2 = AnomalyDetector(window_size=10, z_threshold=2.5,
                           baseline_window_factor=1.0)
    for _ in range(9):
        det2.add_value(0.0)
    is_anom, z = det2.add_value(0.0)
    assert not is_anom and z == 0.0, f"flat continuation must be z=0, got {z}"

    # Zero-variance branch: via add_value the new value always joins the
    # baseline (flat + different is impossible), so probe the scorer directly.
    flat = AnomalyDetector(window_size=4, z_threshold=2.0,
                           baseline_window_factor=1.0)
    for _ in range(4):
        flat.add_value(7.0)
    assert flat._calculate_z_score(99.0) == float("inf"), \
        "deviation above a flat baseline must score inf"
    assert flat._calculate_z_score(-99.0) == float("-inf")
    assert flat._calculate_z_score(7.0) == 0.0

    # Before the baseline window fills, no verdicts are issued.
    young = AnomalyDetector(window_size=10, z_threshold=2.0)
    is_anom, z = young.add_value(1000.0)
    assert not is_anom and z is None, "detector judged before the baseline was full"
    assert young.get_baseline_stats() == (None, None)

    # reset() returns to the young state.
    det2.reset()
    assert det2.get_baseline_stats() == (None, None)

    # Refusals.
    try:
        det.add_value("invalid")  # type: ignore[arg-type]
        assert False, "non-numeric value accepted"
    except TypeError:
        pass
    try:
        AnomalyDetector(window_size=-1)
        assert False, "negative window accepted"
    except ValueError:
        pass

    print("window_sampler: eviction exact (sum 20), outlier z=3.0 flagged, "
          "baseline mean 10/std 30, flat scorer ±inf, young detector abstains — PASS")


if __name__ == "__main__":
    main()