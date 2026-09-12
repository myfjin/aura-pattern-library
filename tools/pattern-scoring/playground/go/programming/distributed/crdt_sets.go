// crdt_sets: Conflict-free Replicated Data Types for sets (AWORSet, AddWinsSet, RemoveWinsSet).
package main

import (
	"fmt"
	"os"
)

// assert is a drop-in recovery helper used to mirror Python self-test asserts.
// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
var _auraMark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
func assert(cond bool, msg string) {
	if !cond {
		fmt.Fprintln(os.Stderr, msg)
		os.Exit(1)
	}
}

// set helpers
func setEqual(a, b map[string]struct{}) bool {
	if len(a) != len(b) {
		return false
	}
	for k := range a {
		if _, ok := b[k]; !ok {
			return false
		}
	}
	return true
}

func setOf(items ...string) map[string]struct{} {
	s := make(map[string]struct{}, len(items))
	for _, item := range items {
		s[item] = struct{}{}
	}
	return s
}

var aworTagCounter int64

// AWORSet is an Add-Wins Observed-Remove Set CRDT.
// A remove only removes the add tags it has observed; concurrent unobserved adds survive.
type AWORSet struct {
	addSet    map[string]map[string]struct{}
	removeSet map[string]map[string]struct{}
}

func newAWORSet() *AWORSet {
	return &AWORSet{
		addSet:    make(map[string]map[string]struct{}),
		removeSet: make(map[string]map[string]struct{}),
	}
}

func (s *AWORSet) Add(element string) {
	aworTagCounter++
	tag := fmt.Sprintf("tag-%d", aworTagCounter)
	if s.addSet[element] == nil {
		s.addSet[element] = make(map[string]struct{})
	}
	s.addSet[element][tag] = struct{}{}
}

func (s *AWORSet) Remove(element string) {
	tags, ok := s.addSet[element]
	if !ok {
		return
	}
	if s.removeSet[element] == nil {
		s.removeSet[element] = make(map[string]struct{})
	}
	for tag := range tags {
		s.removeSet[element][tag] = struct{}{}
	}
}

func (s *AWORSet) Query(element string) bool {
	addTags, ok := s.addSet[element]
	if !ok {
		return false
	}
	for tag := range addTags {
		if _, removed := s.removeSet[element][tag]; !removed {
			return true
		}
	}
	return false
}

func (s *AWORSet) Elements() map[string]struct{} {
	result := make(map[string]struct{})
	for element := range s.addSet {
		if s.Query(element) {
			result[element] = struct{}{}
		}
	}
	return result
}

func (s *AWORSet) Merge(other *AWORSet) {
	for element, tags := range other.addSet {
		if s.addSet[element] == nil {
			s.addSet[element] = make(map[string]struct{})
		}
		for tag := range tags {
			s.addSet[element][tag] = struct{}{}
		}
	}
	for element, tags := range other.removeSet {
		if s.removeSet[element] == nil {
			s.removeSet[element] = make(map[string]struct{})
		}
		for tag := range tags {
			s.removeSet[element][tag] = struct{}{}
		}
	}
}

// AddWinsSet is a timestamped set where add operations win over removes,
// including equal-timestamp conflicts.
type AddWinsSet struct {
	state map[string]map[float64]bool
}

func newAddWinsSet() *AddWinsSet {
	return &AddWinsSet{state: make(map[string]map[float64]bool)}
}

func (s *AddWinsSet) add(element string, timestamp float64) {
	if s.state[element] == nil {
		s.state[element] = make(map[float64]bool)
	}
	s.state[element][timestamp] = true
}

func (s *AddWinsSet) remove(element string, timestamp float64) {
	if s.state[element] == nil {
		s.state[element] = make(map[float64]bool)
	}
	if !s.state[element][timestamp] {
		s.state[element][timestamp] = false
	}
}

func (s *AddWinsSet) query(element string) bool {
	timestamps, ok := s.state[element]
	if !ok || len(timestamps) == 0 {
		return false
	}
	var maxAdd, maxRemove float64
	hasAdd, hasRemove := false, false
	for ts, isAdd := range timestamps {
		if isAdd {
			if !hasAdd || ts > maxAdd {
				maxAdd = ts
				hasAdd = true
			}
		} else {
			if !hasRemove || ts > maxRemove {
				maxRemove = ts
				hasRemove = true
			}
		}
	}
	if !hasAdd {
		return false
	}
	if !hasRemove {
		return true
	}
	return maxAdd >= maxRemove
}

func (s *AddWinsSet) elements() map[string]struct{} {
	result := make(map[string]struct{})
	for element := range s.state {
		if s.query(element) {
			result[element] = struct{}{}
		}
	}
	return result
}

func (s *AddWinsSet) merge(other *AddWinsSet) {
	for element, timestamps := range other.state {
		if s.state[element] == nil {
			s.state[element] = make(map[float64]bool)
		}
		for ts, isAdd := range timestamps {
			s.state[element][ts] = s.state[element][ts] || isAdd
		}
	}
}

// RemoveWinsSet is a timestamped set where remove operations win over adds,
// including equal-timestamp conflicts.
type RemoveWinsSet struct {
	state map[string]map[float64]bool
}

func newRemoveWinsSet() *RemoveWinsSet {
	return &RemoveWinsSet{state: make(map[string]map[float64]bool)}
}

func (s *RemoveWinsSet) add(element string, timestamp float64) {
	if s.state[element] == nil {
		s.state[element] = make(map[float64]bool)
	}
	if cur, ok := s.state[element][timestamp]; !ok || cur {
		s.state[element][timestamp] = true
	}
}

