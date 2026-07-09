"""
Distributed Tracing Sampler Module

This module provides a complete implementation of a distributed tracing sampler
with support for rate limiting, priority traces, and adaptive sampling.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import random
import time
from typing import Dict, Optional, Any
from dataclasses import dataclass
from enum import Enum
from collections import deque
import threading


class SamplingDecision(Enum):
    """Enumeration of possible sampling decisions."""
    SAMPLE = "sample"
    DROP = "drop"


@dataclass
class TraceContext:
    """Context for a trace containing relevant metadata."""
    trace_id: str
    span_id: str
    service_name: str
    operation_name: str
    priority: bool = False
    tags: Optional[Dict[str, Any]] = None
    
    def __post_init__(self):
        if self.tags is None:
            self.tags = {}


@dataclass
class SamplingResult:
    """Result of a sampling decision."""
    decision: SamplingDecision
    sample_rate: float


class Sampler:
    """Base class for all samplers."""
    
    def should_sample(self, context: TraceContext) -> SamplingResult:
        """
        Determine whether a trace should be sampled.
        
        Args:
            context: Trace context containing trace information
            
        Returns:
            SamplingResult with decision and sample rate
        """
        raise NotImplementedError


class AlwaysOnSampler(Sampler):
    """Sampler that always samples traces."""
    
    def should_sample(self, context: TraceContext) -> SamplingResult:
        return SamplingResult(SamplingDecision.SAMPLE, 1.0)


class AlwaysOffSampler(Sampler):
    """Sampler that never samples traces."""
    
    def should_sample(self, context: TraceContext) -> SamplingResult:
        return SamplingResult(SamplingDecision.DROP, 0.0)


class ProbabilisticSampler(Sampler):
    """Sampler that samples traces with a fixed probability."""
    
    def __init__(self, sampling_rate: float):
        """
        Initialize the sampler.
        
        Args:
            sampling_rate: Probability of sampling (0.0 to 1.0)
        """
        if not 0.0 <= sampling_rate <= 1.0:
            raise ValueError("Sampling rate must be between 0.0 and 1.0")
        self.sampling_rate = sampling_rate
    
    def should_sample(self, context: TraceContext) -> SamplingResult:
        if context.priority:
            return SamplingResult(SamplingDecision.SAMPLE, 1.0)
        
        if random.random() < self.sampling_rate:
            return SamplingResult(SamplingDecision.SAMPLE, self.sampling_rate)
        else:
            return SamplingResult(SamplingDecision.DROP, self.sampling_rate)


class RateLimitingSampler(Sampler):
    """Sampler that enforces a maximum number of traces per second."""
    
    def __init__(self, max_traces_per_second: int):
        """
        Initialize the sampler.
        
        Args:
            max_traces_per_second: Maximum number of traces to sample per second
        """
        if max_traces_per_second < 0:
            raise ValueError("Max traces per second must be non-negative")
        self.max_traces_per_second = max_traces_per_second
        self._lock = threading.Lock()
        self._traces_this_second = 0
        self._last_reset_time = time.time()
    
    def should_sample(self, context: TraceContext) -> SamplingResult:
        if context.priority:
            return SamplingResult(SamplingDecision.SAMPLE, 1.0)
        
        if self.max_traces_per_second == 0:
            return SamplingResult(SamplingDecision.DROP, 0.0)
        
        with self._lock:
            current_time = time.time()
            
            # Reset counter if a second has passed
            if current_time - self._last_reset_time >= 1.0:
                self._traces_this_second = 0
                self._last_reset_time = current_time
            
            # Check if we've hit the limit
            if self._traces_this_second < self.max_traces_per_second:
                self._traces_this_second += 1
                return SamplingResult(SamplingDecision.SAMPLE, 
                                    self.max_traces_per_second)
            else:
                return SamplingResult(SamplingDecision.DROP, 
                                    self.max_traces_per_second)


class AdaptiveSampler(Sampler):
    """Sampler that adapts sampling rate based on observed throughput."""
    
    def __init__(self, target_traces_per_second: int, window_size: int = 10):
        """
        Initialize the sampler.
        
        Args:
            target_traces_per_second: Target number of traces per second
            window_size: Number of seconds to consider for rate calculation
        """
        if target_traces_per_second < 0:
            raise ValueError("Target traces per second must be non-negative")
        if window_size <= 0:
            raise ValueError("Window size must be positive")
            
        self.target_traces_per_second = target_traces_per_second
        self.window_size = window_size
        self._lock = threading.Lock()
        
        # Circular buffer to store trace counts per second
        self._trace_counts = deque(maxlen=window_size)
        self._current_second_traces = 0
        self._current_second_start = time.time()
        
        # Initialize with target rate
        self._current_sampling_rate = 1.0 if target_traces_per_second > 0 else 0.0
    
    def should_sample(self, context: TraceContext) -> SamplingResult:
        if context.priority:
            return SamplingResult(SamplingDecision.SAMPLE, 1.0)
        
        with self._lock:
            current_time = time.time()
            
            # Check if we've moved to a new second
            if current_time - self._current_second_start >= 1.0:
                # Add previous second's count to window
                self._trace_counts.append(self._current_second_traces)
                # Reset for current second
                self._current_second_traces = 0
                self._current_second_start = current_time
            
            # Calculate current rate
            if len(self._trace_counts) > 0:
                avg_traces_per_second = sum(self._trace_counts) / len(self._trace_counts)
                if avg_traces_per_second > 0:
                    # Adjust sampling rate inversely to current rate
                    self._current_sampling_rate = min(1.0, 
                        self.target_traces_per_second / avg_traces_per_second)
            
            # Make sampling decision
            decision = SamplingDecision.SAMPLE if random.random() < self._current_sampling_rate else SamplingDecision.DROP
            
            # Update trace count if we're sampling
            if decision == SamplingDecision.SAMPLE:
                self._current_second_traces += 1
            
            return SamplingResult(decision, self._current_sampling_rate)


class PrioritySampler(Sampler):
    """Sampler that gives priority to certain traces while using a base sampler for others."""
    
    def __init__(self, base_sampler: Sampler, priority_tags: Dict[str, Any]):
        """
        Initialize the sampler.
        
        Args:
            base_sampler: The base sampler to use for non-priority traces
            priority_tags: Tags that indicate a trace should be prioritized
        """
        self.base_sampler = base_sampler
        self.priority_tags = priority_tags
    
    def should_sample(self, context: TraceContext) -> SamplingResult:
        # Check if this is already marked as priority
        if context.priority:
            return SamplingResult(SamplingDecision.SAMPLE, 1.0)
        
        # Check if any priority tags match
        if context.tags:
            for key, value in self.priority_tags.items():
                if key in context.tags and context.tags[key] == value:
                    return SamplingResult(SamplingDecision.SAMPLE, 1.0)
        
        # Use base sampler for non-priority traces
        return self.base_sampler.should_sample(context)


def create_sampler(sampler_type: str, **kwargs) -> Sampler:
    """
    Factory function to create samplers.
    
    Args:
        sampler_type: Type of sampler to create
        **kwargs: Arguments for the sampler constructor
        
    Returns:
        A sampler instance
    """
    samplers = {
        "always_on": AlwaysOnSampler,
        "always_off": AlwaysOffSampler,
        "probabilistic": ProbabilisticSampler,
        "rate_limiting": RateLimitingSampler,
        "adaptive": AdaptiveSampler,
        "priority": lambda: PrioritySampler(
            kwargs.pop('base_sampler'), 
            kwargs.pop('priority_tags', {})
        )
    }
    
    if sampler_type not in samplers:
        raise ValueError(f"Unknown sampler type: {sampler_type}")
    
    return samplers[sampler_type](**kwargs)


def main():
    """Demo of the distributed tracing sampler."""
    print("Distributed Tracing Sampler Demo")
    print("=" * 40)
    
    # Test different samplers
    samplers = {
        "Always On": AlwaysOnSampler(),
        "Always Off": AlwaysOffSampler(),
        "Probabilistic (10%)": ProbabilisticSampler(0.1),
        "Rate Limiting (5/sec)": RateLimitingSampler(5),
        "Adaptive (target 3/sec)": AdaptiveSampler(3),
    }
    
    # Add priority sampler
    base_sampler = ProbabilisticSampler(0.1)
    priority_sampler = PrioritySampler(
        base_sampler, 
        {"error": True}
    )
    samplers["Priority"] = priority_sampler
    
    # Generate test traces
    trace_count = 50
    results = {name: {"sampled": 0, "total": 0} for name in samplers}
    
    print(f"Generating {trace_count} traces for each sampler...\n")
    
    for name, sampler in samplers.items():
        sampled_count = 0
        
        for i in range(trace_count):
            # Create a trace context
            context = TraceContext(
                trace_id=f"trace-{i}",
                span_id=f"span-{i}",
                service_name="test-service",
                operation_name=f"operation-{i % 5}",
                tags={"error": i % 10 == 0}  # 10% error traces
            )
            
            # For priority sampler, mark some as priority
            if name == "Priority" and i % 7 == 0:
                context.priority = True
            
            # Make sampling decision
            result = sampler.should_sample(context)
            
            if result.decision == SamplingDecision.SAMPLE:
                sampled_count += 1
        
        results[name]["sampled"] = sampled_count
        results[name]["total"] = trace_count
        
        # Print results
        rate = (sampled_count / trace_count) * 100 if trace_count > 0 else 0
        print(f"{name:25}: {sampled_count:2d}/{trace_count:2d} ({rate:5.1f}%)")
    
    print("\n" + "=" * 40)
    print("Demo completed successfully!")


if __name__ == "__main__":
    main()