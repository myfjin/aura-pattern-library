#!/usr/bin/env python3

"""
Dependency Graph Resolver - Topological Sort Implementation

This module provides a dependency graph resolver that can:
- Detect circular dependencies
- Perform topological sorting
- Group tasks into parallel execution levels
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

from typing import Dict, List, Set, Optional, Tuple, Any, Union
from collections import defaultdict, deque
import sys


class Node:
    """Represents a node in the dependency graph."""
    
    def __init__(self, name: str, data: Any = None):
        """
        Initialize a node.
        
        Args:
            name: Unique identifier for the node
            data: Optional data associated with the node
        """
        self.name = name
        self.data = data
        self.dependencies: Set[str] = set()
        self.dependents: Set[str] = set()
    
    def add_dependency(self, dependency_name: str) -> None:
        """
        Add a dependency to this node.
        
        Args:
            dependency_name: Name of the dependency node
        """
        self.dependencies.add(dependency_name)
    
    def add_dependent(self, dependent_name: str) -> None:
        """
        Add a dependent to this node.
        
        Args:
            dependent_name: Name of the dependent node
        """
        self.dependents.add(dependent_name)
    
    def __repr__(self) -> str:
        return f"Node(name='{self.name}', dependencies={self.dependencies}, dependents={self.dependents})"


class DependencyGraph:
    """A directed acyclic graph for managing task dependencies."""
    
    def __init__(self):
        """Initialize an empty dependency graph."""
        self.nodes: Dict[str, Node] = {}
        self._cached_levels: Optional[List[List[str]]] = None
    
    def add_node(self, name: str, data: Any = None) -> Node:
        """
        Add a node to the graph.
        
        Args:
            name: Unique identifier for the node
            data: Optional data associated with the node
            
        Returns:
            The created node
            
        Raises:
            ValueError: If a node with the same name already exists
        """
        if name in self.nodes:
            raise ValueError(f"Node '{name}' already exists in the graph")
        
        node = Node(name, data)
        self.nodes[name] = node
        self._cached_levels = None  # Invalidate cache
        return node
    
    def get_node(self, name: str) -> Node:
        """
        Get a node by name.
        
        Args:
            name: Name of the node to retrieve
            
        Returns:
            The requested node
            
        Raises:
            KeyError: If the node doesn't exist
        """
        return self.nodes[name]
    
    def add_dependency(self, dependent: str, dependency: str) -> None:
        """
        Add a dependency relationship between two nodes.
        
        Args:
            dependent: Name of the node that depends on another
            dependency: Name of the node being depended on
            
        Raises:
            KeyError: If either node doesn't exist
            ValueError: If adding this dependency would create a cycle
        """
        if dependent not in self.nodes:
            raise KeyError(f"Node '{dependent}' not found in graph")
        if dependency not in self.nodes:
            raise KeyError(f"Node '{dependency}' not found in graph")
        
        # Temporarily add the dependency to check for cycles
        self.nodes[dependent].add_dependency(dependency)
        self.nodes[dependency].add_dependent(dependent)
        
        # Check if this creates a cycle
        if self._has_cycle():
            # Rollback the changes
            self.nodes[dependent].dependencies.remove(dependency)
            self.nodes[dependency].dependents.remove(dependent)
            raise ValueError(f"Adding dependency from '{dependent}' to '{dependency}' would create a cycle")
        
        self._cached_levels = None  # Invalidate cache
    
    def _has_cycle(self) -> bool:
        """
        Check if the graph contains a cycle using DFS.
        
        Returns:
            True if a cycle exists, False otherwise
        """
        visiting: Set[str] = set()
        visited: Set[str] = set()
        
        def dfs(node_name: str) -> bool:
            if node_name in visiting:
                return True  # Cycle detected
            if node_name in visited:
                return False  # Already processed
            
            visiting.add(node_name)
            for dep_name in self.nodes[node_name].dependencies:
                if dfs(dep_name):
                    return True
            visiting.remove(node_name)
            visited.add(node_name)
            return False
        
        for node_name in self.nodes:
            if node_name not in visited:
                if dfs(node_name):
                    return True
        return False
    
    def topological_sort(self) -> List[str]:
        """
        Perform a topological sort of the graph using Kahn's algorithm.
        
        Returns:
            List of node names in topological order
            
        Raises:
            ValueError: If the graph contains cycles
        """
        if self._has_cycle():
            raise ValueError("Cannot perform topological sort: graph contains cycles")
        
        # Calculate in-degrees
        in_degree: Dict[str, int] = {name: 0 for name in self.nodes}
        for node in self.nodes.values():
            for dep in node.dependencies:
                in_degree[dep] += 1
        
        # Initialize queue with nodes having zero in-degree
        queue: deque = deque([name for name, degree in in_degree.items() if degree == 0])
        result: List[str] = []
        
        while queue:
            current = queue.popleft()
            result.append(current)
            
            # Reduce in-degree for all dependents
            for dependent_name in self.nodes[current].dependents:
                in_degree[dependent_name] -= 1
                if in_degree[dependent_name] == 0:
                    queue.append(dependent_name)
        
        # Check if all nodes were processed (graph is acyclic)
        if len(result) != len(self.nodes):
            raise ValueError("Graph contains cycles")
        
        return result
    
    def get_parallel_levels(self) -> List[List[str]]:
        """
        Group nodes into levels that can be executed in parallel.
        
        Returns:
            List of lists, where each inner list contains node names that can be executed in parallel
            
        Raises:
            ValueError: If the graph contains cycles
        """
        if self._cached_levels is not None:
            return self._cached_levels
            
        if self._has_cycle():
            raise ValueError("Cannot determine parallel levels: graph contains cycles")
        
        # Calculate in-degrees
        in_degree: Dict[str, int] = {name: 0 for name in self.nodes}
        for node in self.nodes.values():
            for dep in node.dependencies:
                in_degree[dep] += 1
        
        levels: List[List[str]] = []
        current_level: List[str] = [name for name, degree in in_degree.items() if degree == 0]
        
        while current_level:
            levels.append(current_level[:])  # Add a copy of current level
            
            next_level: List[str] = []
            # Process all nodes in current level
            for node_name in current_level:
                # Reduce in-degree for all dependents
                for dependent_name in self.nodes[node_name].dependents:
                    in_degree[dependent_name] -= 1
                    if in_degree[dependent_name] == 0:
                        next_level.append(dependent_name)
            
            current_level = next_level
        
        self._cached_levels = levels
        return levels
    
    def get_node_data(self, name: str) -> Any:
        """
        Get the data associated with a node.
        
        Args:
            name: Name of the node
            
        Returns:
            Data associated with the node
        """
        return self.nodes[name].data
    
    def __len__(self) -> int:
        """Return the number of nodes in the graph."""
        return len(self.nodes)
    
    def __contains__(self, name: str) -> bool:
        """Check if a node exists in the graph."""
        return name in self.nodes


def main():
    """Demo of the dependency graph resolver with 10 interdependent tasks."""
    print("Dependency Graph Resolver Demo")
    print("=" * 40)
    
    # Create a dependency graph
    graph = DependencyGraph()
    
    # Add 10 tasks
    tasks = [
        ("task_a", "Initialize system"),
        ("task_b", "Load configuration"),
        ("task_c", "Connect to database"),
        ("task_d", "Start web server"),
        ("task_e", "Load plugins"),
        ("task_f", "Initialize cache"),
        ("task_g", "Setup logging"),
        ("task_h", "Validate environment"),
        ("task_i", "Run migrations"),
        ("task_j", "Start background workers")
    ]
    
    for task_name, task_desc in tasks:
        graph.add_node(task_name, task_desc)
    
    # Add dependencies (creating a complex dependency structure)
    dependencies = [
        ("task_b", "task_a"),  # B depends on A
        ("task_c", "task_a"),  # C depends on A
        ("task_d", "task_b"),  # D depends on B
        ("task_e", "task_b"),  # E depends on B
        ("task_f", "task_c"),  # F depends on C
        ("task_g", "task_a"),  # G depends on A
        ("task_h", "task_a"),  # H depends on A
        ("task_i", "task_c"),  # I depends on C
        ("task_j", "task_d"),  # J depends on D
        ("task_j", "task_e"),  # J also depends on E
        ("task_d", "task_f"),  # D also depends on F
        ("task_e", "task_g"),  # E also depends on G
    ]
    
    print("Adding dependencies:")
    for dependent, dependency in dependencies:
        try:
            graph.add_dependency(dependent, dependency)
            print(f"  {dependent} <- {dependency}")
        except ValueError as e:
            print(f"  Error adding {dependent} <- {dependency}: {e}")
    
    print(f"\nGraph has {len(graph)} nodes")
    
    # Perform topological sort
    print("\nTopological order:")
    try:
        order = graph.topological_sort()
        for i, task in enumerate(order, 1):
            desc = graph.get_node_data(task)
            print(f"  {i:2d}. {task} - {desc}")
    except ValueError as e:
        print(f"Error: {e}")
    
    # Get parallel execution levels
    print("\nParallel execution levels:")
    try:
        levels = graph.get_parallel_levels()
        for i, level in enumerate(levels, 1):
            print(f"  Level {i}: {level}")
            for task in level:
                desc = graph.get_node_data(task)
                print(f"    - {task}: {desc}")
    except ValueError as e:
        print(f"Error: {e}")
    
    # Demonstrate cycle detection
    print("\nTesting cycle detection:")
    graph2 = DependencyGraph()
    graph2.add_node("x")
    graph2.add_node("y")
    graph2.add_node("z")
    
    graph2.add_dependency("y", "x")  # y depends on x
    graph2.add_dependency("z", "y")  # z depends on y
    
    try:
        graph2.add_dependency("x", "z")  # x depends on z - would create cycle
        print("ERROR: Cycle was not detected!")
    except ValueError as e:
        print(f"  Cycle correctly detected: {e}")


if __name__ == "__main__":
    main()