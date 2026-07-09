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
    """Demonstrate RTT estimator functionality."""
    print("RTT Estimator Demo")
    print("=" * 50)
    
    # Create estimator
    estimator = RTTEstimator(alpha=0.125, beta=0.25)
    
    # Simulate network measurements
    base_rtt = 0.1  # 100ms base RTT
    jitter = 0.05   # ±50ms jitter
    samples = simulate_network_rtt(base_rtt, jitter, 20)
    
    # Process samples
    for i, rtt in enumerate(samples):
        estimator.add_sample(rtt)
        srtt = estimator.get_rtt_estimate()
        jitter_val = estimator.get_jitter()
        timeout = estimator.get_timeout()
        
        print(f"Sample {i+1:2d}: RTT={rtt*1000:6.1f}ms "
              f"SRTT={srtt*1000:6.1f}ms "
              f"Jitter={jitter_val*1000:5.1f}ms "
              f"RTO={timeout*1000:6.1f}ms")
    
    print("\nFinal Statistics:")
    print(f"  Samples processed: {estimator.get_sample_count()}")
    print(f"  Final SRTT: {estimator.get_rtt_estimate()*1000:.1f}ms")
    print(f"  Final Jitter: {estimator.get_jitter()*1000:.1f}ms")
    print(f"  Recommended RTO: {estimator.get_timeout()*1000:.1f}ms")
    
    # Test error handling
    print("\nTesting error handling:")
    try:
        estimator.add_sample(-0.1)  # Negative RTT
    except ValueError as e:
        print(f"  Caught expected error: {e}")
    
    # Test with different alpha/beta values
    print("\nTesting with higher smoothing (alpha=0.5, beta=0.5):")
    estimator2 = RTTEstimator(alpha=0.5, beta=0.5)
    for rtt in samples[:10]:  # Only first 10 samples
        estimator2.add_sample(rtt)
        print(f"  SRTT={estimator2.get_rtt_estimate()*1000:6.1f}ms "
              f"RTO={estimator2.get_timeout()*1000:6.1f}ms")


if __name__ == "__main__":
    main()