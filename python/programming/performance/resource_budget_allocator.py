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
    """Demo of the BudgetAllocator functionality."""
    # Create resources
    resources = [
        Resource("CPU", 100.0),
        Resource("Memory", 1024.0),
        Resource("Storage", 10000.0)
    ]
    
    # Create allocator
    allocator = BudgetAllocator(resources)
    
    # Test allocations
    print("=== Allocation Tests ===")
    success = allocator.allocate("user1", "CPU", 30.0)
    print(f"User1 allocates 30 CPU: {'Success' if success else 'Failed'}")
    
    success = allocator.allocate("user2", "CPU", 40.0)
    print(f"User2 allocates 40 CPU: {'Success' if success else 'Failed'}")
    
    success = allocator.allocate("user3", "CPU", 40.0)
    print(f"User3 allocates 40 CPU: {'Success' if success else 'Failed'}")  # Should fail
    
    # Check allocations
    print("\n=== Allocation Status ===")
    print(f"User1 CPU allocation: {allocator.get_allocation('user1', 'CPU')}")
    print(f"User2 CPU allocation: {allocator.get_allocation('user2', 'CPU')}")
    print(f"Total CPU allocated: {allocator.get_total_allocated('CPU')}")
    print(f"CPU utilization: {allocator.get_utilization('CPU'):.2%}")
    print(f"CPU available: {allocator.get_available('CPU')}")
    
    # Test release
    print("\n=== Release Tests ===")
    success = allocator.release("user1", "CPU", 10.0)
    print(f"User1 releases 10 CPU: {'Success' if success else 'Failed'}")
    
    success = allocator.release("user1", "CPU", 50.0)
    print(f"User1 releases 50 CPU: {'Success' if success else 'Failed'}")  # Should fail
    
    # Final status
    print("\n=== Final Status ===")
    print(f"User1 CPU allocation: {allocator.get_allocation('user1', 'CPU')}")
    print(f"Total CPU allocated: {allocator.get_total_allocated('CPU')}")
    print(f"CPU utilization: {allocator.get_utilization('CPU'):.2%}")
    print(f"CPU available: {allocator.get_available('CPU')}")
    
    # Test overcommit detection
    print("\n=== Overcommit Detection ===")
    overcommit = allocator.would_overcommit("CPU", 80.0)
    print(f"Would 80 CPU overcommit: {'Yes' if overcommit else 'No'}")
    
    overcommit = allocator.would_overcommit("Memory", 512.0)
    print(f"Would 512 Memory overcommit: {'Yes' if overcommit else 'No'}")


if __name__ == "__main__":
    main()