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
            aggregated = self.aggregate(current_start, current_end, agg_func)
            
            if aggregated is not None:
                # Use midpoint of interval as timestamp for downsampled point
                midpoint = (current_start + current_end) / 2
                result.append(Point(midpoint, aggregated))
                
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
    # Create a series collection
    series_collection = Series()
    
    # Generate sample data
    base_time = time.time()
    for i in range(100):
        # Insert into two different series
        series_collection.insert("temperature", 
                                Point(base_time + i, 20 + (i % 10)))
        series_collection.insert("humidity", 
                                Point(base_time + i, 50 + (i % 20)))
    
    # Query a range
    print("Querying temperature data from last 10 points:")
    temp_points = series_collection.query_range(
        "temperature", base_time + 90, base_time + 99)
    for point in temp_points:
        print(f"  {point.timestamp:.0f}: {point.value}")
    
    # Aggregate data
    print("\nAggregations over all temperature data:")
    total = series_collection.aggregate("temperature", base_time, base_time + 99, sum_func)
    average = series_collection.aggregate("temperature", base_time, base_time + 99, avg_func)
    maximum = series_collection.aggregate("temperature", base_time, base_time + 99, max_func)
    minimum = series_collection.aggregate("temperature", base_time, base_time + 99, min_func)
    
    print(f"  Sum: {total}")
    print(f"  Average: {average:.2f}")
    print(f"  Maximum: {maximum}")
    print(f"  Minimum: {minimum}")
    
    # Downsample data
    print("\nDownsampled temperature data (interval=10, avg):")
    downsampled = series_collection.downsample(
        "temperature", base_time, base_time + 99, 10, avg_func)
    for point in downsampled:
        print(f"  {point.timestamp:.0f}: {point.value:.2f}")
    
    # Show all series names
    print(f"\nAll series: {series_collection.get_series_names()}")
    
    # Test error handling
    try:
        series_collection.aggregate("temperature", 100, 50, avg_func)
    except ValueError as e:
        print(f"\nCaught expected error: {e}")