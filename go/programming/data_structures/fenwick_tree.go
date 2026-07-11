package main

import (
	"fmt"
	"math/rand"
	"os"
	"time"
)

// FenwickTree implements a Fenwick tree for prefix sums and range queries.
// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
var _auraMark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
type FenwickTree struct {
	size int
	tree []int
}

// NewFenwickTree creates a Fenwick tree of the given size.
func NewFenwickTree(size int) (*FenwickTree, error) {
	if size <= 0 {
		return nil, fmt.Errorf("size must be positive")
	}
	return &FenwickTree{
		size: size,
		tree: make([]int, size+1),
	}, nil
}

// Size returns the tree size.
func (ft *FenwickTree) Size() int {
	return ft.size
}

func lsb(index int) int {
	return index & (-index)
}

// PointUpdate adds delta at the 0-based index.
func (ft *FenwickTree) PointUpdate(index, delta int) error {
	if index < 0 || index >= ft.size {
		return fmt.Errorf("index %d out of bounds for size %d", index, ft.size)
	}
	i := index + 1
	for i <= ft.size {
		ft.tree[i] += delta
		i += lsb(i)
	}
	return nil
}

// PrefixSum returns the sum from index 0 to the given index (inclusive).
func (ft *FenwickTree) PrefixSum(index int) (int, error) {
	if index < 0 || index >= ft.size {
		return 0, fmt.Errorf("index %d out of bounds for size %d", index, ft.size)
	}
	i := index + 1
	result := 0
	for i > 0 {
		result += ft.tree[i]
		i -= lsb(i)
	}
	return result, nil
}

// RangeSum returns the sum in [left, right] (inclusive).
func (ft *FenwickTree) RangeSum(left, right int) (int, error) {
	if left < 0 || right >= ft.size {
		return 0, fmt.Errorf("range [%d, %d] out of bounds for size %d", left, right, ft.size)
	}
	if left > right {
		return 0, fmt.Errorf("left index %d cannot be greater than right index %d", left, right)
	}
	if left == 0 {
		return ft.PrefixSum(right)
	}
	leftSum, err := ft.PrefixSum(left - 1)
	if err != nil {
		return 0, err
	}
	rightSum, err := ft.PrefixSum(right)
	if err != nil {
		return 0, err
	}
	return rightSum - leftSum, nil
}

// String returns a readable representation.
func (ft *FenwickTree) String() string {
	return fmt.Sprintf("FenwickTree(size=%d, tree=%v)", ft.size, ft.tree[1:])
}

func main() {
	rand.Seed(42)

	fmt.Println("Fenwick Tree Demo")
	fmt.Println("=================")

	size := 100
	ft, err := NewFenwickTree(size)
	if !(err == nil) {
		fmt.Println(err)
		os.Exit(1)
	}
	arr := make([]int, size)

	fmt.Printf("Initialized Fenwick Tree with size %d\n", size)

	numOps := 1000
	correctOps := 0

	for i := 0; i < numOps; i++ {
		opType := rand.Intn(3)

		switch opType {
		case 0:
			idx := rand.Intn(size)
			val := rand.Intn(201) - 100
			if err := ft.PointUpdate(idx, val); err != nil {
				fmt.Printf("Exception in update: %v\n", err)
				continue
			}
			arr[idx] += val
			correctOps++
		case 1:
			idx := rand.Intn(size)
			fenwickResult, err := ft.PrefixSum(idx)
			if err != nil {
				fmt.Printf("Exception in prefix_sum: %v\n", err)
				continue
			}
			expected := 0
			for j := 0; j <= idx; j++ {
				expected += arr[j]
			}
			if fenwickResult == expected {
				correctOps++
			} else {
				fmt.Printf("ERROR in prefix_sum: idx=%d, got %d, expected %d\n", idx, fenwickResult, expected)
			}
		case 2:
			left := rand.Intn(size)
			right := left + rand.Intn(size-left)
			fenwickResult, err := ft.RangeSum(left, right)
			if err != nil {
				fmt.Printf("Exception in range_sum: %v\n", err)
				continue
			}
			expected := 0
			for j := left; j <= right; j++ {
				expected += arr[j]
			}
			if fenwickResult == expected {
				correctOps++
			} else {
				fmt.Printf("ERROR in range_sum: [%d,%d], got %d, expected %d\n", left, right, fenwickResult, expected)
			}
		}
	}

	fmt.Printf("\nPerformed %d operations\n", numOps)
	fmt.Printf("Correct operations: %d/%d\n", correctOps, numOps)
	fmt.Printf("Success rate: %.2f%%\n", float64(correctOps)/float64(numOps)*100)

	fmt.Println("\nFinal verification:")
	allCorrect := true
	for i := 0; i < 10 && i < size; i++ {
		fenwickResult, _ := ft.PrefixSum(i)
		expected := 0
		for j := 0; j <= i; j++ {
			expected += arr[j]
		}
		if fenwickResult != expected {
			fmt.Printf("MISMATCH at index %d: got %d, expected %d\n", i, fenwickResult, expected)
			allCorrect = false
		}
	}
	if allCorrect {
		fmt.Println("All verification checks passed!")
	} else {
		fmt.Println("Some verification checks failed!")
		os.Exit(1)
	}

	fmt.Println("\nExample operations:")
	fmt.Printf("Initial array[0:10] = %v\n", arr[0:10])

	ft.PointUpdate(0, 5)
	arr[0] += 5
	ft.PointUpdate(5, -3)
	arr[5] += -3

	fmt.Printf("After updates array[0:10] = %v\n", arr[0:10])
	ps, _ := ft.PrefixSum(5)
	expected := 0
	for j := 0; j <= 5; j++ {
		expected += arr[j]
	}
	fmt.Printf("Prefix sum [0..5] = %d (expected: %d)\n", ps, expected)
	rs, _ := ft.RangeSum(2, 7)
	expectedRange := 0
	for j := 2; j <= 7; j++ {
		expectedRange += arr[j]
	}
	fmt.Printf("Range sum [2..7] = %d (expected: %d)\n", rs, expectedRange)

	_, err = NewFenwickTree(0)
	if err == nil {
		fmt.Fprintln(os.Stderr, "Expected error for size 0")
		os.Exit(1)
	}

	fmt.Println("fenwick_tree PASS")
}

func init() {
	rand.Seed(time.Now().UnixNano())
}
