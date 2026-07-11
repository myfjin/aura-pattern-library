// csp_solver: constraint satisfaction problem solver with backtracking and AC-3.
package main

import (
	"fmt"
	"os"
	"sort"
)

// Variable represents a CSP variable with a name and a domain of values.
// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
var _auraMark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
type Variable struct {
	Name   string
	Domain []interface{}
}

// NewVariable creates a variable with the given name and domain.
func NewVariable(name string, domain []interface{}) *Variable {
	d := make([]interface{}, len(domain))
	copy(d, domain)
	return &Variable{Name: name, Domain: d}
}

// equalValues reports whether two concrete domain values are equal.
func equalValues(a, b interface{}) bool {
	switch av := a.(type) {
	case string:
		bv, ok := b.(string)
		return ok && av == bv
	case int:
		bv, ok := b.(int)
		return ok && av == bv
	case float64:
		bv, ok := b.(float64)
		return ok && av == bv
	}
	return false
}

// removeValue removes the first occurrence of value from domain.
func removeValue(domain []interface{}, value interface{}) []interface{} {
	for i, v := range domain {
		if equalValues(v, value) {
			return append(domain[:i], domain[i+1:]...)
		}
	}
	return domain
}

// Constraint represents a constraint over a list of variables.
type Constraint struct {
	Variables []*Variable
	Predicate func(...interface{}) bool
	Desc      string
}

// IsSatisfied evaluates the constraint against the current assignment.
// Missing variables make the constraint trivially satisfied.
func (c *Constraint) IsSatisfied(assignment map[string]interface{}) (ok bool) {
	values := make([]interface{}, 0, len(c.Variables))
	for _, v := range c.Variables {
		val, assigned := assignment[v.Name]
		if !assigned {
			return true
		}
		values = append(values, val)
	}
	defer func() {
		if r := recover(); r != nil {
			ok = false
		}
	}()
	return c.Predicate(values...)
}

// Involves reports whether the constraint references variable.
func (c *Constraint) Involves(variable *Variable) bool {
	for _, v := range c.Variables {
		if v == variable {
			return true
		}
	}
	return false
}

// CSP holds variables and constraints.
type CSP struct {
	Variables   []*Variable
	Constraints []*Constraint
}

// IsConsistent reports whether the assignment satisfies every constraint.
func (csp *CSP) IsConsistent(assignment map[string]interface{}) bool {
	for _, c := range csp.Constraints {
		if !c.IsSatisfied(assignment) {
			return false
		}
	}
	return true
}

// IsComplete reports whether every variable is assigned.
func (csp *CSP) IsComplete(assignment map[string]interface{}) bool {
	return len(assignment) == len(csp.Variables)
}

// GetUnassignedVariable selects an unassigned variable using minimum remaining values.
func (csp *CSP) GetUnassignedVariable(state *SolverState, assignment map[string]interface{}) *Variable {
	var best *Variable
	bestLen := -1
	for _, v := range csp.Variables {
		if _, assigned := assignment[v.Name]; assigned {
			continue
		}
		domain := state.Domains[v.Name]
		if best == nil || len(domain) < bestLen {
			best = v
			bestLen = len(domain)
		}
	}
	return best
}

// OrderDomainValues returns domain values ordered by least constraining value heuristic.
func (csp *CSP) OrderDomainValues(state *SolverState, variable *Variable, assignment map[string]interface{}) []interface{} {
	domain := state.Domains[variable.Name]
	ordered := make([]interface{}, len(domain))
	copy(ordered, domain)
	sort.SliceStable(ordered, func(i, j int) bool {
		return countConflicts(csp, state, variable, ordered[i], assignment) < countConflicts(csp, state, variable, ordered[j], assignment)
	})
	return ordered
}

// countConflicts counts how many values the given choice would eliminate from other domains.
func countConflicts(csp *CSP, state *SolverState, variable *Variable, value interface{}, assignment map[string]interface{}) int {
	conflicts := 0
	temp := make(map[string]interface{}, len(assignment)+1)
	for k, v := range assignment {
		temp[k] = v
	}
	temp[variable.Name] = value

	for _, c := range csp.Constraints {
		if !c.Involves(variable) {
			continue
		}
		for _, other := range c.Variables {
			if other == variable {
				continue
			}
			if _, assigned := assignment[other.Name]; assigned {
				continue
			}
			for _, otherValue := range state.Domains[other.Name] {
				temp[other.Name] = otherValue
				if !c.IsSatisfied(temp) {
					conflicts++
				}
				delete(temp, other.Name)
			}
		}
	}
	return conflicts
}