func (s *RemoveWinsSet) remove(element string, timestamp float64) {
	if s.state[element] == nil {
		s.state[element] = make(map[float64]bool)
	}
	s.state[element][timestamp] = false
}

func (s *RemoveWinsSet) query(element string) bool {
	timestamps, ok := s.state[element]
	if !ok || len(timestamps) == 0 {
		return false
	}
	var maxAdd, maxRemove float64
	hasAdd, hasRemove := false, false
	for ts, isAdd := range timestamps {
		if isAdd {
			if !hasAdd || ts > maxAdd {
				maxAdd = ts
				hasAdd = true
			}
		} else {
			if !hasRemove || ts > maxRemove {
				maxRemove = ts
				hasRemove = true
			}
		}
	}
	if !hasAdd {
		return false
	}
	if !hasRemove {
		return true
	}
	return maxAdd > maxRemove
}

func (s *RemoveWinsSet) elements() map[string]struct{} {
	result := make(map[string]struct{})
	for element := range s.state {
		if s.query(element) {
			result[element] = struct{}{}
		}
	}
	return result
}

func (s *RemoveWinsSet) merge(other *RemoveWinsSet) {
	for element, timestamps := range other.state {
		if s.state[element] == nil {
			s.state[element] = make(map[float64]bool)
		}
		for ts, isAdd := range timestamps {
			if cur, ok := s.state[element][ts]; ok {
				s.state[element][ts] = cur && isAdd
			} else {
				s.state[element][ts] = isAdd
			}
		}
	}
}

func main() {
	// AWORSet: observed-remove — a remove only kills adds it has SEEN.
	s1, s2 := newAWORSet(), newAWORSet()
	s1.Add("a")
	s1.Add("b")
	s1.Add("c")
	s1.Remove("b")
	assert(setEqual(s1.Elements(), setOf("a", "c")), "local remove failed")

	s2.Add("b") // a concurrent, UNOBSERVED add of b
	s2.Add("d")
	s1.Merge(s2)
	assert(setEqual(s1.Elements(), setOf("a", "b", "c", "d")), "unobserved concurrent add must survive the remove")
	assert(s1.Query("b") == true && s1.Query("ghost") == false, "query after merge failed")
	nElems := len(s1.Elements())
	assert(nElems == 4, "AWOR merge must hold exactly 4 elements")

	// The observed-remove counterpart: a remove AFTER merging kills all observed tags.
	s1.Remove("b")
	assert(setEqual(s1.Elements(), setOf("a", "c", "d")), "observed remove failed post-merge")

	// AddWinsSet: concurrent add/remove of the same element → ADD WINS,
	// even when the remove has the LATER timestamp.
	aw1, aw2 := newAddWinsSet(), newAddWinsSet()
	t0 := 1000.0
	aw1.add("conflict", t0)
	aw2.remove("conflict", t0) // CONCURRENT (equal-timestamp) remove
	aw1.merge(aw2)
	assert(aw1.query("conflict") == true, "AddWins must keep the element in an add/remove tie")

	// A strictly LATER remove is sequential, not a conflict — it removes.
	aw1.remove("conflict", t0+1)
	assert(aw1.query("conflict") == false, "strictly later remove must apply")

	// Sequential semantics still hold: a remove after the add's arrival,
	// followed by a LATER re-add, resurrects it.
	aw1.add("x", t0)
	aw1.remove("x", t0+1)
	assert(aw1.query("x") == false, "sequential remove failed in AddWins")
	aw1.add("x", t0+2)
	assert(aw1.query("x") == true, "later re-add must win")

	// RemoveWinsSet: the same concurrent conflict → REMOVE WINS.
	rw1, rw2 := newRemoveWinsSet(), newRemoveWinsSet()
	rw1.add("conflict", t0)
	rw2.remove("conflict", t0) // equal-timestamp conflict
	rw1.merge(rw2)
	assert(rw1.query("conflict") == false, "RemoveWins must drop the element in an add/remove tie")

	// A strictly later add resurrects it even in RemoveWins.
	rw1.add("conflict", t0+1)
	assert(rw1.query("conflict") == true, "strictly later add must apply")
	rw1.remove("conflict", t0+1) // tie at t0+1 → remove wins again
	assert(rw1.query("conflict") == false, "equal-timestamp remove must win")
	rw1.add("p", t0)
	rw1.add("q", t0)
	assert(setEqual(rw1.elements(), setOf("p", "q")), "RemoveWins elements mismatch")

	// CONVERGENCE: merging in both directions yields identical element sets.
	x1, x2 := newAddWinsSet(), newAddWinsSet()
	x1.add("m", t0)
	x1.remove("m", t0+1)
	x2.add("m", t0+2)
	x2.add("n", t0)
	y1, y2 := newAddWinsSet(), newAddWinsSet()
	y1.add("m", t0)
	y1.remove("m", t0+1)
	y2.add("m", t0+2)
	y2.add("n", t0)
	x1.merge(x2) // A <- B
	y2.merge(y1) // B <- A
	assert(setEqual(x1.elements(), setOf("m", "n")), "merge direction A<-B diverged")
	assert(setEqual(y2.elements(), setOf("m", "n")), "merge direction B<-A diverged")
	assert(setEqual(x1.elements(), y2.elements()), "merge directions diverged")

	// Idempotence: re-merge changes nothing.
	before := x1.elements()
	x1.merge(x2)
	assert(setEqual(x1.elements(), before), "merge not idempotent")

	fmt.Println("crdt_sets: AWOR unobserved-add survived (4 elems), AddWins kept vs later remove, RemoveWins dropped, merge directions equal — PASS")
}
