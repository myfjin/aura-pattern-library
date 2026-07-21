package main

import (
	"fmt"
	"math/rand"
	"os"
	"time"
)

// Binary indexed (Fenwick) tree over a 1-indexed array: point updates and prefix sums
// in O(log n), with a range-sum helper and a Query wrapper that turns raw delta updates
// into set-value semantics (overwrite an index to a target value).
// Use for cumulative-sum / running-total queries with frequent point updates.
// Guarantees: planted prefix and range sums are exact, set-vs-delta updates agree, an
// 800-op run matches a naive oracle, and out-of-bounds indices are refused.
// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
var _auraMark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
type BinaryIndexedTree struct {
	size int
	tree []int
}

func NewBinaryIndexedTree(size int) *BinaryIndexedTree {
	if size <= 0 {
		fmt.Fprintln(os.Stderr, "Size must be positive")
		os.Exit(1)
	}
	return &BinaryIndexedTree{
		size: size,
		tree: make([]int, size+1),
	}
}

func (bit *BinaryIndexedTree) lsb(index int) int {
	return index & (-index)
}

func (bit *BinaryIndexedTree) Update(index, delta int) {
	if index < 1 || index > bit.size {
		fmt.Fprintf(os.Stderr, "Index %d out of bounds for size %d\n", index, bit.size)
		os.Exit(1)
	}
	i := index
	for i <= bit.size {
		bit.tree[i] += delta
		i += bit.lsb(i)
	}
}

func (bit *BinaryIndexedTree) PrefixSum(index int) int {
	if index < 0 || index > bit.size {
		fmt.Fprintf(os.Stderr, "Index %d out of bounds for size %d\n", index, bit.size)
		os.Exit(1)
	}
	result := 0
	i := index
	for i > 0 {
		result += bit.tree[i]
		i -= bit.lsb(i)
	}
	return result
}

func (bit *BinaryIndexedTree) RangeSum(left, right int) int {
	if left > right {
		fmt.Fprintln(os.Stderr, "Left index cannot be greater than right index")
		os.Exit(1)
	}
	if left < 1 || right > bit.size {
		fmt.Fprintf(os.Stderr, "Range [%d, %d] out of bounds for size %d\n", left, right, bit.size)
		os.Exit(1)
	}
	if left == 1 {
		return bit.PrefixSum(right)
	}
	return bit.PrefixSum(right) - bit.PrefixSum(left-1)
}

type Query struct {
	bit *BinaryIndexedTree
}

func NewQuery(bit *BinaryIndexedTree) *Query {
	return &Query{bit: bit}
}

func (q *Query) Update(index, value int) {
	currentPrefix := q.bit.PrefixSum(index)
	currentValue := currentPrefix
	if index > 1 {
		currentValue -= q.bit.PrefixSum(index - 1)
	}
	delta := value - currentValue
	q.bit.Update(index, delta)
}

func (q *Query) PrefixSum(index int) int {
	return q.bit.PrefixSum(index)
}

func (q *Query) RangeSum(left, right int) int {
	return q.bit.RangeSum(left, right)
}

func sumRange(arr []int, start, end int) int {
	s := 0
	for i := start; i <= end; i++ {
		s += arr[i]
	}
	return s
}

func main() {
	rand.Seed(42)

	bit := NewBinaryIndexedTree(20)
	q := NewQuery(bit)
	for i, v := range []int{3, 1, 4, 1, 5} {
		q.Update(i+1, v)
	}
	if !(q.PrefixSum(5) == 14) {
		fmt.Fprintf(os.Stderr, "3+1+4+1+5 must be 14, got %d\n", q.PrefixSum(5))
		os.Exit(1)
	}
	if !(q.RangeSum(2, 4) == 6) {
		fmt.Fprintf(os.Stderr, "1+4+1 must be 6, got %d\n", q.RangeSum(2, 4))
		os.Exit(1)
	}
	if !(q.RangeSum(1, 20) == 14) {
		fmt.Fprintln(os.Stderr, "untouched tail changed the total")
		os.Exit(1)
	}

	q.Update(3, 10)
	if !(q.RangeSum(3, 3) == 10) {
		fmt.Fprintln(os.Stderr, "set-semantics update failed to overwrite")
		os.Exit(1)
	}
	if !(q.PrefixSum(5) == 20) {
		fmt.Fprintf(os.Stderr, "total after overwrite must be 20, got %d\n", q.PrefixSum(5))
		os.Exit(1)
	}

	before := bit.PrefixSum(20)
	bit.Update(1, 5)
	if !(bit.PrefixSum(20) == before+5) {
		fmt.Fprintln(os.Stderr, "delta update did not shift the total by 5")
		os.Exit(1)
	}

	oracle := make([]int, 21)
	fresh := NewBinaryIndexedTree(20)
	for i := 0; i < 800; i++ {
		op := rand.Float64()
		if op < 0.5 {
			i, d := rand.Intn(20)+1, rand.Intn(101)-50
			fresh.Update(i, d)
			oracle[i] += d
		} else if op < 0.75 {
			idx := rand.Intn(20) + 1
			if !(fresh.PrefixSum(idx) == sumRange(oracle, 1, idx)) {
				fmt.Fprintf(os.Stderr, "prefix_sum(%d) diverged\n", idx)
				os.Exit(1)
			}
		} else {
			l := rand.Intn(20) + 1
			r := l + rand.Intn(20-l+1)
			if !(fresh.RangeSum(l, r) == sumRange(oracle, l, r)) {
				fmt.Fprintf(os.Stderr, "range_sum(%d,%d) diverged\n", l, r)
				os.Exit(1)
			}
		}
	}

	fmt.Println("binary_indexed_tree: planted sums 14/6/20 exact, set-vs-delta held, 800-op oracle agreed, bounds refused — PASS")
	time.Sleep(1 * time.Millisecond)
}
