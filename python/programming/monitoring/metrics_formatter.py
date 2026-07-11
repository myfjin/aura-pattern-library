#!/usr/bin/env python3
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import re
from typing import Dict, List, Optional, Union
from dataclasses import dataclass
from enum import Enum


class MetricType(Enum):
    COUNTER = "counter"
    GAUGE = "gauge"
    HISTOGRAM = "histogram"
    SUMMARY = "summary"
    UNTYPED = "untyped"


@dataclass
class Label:
    """Represents a metric label with key-value pair."""
    key: str
    value: str

    def __post_init__(self) -> None:
        if not self.key:
            raise ValueError("Label key cannot be empty")
        if not re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', self.key):
            raise ValueError(f"Invalid label key format: {self.key}")

    def __str__(self) -> str:
        return f'{self.key}="{self.escape_value(self.value)}"'

    @staticmethod
    def escape_value(value: str) -> str:
        """Escape special characters in label values."""
        return value.replace('\\', '\\\\').replace('"', '\\"').replace('\n', '\\n')


@dataclass
class Metric:
    """Represents a single metric with name, value, type, labels and help text."""
    name: str
    value: Union[int, float]
    metric_type: MetricType
    labels: Optional[List[Label]] = None
    help_text: Optional[str] = None
    timestamp: Optional[int] = None

    def __post_init__(self) -> None:
        if not self.name:
            raise ValueError("Metric name cannot be empty")
        if not re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', self.name):
            raise ValueError(f"Invalid metric name format: {self.name}")
        if self.labels is None:
            self.labels = []
        if self.help_text is None:
            self.help_text = ""

    def format_labels(self) -> str:
        """Format labels as a string for metric line."""
        if not self.labels:
            return ""
        labels_str = ",".join(str(label) for label in self.labels)
        return f"{{{labels_str}}}"

    def to_prometheus_format(self) -> str:
        """Convert metric to Prometheus text format."""
        labels_part = self.format_labels()
        timestamp_part = f" {self.timestamp}" if self.timestamp else ""
        return f"{self.name}{labels_part} {self.value}{timestamp_part}"


class MetricsFormatter:
    """Formats metrics according to Prometheus/OpenMetrics text format."""

    def __init__(self) -> None:
        self.metrics: List[Metric] = []

    def add_metric(self, metric: Metric) -> None:
        """Add a metric to the formatter."""
        self.metrics.append(metric)

    def clear_metrics(self) -> None:
        """Clear all metrics."""
        self.metrics.clear()

    def format_metrics(self) -> str:
        """Format all metrics in Prometheus/OpenMetrics text format."""
        if not self.metrics:
            return "# No metrics available\n"

        # Group metrics by name
        metrics_by_name: Dict[str, List[Metric]] = {}
        for metric in self.metrics:
            if metric.name not in metrics_by_name:
                metrics_by_name[metric.name] = []
            metrics_by_name[metric.name].append(metric)

        output_lines: List[str] = []

        # Process each metric group
        for name, metrics_group in metrics_by_name.items():
            if not metrics_group:
                continue

            # Add help text if available (from first metric with help text)
            help_text = next((m.help_text for m in metrics_group if m.help_text), "")
            if help_text:
                output_lines.append(f"# HELP {name} {help_text}")

            # Add type information (from first metric)
            metric_type = metrics_group[0].metric_type.value
            output_lines.append(f"# TYPE {name} {metric_type}")

            # Add metric values
            for metric in metrics_group:
                output_lines.append(metric.to_prometheus_format())

        return "\n".join(output_lines) + "\n"


def main() -> None:
    """Self-test: exact Prometheus exposition lines, HELP/TYPE grouping,
    label escaping (the injection trap), name/key validation refused."""
    formatter = MetricsFormatter()
    formatter.add_metric(Metric(
        name="http_requests_total", value=42, metric_type=MetricType.COUNTER,
        help_text="Total number of HTTP requests",
        labels=[Label("method", "GET"), Label("endpoint", "/api/users")]))
    formatter.add_metric(Metric(
        name="http_requests_total", value=17, metric_type=MetricType.COUNTER,
        labels=[Label("method", "POST"), Label("endpoint", "/api/users")]))
    formatter.add_metric(Metric(
        name="cpu_usage_percent", value=75.5, metric_type=MetricType.GAUGE,
        help_text="Current CPU usage percentage",
        labels=[Label("instance", "server01")]))

    out = formatter.format_metrics()
    lines = out.strip().split("\n")

    # Exact exposition lines.
    assert 'http_requests_total{method="GET",endpoint="/api/users"} 42' in lines, \
        f"GET sample line wrong:\n{out}"
    assert 'http_requests_total{method="POST",endpoint="/api/users"} 17' in lines
    assert 'cpu_usage_percent{instance="server01"} 75.5' in lines

    # HELP/TYPE emitted once per metric family, HELP before TYPE before samples.
    assert lines.count("# TYPE http_requests_total counter") == 1, \
        "TYPE must appear exactly once per family"
    assert "# HELP http_requests_total Total number of HTTP requests" in lines
    h = lines.index("# HELP http_requests_total Total number of HTTP requests")
    t = lines.index("# TYPE http_requests_total counter")
    s = lines.index('http_requests_total{method="GET",endpoint="/api/users"} 42')
    assert h < t < s, "HELP/TYPE/sample ordering broken"
    assert s == 2, f"first sample must be line 2 (after HELP, TYPE), got {s}"

    # THE INJECTION TRAP: quotes, backslashes and newlines in label values
    # must be escaped, or one hostile label corrupts the whole exposition.
    esc = MetricsFormatter()
    esc.add_metric(Metric(name="t", value=1, metric_type=MetricType.GAUGE,
                          labels=[Label("loc", 'rack"1'), Label("path", "a\\b"),
                                  Label("note", "line1\nline2")]))
    esc_out = esc.format_metrics()
    assert '\\"' in esc_out, "quote not escaped in label value"
    assert "\\\\" in esc_out, "backslash not escaped"
    assert "\\n" in esc_out and "\nline2" not in esc_out, \
        "raw newline leaked into the exposition format"
    assert len([l for l in esc_out.strip().split("\n") if not l.startswith("#")]) == 1, \
        "escaped metric must still be exactly one sample line"

    # Timestamps append after the value.
    ts = Metric(name="ts_metric", value=5, metric_type=MetricType.COUNTER,
                timestamp=1700000000)
    assert ts.to_prometheus_format() == "ts_metric 5 1700000000"

    # Validation: bad names/keys refused at construction.
    for bad in (lambda: Metric(name="9leading", value=1, metric_type=MetricType.GAUGE),
                lambda: Metric(name="", value=1, metric_type=MetricType.GAUGE),
                lambda: Label("bad-key", "v"), lambda: Label("", "v")):
        try:
            bad()
            assert False, "invalid metric/label name accepted"
        except ValueError:
            pass

    # Empty formatter states its emptiness rather than emitting garbage.
    formatter.clear_metrics()
    assert formatter.format_metrics() == "# No metrics available\n"

    print("metrics_formatter: exposition lines exact (42/17/75.5), HELP<TYPE<sample, "
          "quote/backslash/newline escaped, bad names refused — PASS")


if __name__ == "__main__":
    main()