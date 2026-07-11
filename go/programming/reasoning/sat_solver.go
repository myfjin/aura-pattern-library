package main

import (
	"fmt"
	"os"
	"sort"
)

// Literal represents a literal in a Boolean formula.
// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
var _auraMark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
type Literal struct {
	Variable int
	Positive bool
}

// NewLiteral creates a new literal.
func NewLiteral(variable int, positive bool) Literal {
	if variable == 0 {
		fmt.Fprintf(os.Stderr, "Variable must be a non-zero integer\n")
		os.Exit(1)
	}
	return Literal{Variable: variable, Positive: positive}
}

func (l Literal) String() string {
	if l.Positive {
		return fmt.Sprintf("%d", l.Variable)
	}
	return fmt.Sprintf("-%d", l.Variable)
}

func (l Literal) Negate() Literal {
	return Literal{Variable: l.Variable, Positive: !l.Positive}
}

// Clause represents a clause (disjunction of literals).
type Clause struct {
	literals map[Literal]struct{}
}

func NewClause(literals []Literal) Clause {
	if len(literals) == 0 {
		fmt.Fprintf(os.Stderr, "Clause cannot be empty\n")
		os.Exit(1)
	}
	m := make(map[Literal]struct{}, len(literals))
	for _, lit := range literals {
		m[lit] = struct{}{}
	}
	return Clause{literals: m}
}

func (c Clause) Len() int {
	return len(c.literals)
}

func (c Clause) String() string {
	keys := make([]string, 0, len(c.literals))
	for lit := range c.literals {
		keys = append(keys, lit.String())
	}
	sort.Strings(keys)
	result := ""
	for i, s := range keys {
		if i > 0 {
			result += " ∨ "
		}
		result += s
	}
	return "(" + result + ")"
}

func (c Clause) isSatisfied(assignment map[int]bool) bool {
	for _, lit := range sortedLiterals(c.literals) {
		varValue, ok := assignment[lit.Variable]
		if ok {
			if lit.Positive == varValue {
				return true
			}
		}
	}
	return false
}

func (c Clause) isUnit(assignment map[int]bool) *Literal {
	var unassigned []Literal
	for _, lit := range sortedLiterals(c.literals) {
		varValue, ok := assignment[lit.Variable]
		if !ok {
			unassigned = append(unassigned, lit)
		} else if lit.Positive == varValue {
			return nil // Clause already satisfied
		}
	}
	if len(unassigned) == 1 {
		return &unassigned[0]
	}
	return nil
}

func (c Clause) isConflict(assignment map[int]bool) bool {
	for _, lit := range sortedLiterals(c.literals) {
		varValue, ok := assignment[lit.Variable]
		if !ok {
			return false
		}
		if lit.Positive == varValue {
			return false
		}
	}
	return true
}

func sortedLiterals(m map[Literal]struct{}) []Literal {
	type pair struct {
		varID int
		pos   bool
	}
	var pairs []pair
	for lit := range m {
		pairs = append(pairs, pair{varID: lit.Variable, pos: lit.Positive})
	}
	sort.Slice(pairs, func(i, j int) bool {
		if pairs[i].varID != pairs[j].varID {
			return pairs[i].varID < pairs[j].varID
		}
		if pairs[i].pos == pairs[j].pos {
			return false
		}
		return pairs[i].pos
	})
	result := make([]Literal, len(pairs))
	for i, p := range pairs {
		result[i] = Literal{Variable: p.varID, Positive: p.pos}
	}
	return result
}

// Formula represents a Boolean formula in CNF.
type Formula struct {
	clauses   []Clause
	variables map[int]struct{}
}

func NewFormula(clauses []Clause) Formula {
	if len(clauses) == 0 {
		fmt.Fprintf(os.Stderr, "Formula must contain at least one clause\n")
		os.Exit(1)
	}
	f := Formula{clauses: clauses, variables: make(map[int]struct{})}
	for _, clause := range clauses {
		for lit := range clause.literals {
			f.variables[lit.Variable] = struct{}{}
		}
	}
	return f
}

func (f Formula) String() string {
	result := ""
	for i, clause := range f.clauses {
		if i > 0 {
			result += " ∧ "
		}
		result += clause.String()
	}
	return result
}