// SolverState carries the mutable domains used during search.
type SolverState struct {
	CSP     *CSP
	Domains map[string][]interface{}
}

// Copy returns a deep copy of the current state.
func (s *SolverState) Copy() *SolverState {
	domains := make(map[string][]interface{}, len(s.Domains))
	for k, v := range s.Domains {
		cp := make([]interface{}, len(v))
		copy(cp, v)
		domains[k] = cp
	}
	return &SolverState{CSP: s.CSP, Domains: domains}
}

// NewSolverState creates an initial state from a CSP.
func NewSolverState(csp *CSP) *SolverState {
	domains := make(map[string][]interface{}, len(csp.Variables))
	for _, v := range csp.Variables {
		cp := make([]interface{}, len(v.Domain))
		copy(cp, v.Domain)
		domains[v.Name] = cp
	}
	return &SolverState{CSP: csp, Domains: domains}
}

// AC3Solver enforces arc consistency.
type AC3Solver struct{}

// AC3 reduces domains; returns false if any domain becomes empty.
func (ac *AC3Solver) AC3(state *SolverState, assignment map[string]interface{}) bool {
	varMap := make(map[string]*Variable, len(state.CSP.Variables))
	for _, v := range state.CSP.Variables {
		varMap[v.Name] = v
	}

	type arc struct{ xi, xj string }
	queue := make([]arc, 0)
	for _, c := range state.CSP.Constraints {
		for i := range c.Variables {
			for j := range c.Variables {
				if i != j {
					queue = append(queue, arc{c.Variables[i].Name, c.Variables[j].Name})
				}
			}
		}
	}

	for len(queue) > 0 {
		a := queue[0]
		queue = queue[1:]

		if _, assigned := assignment[a.xi]; assigned {
			continue
		}
		if _, assigned := assignment[a.xj]; assigned {
			continue
		}

		xi := varMap[a.xi]
		xj := varMap[a.xj]
		if ac.revise(state, xi, xj, assignment) {
			if len(state.Domains[xi.Name]) == 0 {
				return false
			}
			for _, c := range state.CSP.Constraints {
				if c.Involves(xi) {
					for _, other := range c.Variables {
						if other != xi && other != xj {
							if _, assigned := assignment[other.Name]; !assigned {
								queue = append(queue, arc{other.Name, xi.Name})
							}
						}
					}
				}
			}
		}
	}
	return true
}

// revise removes values from xi's domain that have no support in xj's domain.
func (ac *AC3Solver) revise(state *SolverState, xi, xj *Variable, assignment map[string]interface{}) bool {
	relevant := make([]*Constraint, 0)
	for _, c := range state.CSP.Constraints {
		if c.Involves(xi) && c.Involves(xj) {
			relevant = append(relevant, c)
		}
	}

	revised := false
	domain := state.Domains[xi.Name]
	for i := 0; i < len(domain); {
		x := domain[i]
		satisfiesAll := false
		for _, y := range state.Domains[xj.Name] {
			temp := make(map[string]interface{}, len(assignment)+2)
			for k, v := range assignment {
				temp[k] = v
			}
			temp[xi.Name] = x
			temp[xj.Name] = y
			allSatisfied := true
			for _, c := range relevant {
				if !c.IsSatisfied(temp) {
					allSatisfied = false
					break
				}
			}
			if allSatisfied {
				satisfiesAll = true
				break
			}
		}
		if !satisfiesAll {
			domain = append(domain[:i], domain[i+1:]...)
			state.Domains[xi.Name] = domain
			revised = true
		} else {
			i++
		}
	}
	return revised
}

// BacktrackingSolver searches for a satisfying assignment.
type BacktrackingSolver struct{}

// Solve runs backtracking with AC-3 on a copy of the CSP.
func (bs *BacktrackingSolver) Solve(csp *CSP) map[string]interface{} {
	state := NewSolverState(csp)
	return bs.backtrack(state, make(map[string]interface{}))
}

