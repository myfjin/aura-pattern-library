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
    # Self-test: counters accumulate per tag-set, gauges overwrite,
    # histogram stats/percentiles exact on planted values, refusals hold.
    agg = MetricAggregator()

    # Counters: same name+tags accumulate; different tags are separate series.
    agg.increment_counter("requests", 1)
    agg.increment_counter("requests", 3)
    agg.increment_counter("errors", 1, {"type": "timeout"})
    agg.increment_counter("errors", 2, {"type": "timeout"})
    agg.increment_counter("errors", 1, {"type": "validation"})
    assert agg.get_counter("requests") == 4, "1+3 must be 4"
    assert agg.get_counter("errors", {"type": "timeout"}) == 3, "1+2 must be 3"
    assert agg.get_counter("errors", {"type": "validation"}) == 1
    assert agg.get_counter("requests") + agg.get_counter("errors", {"type": "timeout"}) == 7

    # Gauges overwrite, never accumulate.
    agg.set_gauge("cpu", 45.2)
    agg.set_gauge("cpu", 67.8)
    assert agg.get_gauge("cpu") == 67.8, "gauge must overwrite"

    # Histogram on 0,5,...,95 (20 values): stats are closed-form.
    for i in range(20):
        agg.record_histogram("rt", i * 5, {"ep": "/users"})
    stats = agg.get_histogram_stats("rt", {"ep": "/users"})
    assert stats["count"] == 20
    assert stats["sum"] == 950, "sum of 0+5+...+95 must be 950"
    assert stats["min"] == 0 and stats["max"] == 95
    assert stats["avg"] == 47.5

    # Tagged series are isolated: a second endpoint has its own histogram.
    for i in range(10):
        agg.record_histogram("rt", i * 10, {"ep": "/orders"})
    assert agg.get_histogram_stats("rt", {"ep": "/orders"})["count"] == 10
    assert agg.get_histogram_stats("rt", {"ep": "/users"})["count"] == 20, \
        "second tag-set polluted the first histogram"

    # Percentiles are order statistics of the planted sequence: monotone,
    # p50 in the middle of 0..95, p99 at the top.
    p50 = agg.get_histogram_percentile("rt", 50, {"ep": "/users"})
    p90 = agg.get_histogram_percentile("rt", 90, {"ep": "/users"})
    p99 = agg.get_histogram_percentile("rt", 99, {"ep": "/users"})
    assert 45 <= p50 <= 50, f"p50 of 0..95 step 5 must be ~47.5, got {p50}"
    assert p50 <= p90 <= p99 <= 95, f"percentiles not monotone: {p50}/{p90}/{p99}"
    assert p99 >= 90, f"p99 of 0..95 must be at the top, got {p99}"

    # Snapshot carries the same numbers.
    snap = agg.snapshot()
    assert snap["counters"]['requests[{}]'] == 4
    users_key = next(k for k in snap["histograms"] if "/users" in k)
    assert snap["histograms"][users_key]["stats"]["sum"] == 950

    # Refusals: negative counter increment, unknown gauge, bad percentile.
    for call, exc in ((lambda: agg.increment_counter("t", -1), ValueError),
                      (lambda: agg.get_gauge("ghost"), KeyError),
                      (lambda: agg.get_histogram_percentile("rt", 150), ValueError)):
        try:
            call()
            assert False, "invalid call accepted"
        except exc:
            pass

    print("metric_aggregator: counters 4/3/1 per tag-set, gauge overwrites, "
          "histogram sum 950/avg 47.5, percentiles monotone, refusals held — PASS")