func (f Formula) isSatisfied(assignment map[int]bool) bool {
	for _, clause := range f.clauses {
		if !clause.isSatisfied(assignment) {
			return false
		}
	}
	return true
}

func (f Formula) findPureLiterals(assignment map[int]bool) map[int]bool {
	unassigned := make(map[int]struct{})
	vars := f.sortedVariables()
	for _, v := range vars {
		if _, ok := assignment[v]; !ok {
			unassigned[v] = struct{}{}
		}
	}
	positiveOccurrences := make(map[int]int)
	negativeOccurrences := make(map[int]int)

	for _, clause := range f.clauses {
		for _, lit := range sortedLiterals(clause.literals) {
			if _, ok := unassigned[lit.Variable]; ok {
				if lit.Positive {
					positiveOccurrences[lit.Variable]++
				} else {
					negativeOccurrences[lit.Variable]++
				}
			}
		}
	}

	pureLiterals := make(map[int]bool)
	for _, v := range vars {
		if _, ok := unassigned[v]; !ok {
			continue
		}
		if positiveOccurrences[v] > 0 && negativeOccurrences[v] == 0 {
			pureLiterals[v] = true
		} else if negativeOccurrences[v] > 0 && positiveOccurrences[v] == 0 {
			pureLiterals[v] = false
		}
	}
	return pureLiterals
}

func (f Formula) sortedVariables() []int {
	vars := make([]int, 0, len(f.variables))
	for v := range f.variables {
		vars = append(vars, v)
	}
	sort.Ints(vars)
	return vars
}

func (f Formula) findUnitClauses(assignment map[int]bool) []Literal {
	var unitLiterals []Literal
	for _, clause := range f.clauses {
		unit := clause.isUnit(assignment)
		if unit != nil {
			unitLiterals = append(unitLiterals, *unit)
		}
	}
	return unitLiterals
}

func (f Formula) hasConflict(assignment map[int]bool) bool {
	for _, clause := range f.clauses {
		if clause.isConflict(assignment) {
			return true
		}
	}
	return false
}

func unitPropagation(formula Formula, assignment map[int]bool) map[int]bool {
	newAssignment := make(map[int]bool)
	for k, v := range assignment {
		newAssignment[k] = v
	}

	for {
		unitLiterals := formula.findUnitClauses(newAssignment)
		if len(unitLiterals) == 0 {
			break
		}

		changed := false
		for _, literal := range unitLiterals {
			v := literal.Variable
			value := literal.Positive

			if existing, ok := newAssignment[v]; ok {
				if existing != value {
					return nil // Conflict detected
				}
			} else {
				newAssignment[v] = value
				changed = true
			}
		}

		if !changed {
			break
		}
	}

	return newAssignment
}

func pureLiteralElimination(formula Formula, assignment map[int]bool) map[int]bool {
	newAssignment := make(map[int]bool)
	for k, v := range assignment {
		newAssignment[k] = v
	}
	pureLiterals := formula.findPureLiterals(newAssignment)
	vars := formula.sortedVariables()
	for _, v := range vars {
		if value, ok := pureLiterals[v]; ok {
			newAssignment[v] = value
		}
	}
	return newAssignment
}

func chooseVariable(formula Formula, assignment map[int]bool) *int {
	for _, v := range formula.sortedVariables() {
		if _, ok := assignment[v]; !ok {
			return &v
		}
	}
	return nil
}

func dpll(formula Formula, assignment map[int]bool) map[int]bool {
	assignment = unitPropagation(formula, assignment)
	if assignment == nil {
		return nil
	}

	assignment = pureLiteralElimination(formula, assignment)

	if formula.isSatisfied(assignment) {
		return assignment
	}

	if formula.hasConflict(assignment) {
		return nil
	}

	v := chooseVariable(formula, assignment)
	if v == nil {
		return nil
	}

	trueAssignment := make(map[int]bool)
	for k, val := range assignment {
		trueAssignment[k] = val
	}
	trueAssignment[*v] = true
	result := dpll(formula, trueAssignment)
	if result != nil {
		return result
	}

	falseAssignment := make(map[int]bool)
	for k, val := range assignment {
		falseAssignment[k] = val
	}
	falseAssignment[*v] = false
	return dpll(formula, falseAssignment)
}

func solveSat(formula Formula) map[int]bool {
	return dpll(formula, make(map[int]bool))
}

