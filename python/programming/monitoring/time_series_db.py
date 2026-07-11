"""
In-memory time-series database module with support for insertion, querying,
aggregation, and downsampling.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

from typing import List, Optional, Tuple, Callable, Dict, Any
from dataclasses import dataclass
import bisect
from collections import defaultdict
import time


@dataclass
class Point:
    """A single data point with timestamp and value."""
    timestamp: float
    value: float

    def __post_init__(self) -> None:
        if self.timestamp < 0:
            raise ValueError("Timestamp cannot be negative")
        if not isinstance(self.value, (int, float)):
            raise TypeError("Value must be a number")


class TimeSeries:
    """A time-series data structure that maintains ordered points."""
    
    def __init__(self) -> None:
        self._points: List[Point] = []
        self._timestamps: List[float] = []
    
    def insert(self, point: Point) -> None:
        """Insert a point into the time series, maintaining order by timestamp."""
        # Find insertion point to keep timestamps sorted
        idx = bisect.bisect_left(self._timestamps, point.timestamp)
        
        # If timestamp already exists, replace the point
        if idx < len(self._timestamps) and self._timestamps[idx] == point.timestamp:
            self._points[idx] = point
        else:
            # Insert new point
            self._points.insert(idx, point)
            self._timestamps.insert(idx, point.timestamp)
    
    def query_range(self, start: float, end: float) -> List[Point]:
        """
        Query points within a time range [start, end].
        
        Args:
            start: Start timestamp (inclusive)
            end: End timestamp (inclusive)
            
        Returns:
            List of points within the specified range
        """
        if start > end:
            raise ValueError("Start time cannot be after end time")
            
        start_idx = bisect.bisect_left(self._timestamps, start)
        end_idx = bisect.bisect_right(self._timestamps, end)
        return self._points[start_idx:end_idx]
    
    def aggregate(self, start: float, end: float, 
                  func: Callable[[List[float]], float]) -> Optional[float]:
        """
        Apply an aggregation function to values in a time range.
        
        Args:
            start: Start timestamp (inclusive)
            end: End timestamp (inclusive)
            func: Aggregation function (e.g., sum, max, min, avg)
            
        Returns:
            Aggregated value or None if no points in range
        """
        points = self.query_range(start, end)
        if not points:
            return None
            
        values = [p.value for p in points]
        return func(values)
    
    def downsample(self, start: float, end: float, interval: float,
                   agg_func: Callable[[List[float]], float]) -> List[Point]:
        """
        Downsample data within a time range using specified aggregation.
        
        Args:
            start: Start timestamp (inclusive)
            end: End timestamp (inclusive)
            interval: Downsampling interval
            agg_func: Aggregation function for each interval
            
        Returns:
            List of downsampled points
        """
        if interval <= 0:
            raise ValueError("Interval must be positive")
        if start > end:
            raise ValueError("Start time cannot be after end time")
            
        result: List[Point] = []
        current_start = start

        while current_start < end:
            current_end = min(current_start + interval, end)
            # Interior buckets are HALF-OPEN [start, end): with the former
            # inclusive aggregate, the point at each boundary was counted
            # into two adjacent buckets. Only the final bucket includes end.
            points = self.query_range(current_start, current_end)
            if current_end < end:
                values = [p.value for p in points if p.timestamp < current_end]
            else:
                values = [p.value for p in points]

            if values:
                # Use midpoint of interval as timestamp for downsampled point
                midpoint = (current_start + current_end) / 2
                result.append(Point(midpoint, agg_func(values)))
                
            current_start = current_end
            
        return result
    
    def __len__(self) -> int:
        """Return the number of points in the time series."""
        return len(self._points)
    
    def __iter__(self):
        """Iterate over all points in timestamp order."""
        return iter(self._points)


class Series:
    """A collection of named time series."""
    
    def __init__(self) -> None:
        self._series: Dict[str, TimeSeries] = defaultdict(TimeSeries)
    
    def insert(self, name: str, point: Point) -> None:
        """
        Insert a point into a named time series.
        
        Args:
            name: Name of the time series
            point: Point to insert
        """
        self._series[name].insert(point)
    
    def query_range(self, name: str, start: float, end: float) -> List[Point]:
        """
        Query points from a named time series within a time range.
        
        Args:
            name: Name of the time series
            start: Start timestamp (inclusive)
            end: End timestamp (inclusive)
            
        Returns:
            List of points within the specified range
        """
        return self._series[name].query_range(start, end)
    
    def aggregate(self, name: str, start: float, end: float,
                  func: Callable[[List[float]], float]) -> Optional[float]:
        """
        Apply an aggregation function to a named time series.
        
        Args:
            name: Name of the time series
            start: Start timestamp (inclusive)
            end: End timestamp (inclusive)
            func: Aggregation function
            
        Returns:
            Aggregated value or None if no points in range
        """
        return self._series[name].aggregate(start, end, func)
    
    def downsample(self, name: str, start: float, end: float, interval: float,
                   agg_func: Callable[[List[float]], float]) -> List[Point]:
        """
        Downsample a named time series.
        
        Args:
            name: Name of the time series
            start: Start timestamp (inclusive)
            end: End timestamp (inclusive)
            interval: Downsampling interval
            agg_func: Aggregation function for each interval
            
        Returns:
            List of downsampled points
        """
        return self._series[name].downsample(start, end, interval, agg_func)
    
    def get_series_names(self) -> List[str]:
        """Get a list of all series names."""
        return list(self._series.keys())


def sum_func(values: List[float]) -> float:
    """Sum aggregation function."""
    return sum(values)


def avg_func(values: List[float]) -> float:
    """Average aggregation function."""
    return sum(values) / len(values)


def max_func(values: List[float]) -> float:
    """Maximum aggregation function."""
    return max(values)


def min_func(values: List[float]) -> float:
    """Minimum aggregation function."""
    return min(values)


if __name__ == "__main__":
    # Self-test on a FIXED time base: every aggregate is exact arithmetic.
    db = Series()
    base = 1000.0
    for i in range(100):
        db.insert("temperature", Point(base + i, 20 + (i % 10)))
        db.insert("humidity", Point(base + i, 50 + (i % 20)))

    # Range query [90..99]: exactly 10 points, values 20..29 in time order.
    pts = db.query_range("temperature", base + 90, base + 99)
    assert [p.value for p in pts] == [20, 21, 22, 23, 24, 25, 26, 27, 28, 29], \
        f"range values wrong: {[p.value for p in pts]}"
    assert [p.timestamp for p in pts] == [base + 90 + k for k in range(10)]

    # Aggregates over all 100 points: 10 full cycles of 20..29.
    assert db.aggregate("temperature", base, base + 99, sum_func) == 2450, \
        "sum of 10 cycles of 20..29 must be 2450"
    assert db.aggregate("temperature", base, base + 99, avg_func) == 24.5
    assert db.aggregate("temperature", base, base + 99, max_func) == 29
    assert db.aggregate("temperature", base, base + 99, min_func) == 20

    # Downsample into 10-second buckets: each bucket is one full cycle → avg 24.5.
    buckets = db.downsample("temperature", base, base + 99, 10, avg_func)
    assert len(buckets) == 10, f"100s at interval 10 must give 10 buckets, got {len(buckets)}"
    assert all(b.value == 24.5 for b in buckets), \
        f"every full-cycle bucket must average 24.5: {[b.value for b in buckets]}"
    # Downsample with sum: each bucket holds one cycle summing to 245.
    sum_buckets = db.downsample("temperature", base, base + 99, 10, sum_func)
    assert [b.value for b in sum_buckets] == [245] * 10

    # Series are independent.
    assert db.aggregate("humidity", base, base + 99, min_func) == 50
    assert sorted(db.get_series_names()) == ["humidity", "temperature"]

    # Out-of-order inserts still query in time order.
    db.insert("ooo", Point(base + 5, 3))
    db.insert("ooo", Point(base + 1, 1))
    db.insert("ooo", Point(base + 3, 2))
    assert [p.value for p in db.query_range("ooo", base, base + 10)] == [1, 2, 3], \
        "out-of-order inserts broke time ordering"

    # Empty range → no aggregate value, empty query.
    assert db.query_range("temperature", base + 500, base + 600) == []
    assert db.aggregate("temperature", base + 500, base + 600, avg_func) is None

    # Inverted range refused.
    try:
        db.aggregate("temperature", base + 100, base + 50, avg_func)
        assert False, "inverted range accepted"
    except ValueError:
        pass

    print("time_series_db: sum 2450 / avg 24.5 / max 29 / min 20 exact, "
          "10 buckets @245, out-of-order sorted, inverted range refused — PASS")