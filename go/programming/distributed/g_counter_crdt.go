package main

import (
	"fmt"
	"os"
	"sort"
	"strings"
)

// GCounter is a grow-only distributed counter.
// Each node maintains its own count, and the total is the sum of all nodes' counts.
// Merging takes the maximum value for each node to ensure convergence.
// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
var _auraMark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
type GCounter struct {
	nodeID string
	counts map[string]int64
}

// NewGCounter initializes a GCounter. If nodeID is empty, a deterministic placeholder is generated.
func NewGCounter(nodeID string) *GCounter {
	if nodeID == "" {
		nodeID = fmt.Sprintf("node-%p", &nodeID)
	}
	return &GCounter{
		nodeID: nodeID,
		counts: map[string]int64{nodeID: 0},
	}
}

// Increment increases this node's counter by amount (must be non-negative).
func (c *GCounter) Increment(amount int64) {
	if amount < 0 {
		panic("GCounter only supports non-negative increments")
	}
	c.counts[c.nodeID] += amount
}

// Value returns the total counter value across all known nodes.
func (c *GCounter) Value() int64 {
	var total int64
	for _, v := range c.counts {
		total += v
	}
	return total
}

// Merge merges another GCounter into this one by taking the maximum count per node.
func (c *GCounter) Merge(other *GCounter) {
	for nodeID, count := range other.counts {
		if current, ok := c.counts[nodeID]; !ok || count > current {
			c.counts[nodeID] = count
		}
	}
}

// GetNodes returns all node IDs known to this counter.
func (c *GCounter) GetNodes() []string {
	nodes := make([]string, 0, len(c.counts))
	for k := range c.counts {
		nodes = append(nodes, k)
	}
	sort.Strings(nodes)
	return nodes
}

// countsString returns a deterministic string representation of the counts map.
func (c *GCounter) countsString() string {
	nodes := c.GetNodes()
	parts := make([]string, len(nodes))
	for i, n := range nodes {
		parts[i] = fmt.Sprintf("%q:%d", n, c.counts[n])
	}
	return "map[" + strings.Join(parts, " ") + "]"
}

func (c *GCounter) String() string {
	return fmt.Sprintf("GCounter(value=%d, nodes=%s)", c.Value(), c.countsString())
}

// PNCounter is a positive-negative distributed counter.
// It uses two GCounters internally: one for increments and one for decrements.
type PNCounter struct {
	nodeID   string
	pCounter *GCounter
	nCounter *GCounter
}

// NewPNCounter initializes a PNCounter. If nodeID is empty, a deterministic placeholder is generated.
func NewPNCounter(nodeID string) *PNCounter {
	if nodeID == "" {
		nodeID = fmt.Sprintf("pn-%p", &nodeID)
	}
	return &PNCounter{
		nodeID:   nodeID,
		pCounter: NewGCounter(nodeID),
		nCounter: NewGCounter(nodeID),
	}
}

// Increment increases the counter. A negative amount counts as a decrement.
func (c *PNCounter) Increment(amount int64) {
	if amount >= 0 {
		c.pCounter.Increment(amount)
	} else {
		c.nCounter.Increment(-amount)
	}
}

// Decrement decreases the counter by amount (must be non-negative).
func (c *PNCounter) Decrement(amount int64) {
	if amount < 0 {
		panic("Decrement amount must be non-negative")
	}
	c.pCounter.Increment(0) // ensure node exists in pCounter
	c.nCounter.Increment(amount)
}

// Value returns the current net value (positive minus negative).
func (c *PNCounter) Value() int64 {
	return c.pCounter.Value() - c.nCounter.Value()
}

// Merge merges another PNCounter into this one.
func (c *PNCounter) Merge(other *PNCounter) {
	c.pCounter.Merge(other.pCounter)
	c.nCounter.Merge(other.nCounter)
}

