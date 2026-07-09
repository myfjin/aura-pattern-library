#!/usr/bin/env python3
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

from typing import List, Set, Dict, Optional, Tuple, Union
from collections import defaultdict
import copy


class Literal:
    """Represents a literal in a Boolean formula."""
    
    def __init__(self, variable: int, positive: bool = True):
        if not isinstance(variable, int) or variable == 0:
            raise ValueError("Variable must be a non-zero integer")
        self.variable = variable
        self.positive = positive
    
    def __eq__(self, other):
        if not isinstance(other, Literal):
            return False
        return self.variable == other.variable and self.positive == other.positive
    
    def __hash__(self):
        return hash((self.variable, self.positive))
    
    def __repr__(self):
        sign = "" if self.positive else "-"
        return f"{sign}{self.variable}"
    
    def negate(self) -> 'Literal':
        """Return the negation of this literal."""
        return Literal(self.variable, not self.positive)


class Clause:
    """Represents a clause (disjunction of literals) in a Boolean formula."""
    
    def __init__(self, literals: List[Literal]):
        if not literals:
            raise ValueError("Clause cannot be empty")
        self.literals = frozenset(literals)
    
    def __len__(self):
        return len(self.literals)
    
    def __repr__(self):
        literals_str = " ∨ ".join(str(lit) for lit in self.literals)
        return f"({literals_str})"
    
    def is_satisfied(self, assignment: Dict[int, bool]) -> bool:
        """Check if the clause is satisfied by the given assignment."""
        for literal in self.literals:
            var_value = assignment.get(literal.variable)
            if var_value is not None:
                if literal.positive == var_value:
                    return True
        return False
    
    def is_unit(self, assignment: Dict[int, bool]) -> Optional[Literal]:
        """Check if the clause is a unit clause and return the unassigned literal if so."""
        unassigned_literals = []
        for literal in self.literals:
            var_value = assignment.get(literal.variable)
            if var_value is None:
                unassigned_literals.append(literal)
            elif literal.positive == var_value:
                return None  # Clause is already satisfied
        if len(unassigned_literals) == 1:
            return unassigned_literals[0]
        return None
    
    def is_conflict(self, assignment: Dict[int, bool]) -> bool:
        """Check if the clause is in conflict (all literals assigned false)."""
        for literal in self.literals:
            var_value = assignment.get(literal.variable)
            if var_value is None:
                return False  # There's an unassigned literal
            if literal.positive == var_value:
                return False  # Clause is satisfied
        return True  # All literals are assigned false


class Formula:
    """Represents a Boolean formula in CNF (Conjunctive Normal Form)."""
    
    def __init__(self, clauses: List[Clause]):
        if not clauses:
            raise ValueError("Formula must contain at least one clause")
        self.clauses = clauses
        self.variables = self._extract_variables()
    
    def _extract_variables(self) -> Set[int]:
        """Extract all variables from the formula."""
        variables = set()
        for clause in self.clauses:
            for literal in clause.literals:
                variables.add(literal.variable)
        return variables
    
    def __repr__(self):
        clauses_str = " ∧ ".join(str(clause) for clause in self.clauses)
        return f"{clauses_str}"
    
    def is_satisfied(self, assignment: Dict[int, bool]) -> bool:
        """Check if the entire formula is satisfied by the given assignment."""
        return all(clause.is_satisfied(assignment) for clause in self.clauses)
    
    def find_pure_literals(self, assignment: Dict[int, bool]) -> Dict[int, bool]:
        """Find all pure literals in the formula with respect to the current assignment."""
        unassigned_vars = set(var for var in self.variables if var not in assignment)
        positive_occurrences = defaultdict(int)
        negative_occurrences = defaultdict(int)
        
        for clause in self.clauses:
            for literal in clause.literals:
                if literal.variable in unassigned_vars:
                    if literal.positive:
                        positive_occurrences[literal.variable] += 1
                    else:
                        negative_occurrences[literal.variable] += 1
        
        pure_literals = {}
        for var in unassigned_vars:
            if positive_occurrences[var] > 0 and negative_occurrences[var] == 0:
                pure_literals[var] = True
            elif negative_occurrences[var] > 0 and positive_occurrences[var] == 0:
                pure_literals[var] = False
        
        return pure_literals
    
    def find_unit_clauses(self, assignment: Dict[int, bool]) -> List[Literal]:
        """Find all unit clauses in the formula with respect to the current assignment."""
        unit_literals = []
        for clause in self.clauses:
            unit_literal = clause.is_unit(assignment)
            if unit_literal is not None:
                unit_literals.append(unit_literal)
        return unit_literals
    
    def has_conflict(self, assignment: Dict[int, bool]) -> bool:
        """Check if the formula has a conflict with the current assignment."""
        return any(clause.is_conflict(assignment) for clause in self.clauses)


def unit_propagation(formula: Formula, assignment: Dict[int, bool]) -> Optional[Dict[int, bool]]:
    """
    Perform unit propagation on the formula.
    
    Returns:
        Updated assignment if successful, None if conflict detected.
    """
    new_assignment = assignment.copy()
    
    while True:
        unit_literals = formula.find_unit_clauses(new_assignment)
        if not unit_literals:
            break
            
        changed = False
        for literal in unit_literals:
            var = literal.variable
            value = literal.positive
            
            if var in new_assignment:
                # Check for conflict
                if new_assignment[var] != value:
                    return None  # Conflict detected
            else:
                new_assignment[var] = value
                changed = True
        
        if not changed:
            break
    
    return new_assignment


