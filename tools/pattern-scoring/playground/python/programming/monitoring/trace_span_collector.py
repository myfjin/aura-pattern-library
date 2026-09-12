"""
Distributed Tracing Span Collector Module

This module provides a complete implementation of a distributed tracing system
with span collection, parent-child relationships, baggage propagation, and sampling.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import time
import uuid
from typing import Dict, List, Optional, Any, Callable
from dataclasses import dataclass, field
from contextlib import contextmanager
import random
import threading


@dataclass
class SpanContext:
    """Represents the context of a span for distributed tracing."""
    trace_id: str
    span_id: str
    parent_span_id: Optional[str]
    baggage: Dict[str, str] = field(default_factory=dict)
    sampled: bool = True


class Span:
    """Represents a single unit of work in a distributed trace."""
    
    def __init__(
        self,
        name: str,
        context: SpanContext,
        start_time: Optional[float] = None
    ):
        """
        Initialize a new Span.
        
        Args:
            name: Name of the span
            context: Span context containing trace information
            start_time: Optional start time (defaults to current time)
        """
        self.name = name
        self.context = context
        self.start_time = start_time or time.time()
        self.end_time: Optional[float] = None
        self.tags: Dict[str, Any] = {}
        self.logs: List[Dict[str, Any]] = []
        self.children: List['Span'] = []
        
    def finish(self, end_time: Optional[float] = None) -> None:
        """
        Mark the span as finished.
        
        Args:
            end_time: Optional end time (defaults to current time)
        """
        if self.end_time is not None:
            raise RuntimeError("Span already finished")
        self.end_time = end_time or time.time()
        
    def set_tag(self, key: str, value: Any) -> None:
        """
        Add a tag to the span.
        
        Args:
            key: Tag key
            value: Tag value
        """
        self.tags[key] = value
        
    def log(self, message: str, timestamp: Optional[float] = None) -> None:
        """
        Add a log entry to the span.
        
        Args:
            message: Log message
            timestamp: Optional timestamp (defaults to current time)
        """
        self.logs.append({
            'timestamp': timestamp or time.time(),
            'message': message
        })
        
    def add_baggage_item(self, key: str, value: str) -> None:
        """
        Add a baggage item to propagate across spans.
        
        Args:
            key: Baggage key
            value: Baggage value
        """
        self.context.baggage[key] = value
        
    def get_baggage_item(self, key: str) -> Optional[str]:
        """
        Get a baggage item value.
        
        Args:
            key: Baggage key
            
        Returns:
            Baggage value or None if not found
        """
        return self.context.baggage.get(key)
        
    @property
    def duration(self) -> Optional[float]:
        """Get the duration of the span in seconds."""
        if self.end_time is None:
            return None
        return self.end_time - self.start_time
        
    def to_dict(self) -> Dict[str, Any]:
        """Convert span to dictionary representation."""
        return {
            'name': self.name,
            'trace_id': self.context.trace_id,
            'span_id': self.context.span_id,
            'parent_span_id': self.context.parent_span_id,
            'start_time': self.start_time,
            'end_time': self.end_time,
            'duration': self.duration,
            'tags': self.tags,
            'logs': self.logs,
            'baggage': self.context.baggage,
            'sampled': self.context.sampled
        }


class Trace:
    """Represents a complete trace containing multiple spans."""
    
    def __init__(self, trace_id: str):
        """
        Initialize a new Trace.
        
        Args:
            trace_id: Unique identifier for the trace
        """
        self.trace_id = trace_id
        self.spans: List[Span] = []
        self.root_spans: List[Span] = []
        
    def add_span(self, span: Span) -> None:
        """
        Add a span to the trace.
        
        Args:
            span: Span to add
        """
        self.spans.append(span)
        # If span has no parent, it's a root span
        if span.context.parent_span_id is None:
            self.root_spans.append(span)
            
    def get_span_by_id(self, span_id: str) -> Optional[Span]:
        """
        Get a span by its ID.
        
        Args:
            span_id: Span ID to search for
            
        Returns:
            Span object or None if not found
        """
        for span in self.spans:
            if span.context.span_id == span_id:
                return span
        return None
        
    def to_dict(self) -> Dict[str, Any]:
        """Convert trace to dictionary representation."""
        return {
            'trace_id': self.trace_id,
            'spans': [span.to_dict() for span in self.spans]
        }


class Sampler:
    """Determines whether traces should be sampled."""
    
    def __init__(self, sampling_rate: float = 1.0):
        """
        Initialize sampler.
        
        Args:
            sampling_rate: Rate at which to sample (0.0 to 1.0)
        """
        if not 0.0 <= sampling_rate <= 1.0:
            raise ValueError("Sampling rate must be between 0.0 and 1.0")
        self.sampling_rate = sampling_rate
        
    def should_sample(self, trace_id: str) -> bool:
        """
        Determine if a trace should be sampled.
        
        Args:
            trace_id: Trace ID to evaluate
            
        Returns:
            True if trace should be sampled, False otherwise
        """
        if self.sampling_rate >= 1.0:
            return True
        if self.sampling_rate <= 0.0:
            return False
            
        # Use trace_id to make consistent sampling decisions
        hash_value = hash(trace_id)
        return (hash_value % 10000) / 10000.0 < self.sampling_rate


class SpanCollector:
    """Collects and manages spans and traces."""
    
    def __init__(self, sampler: Optional[Sampler] = None):
        """
        Initialize span collector.
        
        Args:
            sampler: Optional sampler (defaults to always sample)
        """
        self.sampler = sampler or Sampler()
        self.traces: Dict[str, Trace] = {}
        self._local = threading.local()
        
    def start_span(
        self,
        name: str,
        parent_context: Optional[SpanContext] = None,
        trace_id: Optional[str] = None
    ) -> Span:
        """
        Start a new span.
        
        Args:
            name: Name of the span
            parent_context: Optional parent span context
            trace_id: Optional trace ID (generated if not provided)
            
        Returns:
            New span instance
        """
        # Generate trace ID if not provided
        if trace_id is None:
            if parent_context is not None:
                trace_id = parent_context.trace_id
            else:
                trace_id = str(uuid.uuid4())
        
        # Determine if this trace should be sampled. Children inherit the
        # root's decision so a trace is never half-collected.
        if parent_context is not None:
            sampled = parent_context.sampled
        else:
            sampled = self.sampler.should_sample(trace_id)
        
        # Create span context
        span_id = str(uuid.uuid4())
        parent_span_id = parent_context.span_id if parent_context else None
        
        # Inherit baggage from parent
        baggage = {}
        if parent_context:
            baggage = parent_context.baggage.copy()
            
        context = SpanContext(
            trace_id=trace_id,
            span_id=span_id,
            parent_span_id=parent_span_id,
            baggage=baggage,
            sampled=sampled
        )
        
        # Create span
        span = Span(name, context)
        
        # Add to trace ONLY if sampled — the former code computed the
        # sampling decision and then collected every span anyway, making
        # the sampler decorative.
        if sampled:
            if trace_id not in self.traces:
                self.traces[trace_id] = Trace(trace_id)
            self.traces[trace_id].add_span(span)
        
        # Set as current span
        self._local.current_span = span
        
        return span
        
    def finish_span(self, span: Span) -> None:
        """
        Finish a span and record it.
        
        Args:
            span: Span to finish
        """
        span.finish()
        if hasattr(self._local, 'current_span'):
            del self._local.current_span
            
    def get_current_span(self) -> Optional[Span]:
        """
        Get the currently active span.
        
        Returns:
            Current span or None if no active span
        """
        return getattr(self._local, 'current_span', None)
        
    def get_trace(self, trace_id: str) -> Optional[Trace]:
        """
        Get a trace by ID.
        
        Args:
            trace_id: Trace ID to retrieve
            
        Returns:
            Trace object or None if not found
        """
        return self.traces.get(trace_id)
        
    def get_all_traces(self) -> List[Trace]:
        """
        Get all collected traces.
        
        Returns:
            List of all traces
        """
        return list(self.traces.values())


@contextmanager
def trace_span(collector: SpanCollector, name: str, parent_context: Optional[SpanContext] = None):
    """
    Context manager for creating and managing spans.
    
    Args:
        collector: Span collector instance
        name: Name of the span
        parent_context: Optional parent context
    """
    span = collector.start_span(name, parent_context)
    try:
        yield span
    finally:
        collector.finish_span(span)


def main():
    """Self-test: nested spans share one trace with correct parent ids,
    baggage propagates parent→child, sampling 0% collects nothing,
    to_dict round-trips the structure."""
    collector = SpanCollector(Sampler(sampling_rate=1.0))

    # Nested spans: parent → child1 → grandchild, plus child2 under parent.
    with trace_span(collector, "parent") as parent:
        parent.set_tag("component", "backend")
        parent.add_baggage_item("user_id", "12345")
        with trace_span(collector, "child1", parent.context) as child1:
            child1.set_tag("db.rows", 10)
            with trace_span(collector, "grandchild", child1.context) as grandchild:
                grandchild.set_tag("cache.hit", False)
        with trace_span(collector, "child2", parent.context) as child2:
            child2.set_tag("http.status", 200)
            # Baggage must have propagated from the parent context.
            assert child2.get_baggage_item("user_id") == "12345", \
                "baggage did not propagate parent → child"

    # All four spans belong to ONE trace.
    traces = collector.get_all_traces()
    assert len(traces) == 1, f"nested spans created {len(traces)} traces, want 1"
    trace = traces[0]
    assert len(trace.spans) == 4, f"trace must hold 4 spans, got {len(trace.spans)}"
    by_name = {s.name: s for s in trace.spans}
    assert set(by_name) == {"parent", "child1", "grandchild", "child2"}

    # Parent links are exact.
    assert by_name["parent"].context.parent_span_id is None
    assert by_name["child1"].context.parent_span_id == by_name["parent"].context.span_id
    assert by_name["child2"].context.parent_span_id == by_name["parent"].context.span_id
    assert by_name["grandchild"].context.parent_span_id == by_name["child1"].context.span_id, \
        "grandchild not linked to child1"
    assert all(s.context.trace_id == trace.trace_id for s in trace.spans)

    # Tags survive; durations set by finish and children fit inside parents.
    assert by_name["child1"].tags["db.rows"] == 10
    assert by_name["grandchild"].tags["cache.hit"] is False
    for s in trace.spans:
        assert s.duration is not None and s.duration >= 0, f"{s.name} has no duration"
    assert by_name["parent"].duration >= by_name["child1"].duration, \
        "child outlived its parent"

    # Separate root spans start separate traces.
    for i in range(3):
        with trace_span(collector, f"root-{i}") as s:
            s.set_tag("n", i)
    assert len(collector.get_all_traces()) == 4, \
        f"3 new roots must give 4 traces total, got {len(collector.get_all_traces())}"

    # 0% sampling collects nothing (but spans still work as no-ops).
    quiet = SpanCollector(Sampler(sampling_rate=0.0))
    with trace_span(quiet, "unsampled") as s:
        s.set_tag("x", 1)
    assert len(quiet.get_all_traces()) == 0, "0%-sampler still collected a trace"

    # Export: to_dict carries all spans with their ids.
    exported = trace.to_dict()
    assert len(exported["spans"]) == 4
    assert exported["trace_id"] == trace.trace_id
    exported_names = sorted(s["name"] for s in exported["spans"])
    assert exported_names == ["child1", "child2", "grandchild", "parent"]

    # Honest lookups.
    assert collector.get_trace(trace.trace_id) is trace
    assert collector.get_trace("ghost") is None

    print("trace_span_collector: 4 spans/1 trace, parent ids exact, baggage "
          "propagated, 0% sampler silent, to_dict complete — PASS")


if __name__ == "__main__":
    main()