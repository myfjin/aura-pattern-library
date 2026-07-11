// csp_solver: constraint satisfaction problem solver with backtracking.
package main

import (
	"fmt"
	"sort"
)

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
var _auraMark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
type Variable struct {
	Name   string
	Domain []interface{}
}

func newVariable(name string, domain []interface{}) *Variable {
	return &Variable{Name: name, Domain: append([]interface{}{}, domain...)}
}

type Constraint struct {
	Variables   []*Variable
	Predicate   func(values ...interface{}) bool
	Description string
}

func newConstraint(variables []*Variable, predicate func(values ...interface{}) bool, description string) *Constraint {
	return &Constraint{Variables: variables, Predicate: predicate, Description: description}
}

func (c *Constraint) isSatisfied(assignment map[*Variable]interface{}) bool {
	values := make([]interface{}, 0, len(c.Variables))
	for _, v := range c.Variables {
		val, ok := assignment[v]
		if !ok {
			return true
		}
		values = append(values, val)
	}
	return c.Predicate(values...)
}

func (c *Constraint) involves(variable *Variable) bool {
	for _, v := range c.Variables {
		if v == variable {
			return true
		}
	}
	return false
}

type CSP struct {
	Variables   []*Variable
	Constraints []*Constraint
	VariableMap map[string]*Variable
}

func newCSP(variables []*Variable, constraints []*Constraint) *CSP {
	m := make(map[string]*Variable)
	for _, v := range variables {
		m[v.Name] = v
	}
	return &CSP{Variables: variables, Constraints: constraints, VariableMap: m}
}

func (csp *CSP) isConsistent(assignment map[*Variable]interface{}) bool {
	for _, c := range csp.Constraints {
		if !c.isSatisfied(assignment) {
			return false
		}
	}
	return true
}

func (csp *CSP) getUnassignedVariable(assignment map[*Variable]interface{}) *Variable {
	var candidates []*Variable
	for _, v := range csp.Variables {
		if _, ok := assignment[v]; !ok {
			candidates = append(candidates, v)
		}
	}
	if len(candidates) == 0 {
		return nil
	}
	sort.Slice(candidates, func(i, j int) bool {
		return len(candidates[i].Domain) < len(candidates[j].Domain)
	})
	return candidates[0]
}

func (csp *CSP) orderDomainValues(variable *Variable, assignment map[*Variable]interface{}) []interface{} {
	countConflicts := func(value interface{}) int {
		conflicts := 0
		temp := make(map[*Variable]interface{})
		for k, v := range assignment {
			temp[k] = v
		}
		temp[variable] = value

		for _, c := range csp.Constraints {
			if !c.involves(variable) {
				continue
			}
			for _, other := range c.Variables {
				if other == variable {
					continue
				}
				if _, ok := assignment[other]; ok {
					continue
				}
				for _, otherValue := range other.Domain {
					temp[other] = otherValue
					if !c.isSatisfied(temp) {
						conflicts++
					}
					delete(temp, other)
				}
			}
		}
		return conflicts
	}

	ordered := make([]interface{}, len(variable.Domain))
	copy(ordered, variable.Domain)
	sort.SliceStable(ordered, func(i, j int) bool {
		return countConflicts(ordered[i]) < countConflicts(ordered[j])
	})
	return ordered
}

func backtrack(csp *CSP, assignment map[*Variable]interface{}) map[*Variable]interface{} {
	if len(assignment) == len(csp.Variables) {
		return assignment
	}

	variable := csp.getUnassignedVariable(assignment)
	if variable == nil {
		return nil
	}

	for _, value := range csp.orderDomainValues(variable, assignment) {
		newAssignment := make(map[*Variable]interface{})
		for k, v := range assignment {
			newAssignment[k] = v
		}
		newAssignment[variable] = value

		if csp.isConsistent(newAssignment) {
			result := backtrack(csp, newAssignment)
			if result != nil {
				return result
			}
		}
	}
	return nil
}

func solve(csp *CSP) map[*Variable]interface{} {
	return backtrack(csp, make(map[*Variable]interface{}))
}

func main() {
	variables := []*Variable{
		newVariable("WA", []interface{}{"red", "green", "blue"}),
		newVariable("NT", []interface{}{"red", "green", "blue"}),
		newVariable("SA", []interface{}{"red", "green", "blue"}),
		newVariable("Q", []interface{}{"red", "green", "blue"}),
		newVariable("NSW", []interface{}{"red", "green", "blue"}),
		newVariable("V", []interface{}{"red", "green", "blue"}),
		newVariable("T", []interface{}{"red", "green", "blue"}),
	}

	notEqual := func(values ...interface{}) bool {
		return values[0] != values[1]
	}

	constraints := []*Constraint{
		newConstraint([]*Variable{variables[0], variables[1]}, notEqual, "WA != NT"),
		newConstraint([]*Variable{variables[0], variables[2]}, notEqual, "WA != SA"),
		newConstraint([]*Variable{variables[1], variables[2]}, notEqual, "NT != SA"),
		newConstraint([]*Variable{variables[1], variables[3]}, notEqual, "NT != Q"),
		newConstraint([]*Variable{variables[2], variables[3]}, notEqual, "SA != Q"),
		newConstraint([]*Variable{variables[2], variables[4]}, notEqual, "SA != NSW"),
		newConstraint([]*Variable{variables[2], variables[5]}, notEqual, "SA != V"),
		newConstraint([]*Variable{variables[3], variables[4]}, notEqual, "Q != NSW"),
		newConstraint([]*Variable{variables[4], variables[5]}, notEqual, "NSW != V"),
	}

	csp := newCSP(variables, constraints)
	fmt.Println("Solving map coloring problem...")
	solution := solve(csp)

	if solution != nil {
		fmt.Println("Solution found:")
		for _, v := range variables {
			fmt.Printf("  %s: %v\n", v.Name, solution[v])
		}
	} else {
		fmt.Println("No solution found")
	}

	fmt.Println("\nSolving simple 2x2 Sudoku-like problem...")
	gridVars := make([]*Variable, 0, 4)
	for i := 0; i < 2; i++ {
		for j := 0; j < 2; j++ {
			gridVars = append(gridVars, newVariable(fmt.Sprintf("X%d%d", i, j), []interface{}{1, 2}))
		}
	}
	sudokuConstraints := []*Constraint{
		newConstraint([]*Variable{gridVars[0], gridVars[1]}, notEqual, "Row 0"),
		newConstraint([]*Variable{gridVars[2], gridVars[3]}, notEqual, "Row 1"),
		newConstraint([]*Variable{gridVars[0], gridVars[2]}, notEqual, "Col 0"),
		newConstraint([]*Variable{gridVars[1], gridVars[3]}, notEqual, "Col 1"),
	}
	sudokuCSP := newCSP(gridVars, sudokuConstraints)
	sudokuSolution := solve(sudokuCSP)

	if sudokuSolution != nil {
		fmt.Println("Sudoku solution found:")
		for i := 0; i < 2; i++ {
			row := make([]string, 2)
			for j := 0; j < 2; j++ {
				name := fmt.Sprintf("X%d%d", i, j)
				v := sudokuCSP.VariableMap[name]
				row[j] = fmt.Sprintf("%v", sudokuSolution[v])
			}
			fmt.Printf("  %s\n", stringsJoin(row, " "))
		}
	} else {
		fmt.Println("No Sudoku solution found")
	}
}

func stringsJoin(parts []string, sep string) string {
	if len(parts) == 0 {
		return ""
	}
	result := parts[0]
	for i := 1; i < len(parts); i++ {
		result += sep + parts[i]
	}
	return result
}