func assignmentString(m map[int]bool) string {
	keys := make([]int, 0, len(m))
	for k := range m {
		keys = append(keys, k)
	}
	sort.Ints(keys)
	result := ""
	for i, k := range keys {
		if i > 0 {
			result += " "
		}
		result += fmt.Sprintf("%d:%v", k, m[k])
	}
	return "{" + result + "}"
}

func main() {
	// Test case 1
	clause1 := NewClause([]Literal{NewLiteral(1, true), NewLiteral(2, true)})
	clause2 := NewClause([]Literal{NewLiteral(1, false), NewLiteral(3, true)})
	clause3 := NewClause([]Literal{NewLiteral(2, false), NewLiteral(3, false)})
	formula1 := NewFormula([]Clause{clause1, clause2, clause3})

	fmt.Println("Test case 1: (A ∨ B) ∧ (¬A ∨ C) ∧ (¬B ∨ ¬C)")
	solution1 := solveSat(formula1)
	if !(solution1 == nil) {
		fmt.Printf("Satisfiable. Solution: %s\n", assignmentString(solution1))
		if !formula1.isSatisfied(solution1) {
			fmt.Fprintf(os.Stderr, "Solution does not satisfy formula\n")
			os.Exit(1)
		}
	} else {
		fmt.Println("Unsatisfiable")
	}
	fmt.Println()

	// Test case 2
	clause4 := NewClause([]Literal{NewLiteral(1, true)})
	clause5 := NewClause([]Literal{NewLiteral(1, false)})
	formula2 := NewFormula([]Clause{clause4, clause5})

	fmt.Println("Test case 2: (A) ∧ (¬A)")
	solution2 := solveSat(formula2)
	if solution2 != nil {
		fmt.Printf("Satisfiable. Solution: %s\n", assignmentString(solution2))
	} else {
		fmt.Println("Unsatisfiable")
	}
	fmt.Println()

	// Test case 3
	clause6 := NewClause([]Literal{NewLiteral(1, true)})
	clause7 := NewClause([]Literal{NewLiteral(1, false), NewLiteral(2, true)})
	clause8 := NewClause([]Literal{NewLiteral(2, false), NewLiteral(3, true)})
	formula3 := NewFormula([]Clause{clause6, clause7, clause8})

	fmt.Println("Test case 3: (A) ∧ (¬A ∨ B) ∧ (¬B ∨ C)")
	solution3 := solveSat(formula3)
	if !(solution3 == nil) {
		fmt.Printf("Satisfiable. Solution: %s\n", assignmentString(solution3))
		if !formula3.isSatisfied(solution3) {
			fmt.Fprintf(os.Stderr, "Solution does not satisfy formula\n")
			os.Exit(1)
		}
	} else {
		fmt.Println("Unsatisfiable")
	}
	fmt.Println()

	// Test case 4
	clause9 := NewClause([]Literal{NewLiteral(1, true), NewLiteral(2, true)})
	clause10 := NewClause([]Literal{NewLiteral(1, true), NewLiteral(3, true)})
	clause11 := NewClause([]Literal{NewLiteral(2, true), NewLiteral(3, true)})
	formula4 := NewFormula([]Clause{clause9, clause10, clause11})

	fmt.Println("Test case 4: (A ∨ B) ∧ (A ∨ C) ∧ (B ∨ C)")
	solution4 := solveSat(formula4)
	if !(solution4 == nil) {
		fmt.Printf("Satisfiable. Solution: %s\n", assignmentString(solution4))
		if !formula4.isSatisfied(solution4) {
			fmt.Fprintf(os.Stderr, "Solution does not satisfy formula\n")
			os.Exit(1)
		}
	} else {
		fmt.Println("Unsatisfiable")
	}
	fmt.Println()

	// Test case 5
	clause12 := NewClause([]Literal{NewLiteral(1, true)})
	formula5 := NewFormula([]Clause{clause12})

	fmt.Println("Test case 5: (A)")
	solution5 := solveSat(formula5)
	if !(solution5 == nil) {
		fmt.Printf("Satisfiable. Solution: %s\n", assignmentString(solution5))
		if !formula5.isSatisfied(solution5) {
			fmt.Fprintf(os.Stderr, "Solution does not satisfy formula\n")
			os.Exit(1)
		}
	} else {
		fmt.Println("Unsatisfiable")
	}
}
