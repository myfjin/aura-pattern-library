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


def _brute_force_sat(clauses_spec, n_vars):
    """Exhaustive truth-table oracle: is the formula satisfiable at all?"""
    from itertools import product
    for bits in product([False, True], repeat=n_vars):
        assignment = {v + 1: bits[v] for v in range(n_vars)}
        if all(any(assignment[var] == pol for var, pol in clause)
               for clause in clauses_spec):
            return True
    return False


def _build(clauses_spec):
    return Formula([Clause([Literal(v, p) for v, p in c]) for c in clauses_spec])


def main():
    """Self-test: known SAT/UNSAT verdicts exact, unit propagation forced
    assignments checked, 60 random formulas vs a truth-table oracle."""
    # (A∨B) ∧ (¬A∨C) ∧ (¬B∨¬C): satisfiable, and the model must satisfy it.
    f1 = _build([[(1, True), (2, True)], [(1, False), (3, True)],
                 [(2, False), (3, False)]])
    m1 = solve_sat(f1)
    assert m1 is not None, "satisfiable formula reported UNSAT"
    assert f1.is_satisfied(m1), "returned model does not satisfy the formula"

    # (A) ∧ (¬A): the canonical contradiction must be UNSAT.
    f2 = _build([[(1, True)], [(1, False)]])
    assert solve_sat(f2) is None, "A AND NOT-A reported satisfiable"

    # Unit-propagation chain (A) ∧ (¬A∨B) ∧ (¬B∨C): forces A=B=C=True.
    f3 = _build([[(1, True)], [(1, False), (2, True)], [(2, False), (3, True)]])
    m3 = solve_sat(f3)
    assert m3 is not None and f3.is_satisfied(m3)
    assert m3[1] is True and m3[2] is True and m3[3] is True, \
        f"unit propagation must force all True, got {m3}"

    # A bigger planted UNSAT: all 8 clauses over 3 vars (every assignment killed).
    from itertools import product as _prod
    all_clauses = [[(1, a), (2, b), (3, c)] for a, b, c in
                   _prod([True, False], repeat=3)]
    assert solve_sat(_build(all_clauses)) is None, \
        "complete 3-var clause set is UNSAT by construction"

    # ORACLE FUZZ: 60 random 3-CNF formulas over 5 vars; the solver's verdict
    # must match the truth table, and every SAT model must check out.
    import random
    random.seed(42)
    sat_seen = unsat_seen = 0
    for _ in range(60):
        spec = [[(random.randint(1, 5), random.random() < 0.5) for _ in range(3)]
                for _ in range(random.randint(3, 12))]
        verdict_true = _brute_force_sat(spec, 5)
        model = solve_sat(_build(spec))
        if verdict_true:
            assert model is not None, f"solver missed a satisfiable formula: {spec}"
            assert _build(spec).is_satisfied(model), "solver returned a non-model"
            sat_seen += 1
        else:
            assert model is None, f"solver 'solved' an UNSAT formula: {spec}"
            unsat_seen += 1
    assert sat_seen + unsat_seen == 60
    assert sat_seen > 0 and unsat_seen > 0, \
        f"fuzz must exercise both verdicts (sat {sat_seen}, unsat {unsat_seen})"

    print(f"sat_solver: known SAT/UNSAT exact, propagation forces T/T/T, "
          f"60/60 oracle verdicts agree ({sat_seen} sat, {unsat_seen} unsat) — PASS")


if __name__ == "__main__":
    main()