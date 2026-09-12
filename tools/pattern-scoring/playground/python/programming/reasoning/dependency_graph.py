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
        
        # In-degree = number of prerequisites a node waits on. (The former
        # code incremented in_degree[dep] — counting DEPENDENTS — which
        # seeded the queue with sinks and made every non-trivial graph
        # report "contains cycles".)
        in_degree: Dict[str, int] = {name: len(node.dependencies)
                                     for name, node in self.nodes.items()}
        
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
        
        # In-degree = number of prerequisites a node waits on. (The former
        # code incremented in_degree[dep] — counting DEPENDENTS — which
        # seeded the queue with sinks and made every non-trivial graph
        # report "contains cycles".)
        in_degree: Dict[str, int] = {name: len(node.dependencies)
                                     for name, node in self.nodes.items()}
        
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
    """Self-test: the topological INVARIANT (every dependency precedes its
    dependent) verified edge-by-edge, parallel levels exact, cycles refused."""
    graph = DependencyGraph()
    for name in "abcdefghij":
        graph.add_node(f"task_{name}", f"work {name}")

    dependencies = [
        ("task_b", "task_a"), ("task_c", "task_a"), ("task_d", "task_b"),
        ("task_e", "task_b"), ("task_f", "task_c"), ("task_g", "task_a"),
        ("task_h", "task_a"), ("task_i", "task_c"), ("task_j", "task_d"),
        ("task_j", "task_e"), ("task_d", "task_f"), ("task_e", "task_g"),
    ]
    for dependent, dependency in dependencies:
        graph.add_dependency(dependent, dependency)
    assert len(graph) == 10 and "task_a" in graph and "ghost" not in graph

    # THE INVARIANT: in the topological order, every dependency comes
    # strictly before its dependent — checked for all 12 edges.
    order = graph.topological_sort()
    assert sorted(order) == sorted(f"task_{n}" for n in "abcdefghij"), \
        "topological sort lost or invented nodes"
    pos = {name: i for i, name in enumerate(order)}
    violations = [(d, dep) for d, dep in dependencies if pos[dep] >= pos[d]]
    assert violations == [], f"ordering violates dependencies: {violations}"
    assert pos["task_a"] == 0, "the only root must come first"

    # Parallel levels: level k = tasks whose longest chain from a root is k.
    levels = graph.get_parallel_levels()
    assert [sorted(l) for l in levels] == [
        ["task_a"],
        ["task_b", "task_c", "task_g", "task_h"],
        ["task_e", "task_f", "task_i"],
        ["task_d"],
        ["task_j"],
    ], f"parallel levels wrong: {[sorted(l) for l in levels]}"
    assert sum(len(l) for l in levels) == 10, "levels lost tasks"

    # Node data survives.
    assert graph.get_node_data("task_c") == "work c"

    # CYCLE: closing x→y→z back to x must be refused, leaving the graph usable.
    g2 = DependencyGraph()
    for n in "xyz":
        g2.add_node(n)
    g2.add_dependency("y", "x")
    g2.add_dependency("z", "y")
    try:
        g2.add_dependency("x", "z")
        assert False, "cycle x→z→y→x was accepted"
    except ValueError:
        pass
    assert g2.topological_sort() == ["x", "y", "z"], \
        "graph corrupted after the rejected cycle"

    # Self-dependency is the smallest cycle.
    try:
        g2.add_dependency("x", "x")
        assert False, "self-dependency accepted"
    except ValueError:
        pass

    # Unknown nodes refused.
    try:
        g2.add_dependency("x", "ghost")
        assert False, "dependency on a missing node accepted"
    except (ValueError, KeyError):
        pass

    print("dependency_graph: 12/12 edges respected in topo order, levels "
          "1/4/3/1/1 exact, cycle+self-dep refused, graph intact — PASS")


if __name__ == "__main__":
    main()