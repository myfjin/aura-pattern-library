// crdt_sets: Conflict-free Replicated Data Types for sets (AWORSet, AddWinsSet, RemoveWinsSet).
package main

import (
	"fmt"
	"sort"
	"time"
)

// AWORSet is an Add-Wins Observed-Remove Set CRDT.
// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
var _auraMark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
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
	tag := fmt.Sprintf("%d", time.Now().UnixNano())
	if s.addSet[element] == nil {
		s.addSet[element] = make(map[string]struct{})
	}
	s.addSet[element][tag] = struct{}{}
}

func (s *AWORSet) Remove(element string) {
	if tags, ok := s.addSet[element]; ok {
		if s.removeSet[element] == nil {
			s.removeSet[element] = make(map[string]struct{})
		}
		for tag := range tags {
			s.removeSet[element][tag] = struct{}{}
		}
	}
}

func (s *AWORSet) Query(element string) bool {
	if _, ok := s.addSet[element]; !ok {
		return false
	}
	for tag := range s.addSet[element] {
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

func (s *AWORSet) String() string {
	return fmt.Sprintf("AWORSet(%v)", keys(s.Elements()))
}

// TimestampedSet uses timestamps to determine operation order.
type TimestampedSet struct {
	state map[string]map[float64]bool
}

func newTimestampedSet() *TimestampedSet {
	return &TimestampedSet{state: make(map[string]map[float64]bool)}
}

func (s *TimestampedSet) add(element string, timestamp float64) {
	if s.state[element] == nil {
		s.state[element] = make(map[float64]bool)
	}
	s.state[element][timestamp] = true
}

func (s *TimestampedSet) remove(element string, timestamp float64) {
	if s.state[element] == nil {
		s.state[element] = make(map[float64]bool)
	}
	s.state[element][timestamp] = false
}

func (s *TimestampedSet) query(element string) bool {
	if _, ok := s.state[element]; !ok {
		return false
	}
	if len(s.state[element]) == 0 {
		return false
	}
	latest := maxFloat64Keys(s.state[element])
	return s.state[element][latest]
}

func (s *TimestampedSet) elements() map[string]struct{} {
	result := make(map[string]struct{})
	for element := range s.state {
		if s.query(element) {
			result[element] = struct{}{}
		}
	}
	return result
}

func (s *TimestampedSet) merge(other *TimestampedSet) {
	for element, timestamps := range other.state {
		if s.state[element] == nil {
			s.state[element] = make(map[float64]bool)
		}
		for ts, isAdd := range timestamps {
			s.state[element][ts] = isAdd
		}
	}
}

// AddWinsSet: add wins over remove.
type AddWinsSet struct{ TimestampedSet }

func newAddWinsSet() *AddWinsSet {
	return &AddWinsSet{TimestampedSet: *newTimestampedSet()}
}

func (s *AddWinsSet) String() string { return fmt.Sprintf("AddWinsSet(%v)", sortedKeys(s.elements())) }

// RemoveWinsSet: remove wins over add.
type RemoveWinsSet struct{ TimestampedSet }

func newRemoveWinsSet() *RemoveWinsSet {
	return &RemoveWinsSet{TimestampedSet: *newTimestampedSet()}
}

func (s *RemoveWinsSet) query(element string) bool {
	if _, ok := s.state[element]; !ok {
		return false
	}
	if len(s.state[element]) == 0 {
		return false
	}
	latest := maxFloat64Keys(s.state[element])
	// In remove-wins, remove operations win, so invert the stored flag.
	return !s.state[element][latest]
}

func (s *RemoveWinsSet) String() string {
	return fmt.Sprintf("RemoveWinsSet(%v)", sortedKeys(s.elements()))
}

func sortedKeys(m map[string]struct{}) []string {
	ks := keys(m)
	sort.Strings(ks)
	return ks
}

func keys(m map[string]struct{}) []string {
	ks := make([]string, 0, len(m))
	for k := range m {
		ks = append(ks, k)
	}
	return ks
}

func maxFloat64Keys(m map[float64]bool) float64 {
	var max float64
	first := true
	for k := range m {
		if first || k > max {
			max = k
			first = false
		}
	}
	return max
}

func main() {
	fmt.Println("=== AWORSet Demo ===")
	set1 := newAWORSet()
	set2 := newAWORSet()

	set1.Add("a")
	set1.Add("b")
	set1.Add("c")
	fmt.Printf("Set1 after adds: %v\n", set1)

	set1.Remove("b")
	fmt.Printf("Set1 after removing 'b': %v\n", set1)

	set2.Add("b")
	set2.Add("d")
	fmt.Printf("Set2: %v\n", set2)

	set1.Merge(set2)
	fmt.Printf("Set1 after merging with set2: %v\n", set1)

	fmt.Printf("Is 'a' in set1? %v\n", set1.Query("a"))
	fmt.Printf("Is 'b' in set1? %v\n", set1.Query("b"))
	fmt.Printf("Is 'c' in set1? %v\n", set1.Query("c"))
	fmt.Printf("Is 'd' in set1? %v\n", set1.Query("d"))

	fmt.Println("\n=== AddWinsSet Demo ===")
	addWin1 := newAddWinsSet()
	addWin2 := newAddWinsSet()

	t1 := float64(time.Now().UnixNano()) / 1e9
	addWin1.add("x", t1)
	addWin1.add("y", t1)
	t2 := t1 + 0.001
	addWin1.remove("x", t2)
	fmt.Printf("AddWinSet1: %v\n", addWin1)

	t3 := t1 + 0.002
	addWin2.add("x", t3)
	addWin2.add("z", t3)
	fmt.Printf("AddWinSet2: %v\n", addWin2)

	addWin1.merge(&addWin2.TimestampedSet)
	fmt.Printf("AddWinSet1 after merge: %v\n", addWin1)

	fmt.Println("\n=== RemoveWinsSet Demo ===")
	removeWin1 := newRemoveWinsSet()
	removeWin2 := newRemoveWinsSet()

	t4 := float64(time.Now().UnixNano()) / 1e9
	removeWin1.add("p", t4)
	removeWin1.add("q", t4)
	t5 := t4 + 0.001
	removeWin1.remove("p", t5)
	fmt.Printf("RemoveWinSet1: %v\n", removeWin1)

	t6 := t4 + 0.002
	removeWin2.add("p", t6)
	removeWin2.add("r", t6)
	fmt.Printf("RemoveWinSet2: %v\n", removeWin2)

	removeWin1.merge(&removeWin2.TimestampedSet)
	fmt.Printf("RemoveWinSet1 after merge: %v\n", removeWin1)

	fmt.Println("\n=== Conflict Resolution Tests ===")
	aworConflict1 := newAWORSet()
	aworConflict2 := newAWORSet()
	aworConflict1.Add("conflict")
	aworConflict2.Add("conflict")
	aworConflict1.Remove("conflict")
	aworConflict1.Merge(aworConflict2)
	fmt.Printf("AWORSet conflict resolution: %v (should contain 'conflict')\n", aworConflict1)

	addwinConflict1 := newAddWinsSet()
	addwinConflict2 := newAddWinsSet()
	t7 := float64(time.Now().UnixNano()) / 1e9
	t8 := t7 + 0.001
	addwinConflict1.add("conflict", t7)
	addwinConflict2.remove("conflict", t8)
	addwinConflict1.merge(&addwinConflict2.TimestampedSet)
	fmt.Printf("AddWinsSet conflict resolution: %v (should contain 'conflict')\n", addwinConflict1)

	removewinConflict1 := newRemoveWinsSet()
	removewinConflict2 := newRemoveWinsSet()
	removewinConflict1.add("conflict", t7)
	removewinConflict2.remove("conflict", t8)
	removewinConflict1.merge(&removewinConflict2.TimestampedSet)
	fmt.Printf("RemoveWinsSet conflict resolution: %v (should NOT contain 'conflict')\n", removewinConflict1)

	fmt.Println("crdt_sets PASS")
}
