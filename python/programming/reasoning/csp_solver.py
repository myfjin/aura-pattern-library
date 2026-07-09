"""
Constraint Satisfaction Problem (CSP) Solver Module

This module implements a complete CSP solver with backtracking search and
arc consistency (AC-3) algorithm for constraint propagation.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

from typing import List, Dict, Set, Tuple, Callable, Optional, Any, Union
from collections import deque
import copy


class Variable:
    """
    Represents a variable in a CSP with a name and domain of possible values.
    """
    
    def __init__(self, name: str, domain: List[Any]):
        """
        Initialize a variable.
        
        Args:
            name: Unique identifier for the variable
            domain: List of possible values the variable can take
        """
        self.name = name
        self.domain = list(domain)
        self.original_domain = list(domain)
    
    def __repr__(self) -> str:
        return f"Variable({self.name}, {self.domain})"
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, Variable):
            return False
        return self.name == other.name
    
    def __hash__(self) -> int:
        return hash(self.name)


class Constraint:
    """
    Represents a constraint between variables in a CSP.
    """
    
    def __init__(self, variables: List[Variable], 
                 predicate: Callable[..., bool], 
                 description: str = ""):
        """
        Initialize a constraint.
        
        Args:
            variables: List of variables involved in this constraint
            predicate: Function that returns True if the constraint is satisfied
            description: Optional description of the constraint
        """
        self.variables = variables
        self.predicate = predicate
        self.description = description
    
    def is_satisfied(self, assignment: Dict[Variable, Any]) -> bool:
        """
        Check if the constraint is satisfied by the given assignment.
        
        Args:
            assignment: Dictionary mapping variables to their assigned values
            
        Returns:
            True if the constraint is satisfied, False otherwise
        """
        # Get values for all variables in this constraint
        values = []
        for var in self.variables:
            if var not in assignment:
                # If any variable is not assigned, we can't evaluate the constraint
                return True
            values.append(assignment[var])
        
        # Apply the predicate to check if constraint is satisfied
        try:
            return self.predicate(*values)
        except Exception:
            return False
    
    def involves(self, variable: Variable) -> bool:
        """
        Check if this constraint involves the given variable.
        
        Args:
            variable: Variable to check
            
        Returns:
            True if the constraint involves the variable, False otherwise
        """
        return variable in self.variables


class CSP:
    """
    Constraint Satisfaction Problem representation.
    """
    
    def __init__(self, variables: List[Variable], constraints: List[Constraint]):
        """
        Initialize a CSP.
        
        Args:
            variables: List of variables in the problem
            constraints: List of constraints that must be satisfied
        """
        self.variables = variables
        self.constraints = constraints
        self.variable_map = {var.name: var for var in variables}
    
    def is_consistent(self, assignment: Dict[Variable, Any]) -> bool:
        """
        Check if the given assignment is consistent with all constraints.
        
        Args:
            assignment: Dictionary mapping variables to their assigned values
            
        Returns:
            True if the assignment is consistent, False otherwise
        """
        for constraint in self.constraints:
            if not constraint.is_satisfied(assignment):
                return False
        return True
    
    def is_complete(self, assignment: Dict[Variable, Any]) -> bool:
        """
        Check if the assignment is complete (all variables assigned).
        
        Args:
            assignment: Dictionary mapping variables to their assigned values
            
        Returns:
            True if all variables are assigned, False otherwise
        """
        return len(assignment) == len(self.variables)
    
    def get_unassigned_variable(self, assignment: Dict[Variable, Any]) -> Optional[Variable]:
        """
        Get an unassigned variable using the minimum remaining values heuristic.
        
        Args:
            assignment: Current assignment of variables
            
        Returns:
            An unassigned variable, or None if all variables are assigned
        """
        unassigned = [var for var in self.variables if var not in assignment]
        if not unassigned:
            return None
        
        # Return variable with minimum remaining values
        return min(unassigned, key=lambda var: len(var.domain))
    
    def order_domain_values(self, variable: Variable, assignment: Dict[Variable, Any]) -> List[Any]:
        """
        Order domain values using the least constraining value heuristic.
        
        Args:
            variable: Variable to order domain values for
            assignment: Current assignment of variables
            
        Returns:
            List of domain values ordered by least constraining first
        """
        def count_conflicts(value):
            # Count how many values this choice would eliminate from other domains
            conflicts = 0
            temp_assignment = assignment.copy()
            temp_assignment[variable] = value
            
            for constraint in self.constraints:
                if constraint.involves(variable):
                    for other_var in constraint.variables:
                        if other_var != variable and other_var not in assignment:
                            for other_value in other_var.domain:
                                temp_assignment[other_var] = other_value
                                if not constraint.is_satisfied(temp_assignment):
                                    conflicts += 1
                                del temp_assignment[other_var]
            return conflicts
        
        return sorted(variable.domain, key=count_conflicts)
    
    def restore_domains(self):
        """Restore all variables to their original domains."""
        for var in self.variables:
            var.domain = list(var.original_domain)


class AC3Solver:
    """
    Arc consistency solver using the AC-3 algorithm.
    """
    
    @staticmethod
    def ac3(csp: CSP, assignment: Dict[Variable, Any] = None) -> bool:
        """
        Enforce arc consistency on the CSP.
        
        Args:
            csp: Constraint satisfaction problem
            assignment: Current partial assignment
            
        Returns:
            True if arc consistency is achieved, False if domain becomes empty
        """
        if assignment is None:
            assignment = {}
            
        # Create a queue of arcs (pairs of variables)
        queue = deque()
        
        # Add all arcs to the queue
        for constraint in csp.constraints:
            for i in range(len(constraint.variables)):
                for j in range(len(constraint.variables)):
                    if i != j:
                        queue.append((constraint.variables[i], constraint.variables[j]))
        
        # Process arcs until queue is empty
        while queue:
            xi, xj = queue.popleft()
            
            # Skip if either variable is already assigned
            if xi in assignment or xj in assignment:
                continue
                
            # Revise the domain of xi
            if AC3Solver._revise(csp, xi, xj, assignment):
                # If domain becomes empty, return False
                if not xi.domain:
                    return False
                    
                # Add related arcs back to queue
                for constraint in csp.constraints:
                    if constraint.involves(xi):
                        for var in constraint.variables:
                            if var != xi and var != xj and var not in assignment:
                                queue.append((var, xi))
        
        return True
    
    @staticmethod
    def _revise(csp: CSP, xi: Variable, xj: Variable, assignment: Dict[Variable, Any]) -> bool:
        """
        Revise the domain of xi based on constraints with xj.
        
        Args:
            csp: Constraint satisfaction problem
            xi: Variable whose domain to revise
            xj: Variable to check against
            assignment: Current partial assignment
            
        Returns:
            True if xi's domain was revised, False otherwise
        """
        revised = False
        
        # Find constraints involving both xi and xj
        relevant_constraints = [
            c for c in csp.constraints 
            if c.involves(xi) and c.involves(xj)
        ]
        
        # For each value in xi's domain
        for x in xi.domain[:]:  # Use slice to avoid modification during iteration
            # Check if there's a value in xj's domain that satisfies all constraints
            satisfies_all = False
            
            for y in xj.domain:
                # Test all relevant constraints
                temp_assignment = assignment.copy()
                temp_assignment[xi] = x
                temp_assignment[xj] = y
                
                all_satisfied = True
                for constraint in relevant_constraints:
                    if not constraint.is_satisfied(temp_assignment):
                        all_satisfied = False
                        break
                
                if all_satisfied:
                    satisfies_all = True
                    break
            
            # If no value in xj's domain works with this value of xi, remove it
            if not satisfies_all:
                xi.domain.remove(x)
                revised = True
                
        return revised


class BacktrackingSolver:
    """
    Backtracking solver with constraint propagation.
    """
    
    @staticmethod
    def solve(csp: CSP) -> Optional[Dict[Variable, Any]]:
        """
        Solve the CSP using backtracking search with arc consistency.
        
        Args:
            csp: Constraint satisfaction problem to solve
            
        Returns:
            A solution assignment or None if no solution exists
        """
        # Make a copy of the CSP to avoid modifying the original
        csp_copy = copy.deepcopy(csp)
        return BacktrackingSolver._backtrack(csp_copy, {})
    
    @staticmethod
    def _backtrack(csp: CSP, assignment: Dict[Variable, Any]) -> Optional[Dict[Variable, Any]]:
        """
        Recursive backtracking algorithm.
        
        Args:
            csp: Constraint satisfaction problem
            assignment: Current partial assignment
            
        Returns:
            A solution assignment or None if no solution exists
        """
        # If assignment is complete, return it
        if csp.is_complete(assignment):
            return assignment
        
        # Select an unassigned variable
        var = csp.get_unassigned_variable(assignment)
        if var is None:
            return None
            
        # Order domain values
        for value in csp.order_domain_values(var, assignment):
            # Create a copy of the assignment
            new_assignment = assignment.copy()
            new_assignment[var] = value
            
            # Check if the assignment is consistent
            if csp.is_consistent(new_assignment):
                # Create a temporary CSP with this assignment
                temp_csp = copy.deepcopy(csp)
                temp_assignment = new_assignment.copy()
                
                # Enforce arc consistency
                if AC3Solver.ac3(temp_csp, temp_assignment):
                    # Recursively solve
                    result = BacktrackingSolver._backtrack(temp_csp, temp_assignment)
                    if result is not None:
                        return result
        
        # No solution found with this path
        return None


def main():
    """Demo: Solve a simple map coloring problem."""
    
    # Define variables (regions) with domain (colors)
    variables = [
        Variable("WA", ["red", "green", "blue"]),
        Variable("NT", ["red", "green", "blue"]),
        Variable("SA", ["red", "green", "blue"]),
        Variable("Q", ["red", "green", "blue"]),
        Variable("NSW", ["red", "green", "blue"]),
        Variable("V", ["red", "green", "blue"]),
        Variable("T", ["red", "green", "blue"])
    ]
    
    # Define constraints (adjacent regions must have different colors)
    def not_equal(a, b):
        return a != b
    
    constraints = [
        Constraint([variables[0], variables[1]], not_equal, "WA != NT"),
        Constraint([variables[0], variables[2]], not_equal, "WA != SA"),
        Constraint([variables[1], variables[2]], not_equal, "NT != SA"),
        Constraint([variables[1], variables[3]], not_equal, "NT != Q"),
        Constraint([variables[2], variables[3]], not_equal, "SA != Q"),
        Constraint([variables[2], variables[4]], not_equal, "SA != NSW"),
        Constraint([variables[2], variables[5]], not_equal, "SA != V"),
        Constraint([variables[3], variables[4]], not_equal, "Q != NSW"),
        Constraint([variables[4], variables[5]], not_equal, "NSW != V")
    ]
    
    # Create CSP
    csp = CSP(variables, constraints)
    
    # Solve the CSP
    print("Solving map coloring problem...")
    solution = BacktrackingSolver.solve(csp)
    
    if solution:
        print("Solution found:")
        for var, value in solution.items():
            print(f"  {var.name}: {value}")
    else:
        print("No solution found")
    
    # Demo with a simple Sudoku-like problem
    print("\nSolving simple 2x2 Sudoku-like problem...")
    
    # Variables for a 2x2 grid
    grid_vars = []
    for i in range(2):
        for j in range(2):
            grid_vars.append(Variable(f"X{i}{j}", [1, 2]))
    
    # Constraints: all different in rows and columns
    sudoku_constraints = [
        Constraint([grid_vars[0], grid_vars[1]], not_equal, "Row 0"),
        Constraint([grid_vars[2], grid_vars[3]], not_equal, "Row 1"),
        Constraint([grid_vars[0], grid_vars[2]], not_equal, "Col 0"),
        Constraint([grid_vars[1], grid_vars[3]], not_equal, "Col 1")
    ]
    
    sudoku_csp = CSP(grid_vars, sudoku_constraints)
    sudoku_solution = BacktrackingSolver.solve(sudoku_csp)
    
    if sudoku_solution:
        print("Sudoku solution found:")
        for i in range(2):
            row = []
            for j in range(2):
                var_name = f"X{i}{j}"
                var = next(v for v in grid_vars if v.name == var_name)
                row.append(str(sudoku_solution[var]))
            print(f"  {' '.join(row)}")
    else:
        print("No Sudoku solution found")


if __name__ == "__main__":
    main()