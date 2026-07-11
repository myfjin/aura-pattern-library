"""
Resource Budget Allocator Module

This module provides functionality for allocating and managing resource budgets
with quota tracking and overcommit detection.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

from typing import Dict, Optional, List
from dataclasses import dataclass
from collections import defaultdict
import threading


@dataclass
class Resource:
    """Represents a resource with a name and capacity."""
    name: str
    capacity: float


class BudgetAllocator:
    """Manages resource allocation with quota tracking and overcommit detection."""
    
    def __init__(self, resources: List[Resource]):
        """
        Initialize the BudgetAllocator with available resources.
        
        Args:
            resources: List of Resource objects defining available resources
        """
        self._resources = {r.name: r.capacity for r in resources}
        self._allocated: Dict[str, float] = defaultdict(float)
        self._quotas: Dict[str, Dict[str, float]] = defaultdict(lambda: defaultdict(float))
        self._lock = threading.RLock()
        
        # Validate resources
        for name, capacity in self._resources.items():
            if capacity < 0:
                raise ValueError(f"Resource {name} has negative capacity: {capacity}")
    
    def allocate(self, user_id: str, resource_name: str, amount: float) -> bool:
        """
        Allocate resources to a user.
        
        Args:
            user_id: Identifier for the user
            resource_name: Name of the resource to allocate
            amount: Amount of resource to allocate
            
        Returns:
            True if allocation successful, False if it would cause overcommit
            
        Raises:
            ValueError: If amount is negative or resource doesn't exist
        """
        if amount < 0:
            raise ValueError("Allocation amount cannot be negative")
            
        if resource_name not in self._resources:
            raise ValueError(f"Unknown resource: {resource_name}")
        
        with self._lock:
            # Check if allocation would exceed capacity
            if self._allocated[resource_name] + amount > self._resources[resource_name]:
                return False
            
            self._allocated[resource_name] += amount
            self._quotas[user_id][resource_name] += amount
            return True
    
    def release(self, user_id: str, resource_name: str, amount: float) -> bool:
        """
        Release previously allocated resources.
        
        Args:
            user_id: Identifier for the user
            resource_name: Name of the resource to release
            amount: Amount of resource to release
            
        Returns:
            True if release successful, False if trying to release more than allocated
            
        Raises:
            ValueError: If amount is negative or resource doesn't exist
        """
        if amount < 0:
            raise ValueError("Release amount cannot be negative")
            
        if resource_name not in self._resources:
            raise ValueError(f"Unknown resource: {resource_name}")
        
        with self._lock:
            # Check if user has enough allocated
            if self._quotas[user_id][resource_name] < amount:
                return False
            
            # Check if system has enough allocated
            if self._allocated[resource_name] < amount:
                return False
                
            self._allocated[resource_name] -= amount
            self._quotas[user_id][resource_name] -= amount
            
            # Clean up empty quotas
            if self._quotas[user_id][resource_name] == 0:
                del self._quotas[user_id][resource_name]
                if not self._quotas[user_id]:
                    del self._quotas[user_id]
            
            return True
    
    def get_allocation(self, user_id: str, resource_name: str) -> float:
        """
        Get current allocation for a user-resource pair.
        
        Args:
            user_id: Identifier for the user
            resource_name: Name of the resource
            
        Returns:
            Amount of resource allocated to the user
        """
        with self._lock:
            return self._quotas[user_id][resource_name]
    
    def get_total_allocated(self, resource_name: str) -> float:
        """
        Get total allocated amount for a resource.
        
        Args:
            resource_name: Name of the resource
            
        Returns:
            Total amount of resource currently allocated
        """
        with self._lock:
            return self._allocated[resource_name]
    
    def get_utilization(self, resource_name: str) -> float:
        """
        Get utilization percentage for a resource.
        
        Args:
            resource_name: Name of the resource
            
        Returns:
            Utilization as a percentage (0.0 to 1.0)
            
        Raises:
            ValueError: If resource doesn't exist
        """
        if resource_name not in self._resources:
            raise ValueError(f"Unknown resource: {resource_name}")
            
        with self._lock:
            if self._resources[resource_name] == 0:
                return 0.0 if self._allocated[resource_name] == 0 else float('inf')
            return self._allocated[resource_name] / self._resources[resource_name]
    
    def would_overcommit(self, resource_name: str, amount: float) -> bool:
        """
        Check if allocating an amount would cause overcommit.
        
        Args:
            resource_name: Name of the resource
            amount: Amount to check
            
        Returns:
            True if allocation would overcommit, False otherwise
            
        Raises:
            ValueError: If amount is negative or resource doesn't exist
        """
        if amount < 0:
            raise ValueError("Amount cannot be negative")
            
        if resource_name not in self._resources:
            raise ValueError(f"Unknown resource: {resource_name}")
        
        with self._lock:
            return self._allocated[resource_name] + amount > self._resources[resource_name]
    
    def get_available(self, resource_name: str) -> float:
        """
        Get available amount for a resource.
        
        Args:
            resource_name: Name of the resource
            
        Returns:
            Available amount of resource
            
        Raises:
            ValueError: If resource doesn't exist
        """
        if resource_name not in self._resources:
            raise ValueError(f"Unknown resource: {resource_name}")
            
        with self._lock:
            return self._resources[resource_name] - self._allocated[resource_name]


def main():
    """Self-test: exact quota arithmetic, overcommit refusal at the boundary,
    cross-user isolation, and no overcommit under thread contention."""
    a = BudgetAllocator([Resource("CPU", 100.0), Resource("Mem", 500.0),
                         Resource("Zero", 0.0)])

    # Exact ledger: 30 + 40 fit in 100; the next 40 must be REFUSED.
    assert a.allocate("u1", "CPU", 30.0) is True
    assert a.allocate("u2", "CPU", 40.0) is True
    assert a.allocate("u3", "CPU", 40.0) is False, "70+40 overcommitted a 100-capacity resource"
    assert a.get_total_allocated("CPU") == 70.0
    assert a.get_utilization("CPU") == 0.7, f"70/100 must be 0.7, got {a.get_utilization('CPU')}"
    assert a.get_available("CPU") == 30.0

    # Boundary is inclusive: exactly-full is allowed, one unit past is not.
    assert a.would_overcommit("CPU", 30.0) is False, "filling to exactly capacity flagged"
    assert a.would_overcommit("CPU", 31.0) is True, "capacity+1 not flagged"

    # Release honesty: only what you hold, only from your own quota.
    assert a.release("u1", "CPU", 10.0) is True
    assert a.release("u1", "CPU", 50.0) is False, "released more than the user held"
    assert a.release("u3", "CPU", 10.0) is False, "u3 released resources it never held"
    assert a.get_allocation("u1", "CPU") == 20.0
    assert a.get_total_allocated("CPU") == 60.0

    # Zero-capacity resource: utilization defined as 0.0, allocation impossible.
    assert a.get_utilization("Zero") == 0.0
    assert a.allocate("u1", "Zero", 1.0) is False

    # Refusals.
    for call in (lambda: a.allocate("u", "CPU", -1.0),
                 lambda: a.allocate("u", "GPU", 1.0),
                 lambda: a.release("u", "GPU", 1.0),
                 lambda: a.would_overcommit("CPU", -5.0),
                 lambda: BudgetAllocator([Resource("bad", -1.0)])):
        try:
            call()
            assert False, "invalid call accepted"
        except ValueError:
            pass

    # THE DISASTER: racing allocators must never overshoot capacity.
    # 8 threads try 100 x 1.0 units of Mem (cap 500): exactly 500 must win.
    wins = []
    def _grab(uid: str) -> None:
        got = sum(1 for _ in range(100) if a.allocate(uid, "Mem", 1.0))
        wins.append(got)
    threads = [threading.Thread(target=_grab, args=(f"w{i}",)) for i in range(8)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    assert sum(wins) == 500, f"race granted {sum(wins)} units of a 500-cap resource"
    assert a.get_total_allocated("Mem") == 500.0
    assert a.would_overcommit("Mem", 1.0) is True

    print("resource_budget_allocator: ledger exact (70→60), boundary inclusive, "
          "cross-user release refused, race granted 500/500 — PASS")


if __name__ == "__main__":
    main()