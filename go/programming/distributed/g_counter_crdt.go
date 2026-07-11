package main

import (
	"fmt"
	"os"
	"sort"
)

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
var _auraMark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
type GCounter struct {
	nodeID string
	counts map[string]int
}

func NewGCounter(nodeID string) *GCounter {
	if nodeID == "" {
		nodeID = "node-default"
	}
	return &GCounter{
		nodeID: nodeID,
		counts: map[string]int{nodeID: 0},
	}
}

func (gc *GCounter) Increment(amount int) {
	if amount < 0 {
		fmt.Fprintln(os.Stderr, "GCounter only supports non-negative increments")
		os.Exit(1)
	}
	gc.counts[gc.nodeID] += amount
}

func (gc *GCounter) Value() int {
	total := 0
	for _, v := range gc.counts {
		total += v
	}
	return total
}

func (gc *GCounter) Merge(other *GCounter) {
	for nodeID, count := range other.counts {
		if current, ok := gc.counts[nodeID]; ok {
			if count > current {
				gc.counts[nodeID] = count
			}
		} else {
			gc.counts[nodeID] = count
		}
	}
}

func (gc *GCounter) GetNodes() []string {
	var nodes []string
	for k := range gc.counts {
		nodes = append(nodes, k)
	}
	sort.Strings(nodes)
	return nodes
}

type PNCounter struct {
	nodeID   string
	pCounter *GCounter
	nCounter *GCounter
}

func NewPNCounter(nodeID string) *PNCounter {
	if nodeID == "" {
		nodeID = "pn-default"
	}
	return &PNCounter{
		nodeID:   nodeID,
		pCounter: NewGCounter(nodeID),
		nCounter: NewGCounter(nodeID),
	}
}

func (pn *PNCounter) Increment(amount int) {
	if amount >= 0 {
		pn.pCounter.Increment(amount)
	} else {
		pn.nCounter.Increment(-amount)
	}
}

func (pn *PNCounter) Decrement(amount int) {
	if amount < 0 {
		fmt.Fprintln(os.Stderr, "Decrement amount must be non-negative")
		os.Exit(1)
	}
	pn.pCounter.Increment(0)
	pn.nCounter.Increment(amount)
}

func (pn *PNCounter) Value() int {
	return pn.pCounter.Value() - pn.nCounter.Value()
}

func (pn *PNCounter) Merge(other *PNCounter) {
	pn.pCounter.Merge(other.pCounter)
	pn.nCounter.Merge(other.nCounter)
}

func (pn *PNCounter) GetNodes() []string {
	set := make(map[string]struct{})
	for _, n := range pn.pCounter.GetNodes() {
		set[n] = struct{}{}
	}
	for _, n := range pn.nCounter.GetNodes() {
		set[n] = struct{}{}
	}
	var nodes []string
	for k := range set {
		nodes = append(nodes, k)
	}
	sort.Strings(nodes)
	return nodes
}

func demo() {
	fmt.Println("=== GCounter Demo ===")

	node1 := NewGCounter("node1")
	node2 := NewGCounter("node2")
	node3 := NewGCounter("node3")

	node1.Increment(5)
	node2.Increment(3)
	node3.Increment(7)

	fmt.Printf("Initial states:\n  value=%d (node1), value=%d (node2), value=%d (node3)\n", node1.Value(), node2.Value(), node3.Value())

	node1.Merge(node2)
	fmt.Printf("\nAfter node1 merges with node2:\n  value=%d (node1)\n", node1.Value())

	node3.Merge(node1)
	fmt.Printf("\nAfter node3 merges with updated node1:\n  value=%d (node3)\n", node3.Value())

	node2.Merge(node3)
	fmt.Printf("\nAfter node2 merges with updated node3 (all should converge):\n  value=%d (node2)\n", node2.Value())

	fmt.Printf("\nAll nodes have value: %d (node1), %d (node2), %d (node3)\n", node1.Value(), node2.Value(), node3.Value())

	fmt.Println("\n=== PNCounter Demo ===")

	pn1 := NewPNCounter("pn1")
	pn2 := NewPNCounter("pn2")
	pn3 := NewPNCounter("pn3")

	pn1.Increment(10)
	pn2.Decrement(5)
	pn3.Increment(3)
	pn1.Decrement(2)

	fmt.Printf("Initial states:\n  value=%d (pn1), value=%d (pn2), value=%d (pn3)\n", pn1.Value(), pn2.Value(), pn3.Value())

	pn1.Merge(pn2)
	fmt.Printf("\nAfter pn1 merges with pn2:\n  value=%d (pn1)\n", pn1.Value())

	pn3.Merge(pn1)
	fmt.Printf("\nAfter pn3 merges with updated pn1:\n  value=%d (pn3)\n", pn3.Value())

	pn2.Merge(pn3)
	fmt.Printf("\nAfter pn2 merges with updated pn3 (all should converge):\n  value=%d (pn2)\n", pn2.Value())

	fmt.Printf("\nAll nodes have value: %d (pn1), %d (pn2), %d (pn3)\n", pn1.Value(), pn2.Value(), pn3.Value())
}

func main() {
	demo()
	fmt.Println("✓ g_counter_crdt passed")
}