def pure_literal_elimination(formula: Formula, assignment: Dict[int, bool]) -> Dict[int, bool]:
    """
    Perform pure literal elimination on the formula.
    
    Returns:
        Updated assignment with pure literals assigned.
    """
    new_assignment = assignment.copy()
    pure_literals = formula.find_pure_literals(new_assignment)
    
    for var, value in pure_literals.items():
        new_assignment[var] = value
    
    return new_assignment


def choose_variable(formula: Formula, assignment: Dict[int, bool]) -> Optional[int]:
    """Choose an unassigned variable to branch on."""
    for var in formula.variables:
        if var not in assignment:
            return var
    return None


def dpll(formula: Formula, assignment: Dict[int, bool]) -> Optional[Dict[int, bool]]:
    """
    DPLL algorithm for solving SAT problems.
    
    Returns:
        A satisfying assignment if the formula is satisfiable, None otherwise.
    """
    # Unit propagation
    assignment = unit_propagation(formula, assignment)
    if assignment is None:
        return None  # Conflict detected
    
    # Pure literal elimination
    assignment = pure_literal_elimination(formula, assignment)
    
    # Check if formula is satisfied
    if formula.is_satisfied(assignment):
        return assignment
    
    # Check for conflict
    if formula.has_conflict(assignment):
        return None
    
    # Choose variable to branch on
    var = choose_variable(formula, assignment)
    if var is None:
        # All variables assigned but formula not satisfied
        return None
    
    # Try assigning True to the variable
    true_assignment = assignment.copy()
    true_assignment[var] = True
    result = dpll(formula, true_assignment)
    if result is not None:
        return result
    
    # Try assigning False to the variable
    false_assignment = assignment.copy()
    false_assignment[var] = False
    return dpll(formula, false_assignment)


def solve_sat(formula: Formula) -> Optional[Dict[int, bool]]:
    """
    Solve the SAT problem for the given formula.
    
    Returns:
        A satisfying assignment if the formula is satisfiable, None otherwise.
    """
    return dpll(formula, {})


def main():
    """Demo of the SAT solver with several test cases."""
    
    # Test case 1: Satisfiable formula (A ∨ B) ∧ (¬A ∨ C) ∧ (¬B ∨ ¬C)
    # Solution: A=True, B=False, C=True
    clause1 = Clause([Literal(1, True), Literal(2, True)])    # (A ∨ B)
    clause2 = Clause([Literal(1, False), Literal(3, True)])   # (¬A ∨ C)
    clause3 = Clause([Literal(2, False), Literal(3, False)])  # (¬B ∨ ¬C)
    formula1 = Formula([clause1, clause2, clause3])
    
    print("Test case 1: (A ∨ B) ∧ (¬A ∨ C) ∧ (¬B ∨ ¬C)")
    solution1 = solve_sat(formula1)
    if solution1:
        print(f"Satisfiable. Solution: {solution1}")
        # Verify solution
        assert formula1.is_satisfied(solution1)
    else:
        print("Unsatisfiable")
    print()
    
    # Test case 2: Unsatisfiable formula (A) ∧ (¬A)
    clause4 = Clause([Literal(1, True)])   # (A)
    clause5 = Clause([Literal(1, False)])  # (¬A)
    formula2 = Formula([clause4, clause5])
    
    print("Test case 2: (A) ∧ (¬A)")
    solution2 = solve_sat(formula2)
    if solution2:
        print(f"Satisfiable. Solution: {solution2}")
    else:
        print("Unsatisfiable")
    print()
    
    # Test case 3: Satisfiable formula with unit propagation (A) ∧ (¬A ∨ B) ∧ (¬B ∨ C)
    clause6 = Clause([Literal(1, True)])           # (A)
    clause7 = Clause([Literal(1, False), Literal(2, True)])   # (¬A ∨ B)
    clause8 = Clause([Literal(2, False), Literal(3, True)])   # (¬B ∨ C)
    formula3 = Formula([clause6, clause7, clause8])
    
    print("Test case 3: (A) ∧ (¬A ∨ B) ∧ (¬B ∨ C)")
    solution3 = solve_sat(formula3)
    if solution3:
        print(f"Satisfiable. Solution: {solution3}")
        # Verify solution
        assert formula3.is_satisfied(solution3)
    else:
        print("Unsatisfiable")
    print()
    
    # Test case 4: Satisfiable formula with pure literals (A ∨ B) ∧ (A ∨ C) ∧ (B ∨ C)
    clause9 = Clause([Literal(1, True), Literal(2, True)])   # (A ∨ B)
    clause10 = Clause([Literal(1, True), Literal(3, True)])  # (A ∨ C)
    clause11 = Clause([Literal(2, True), Literal(3, True)])  # (B ∨ C)
    formula4 = Formula([clause9, clause10, clause11])
    
    print("Test case 4: (A ∨ B) ∧ (A ∨ C) ∧ (B ∨ C)")
    solution4 = solve_sat(formula4)
    if solution4:
        print(f"Satisfiable. Solution: {solution4}")
        # Verify solution
        assert formula4.is_satisfied(solution4)
    else:
        print("Unsatisfiable")
    print()
    
    # Test case 5: Single variable formula (A)
    clause12 = Clause([Literal(1, True)])  # (A)
    formula5 = Formula([clause12])
    
    print("Test case 5: (A)")
    solution5 = solve_sat(formula5)
    if solution5:
        print(f"Satisfiable. Solution: {solution5}")
        # Verify solution
        assert formula5.is_satisfied(solution5)
    else:
        print("Unsatisfiable")


if __name__ == "__main__":
    main()