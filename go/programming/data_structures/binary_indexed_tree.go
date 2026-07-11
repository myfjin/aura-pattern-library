package main

import (
	"errors"
	"fmt"
)

// BinaryIndexedTree implements a Fenwick tree for prefix sums and range queries.
// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
var _auraMark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
type BinaryIndexedTree struct {
	size int
	tree []int
}

// NewBinaryIndexedTree creates a BIT of the given size (1-indexed).
func NewBinaryIndexedTree(size int) (*BinaryIndexedTree, error) {
	if size <= 0 {
		return nil, errors.New("size must be positive")
	}
	return &BinaryIndexedTree{
		size: size,
		tree: make([]int, size+1),
	}, nil
}

// Size returns the tree size.
func (bit *BinaryIndexedTree) Size() int {
	return bit.size
}

func lsb(index int) int {
	return index & (-index)
}

// Update adds delta at the 1-based index.
func (bit *BinaryIndexedTree) Update(index, delta int) error {
	if index < 1 || index > bit.size {
		return errors.New("index out of bounds")
	}
	for index <= bit.size {
		bit.tree[index] += delta
		index += lsb(index)
	}
	return nil
}

// PrefixSum returns the sum from 1 to index (inclusive). index may be 0.
func (bit *BinaryIndexedTree) PrefixSum(index int) (int, error) {
	if index < 0 || index > bit.size {
		return 0, errors.New("index out of bounds")
	}
	result := 0
	for index > 0 {
		result += bit.tree[index]
		index -= lsb(index)
	}
	return result, nil
}

// RangeSum returns the sum in [left, right] (inclusive).
func (bit *BinaryIndexedTree) RangeSum(left, right int) (int, error) {
	if left > right {
		return 0, errors.New("left index cannot be greater than right index")
	}
	if left < 1 || right > bit.size {
		return 0, errors.New("range out of bounds")
	}
	if left == 1 {
		return bit.PrefixSum(right)
	}
	leftSum, err := bit.PrefixSum(left - 1)
	if err != nil {
		return 0, err
	}
	rightSum, err := bit.PrefixSum(right)
	if err != nil {
		return 0, err
	}
	return rightSum - leftSum, nil
}

// String returns a readable representation.
func (bit *BinaryIndexedTree) String() string {
	return fmt.Sprintf("BinaryIndexedTree(size=%d, tree=%v)", bit.size, bit.tree[1:])
}

// Query provides convenience operations on a BIT. It assumes the underlying
// array starts at zero and tracks values via set-style updates.
type Query struct {
	bit *BinaryIndexedTree
}

// NewQuery creates a Query wrapper around a BIT.
func NewQuery(bit *BinaryIndexedTree) *Query {
	return &Query{bit: bit}
}

// Update sets the value at index to value (compute delta from current).
func (q *Query) Update(index, value int) error {
	currentPrefix, err := q.bit.PrefixSum(index)
	if err != nil {
		return err
	}
	var currentValue int
	if index > 1 {
		prevPrefix, err := q.bit.PrefixSum(index - 1)
		if err != nil {
			return err
		}
		currentValue = currentPrefix - prevPrefix
	} else {
		currentValue = currentPrefix
	}
	delta := value - currentValue
	return q.bit.Update(index, delta)
}

// PrefixSum returns the prefix sum up to index.
func (q *Query) PrefixSum(index int) (int, error) {
	return q.bit.PrefixSum(index)
}

// RangeSum returns the sum in [left, right].
func (q *Query) RangeSum(left, right int) (int, error) {
	return q.bit.RangeSum(left, right)
}

func main() {
	fmt.Println("Binary Indexed Tree Demo")
	fmt.Println("=========================")

	bit, err := NewBinaryIndexedTree(20)
	if err != nil {
		fmt.Println(err)
		return
	}
	query := NewQuery(bit)

	for i := 1; i <= 100; i++ {
		index := (i % 20) + 1
		value := i
		if err := query.Update(index, value); err != nil {
			fmt.Println(err)
			return
		}
		if i%10 == 0 {
			fmt.Printf("After %d updates:\n", i)
			ps, _ := query.PrefixSum(10)
			rs, _ := query.RangeSum(5, 15)
			fmt.Printf("  Prefix sum at index 10: %d\n", ps)
			fmt.Printf("  Range sum [5, 15]: %d\n\n", rs)
		}
	}

	fmt.Println("Final verification:")
	ps, _ := query.PrefixSum(20)
	rs, _ := query.RangeSum(1, 20)
	fmt.Printf("Prefix sum at index 20: %d\n", ps)
	fmt.Printf("Range sum [1, 20]: %d\n", rs)

	fmt.Println("\nTesting error handling:")
	if _, err := bit.PrefixSum(25); err != nil {
		fmt.Printf("Caught expected error: %v\n", err)
	}
	if _, err := bit.RangeSum(15, 10); err != nil {
		fmt.Printf("Caught expected error: %v\n", err)
	}
}
