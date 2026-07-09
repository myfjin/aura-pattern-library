"""
Bayesian Belief Network Implementation

This module provides a complete implementation of a Bayesian Belief Network
with support for conditional probability tables, inference by enumeration,
and conditional probability queries.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

from typing import Dict, List, Tuple, Set, Any, Optional, Union
from collections import defaultdict
import itertools
import math


class CPT:
    """
    Conditional Probability Table for a Bayesian Network Node.
    
    Represents P(Node | Parents) where parents are other nodes in the network.
    """
    
    def __init__(self, node_name: str, parent_names: List[str]):
        """
        Initialize a CPT.
        
        Args:
            node_name: Name of the node this CPT belongs to
            parent_names: List of parent node names
        """
        self.node_name = node_name
        self.parent_names = parent_names
        self.probabilities: Dict[Tuple[Any, ...], Dict[Any, float]] = {}
    
    def add_entry(self, parent_values: Tuple[Any, ...], node_value: Any, probability: float) -> None:
        """
        Add a probability entry to the CPT.
        
        Args:
            parent_values: Tuple of parent values (must match parent_names order)
            node_value: Value of the node
            probability: Conditional probability P(node_value | parent_values)
        """
        if len(parent_values) != len(self.parent_names):
            raise ValueError("Number of parent values must match number of parents")
        
        if parent_values not in self.probabilities:
            self.probabilities[parent_values] = {}
        
        self.probabilities[parent_values][node_value] = probability
    
    def get_probability(self, parent_values: Tuple[Any, ...], node_value: Any) -> float:
        """
        Get the conditional probability for given parent values and node value.
        
        Args:
            parent_values: Tuple of parent values
            node_value: Value of the node
            
        Returns:
            Conditional probability P(node_value | parent_values)
        """
        if parent_values not in self.probabilities:
            raise ValueError(f"No probability entry for parent values {parent_values}")
        
        if node_value not in self.probabilities[parent_values]:
            raise ValueError(f"No probability for node value {node_value} given parents {parent_values}")
        
        return self.probabilities[parent_values][node_value]
    
    def validate(self) -> bool:
        """
        Validate that all probability distributions sum to 1.
        
        Returns:
            True if all distributions are valid
        """
        for parent_values, node_probs in self.probabilities.items():
            total = sum(node_probs.values())
            if not math.isclose(total, 1.0, abs_tol=1e-9):
                return False
        return True


class Node:
    """
    Node in a Bayesian Belief Network.
    
    Represents a random variable with possible values and conditional dependencies.
    """
    
    def __init__(self, name: str, values: List[Any]):
        """
        Initialize a node.
        
        Args:
            name: Unique identifier for the node
            values: List of possible values the node can take
        """
        self.name = name
        self.values = values
        self.parents: List['Node'] = []
        self.children: List['Node'] = []
        self.cpt: Optional[CPT] = None
    
    def add_parent(self, parent: 'Node') -> None:
        """Add a parent node."""
        if parent not in self.parents:
            self.parents.append(parent)
    
    def add_child(self, child: 'Node') -> None:
        """Add a child node."""
        if child not in self.children:
            self.children.append(child)
    
    def set_cpt(self, cpt: CPT) -> None:
        """Set the conditional probability table for this node."""
        self.cpt = cpt
    
    def get_parent_values(self, assignment: Dict[str, Any]) -> Tuple[Any, ...]:
        """
        Get parent values from an assignment.
        
        Args:
            assignment: Dictionary mapping node names to values
            
        Returns:
            Tuple of parent values in order of parent_names in CPT
        """
        if not self.cpt:
            raise ValueError("CPT not set for this node")
        
        return tuple(assignment[parent_name] for parent_name in self.cpt.parent_names)


class BayesianNetwork:
    """
    Bayesian Belief Network implementation.
    
    Supports construction of networks, probability calculations, and inference.
    """
    
    def __init__(self):
        """Initialize an empty Bayesian network."""
        self.nodes: Dict[str, Node] = {}
        self.node_order: List[str] = []
    
    def add_node(self, node: Node) -> None:
        """
        Add a node to the network.
        
        Args:
            node: Node to add
        """
        if node.name in self.nodes:
            raise ValueError(f"Node {node.name} already exists in network")
        
        self.nodes[node.name] = node
        self.node_order.append(node.name)
    
    def add_edge(self, parent_name: str, child_name: str) -> None:
        """
        Add a directed edge from parent to child.
        
        Args:
            parent_name: Name of parent node
            child_name: Name of child node
        """
        if parent_name not in self.nodes:
            raise ValueError(f"Parent node {parent_name} not found")
        
        if child_name not in self.nodes:
            raise ValueError(f"Child node {child_name} not found")
        
        parent = self.nodes[parent_name]
        child = self.nodes[child_name]
        
        parent.add_child(child)
        child.add_parent(parent)
    
    def set_cpt(self, node_name: str, cpt: CPT) -> None:
        """
        Set the CPT for a node.
        
        Args:
            node_name: Name of the node
            cpt: Conditional probability table
        """
        if node_name not in self.nodes:
            raise ValueError(f"Node {node_name} not found")
        
        # Validate CPT matches node
        node = self.nodes[node_name]
        if cpt.node_name != node_name:
            raise ValueError("CPT node name doesn't match node")
        
        parent_names = [parent.name for parent in node.parents]
        if set(cpt.parent_names) != set(parent_names):
            raise ValueError("CPT parent names don't match node's parents")
        
        # Validate CPT
        if not cpt.validate():
            raise ValueError("CPT probabilities don't sum to 1")
        
        node.set_cpt(cpt)
    
    def get_node(self, name: str) -> Node:
        """
        Get a node by name.
        
        Args:
            name: Name of the node
            
        Returns:
            The node with the given name
        """
        if name not in self.nodes:
            raise ValueError(f"Node {name} not found")
        return self.nodes[name]
    
    def joint_probability(self, assignment: Dict[str, Any]) -> float:
        """
        Calculate the joint probability of an assignment.
        
        Args:
            assignment: Dictionary mapping node names to values
            
        Returns:
            Joint probability P(assignment)
        """
        # Validate assignment
        for node_name in self.nodes:
            if node_name not in assignment:
                raise ValueError(f"Assignment missing value for node {node_name}")
        
        probability = 1.0
        for node_name in self.node_order:
            node = self.nodes[node_name]
            if not node.cpt:
                raise ValueError(f"Node {node_name} has no CPT")
            
            parent_values = node.get_parent_values(assignment)
            node_value = assignment[node_name]
            probability *= node.cpt.get_probability(parent_values, node_value)
        
        return probability
    
    def _enumerate_all(self, vars_order: List[str], e: Dict[str, Any]) -> float:
        """
        Enumerate all possible assignments to compute probability.
        
        Args:
            vars_order: Ordered list of variable names
            e: Evidence (partial assignment)
            
        Returns:
            Sum of probabilities for all consistent assignments
        """
        if not vars_order:
            return 1.0
        
        first_var = vars_order[0]
        rest_vars = vars_order[1:]
        
        node = self.nodes[first_var]
        
        if first_var in e:
            # Variable is in evidence
            if not node.cpt:
                raise ValueError(f"Node {first_var} has no CPT")
            
            parent_values = node.get_parent_values(e)
            prob = node.cpt.get_probability(parent_values, e[first_var])
            return prob * self._enumerate_all(rest_vars, e)
        else:
            # Sum over all possible values
            total = 0.0
            for value in node.values:
                new_e = e.copy()
                new_e[first_var] = value
                if not node.cpt:
                    raise ValueError(f"Node {first_var} has no CPT")
                
                parent_values = node.get_parent_values(new_e)
                prob = node.cpt.get_probability(parent_values, value)
                total += prob * self._enumerate_all(rest_vars, new_e)
            
            return total
    
    def inference_by_enumeration(self, query: Dict[str, Any], evidence: Dict[str, Any]) -> float:
        """
        Perform inference using enumeration algorithm.
        
        Args:
            query: Variables and values to query
            evidence: Observed evidence variables and values
            
        Returns:
            Conditional probability P(query | evidence)
        """
        # Combine evidence and query for numerator calculation
        combined = {**evidence, **query}
        
        # Calculate numerator: P(query, evidence)
        numerator = self._enumerate_all(self.node_order, combined)
        
        # Calculate denominator: P(evidence)
        denominator = self._enumerate_all(self.node_order, evidence)
        
        if denominator == 0:
            raise ValueError("Evidence has zero probability")
        
        return numerator / denominator
    
    def conditional_probability(self, query: Dict[str, Any], evidence: Dict[str, Any]) -> float:
        """
        Calculate conditional probability P(query | evidence).
        
        Args:
            query: Variables and values to query
            evidence: Observed evidence variables and values
            
        Returns:
            Conditional probability P(query | evidence)
        """
        return self.inference_by_enumeration(query, evidence)


def create_sample_network() -> BayesianNetwork:
    """
    Create a sample Bayesian network for testing.
    
    Network structure:
    Cloudy -> Sprinkler
    Cloudy -> Rain
    Sprinkler, Rain -> WetGrass
    """
    # Create network
    bn = BayesianNetwork()
    
    # Create nodes
    cloudy = Node("Cloudy", [True, False])
    sprinkler = Node("Sprinkler", [True, False])
    rain = Node("Rain", [True, False])
    wet_grass = Node("WetGrass", [True, False])
    
    # Add nodes to network
    bn.add_node(cloudy)
    bn.add_node(sprinkler)
    bn.add_node(rain)
    bn.add_node(wet_grass)
    
    # Add edges
    bn.add_edge("Cloudy", "Sprinkler")
    bn.add_edge("Cloudy", "Rain")
    bn.add_edge("Sprinkler", "WetGrass")
    bn.add_edge("Rain", "WetGrass")
    
    # Create CPTs
    # P(Cloudy)
    cpt_cloudy = CPT("Cloudy", [])
    cpt_cloudy.add_entry((), True, 0.5)
    cpt_cloudy.add_entry((), False, 0.5)
    bn.set_cpt("Cloudy", cpt_cloudy)
    
    # P(Sprinkler | Cloudy)
    cpt_sprinkler = CPT("Sprinkler", ["Cloudy"])
    cpt_sprinkler.add_entry((True,), True, 0.1)
    cpt_sprinkler.add_entry((True,), False, 0.9)
    cpt_sprinkler.add_entry((False,), True, 0.5)
    cpt_sprinkler.add_entry((False,), False, 0.5)
    bn.set_cpt("Sprinkler", cpt_sprinkler)
    
    # P(Rain | Cloudy)
    cpt_rain = CPT("Rain", ["Cloudy"])
    cpt_rain.add_entry((True,), True, 0.8)
    cpt_rain.add_entry((True,), False, 0.2)
    cpt_rain.add_entry((False,), True, 0.2)
    cpt_rain.add_entry((False,), False, 0.8)
    bn.set_cpt("Rain", cpt_rain)
    
    # P(WetGrass | Sprinkler, Rain)
    cpt_wet_grass = CPT("WetGrass", ["Sprinkler", "Rain"])
    cpt_wet_grass.add_entry((True, True), True, 0.99)
    cpt_wet_grass.add_entry((True, True), False, 0.01)
    cpt_wet_grass.add_entry((True, False), True, 0.9)
    cpt_wet_grass.add_entry((True, False), False, 0.1)
    cpt_wet_grass.add_entry((False, True), True, 0.9)
    cpt_wet_grass.add_entry((False, True), False, 0.1)
    cpt_wet_grass.add_entry((False, False), True, 0.0)
    cpt_wet_grass.add_entry((False, False), False, 1.0)
    bn.set_cpt("WetGrass", cpt_wet_grass)
    
    return bn


def main():
    """Demo the Bayesian network implementation."""
    print("Bayesian Network Demo")
    print("=" * 30)
    
    # Create sample network
    bn = create_sample_network()
    
    # Test joint probability calculation
    print("\n1. Joint Probability Calculations:")
    assignments = [
        {"Cloudy": True, "Sprinkler": True, "Rain": True, "WetGrass": True},
        {"Cloudy": False, "Sprinkler": False, "Rain": False, "WetGrass": False},
        {"Cloudy": True, "Sprinkler": False, "Rain": True, "WetGrass": True}
    ]
    
    for i, assignment in enumerate(assignments, 1):
        try:
            prob = bn.joint_probability(assignment)
            print(f"   Assignment {i}: P({assignment}) = {prob:.6f}")
        except Exception as e:
            print(f"   Assignment {i}: Error - {e}")
    
    # Test conditional probability inference
    print("\n2. Conditional Probability Inference:")
    queries = [
        ({"WetGrass": True}, {"Rain": True}, "P(WetGrass=True | Rain=True)"),
        ({"WetGrass": True}, {"Rain": False}, "P(WetGrass=True | Rain=False)"),
        ({"Sprinkler": True}, {"Cloudy": True}, "P(Sprinkler=True | Cloudy=True)"),
        ({"Sprinkler": True}, {"Cloudy": False}, "P(Sprinkler=True | Cloudy=False)")
    ]
    
    for query_vars, evidence, description in queries:
        try:
            prob = bn.conditional_probability(query_vars, evidence)
            print(f"   {description} = {prob:.6f}")
        except Exception as e:
            print(f"   {description}: Error - {e}")
    
    # Test more complex inference
    print("\n3. Complex Inference:")
    try:
        # P(Cloudy=True | WetGrass=True)
        prob = bn.inference_by_enumeration(
            {"Cloudy": True}, 
            {"WetGrass": True}
        )
        print(f"   P(Cloudy=True | WetGrass=True) = {prob:.6f}")
        
        # P(Rain=True | WetGrass=True, Sprinkler=False)
        prob = bn.inference_by_enumeration(
            {"Rain": True}, 
            {"WetGrass": True, "Sprinkler": False}
        )
        print(f"   P(Rain=True | WetGrass=True, Sprinkler=False) = {prob:.6f}")
    except Exception as e:
        print(f"   Error in complex inference: {e}")
    
    print("\nDemo completed successfully!")


if __name__ == "__main__":
    main()