// GetNodes returns all node IDs from both the positive and negative counters.
func (c *PNCounter) GetNodes() []string {
	seen := make(map[string]struct{})
	for _, n := range c.pCounter.GetNodes() {
		seen[n] = struct{}{}
	}
	for _, n := range c.nCounter.GetNodes() {
		seen[n] = struct{}{}
	}
	nodes := make([]string, 0, len(seen))
	for k := range seen {
		nodes = append(nodes, k)
	}
	sort.Strings(nodes)
	return nodes
}

func (c *PNCounter) String() string {
	return fmt.Sprintf("PNCounter(value=%d, P=%s, N=%s)", c.Value(), c.pCounter.countsString(), c.nCounter.countsString())
}

func contains(slice []string, item string) bool {
	for _, s := range slice {
		if s == item {
			return true
		}
	}
	return false
}

func main() {
	// GCounter: independent increments converge to the exact global sum.
	n1, n2, n3 := NewGCounter("node1"), NewGCounter("node2"), NewGCounter("node3")
	n1.Increment(5)
	n2.Increment(3)
	n3.Increment(7)
	if !(n1.Value() == 5) {
		fmt.Fprintf(os.Stderr, "n1 initial value mismatch: %d\n", n1.Value())
		os.Exit(1)
	}
	if !(n2.Value() == 3) {
		fmt.Fprintf(os.Stderr, "n2 initial value mismatch: %d\n", n2.Value())
		os.Exit(1)
	}
	if !(n3.Value() == 7) {
		fmt.Fprintf(os.Stderr, "n3 initial value mismatch: %d\n", n3.Value())
		os.Exit(1)
	}

	// Anti-entropy gossip: after full exchange, every replica reads 15.
	n1.Merge(n2)
	if !(n1.Value() == 8) {
		fmt.Fprintf(os.Stderr, "5+3 must be 8, got %d\n", n1.Value())
		os.Exit(1)
	}
	n3.Merge(n1)
	if !(n3.Value() == 15) {
		fmt.Fprintf(os.Stderr, "5+3+7 must be 15, got %d\n", n3.Value())
		os.Exit(1)
	}
	n2.Merge(n3)
	n1.Merge(n3)
	if !(n1.Value() == 15) {
		fmt.Fprintf(os.Stderr, "n1 replica diverged: %d\n", n1.Value())
		os.Exit(1)
	}
	if !(n2.Value() == 15) {
		fmt.Fprintf(os.Stderr, "n2 replica diverged: %d\n", n2.Value())
		os.Exit(1)
	}
	if !(n3.Value() == 15) {
		fmt.Fprintf(os.Stderr, "n3 replica diverged: %d\n", n3.Value())
		os.Exit(1)
	}

	// IDEMPOTENCE: re-merging the same state changes nothing.
	n1.Merge(n3)
	n1.Merge(n3)
	if !(n1.Value() == 15) {
		fmt.Fprintf(os.Stderr, "merge is not idempotent: %d\n", n1.Value())
		os.Exit(1)
	}

	// COMMUTATIVITY: A.Merge(B) == B.Merge(A), state-wise.
	a, b := NewGCounter("A"), NewGCounter("B")
	a.Increment(4)
	b.Increment(9)
	ab, ba := NewGCounter("A"), NewGCounter("B")
	ab.Increment(4)
	ba.Increment(9)
	a.Merge(b)
	ba.Merge(ab)
	if !(a.Value() == 13) {
		fmt.Fprintf(os.Stderr, "merge order changed a: %d\n", a.Value())
		os.Exit(1)
	}
	if !(ba.Value() == 13) {
		fmt.Fprintf(os.Stderr, "merge order changed ba: %d\n", ba.Value())
		os.Exit(1)
	}
	if !(a.countsString() == ba.countsString()) {
		fmt.Fprintf(os.Stderr, "states differ: %s vs %s\n", a.countsString(), ba.countsString())
		os.Exit(1)
	}

	// Merge never loses increments that happened concurrently.
	a.Increment(1)
	if !(a.Value() == 14) {
		fmt.Fprintf(os.Stderr, "concurrent increment lost: %d\n", a.Value())
		os.Exit(1)
	}

	// GCounter is grow-only: negative increments refused.
	{
		c := NewGCounter("neg-test")
		errCaught := false
		func() {
			defer func() {
				if r := recover(); r != nil {
					errCaught = true
				}
			}()
			c.Increment(-1)
		}()
		if !(errCaught == true) {
			fmt.Fprintln(os.Stderr, "grow-only counter accepted a negative increment")
			os.Exit(1)
		}
	}

	// PNCounter: increments and decrements converge to the exact net value.
	pn1, pn2, pn3 := NewPNCounter("pn1"), NewPNCounter("pn2"), NewPNCounter("pn3")
	pn1.Increment(10)
	pn2.Decrement(5)
	pn3.Increment(3)
	pn1.Decrement(2)
	if !(pn1.Value() == 8) {
		fmt.Fprintf(os.Stderr, "pn1 initial value mismatch: %d\n", pn1.Value())
		os.Exit(1)
	}
	if !(pn2.Value() == -5) {
		fmt.Fprintf(os.Stderr, "pn2 initial value mismatch: %d\n", pn2.Value())
		os.Exit(1)
	}
	if !(pn3.Value() == 3) {
		fmt.Fprintf(os.Stderr, "pn3 initial value mismatch: %d\n", pn3.Value())
		os.Exit(1)
	}

	pn1.Merge(pn2)
	if !(pn1.Value() == 3) {
		fmt.Fprintf(os.Stderr, "8 + (-5) must be 3, got %d\n", pn1.Value())
		os.Exit(1)
	}
	pn3.Merge(pn1)
	pn2.Merge(pn3)
	pn1.Merge(pn3)
	if !(pn1.Value() == 6) {
		fmt.Fprintf(os.Stderr, "pn1 replica diverged: %d\n", pn1.Value())
		os.Exit(1)
	}
	if !(pn2.Value() == 6) {
		fmt.Fprintf(os.Stderr, "pn2 replica diverged: %d\n", pn2.Value())
		os.Exit(1)
	}
	if !(pn3.Value() == 6) {
		fmt.Fprintf(os.Stderr, "pn3 replica diverged: %d\n", pn3.Value())
		os.Exit(1)
	}
	if !(pn1.Value() == 10-5+3-2) {
		fmt.Fprintf(os.Stderr, "net value must be the sum of all ops: %d\n", pn1.Value())
		os.Exit(1)
	}

	// Node bookkeeping.
	nodes := pn1.GetNodes()
	if !(len(nodes) >= 3) {
		fmt.Fprintf(os.Stderr, "node bookkeeping missing expected nodes: %v\n", nodes)
		os.Exit(1)
	}
	if !(contains(nodes, "pn1") == true) {
		fmt.Fprintf(os.Stderr, "node pn1 missing: %v\n", nodes)
		os.Exit(1)
	}
	if !(contains(nodes, "pn2") == true) {
		fmt.Fprintf(os.Stderr, "node pn2 missing: %v\n", nodes)
		os.Exit(1)
	}
	if !(contains(nodes, "pn3") == true) {
		fmt.Fprintf(os.Stderr, "node pn3 missing: %v\n", nodes)
		os.Exit(1)
	}

	// Negative decrement refused.
	{
		c := NewPNCounter("neg-dec")
		errCaught := false
		func() {
			defer func() {
				if r := recover(); r != nil {
					errCaught = true
				}
			}()
			c.Decrement(-3)
		}()
		if !(errCaught == true) {
			fmt.Fprintln(os.Stderr, "negative decrement accepted")
			os.Exit(1)
		}
	}

	fmt.Println("g_counter_crdt: GCounter converged to 15 on all replicas (idempotent, commutative), PNCounter net 6 everywhere — PASS")
}
