# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import time
import uuid
from typing import Dict, List, Optional, Any
from dataclasses import dataclass, field
from collections import defaultdict


@dataclass
class Span:
    """A single unit of work in a trace."""
    span_id: str
    name: str
    start_time: float
    end_time: Optional[float] = None
    parent_id: Optional[str] = None
    trace_id: Optional[str] = None
    attributes: Dict[str, Any] = field(default_factory=dict)
    status: str = "unset"

    def finish(self) -> None:
        """Mark the span as finished."""
        if self.end_time is None:
            self.end_time = time.time()
            self.status = "ok"

    def set_attribute(self, key: str, value: Any) -> None:
        """Set an attribute on the span."""
        self.attributes[key] = value

    def set_error(self) -> None:
        """Mark the span as having an error."""
        self.status = "error"

    @property
    def duration(self) -> float:
        """Get the duration of the span in seconds."""
        if self.end_time is None:
            return 0.0
        return self.end_time - self.start_time


class Trace:
    """A collection of spans that represent a single operation."""

    def __init__(self, trace_id: Optional[str] = None):
        self.trace_id: str = trace_id or str(uuid.uuid4())
        self.spans: Dict[str, Span] = {}
        self.root_spans: List[str] = []

    def add_span(self, span: Span) -> None:
        """Add a span to the trace."""
        span.trace_id = self.trace_id
        self.spans[span.span_id] = span
        if span.parent_id is None:
            self.root_spans.append(span.span_id)

    def get_span(self, span_id: str) -> Optional[Span]:
        """Get a span by ID."""
        return self.spans.get(span_id)

    def get_children(self, span_id: str) -> List[Span]:
        """Get all direct children of a span."""
        return [span for span in self.spans.values() if span.parent_id == span_id]

    def get_trace_tree(self) -> Dict[str, Any]:
        """Get a tree representation of the trace."""
        def build_tree(span_id: str) -> Dict[str, Any]:
            span = self.spans[span_id]
            children = self.get_children(span_id)
            return {
                "span": span,
                "children": [build_tree(child.span_id) for child in children]
            }
        
        return {
            "trace_id": self.trace_id,
            "roots": [build_tree(root_id) for root_id in self.root_spans]
        }


class Collector:
    """Collects and manages traces."""

    def __init__(self):
        self.traces: Dict[str, Trace] = {}

    def create_trace(self, trace_id: Optional[str] = None) -> Trace:
        """Create a new trace."""
        trace = Trace(trace_id)
        self.traces[trace.trace_id] = trace
        return trace

    def get_trace(self, trace_id: str) -> Optional[Trace]:
        """Get a trace by ID."""
        return self.traces.get(trace_id)

    def create_span(self, 
                   name: str, 
                   trace_id: Optional[str] = None, 
                   parent_span_id: Optional[str] = None) -> Span:
        """Create a new span, creating a trace if needed."""
        if trace_id is None:
            # If no trace ID, create a new trace
            trace = self.create_trace()
            trace_id = trace.trace_id
        elif trace_id not in self.traces:
            # If trace doesn't exist, create it
            trace = self.create_trace(trace_id)
        else:
            trace = self.traces[trace_id]

        span = Span(
            span_id=str(uuid.uuid4()),
            name=name,
            start_time=time.time(),
            parent_id=parent_span_id,
            trace_id=trace_id
        )
        
        trace.add_span(span)
        return span

    def get_all_traces(self) -> List[Trace]:
        """Get all traces."""
        return list(self.traces.values())


def _print_trace_tree(node: Dict[str, Any], indent: int = 0) -> None:
    """Helper function to print a trace tree."""
    span = node["span"]
    status_icon = "✓" if span.status == "ok" else "✗" if span.status == "error" else "○"
    print(f"{'  ' * indent}{status_icon} {span.name} ({span.duration:.3f}s)")
    
    for key, value in span.attributes.items():
        print(f"{'  ' * (indent + 1)}{key}: {value}")
    
    for child in node["children"]:
        _print_trace_tree(child, indent + 1)


if __name__ == "__main__":
    # Create a collector
    collector = Collector()
    
    # Create a trace with a root span
    root_span = collector.create_span("HTTP GET /api/users")
    root_span.set_attribute("http.method", "GET")
    root_span.set_attribute("http.url", "/api/users")
    
    # Add a child span for database query
    db_span = collector.create_span(
        "SELECT users", 
        trace_id=root_span.trace_id, 
        parent_span_id=root_span.span_id
    )
    db_span.set_attribute("db.statement", "SELECT * FROM users")
    db_span.set_attribute("db.type", "sql")
    
    # Simulate some work
    time.sleep(0.01)
    db_span.finish()
    
    # Add another child span for external API call
    api_span = collector.create_span(
        "Call external API", 
        trace_id=root_span.trace_id, 
        parent_span_id=root_span.span_id
    )
    api_span.set_attribute("http.url", "https://api.external.com/users")
    api_span.set_attribute("http.method", "GET")
    
    # Simulate some work and an error
    time.sleep(0.02)
    api_span.set_error()
    api_span.finish()
    
    # Finish the root span
    root_span.finish()
    
    # Create another trace
    second_root = collector.create_span("Process batch job")
    second_root.set_attribute("job.type", "data_processing")
    
    child_job = collector.create_span(
        "Process file", 
        trace_id=second_root.trace_id, 
        parent_span_id=second_root.span_id
    )
    child_job.set_attribute("file.name", "data.csv")
    time.sleep(0.01)
    child_job.finish()
    second_root.finish()
    
    # Print all traces
    print("Traces collected:")
    print("=" * 50)
    
    for trace in collector.get_all_traces():
        tree = trace.get_trace_tree()
        print(f"Trace ID: {tree['trace_id']}")
        for root in tree["roots"]:
            _print_trace_tree(root)
        print()