func (bs *BacktrackingSolver) backtrack(state *SolverState, assignment map[string]interface{}) map[string]interface{} {
	if state.CSP.IsComplete(assignment) {
		return assignment
	}

	variable := state.CSP.GetUnassignedVariable(state, assignment)
	if variable == nil {
		return nil
	}

	for _, value := range state.CSP.OrderDomainValues(state, variable, assignment) {
		newAssignment := make(map[string]interface{}, len(assignment)+1)
		for k, v := range assignment {
			newAssignment[k] = v
		}
		newAssignment[variable.Name] = value

		if !state.CSP.IsConsistent(newAssignment) {
			continue
		}

		newState := state.Copy()
		newState.Domains[variable.Name] = []interface{}{value}

		ac3 := &AC3Solver{}
		if ac3.AC3(newState, newAssignment) {
			result := bs.backtrack(newState, newAssignment)
			if result != nil {
				return result
			}
		}
	}
	return nil
}

func notEqual(values ...interface{}) bool {
	if len(values) != 2 {
		return false
	}
	return !equalValues(values[0], values[1])
}

func main() {
	// Self-test 1: 3-color Australia map coloring.
	variables := []*Variable{
		NewVariable("WA", []interface{}{"red", "green", "blue"}),
		NewVariable("NT", []interface{}{"red", "green", "blue"}),
		NewVariable("SA", []interface{}{"red", "green", "blue"}),
		NewVariable("Q", []interface{}{"red", "green", "blue"}),
		NewVariable("NSW", []interface{}{"red", "green", "blue"}),
		NewVariable("V", []interface{}{"red", "green", "blue"}),
		NewVariable("T", []interface{}{"red", "green", "blue"}),
	}

	constraints := []*Constraint{
		{Variables: []*Variable{variables[0], variables[1]}, Predicate: notEqual, Desc: "WA != NT"},
		{Variables: []*Variable{variables[0], variables[2]}, Predicate: notEqual, Desc: "WA != SA"},
		{Variables: []*Variable{variables[1], variables[2]}, Predicate: notEqual, Desc: "NT != SA"},
		{Variables: []*Variable{variables[1], variables[3]}, Predicate: notEqual, Desc: "NT != Q"},
		{Variables: []*Variable{variables[2], variables[3]}, Predicate: notEqual, Desc: "SA != Q"},
		{Variables: []*Variable{variables[2], variables[4]}, Predicate: notEqual, Desc: "SA != NSW"},
		{Variables: []*Variable{variables[2], variables[5]}, Predicate: notEqual, Desc: "SA != V"},
		{Variables: []*Variable{variables[3], variables[4]}, Predicate: notEqual, Desc: "Q != NSW"},
		{Variables: []*Variable{variables[4], variables[5]}, Predicate: notEqual, Desc: "NSW != V"},
	}

	csp := &CSP{Variables: variables, Constraints: constraints}
	solution := (&BacktrackingSolver{}).Solve(csp)
	if !(solution != nil) {
		fmt.Fprintln(os.Stderr, "3-colorable Australia map reported unsolvable")
		os.Exit(1)
	}
	if !(len(solution) == 7) {
		fmt.Fprintf(os.Stderr, "solution must assign all 7 regions, got %d\n", len(solution))
		os.Exit(1)
	}

	adjacent := [][2]string{
		{"WA", "NT"}, {"WA", "SA"}, {"NT", "SA"}, {"NT", "Q"},
		{"SA", "Q"}, {"SA", "NSW"}, {"SA", "V"}, {"Q", "NSW"}, {"NSW", "V"},
	}
	for _, pair := range adjacent {
		if !(!equalValues(solution[pair[0]], solution[pair[1]])) {
			fmt.Fprintf(os.Stderr, "solution violates adjacency: %s == %s both %v\n", pair[0], pair[1], solution[pair[0]])
			os.Exit(1)
		}
	}
	for _, v := range solution {
		if !(v == "red" || v == "green" || v == "blue") {
			fmt.Fprintf(os.Stderr, "color out of range: %v\n", v)
			os.Exit(1)
		}
	}

	// Self-test 2: 2x2 latin square.
	gridVars := make([]*Variable, 0, 4)
	for i := 0; i < 2; i++ {
		for j := 0; j < 2; j++ {
			gridVars = append(gridVars, NewVariable(fmt.Sprintf("X%d%d", i, j), []interface{}{1, 2}))
		}
	}
	sudoku := []*Constraint{
		{Variables: []*Variable{gridVars[0], gridVars[1]}, Predicate: notEqual, Desc: "Row 0"},
		{Variables: []*Variable{gridVars[2], gridVars[3]}, Predicate: notEqual, Desc: "Row 1"},
		{Variables: []*Variable{gridVars[0], gridVars[2]}, Predicate: notEqual, Desc: "Col 0"},
		{Variables: []*Variable{gridVars[1], gridVars[3]}, Predicate: notEqual, Desc: "Col 1"},
	}
	sol := (&BacktrackingSolver{}).Solve(&CSP{Variables: gridVars, Constraints: sudoku})
	if !(sol != nil) {
		fmt.Fprintln(os.Stderr, "2x2 latin square reported unsolvable")
		os.Exit(1)
	}
	g := make(map[string]interface{}, len(sol))
	for _, v := range gridVars {
		g[v.Name] = sol[v.Name]
	}
	if !(g["X00"] != g["X01"] && g["X10"] != g["X11"]) {
		fmt.Fprintf(os.Stderr, "row constraint violated: %v\n", g)
		os.Exit(1)
	}
	if !(g["X00"] != g["X10"] && g["X01"] != g["X11"]) {
		fmt.Fprintf(os.Stderr, "column constraint violated: %v\n", g)
		os.Exit(1)
	}
	if !(g["X00"] == g["X11"] && g["X01"] == g["X10"]) {
		fmt.Fprintf(os.Stderr, "a 2x2 latin square forces the diagonal equality: %v\n", g)
		os.Exit(1)
	}
	sum := 0
	for _, v := range g {
		sum += v.(int)
	}
	if !(sum == 6) {
		fmt.Fprintf(os.Stderr, "cells must be two 1s and two 2s (sum 6), got %d\n", sum)
		os.Exit(1)
	}

	// Self-test 3: 2-coloring a triangle is impossible.
	tri := []*Variable{
		NewVariable("A", []interface{}{"red", "green"}),
		NewVariable("B", []interface{}{"red", "green"}),
		NewVariable("C", []interface{}{"red", "green"}),
	}
	triCons := []*Constraint{
		{Variables: []*Variable{tri[0], tri[1]}, Predicate: notEqual, Desc: "A!=B"},
		{Variables: []*Variable{tri[1], tri[2]}, Predicate: notEqual, Desc: "B!=C"},
		{Variables: []*Variable{tri[0], tri[2]}, Predicate: notEqual, Desc: "A!=C"},
	}
	if !((&BacktrackingSolver{}).Solve(&CSP{Variables: tri, Constraints: triCons}) == nil) {
		fmt.Fprintln(os.Stderr, "2-coloring a triangle is impossible, but the solver 'solved' it")
		os.Exit(1)
	}

	// Self-test 4: forced chain propagates to a unique solution.
	a := NewVariable("a", []interface{}{"x"})
	b := NewVariable("b", []interface{}{"x", "y"})
	c := NewVariable("c", []interface{}{"x", "y", "z"})
	chain := []*Constraint{
		{Variables: []*Variable{a, b}, Predicate: notEqual, Desc: "a!=b"},
		{Variables: []*Variable{b, c}, Predicate: notEqual, Desc: "b!=c"},
		{Variables: []*Variable{a, c}, Predicate: notEqual, Desc: "a!=c"},
	}
	forced := (&BacktrackingSolver{}).Solve(&CSP{Variables: []*Variable{a, b, c}, Constraints: chain})
	if !(forced != nil) {
		fmt.Fprintln(os.Stderr, "forced chain reported unsolvable")
		os.Exit(1)
	}
	fmap := map[string]interface{}{
		"a": forced["a"],
		"b": forced["b"],
		"c": forced["c"],
	}
	expected := map[string]interface{}{"a": "x", "b": "y", "c": "z"}
	if !(fmap["a"] == expected["a"] && fmap["b"] == expected["b"] && fmap["c"] == expected["c"]) {
		fmt.Fprintf(os.Stderr, "forced chain wrong: %v\n", fmap)
		os.Exit(1)
	}

	fmt.Println("csp_solver: Australia 9/9 constraints hold, 2x2 latin square exact " +
		"(sum 6), 2-color triangle UNSAT, forced chain x/y/z — PASS")
}
