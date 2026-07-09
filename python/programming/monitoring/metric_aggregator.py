"""
Metric aggregator with tags for counters, gauges, and histograms.
Supports percentile calculations and tagged metrics.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import bisect
import collections
import json
import time
from typing import Any, Dict, List, Optional, Tuple, Union


class TaggedMetric:
    """Represents a metric with associated tags."""
    
    def __init__(self, name: str, tags: Optional[Dict[str, str]] = None):
        """
        Initialize a tagged metric.
        
        Args:
            name: The metric name
            tags: Optional dictionary of tags
        """
        self.name = name
        self.tags = tags or {}
        self._key = (name, tuple(sorted(self.tags.items())))
    
    def __hash__(self) -> int:
        return hash(self._key)
    
    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, TaggedMetric):
            return False
        return self._key == other._key
    
    def __repr__(self) -> str:
        tags_str = ",".join(f"{k}={v}" for k, v in self.tags.items())
        return f"TaggedMetric({self.name}[{tags_str}])"


class MetricAggregator:
    """Aggregates metrics with tags, supporting counters, gauges, and histograms."""
    
    def __init__(self):
        """Initialize the metric aggregator."""
        self._counters: Dict[TaggedMetric, float] = collections.defaultdict(float)
        self._gauges: Dict[TaggedMetric, float] = {}
        self._histograms: Dict[TaggedMetric, List[float]] = collections.defaultdict(list)
        self._histogram_counts: Dict[TaggedMetric, int] = collections.defaultdict(int)
        self._histogram_sums: Dict[TaggedMetric, float] = collections.defaultdict(float)
    
    def increment_counter(self, name: str, value: float = 1.0, tags: Optional[Dict[str, str]] = None) -> None:
        """
        Increment a counter metric.
        
        Args:
            name: Metric name
            value: Value to increment by (default: 1.0)
            tags: Optional tags dictionary
        """
        if value < 0:
            raise ValueError("Counter increment value must be non-negative")
        
        metric = TaggedMetric(name, tags)
        self._counters[metric] += value
    
    def set_gauge(self, name: str, value: float, tags: Optional[Dict[str, str]] = None) -> None:
        """
        Set a gauge metric value.
        
        Args:
            name: Metric name
            value: Gauge value
            tags: Optional tags dictionary
        """
        metric = TaggedMetric(name, tags)
        self._gauges[metric] = value
    
    def record_histogram(self, name: str, value: float, tags: Optional[Dict[str, str]] = None) -> None:
        """
        Record a value in a histogram.
        
        Args:
            name: Metric name
            value: Value to record
            tags: Optional tags dictionary
        """
        if value < 0:
            raise ValueError("Histogram values must be non-negative")
        
        metric = TaggedMetric(name, tags)
        bisect.insort(self._histograms[metric], value)
        self._histogram_counts[metric] += 1
        self._histogram_sums[metric] += value
    
    def get_counter(self, name: str, tags: Optional[Dict[str, str]] = None) -> float:
        """
        Get the current value of a counter.
        
        Args:
            name: Metric name
            tags: Optional tags dictionary
            
        Returns:
            Current counter value
        """
        metric = TaggedMetric(name, tags)
        return self._counters[metric]
    
    def get_gauge(self, name: str, tags: Optional[Dict[str, str]] = None) -> float:
        """
        Get the current value of a gauge.
        
        Args:
            name: Metric name
            tags: Optional tags dictionary
            
        Returns:
            Current gauge value
            
        Raises:
            KeyError: If gauge doesn't exist
        """
        metric = TaggedMetric(name, tags)
        return self._gauges[metric]
    
    def get_histogram_percentile(self, name: str, percentile: float, tags: Optional[Dict[str, str]] = None) -> float:
        """
        Calculate a percentile value for a histogram.
        
        Args:
            name: Metric name
            percentile: Percentile to calculate (0-100)
            tags: Optional tags dictionary
            
        Returns:
            Calculated percentile value
            
        Raises:
            ValueError: If percentile is not between 0 and 100
            KeyError: If histogram doesn't exist or is empty
        """
        if not 0 <= percentile <= 100:
            raise ValueError("Percentile must be between 0 and 100")
        
        metric = TaggedMetric(name, tags)
        values = self._histograms[metric]
        
        if not values:
            raise KeyError(f"Histogram {name} with tags {tags} is empty")
        
        # Calculate index for percentile
        index = (percentile / 100) * (len(values) - 1)
        
        # If exact index, return that value
        if index.is_integer():
            return values[int(index)]
        
        # Otherwise interpolate between adjacent values
        lower_index = int(index)
        upper_index = lower_index + 1
        weight = index - lower_index
        
        if upper_index >= len(values):
            return values[lower_index]
        
        return values[lower_index] * (1 - weight) + values[upper_index] * weight
    
    def get_histogram_stats(self, name: str, tags: Optional[Dict[str, str]] = None) -> Dict[str, Union[int, float]]:
        """
        Get statistics for a histogram.
        
        Args:
            name: Metric name
            tags: Optional tags dictionary
            
        Returns:
            Dictionary with count, sum, min, max, and avg
        """
        metric = TaggedMetric(name, tags)
        values = self._histograms[metric]
        
        if not values:
            return {
                "count": 0,
                "sum": 0.0,
                "min": 0.0,
                "max": 0.0,
                "avg": 0.0
            }
        
        return {
            "count": self._histogram_counts[metric],
            "sum": self._histogram_sums[metric],
            "min": min(values),
            "max": max(values),
            "avg": self._histogram_sums[metric] / self._histogram_counts[metric]
        }
    
    def snapshot(self) -> Dict[str, Any]:
        """
        Take a snapshot of all current metrics.
        
        Returns:
            Dictionary representation of all metrics
        """
        result = {
            "counters": {},
            "gauges": {},
            "histograms": {}
        }
        
        # Process counters
        for metric, value in self._counters.items():
            tag_str = json.dumps(metric.tags, sort_keys=True)
            result["counters"][f"{metric.name}[{tag_str}]"] = value
        
        # Process gauges
        for metric, value in self._gauges.items():
            tag_str = json.dumps(metric.tags, sort_keys=True)
            result["gauges"][f"{metric.name}[{tag_str}]"] = value
        
        # Process histograms
        for metric in self._histograms.keys():
            tag_str = json.dumps(metric.tags, sort_keys=True)
            result["histograms"][f"{metric.name}[{tag_str}]"] = {
                "stats": self.get_histogram_stats(metric.name, metric.tags),
                "percentiles": {
                    "50": self.get_histogram_percentile(metric.name, 50, metric.tags),
                    "90": self.get_histogram_percentile(metric.name, 90, metric.tags),
                    "95": self.get_histogram_percentile(metric.name, 95, metric.tags),
                    "99": self.get_histogram_percentile(metric.name, 99, metric.tags)
                }
            }
        
        return result


if __name__ == "__main__":
    # Create aggregator
    aggregator = MetricAggregator()
    
    # Test counters
    aggregator.increment_counter("requests", 1)
    aggregator.increment_counter("requests", 3)
    aggregator.increment_counter("errors", 1, {"type": "timeout"})
    aggregator.increment_counter("errors", 2, {"type": "timeout"})
    aggregator.increment_counter("errors", 1, {"type": "validation"})
    
    # Test gauges
    aggregator.set_gauge("memory_usage", 1024.5)
    aggregator.set_gauge("cpu_usage", 45.2)
    aggregator.set_gauge("cpu_usage", 67.8)  # Update value
    
    # Test histograms
    for i in range(20):
        aggregator.record_histogram("response_time", i * 5, {"endpoint": "/api/users"})
    
    for i in range(10):
        aggregator.record_histogram("response_time", i * 10, {"endpoint": "/api/orders"})
    
    # Print results
    print("=== Metrics Snapshot ===")
    snapshot = aggregator.snapshot()
    
    print("\nCounters:")
    for name, value in snapshot["counters"].items():
        print(f"  {name}: {value}")
    
    print("\nGauges:")
    for name, value in snapshot["gauges"].items():
        print(f"  {name}: {value}")
    
    print("\nHistograms:")
    for name, data in snapshot["histograms"].items():
        print(f"  {name}:")
        stats = data["stats"]
        percentiles = data["percentiles"]
        print(f"    Count: {stats['count']}, Sum: {stats['sum']:.2f}")
        print(f"    Min: {stats['min']:.2f}, Max: {stats['max']:.2f}, Avg: {stats['avg']:.2f}")
        print(f"    50%: {percentiles['50']:.2f}, 90%: {percentiles['90']:.2f}, "
              f"95%: {percentiles['95']:.2f}, 99%: {percentiles['99']:.2f}")
    
    # Test specific queries
    print("\n=== Specific Queries ===")
    print(f"Total requests: {aggregator.get_counter('requests')}")
    print(f"Timeout errors: {aggregator.get_counter('errors', {'type': 'timeout'})}")
    print(f"Current CPU usage: {aggregator.get_gauge('cpu_usage')}")
    print(f"Response time 95th percentile (/api/users): "
          f"{aggregator.get_histogram_percentile('response_time', 95, {'endpoint': '/api/users'})}")
    
    # Test error conditions
    print("\n=== Error Handling ===")
    try:
        aggregator.increment_counter("test", -1)
    except ValueError as e:
        print(f"Caught expected error: {e}")
    
    try:
        aggregator.get_gauge("nonexistent")
    except KeyError as e:
        print(f"Caught expected error: {e}")
    
    try:
        aggregator.get_histogram_percentile("response_time", 150)
    except ValueError as e:
        print(f"Caught expected error: {e}")