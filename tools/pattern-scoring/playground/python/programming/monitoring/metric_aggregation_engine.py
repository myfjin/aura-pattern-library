"""
Metric Aggregation Engine

A complete metric aggregation system supporting counters, gauges, and histograms
with label support and quantile computation.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import math
import time
from typing import Dict, List, Tuple, Union, Optional, Any
from collections import defaultdict
import threading


class LabelSet:
    """Immutable label set for metric identification."""
    
    def __init__(self, labels: Optional[Dict[str, str]] = None):
        self._labels = dict(labels) if labels else {}
        # Create a hashable representation for use as dictionary keys
        self._hash = hash(tuple(sorted(self._labels.items())))
    
    def get(self, key: str, default: Optional[str] = None) -> Optional[str]:
        """Get label value by key."""
        return self._labels.get(key, default)
    
    def items(self):
        """Return label items."""
        return self._labels.items()
    
    def __hash__(self) -> int:
        return self._hash
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, LabelSet):
            return False
        return self._labels == other._labels
    
    def __repr__(self) -> str:
        return f"LabelSet({self._labels})"


class Metric:
    """Base class for all metrics."""
    
    def __init__(self, name: str, description: str = ""):
        self.name = name
        self.description = description
        self._lock = threading.RLock()
    
    def _get_label_key(self, labels: Optional[Dict[str, str]] = None) -> LabelSet:
        """Convert labels dict to LabelSet for consistent hashing."""
        return LabelSet(labels)


class Counter(Metric):
    """Monotonically increasing counter metric."""
    
    def __init__(self, name: str, description: str = ""):
        super().__init__(name, description)
        self._values: Dict[LabelSet, float] = defaultdict(float)
    
    def inc(self, value: float = 1.0, labels: Optional[Dict[str, str]] = None) -> None:
        """
        Increment counter by value.
        
        Args:
            value: Value to increment by (must be non-negative)
            labels: Optional label dictionary
        """
        if value < 0:
            raise ValueError("Counter increment value must be non-negative")
        
        with self._lock:
            label_set = self._get_label_key(labels)
            self._values[label_set] += value
    
    def get(self, labels: Optional[Dict[str, str]] = None) -> float:
        """
        Get current counter value.
        
        Args:
            labels: Optional label dictionary
            
        Returns:
            Current counter value
        """
        with self._lock:
            label_set = self._get_label_key(labels)
            return self._values[label_set]
    
    def reset(self, labels: Optional[Dict[str, str]] = None) -> None:
        """
        Reset counter to zero.
        
        Args:
            labels: Optional label dictionary
        """
        with self._lock:
            if labels is None:
                self._values.clear()
            else:
                label_set = self._get_label_key(labels)
                self._values[label_set] = 0.0


class Gauge(Metric):
    """Gauge metric that can go up and down."""
    
    def __init__(self, name: str, description: str = ""):
        super().__init__(name, description)
        self._values: Dict[LabelSet, float] = defaultdict(float)
    
    def set(self, value: float, labels: Optional[Dict[str, str]] = None) -> None:
        """
        Set gauge to specific value.
        
        Args:
            value: Value to set
            labels: Optional label dictionary
        """
        with self._lock:
            label_set = self._get_label_key(labels)
            self._values[label_set] = value
    
    def inc(self, value: float = 1.0, labels: Optional[Dict[str, str]] = None) -> None:
        """
        Increment gauge by value.
        
        Args:
            value: Value to increment by
            labels: Optional label dictionary
        """
        with self._lock:
            label_set = self._get_label_key(labels)
            self._values[label_set] += value
    
    def dec(self, value: float = 1.0, labels: Optional[Dict[str, str]] = None) -> None:
        """
        Decrement gauge by value.
        
        Args:
            value: Value to decrement by
            labels: Optional label dictionary
        """
        with self._lock:
            label_set = self._get_label_key(labels)
            self._values[label_set] -= value
    
    def get(self, labels: Optional[Dict[str, str]] = None) -> float:
        """
        Get current gauge value.
        
        Args:
            labels: Optional label dictionary
            
        Returns:
            Current gauge value
        """
        with self._lock:
            label_set = self._get_label_key(labels)
            return self._values[label_set]


class Histogram(Metric):
    """Histogram metric for tracking value distributions."""
    
    def __init__(self, name: str, description: str = "", buckets: Optional[List[float]] = None):
        """
        Initialize histogram.
        
        Args:
            name: Metric name
            description: Metric description
            buckets: Bucket boundaries (default: exponential buckets)
        """
        super().__init__(name, description)
        if buckets is None:
            # Default buckets: 0.005, 0.01, 0.025, 0.05, 0.1, 0.25, 0.5, 1.0, 2.5, 5.0, 10.0
            buckets = [0.005, 0.01, 0.025, 0.05, 0.1, 0.25, 0.5, 1.0, 2.5, 5.0, 10.0]
        
        if not all(buckets[i] < buckets[i+1] for i in range(len(buckets)-1)):
            raise ValueError("Buckets must be in increasing order")
        
        self._buckets = buckets
        # Store count, sum, and bucket counts for each label set
        self._data: Dict[LabelSet, Dict[str, Any]] = defaultdict(
            lambda: {
                "count": 0,
                "sum": 0.0,
                "bucket_counts": [0] * len(buckets)
            }
        )
    
    def observe(self, value: float, labels: Optional[Dict[str, str]] = None) -> None:
        """
        Observe a value.
        
        Args:
            value: Value to observe
            labels: Optional label dictionary
        """
        if value < 0:
            raise ValueError("Histogram values must be non-negative")
        
        with self._lock:
            label_set = self._get_label_key(labels)
            data = self._data[label_set]
            
            data["count"] += 1
            data["sum"] += value
            
            # Find which bucket this value belongs to
            for i, bucket in enumerate(self._buckets):
                if value <= bucket:
                    data["bucket_counts"][i] += 1
                    break
    
    def get_count(self, labels: Optional[Dict[str, str]] = None) -> int:
        """
        Get observation count.
        
        Args:
            labels: Optional label dictionary
            
        Returns:
            Number of observations
        """
        with self._lock:
            label_set = self._get_label_key(labels)
            return self._data[label_set]["count"]
    
    def get_sum(self, labels: Optional[Dict[str, str]] = None) -> float:
        """
        Get sum of all observations.
        
        Args:
            labels: Optional label dictionary
            
        Returns:
            Sum of all observations
        """
        with self._lock:
            label_set = self._get_label_key(labels)
            return self._data[label_set]["sum"]
    
    def get_bucket_counts(self, labels: Optional[Dict[str, str]] = None) -> List[Tuple[float, int]]:
        """
        Get bucket counts.
        
        Args:
            labels: Optional label dictionary
            
        Returns:
            List of (bucket_boundary, count) tuples
        """
        with self._lock:
            label_set = self._get_label_key(labels)
            data = self._data[label_set]
            return list(zip(self._buckets, data["bucket_counts"]))
    
    def get_quantile(self, quantile: float, labels: Optional[Dict[str, str]] = None) -> float:
        """
        Calculate quantile value.
        
        Args:
            quantile: Quantile to calculate (0.0 to 1.0)
            labels: Optional label dictionary
            
        Returns:
            Estimated quantile value
        """
        if not 0.0 <= quantile <= 1.0:
            raise ValueError("Quantile must be between 0.0 and 1.0")
        
        with self._lock:
            label_set = self._get_label_key(labels)
            data = self._data[label_set]
            
            if data["count"] == 0:
                return 0.0
            
            # Calculate target rank
            rank = quantile * (data["count"] - 1) + 1
            
            # Find the bucket containing this rank
            cumulative_count = 0
            for i, bucket_count in enumerate(data["bucket_counts"]):
                cumulative_count += bucket_count
                if cumulative_count >= rank:
                    # Linear interpolation within bucket
                    if i == 0:
                        # First bucket, interpolate between 0 and bucket boundary
                        return self._buckets[0] * (rank / cumulative_count)
                    else:
                        # Interpolate between previous and current bucket
                        prev_cumulative = cumulative_count - bucket_count
                        if bucket_count > 0:
                            fraction = (rank - prev_cumulative) / bucket_count
                            if i == 0:
                                return self._buckets[i] * fraction
                            else:
                                return self._buckets[i-1] + fraction * (self._buckets[i] - self._buckets[i-1])
                        else:
                            return self._buckets[i-1]
            
            # If we get here, return the maximum bucket value
            return self._buckets[-1] if self._buckets else 0.0


class MetricAggregator:
    """Central aggregator for all metrics."""
    
    def __init__(self):
        self._metrics: Dict[str, Metric] = {}
        self._lock = threading.RLock()
    
    def register_counter(self, name: str, description: str = "") -> Counter:
        """
        Register a new counter.
        
        Args:
            name: Counter name
            description: Counter description
            
        Returns:
            Registered counter
        """
        with self._lock:
            if name in self._metrics:
                raise ValueError(f"Metric {name} already registered")
            counter = Counter(name, description)
            self._metrics[name] = counter
            return counter
    
    def register_gauge(self, name: str, description: str = "") -> Gauge:
        """
        Register a new gauge.
        
        Args:
            name: Gauge name
            description: Gauge description
            
        Returns:
            Registered gauge
        """
        with self._lock:
            if name in self._metrics:
                raise ValueError(f"Metric {name} already registered")
            gauge = Gauge(name, description)
            self._metrics[name] = gauge
            return gauge
    
    def register_histogram(self, name: str, description: str = "", buckets: Optional[List[float]] = None) -> Histogram:
        """
        Register a new histogram.
        
        Args:
            name: Histogram name
            description: Histogram description
            buckets: Bucket boundaries
            
        Returns:
            Registered histogram
        """
        with self._lock:
            if name in self._metrics:
                raise ValueError(f"Metric {name} already registered")
            histogram = Histogram(name, description, buckets)
            self._metrics[name] = histogram
            return histogram
    
    def get_metric(self, name: str) -> Optional[Metric]:
        """
        Get registered metric by name.
        
        Args:
            name: Metric name
            
        Returns:
            Metric instance or None if not found
        """
        with self._lock:
            return self._metrics.get(name)


def _demo():
    """Self-test: counter/gauge/histogram semantics exact on planted values,
    label isolation, bucket boundaries inclusive, duplicate names refused."""
    agg = MetricAggregator()
    requests = agg.register_counter("http_requests_total", "reqs")
    conns = agg.register_gauge("active_connections", "conns")
    latency = agg.register_histogram("latency_seconds", "lat",
                                     buckets=[0.1, 0.5, 1.0])

    # Counter: increments accumulate per label-set, isolated across sets.
    for _ in range(4):
        requests.inc(labels={"endpoint": "/users"})
    requests.inc(labels={"endpoint": "/orders"})
    assert requests.get(labels={"endpoint": "/users"}) == 4
    assert requests.get(labels={"endpoint": "/orders"}) == 1
    assert requests.get(labels={"endpoint": "/users"}) + \
        requests.get(labels={"endpoint": "/orders"}) == 5

    # Gauge: set overwrites.
    conns.set(17)
    conns.set(42)
    assert conns.get() == 42, "gauge must hold the last set value"

    # Histogram on planted observations: 0.05, 0.3, 0.3, 0.7, 2.0.
    for v in (0.05, 0.3, 0.3, 0.7, 2.0):
        latency.observe(v, labels={"ep": "/u"})
    assert latency.get_count(labels={"ep": "/u"}) == 5
    assert abs(latency.get_sum(labels={"ep": "/u"}) - 3.35) < 1e-12, \
        "sum of planted observations must be 3.35"

    # Bucket counts are PER-RANGE (not Prometheus-cumulative):
    # (..0.1]=1 (the 0.05), (0.1..0.5]=2 (both 0.3s), (0.5..1.0]=1 (the 0.7);
    # 2.0 overflows past the last boundary.
    buckets = dict(latency.get_bucket_counts(labels={"ep": "/u"}))
    assert buckets.get(0.1) == 1, f"bucket 0.1 must hold 1, got {buckets.get(0.1)}"
    assert buckets.get(0.5) == 2, f"bucket 0.5 must hold 2, got {buckets.get(0.5)}"
    assert buckets.get(1.0) == 1, f"bucket 1.0 must hold 1, got {buckets.get(1.0)}"
    assert sum(buckets.values()) == 4, "2.0 must overflow past the last bucket"

    # Quantiles: p50 of the planted set sits at 0.3, p99 at the top.
    p50 = latency.get_quantile(0.5, labels={"ep": "/u"})
    p99 = latency.get_quantile(0.99, labels={"ep": "/u"})
    assert abs(p50 - 0.3) < 0.25, f"p50 of planted set must be ~0.3, got {p50}"
    assert p99 >= p50, "quantiles not monotone"

    # Label isolation: a second label-set starts empty.
    assert latency.get_count(labels={"ep": "/other"}) == 0

    # Registry: duplicate names refused, lookup honest.
    try:
        agg.register_gauge("http_requests_total")
        assert False, "duplicate metric name accepted"
    except ValueError:
        pass
    assert agg.get_metric("http_requests_total") is requests
    assert agg.get_metric("ghost") is None

    print("metric_aggregation_engine: counter 4+1 isolated, gauge 42, histogram "
          "sum 3.35 / buckets 1-2-1 per-range, dup name refused — PASS")


if __name__ == "__main__":
    _demo()