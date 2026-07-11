#!/usr/bin/env python3
"""
Round-trip time estimator module with EWMA smoothing and timeout calculation.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import time
from typing import List, Optional, Tuple
from dataclasses import dataclass


@dataclass
class Sample:
    """Represents a single RTT measurement."""
    timestamp: float
    rtt: float


class RTTEstimator:
    """Estimates round-trip time using EWMA smoothing."""
    
    def __init__(self, alpha: float = 0.125, beta: float = 0.25) -> None:
        """
        Initialize RTT estimator.
        
        Args:
            alpha: Smoothing factor for RTT (0 < alpha <= 1)
            beta: Smoothing factor for jitter (0 < beta <= 1)
        """
        if not 0 < alpha <= 1:
            raise ValueError("alpha must be in range (0, 1]")
        if not 0 < beta <= 1:
            raise ValueError("beta must be in range (0, 1]")
            
        self.alpha = alpha
        self.beta = beta
        self.srtt: Optional[float] = None  # Smoothed RTT
        self.rttvar: Optional[float] = None  # RTT variation
        self.rto: float = 1.0  # Retransmission timeout (default 1 second)
        self.samples: List[Sample] = []
    
    def add_sample(self, rtt: float, timestamp: Optional[float] = None) -> None:
        """
        Add a new RTT sample and update estimates.
        
        Args:
            rtt: Measured round-trip time in seconds
            timestamp: Optional timestamp of measurement (defaults to current time)
        """
        if rtt < 0:
            raise ValueError("RTT cannot be negative")
            
        if timestamp is None:
            timestamp = time.time()
            
        self.samples.append(Sample(timestamp, rtt))
        
        # First sample
        if self.srtt is None:
            self.srtt = rtt
            self.rttvar = rtt / 2
        else:
            # Update jitter (RTT variation)
            if self.rttvar is not None:
                jitter = abs(rtt - self.srtt)
                self.rttvar = (1 - self.beta) * self.rttvar + self.beta * jitter
            
            # Update smoothed RTT
            self.srtt = (1 - self.alpha) * self.srtt + self.alpha * rtt
        
        # Calculate retransmission timeout
        if self.srtt is not None and self.rttvar is not None:
            self.rto = self.srtt + 4 * self.rttvar
    
    def get_rtt_estimate(self) -> Optional[float]:
        """
        Get current smoothed RTT estimate.
        
        Returns:
            Smoothed RTT in seconds, or None if no samples
        """
        return self.srtt
    
    def get_jitter(self) -> Optional[float]:
        """
        Get current RTT variation (jitter) estimate.
        
        Returns:
            RTT variation in seconds, or None if no samples
        """
        return self.rttvar
    
    def get_timeout(self) -> float:
        """
        Get recommended retransmission timeout.
        
        Returns:
            Timeout value in seconds
        """
        return self.rto
    
    def get_sample_count(self) -> int:
        """
        Get number of samples collected.
        
        Returns:
            Number of RTT samples
        """
        return len(self.samples)
    
    def get_samples(self) -> List[Sample]:
        """
        Get all collected samples.
        
        Returns:
            List of all RTT samples
        """
        return self.samples.copy()


def simulate_network_rtt(base_rtt: float, jitter: float, count: int) -> List[float]:
    """
    Simulate network RTT measurements with jitter.
    
    Args:
        base_rtt: Base RTT in seconds
        jitter: Maximum jitter in seconds
        count: Number of samples to generate
        
    Returns:
        List of simulated RTT measurements
    """
    import random
    random.seed(42)  # For reproducible results
    
    samples = []
    for _ in range(count):
        # Add random jitter (-jitter to +jitter)
        jitter_offset = random.uniform(-jitter, jitter)
        rtt = max(0.001, base_rtt + jitter_offset)  # Minimum 1ms
        samples.append(rtt)
    
    return samples


def main() -> None:
    """Self-test: hand-traced EWMA arithmetic (RFC 6298 shape) is exact,
    convergence on a steady link, RTO responds to jitter."""
    # alpha=beta=0.5 makes the recurrence exactly traceable.
    est = RTTEstimator(alpha=0.5, beta=0.5)
    assert est.get_rtt_estimate() is None and est.get_jitter() is None
    assert est.get_timeout() == 1.0, "default RTO before any sample must be 1.0"

    # Sample 1 (0.1s): srtt=0.1, rttvar=0.05, rto=0.1+4*0.05=0.3.
    est.add_sample(0.1, timestamp=1.0)
    assert abs(est.get_rtt_estimate() - 0.1) < 1e-12
    assert abs(est.get_jitter() - 0.05) < 1e-12
    assert abs(est.get_timeout() - 0.3) < 1e-12, f"RTO must be 0.3, got {est.get_timeout()}"

    # Sample 2 (0.2s): jitter=|0.2-0.1|=0.1 → rttvar=0.075; srtt=0.15; rto=0.45.
    est.add_sample(0.2, timestamp=2.0)
    assert abs(est.get_rtt_estimate() - 0.15) < 1e-12
    assert abs(est.get_jitter() - 0.075) < 1e-12
    assert abs(est.get_timeout() - 0.45) < 1e-12

    # Sample 3 (0.15s): jitter=0 → rttvar=0.0375; srtt stays 0.15; rto=0.3.
    est.add_sample(0.15, timestamp=3.0)
    assert abs(est.get_rtt_estimate() - 0.15) < 1e-12
    assert abs(est.get_jitter() - 0.0375) < 1e-12
    assert abs(est.get_timeout() - 0.3) < 1e-12
    assert est.get_sample_count() == 3

    # Steady link: constant 80ms drives srtt→0.08 and jitter→0.
    steady = RTTEstimator(alpha=0.125, beta=0.25)
    for _ in range(200):
        steady.add_sample(0.08, timestamp=0.0)
    assert abs(steady.get_rtt_estimate() - 0.08) < 1e-9, "srtt did not converge"
    assert steady.get_jitter() < 1e-6, "jitter did not decay on a steady link"
    assert abs(steady.get_timeout() - 0.08) < 1e-4, "RTO must approach srtt when jitter dies"

    # A jittery link keeps RTO safely above srtt (the whole point of the 4x term).
    noisy = RTTEstimator(alpha=0.125, beta=0.25)
    for i in range(100):
        noisy.add_sample(0.1 if i % 2 == 0 else 0.2, timestamp=float(i))
    assert noisy.get_timeout() > noisy.get_rtt_estimate() + 0.1, \
        "RTO on an alternating 100/200ms link must include a jitter margin"

    # Samples are recorded with timestamps; copies protect internals.
    s = est.get_samples()
    assert [x.rtt for x in s] == [0.1, 0.2, 0.15]
    s.append(Sample(9.0, 9.9))
    assert est.get_sample_count() == 3, "get_samples leaked the internal list"

    # Refusals.
    for bad in (lambda: est.add_sample(-0.1),
                lambda: RTTEstimator(alpha=0.0), lambda: RTTEstimator(beta=1.5)):
        try:
            bad()
            assert False, "invalid input accepted"
        except ValueError:
            pass

    print("rtt_estimator: EWMA trace 0.3/0.45/0.3 exact, steady link converged "
          "(jitter→0), noisy link keeps margin, internals copy-safe — PASS")


if __name__ == "__main__":
    main()