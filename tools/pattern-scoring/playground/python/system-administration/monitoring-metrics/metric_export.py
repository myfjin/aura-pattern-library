#!/usr/bin/env python3
"""metric_export: export metrics in standard formats."""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import sys
import json
import tempfile
from pathlib import Path

class MetricRegistry:
    """Registry of metrics for export."""
    def __init__(self):
        self.metrics = {}

    def register_counter(self, name, value):
        """Register counter metric."""
        self.metrics[name] = {"type": "counter", "value": value}

    def register_gauge(self, name, value):
        """Register gauge metric."""
        self.metrics[name] = {"type": "gauge", "value": value}

    def register_histogram(self, name, buckets):
        """Register histogram metric."""
        self.metrics[name] = {"type": "histogram", "buckets": buckets}

    def export_json(self):
        """Export metrics as JSON."""
        return json.dumps(self.metrics, indent=2)

    def export_prometheus_text(self):
        """Export metrics in Prometheus text format."""
        lines = []
        for name, metric in self.metrics.items():
            metric_type = metric.get("type", "untyped")
            if metric_type == "counter":
                lines.append(f"{name}_total {metric['value']}")
            elif metric_type == "gauge":
                lines.append(f"{name} {metric['value']}")
            elif metric_type == "histogram":
                buckets = metric.get("buckets", {})
                for bucket, count in buckets.items():
                    lines.append(f"{name}_bucket{{le=\"{bucket}\"}} {count}")
                lines.append(f"{name}_bucket{{le=\"+Inf\"}} {sum(buckets.values())}")
        return "\n".join(lines)

    def export_csv(self):
        """Export metrics as CSV."""
        lines = ["metric_name,type,value"]
        for name, metric in self.metrics.items():
            metric_type = metric.get("type", "untyped")
            value = metric.get("value", "")
            lines.append(f"{name},{metric_type},{value}")
        return "\n".join(lines)

def test_metric_export():
    """Test: register metrics, export to JSON/Prometheus/CSV, verify formats."""
    registry = MetricRegistry()

    # Register test metrics
    registry.register_counter("requests_total", 10000)
    registry.register_gauge("temperature_celsius", 25.5)
    registry.register_histogram("latency_ms", {
        "0.1": 50,
        "1.0": 200,
        "10.0": 500,
        "100.0": 950
    })

    # Test JSON export
    json_output = registry.export_json()
    assert isinstance(json_output, str), "JSON export should return string"

    parsed = json.loads(json_output)
    assert "requests_total" in parsed, "Should have requests_total"
    assert parsed["requests_total"]["type"] == "counter"
    assert parsed["requests_total"]["value"] == 10000

    assert "temperature_celsius" in parsed, "Should have temperature_celsius"
    assert parsed["temperature_celsius"]["type"] == "gauge"
    assert parsed["temperature_celsius"]["value"] == 25.5

    assert "latency_ms" in parsed, "Should have latency_ms"
    assert parsed["latency_ms"]["type"] == "histogram"

    # Test Prometheus text export
    prom_output = registry.export_prometheus_text()
    assert isinstance(prom_output, str), "Prometheus export should return string"

    assert "requests_total_total" in prom_output, "Counter should have _total suffix"
    assert "10000" in prom_output, "Should contain counter value"

    assert "temperature_celsius" in prom_output, "Should have gauge"
    assert "25.5" in prom_output, "Should contain gauge value"

    assert "latency_ms_bucket" in prom_output, "Should have histogram buckets"
    assert 'le="0.1"' in prom_output, "Should have bucket label"
    assert 'le="10.0"' in prom_output, "Should have multiple bucket labels"
    assert 'le="+Inf"' in prom_output, "Should have +Inf bucket"

    # Test CSV export
    csv_output = registry.export_csv()
    assert isinstance(csv_output, str), "CSV export should return string"

    csv_lines = csv_output.split("\n")
    assert len(csv_lines) >= 4, f"CSV should have header + 3 metrics, got {len(csv_lines)}"

    assert "metric_name,type,value" in csv_output, "CSV should have header"
    assert "requests_total,counter,10000" in csv_output, "CSV should have counter row"
    assert "temperature_celsius,gauge,25.5" in csv_output, "CSV should have gauge row"
    assert "latency_ms,histogram" in csv_output, "CSV should have histogram row"

    # Test write to file
    with tempfile.TemporaryDirectory() as tmpdir:
        json_path = Path(tmpdir) / "metrics.json"
        json_path.write_text(json_output)
        assert json_path.exists(), "JSON file should be created"

        parsed_from_file = json.loads(json_path.read_text())
        assert parsed_from_file["requests_total"]["value"] == 10000

        prom_path = Path(tmpdir) / "metrics.txt"
        prom_path.write_text(prom_output)
        assert prom_path.exists(), "Prometheus file should be created"

        content = prom_path.read_text()
        assert "requests_total_total" in content

        csv_path = Path(tmpdir) / "metrics.csv"
        csv_path.write_text(csv_output)
        assert csv_path.exists(), "CSV file should be created"

    # Test empty registry
    empty_registry = MetricRegistry()
    assert empty_registry.export_json() == "{}"
    assert empty_registry.export_prometheus_text() == ""
    csv_empty = empty_registry.export_csv()
    assert "metric_name,type,value" in csv_empty, "CSV header should be present"

    # Test metric update
    registry.register_counter("requests_total", 11000)  # Update value
    updated_json = json.loads(registry.export_json())
    assert updated_json["requests_total"]["value"] == 11000, "Metric should be updated"

    # Test special characters in metric names
    registry.register_gauge("cpu_usage_percent", 45.2)
    special_json = json.loads(registry.export_json())
    assert "cpu_usage_percent" in special_json, "Should handle underscores in names"

if __name__ == "__main__":
    test_metric_export()
    print("✓ metric_export passed")
