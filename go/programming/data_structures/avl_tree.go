package main

import (
	"fmt"
	"math"
	"math/rand"
	"os"
)

// AVLNode is a node class for AVL tree.
// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
var _auraMark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
type AVLNode struct {
	Key    int
	Left   *AVLNode
	Right  *AVLNode
	Height int
}

// NewAVLNode initializes an AVL node.
func NewAVLNode(key int) *AVLNode {
	return &AVLNode{Key: key, Height: 1}
}

// AVLTree is an AVL tree implementation with self-balancing properties.
type AVLTree struct {
	Root *AVLNode
}

// NewAVLTree initializes an empty AVL tree.
func NewAVLTree() *AVLTree {
	return &AVLTree{}
}

func (t *AVLTree) getHeight(node *AVLNode) int {
	if node == nil {
		return 0
	}
	return node.Height
}

func (t *AVLTree) getBalance(node *AVLNode) int {
	if node == nil {
		return 0
	}
	return t.getHeight(node.Left) - t.getHeight(node.Right)
}

func (t *AVLTree) updateHeight(node *AVLNode) {
	if node == nil {
		return
	}
	node.Height = 1 + int(math.Max(float64(t.getHeight(node.Left)), float64(t.getHeight(node.Right))))
}

func (t *AVLTree) rotateRight(y *AVLNode) *AVLNode {
	x := y.Left
	if x == nil {
		fmt.Fprintf(os.Stderr, "Cannot rotate right: left child is nil\n")
		os.Exit(1)
	}
	T2 := x.Right

	x.Right = y
	y.Left = T2

	t.updateHeight(y)
	t.updateHeight(x)

	return x
}

func (t *AVLTree) rotateLeft(x *AVLNode) *AVLNode {
	y := x.Right
	if y == nil {
		fmt.Fprintf(os.Stderr, "Cannot rotate left: right child is nil\n")
		os.Exit(1)
	}
	T2 := y.Left

	y.Left = x
	x.Right = T2

	t.updateHeight(x)
	t.updateHeight(y)

	return y
}

// Insert inserts a key into the AVL tree.
func (t *AVLTree) Insert(key int) {
	t.Root = t.insertRecursive(t.Root, key)
}

func (t *AVLTree) insertRecursive(node *AVLNode, key int) *AVLNode {
	if node == nil {
		return NewAVLNode(key)
	}

	if key < node.Key {
		node.Left = t.insertRecursive(node.Left, key)
	} else if key > node.Key {
		node.Right = t.insertRecursive(node.Right, key)
	} else {
		return node
	}

	t.updateHeight(node)
	balance := t.getBalance(node)

	// Left Left Case
	if balance > 1 && key < node.Left.Key {
		return t.rotateRight(node)
	}

	// Right Right Case
	if balance < -1 && key > node.Right.Key {
		return t.rotateLeft(node)
	}

	// Left Right Case
	if balance > 1 && key > node.Left.Key {
		node.Left = t.rotateLeft(node.Left)
		return t.rotateRight(node)
	}

	// Right Left Case
	if balance < -1 && key < node.Right.Key {
		node.Right = t.rotateRight(node.Right)
		return t.rotateLeft(node)
	}

	return node
}

// Delete deletes a key from the AVL tree.
func (t *AVLTree) Delete(key int) {
	t.Root = t.deleteRecursive(t.Root, key)
}

func (t *AVLTree) deleteRecursive(node *AVLNode, key int) *AVLNode {
	if node == nil {
		return node
	}

	if key < node.Key {
		node.Left = t.deleteRecursive(node.Left, key)
	} else if key > node.Key {
		node.Right = t.deleteRecursive(node.Right, key)
	} else {
		if node.Left == nil || node.Right == nil {
			var temp *AVLNode
			if node.Left != nil {
				temp = node.Left
			} else {
				temp = node.Right
			}
			if temp == nil {
				node = nil
			} else {
				node = temp
			}
		} else {
			temp := t.getMinValueNode(node.Right)
			node.Key = temp.Key
			node.Right = t.deleteRecursive(node.Right, temp.Key)
		}
	}

	if node == nil {
		return node
	}

	t.updateHeight(node)
	balance := t.getBalance(node)

	// Left Left Case
	if balance > 1 && t.getBalance(node.Left) >= 0 {
		return t.rotateRight(node)
	}

	// Left Right Case
	if balance > 1 && t.getBalance(node.Left) < 0 {
		node.Left = t.rotateLeft(node.Left)
		return t.rotateRight(node)
	}

	// Right Right Case
	if balance < -1 && t.getBalance(node.Right) <= 0 {
		return t.rotateLeft(node)
	}

	// Right Left Case
	if balance < -1 && t.getBalance(node.Right) > 0 {
		node.Right = t.rotateRight(node.Right)
		return t.rotateLeft(node)
	}

	return node
}

func (t *AVLTree) getMinValueNode(node *AVLNode) *AVLNode {
	current := node
	for current.Left != nil {
		current = current.Left
	}
	return current
}

// InorderTraversal performs inorder traversal of the tree.
func (t *AVLTree) InorderTraversal() []int {
	result := []int{}
	t.inorderRecursive(t.Root, &result)
	return result
}

func (t *AVLTree) inorderRecursive(node *AVLNode, result *[]int) {
	if node != nil {
		t.inorderRecursive(node.Left, result)
		*result = append(*result, node.Key)
		t.inorderRecursive(node.Right, result)
	}
}

// Search searches for a key in the AVL tree.
func (t *AVLTree) Search(key int) bool {
	return t.searchRecursive(t.Root, key)
}

func (t *AVLTree) searchRecursive(node *AVLNode, key int) bool {
	if node == nil {
		return false
	}
	if key == node.Key {
		return true
	} else if key < node.Key {
		return t.searchRecursive(node.Left, key)
	}
	return t.searchRecursive(node.Right, key)
}

// IsBalanced checks if the tree is balanced.
func (t *AVLTree) IsBalanced() bool {
	return t.isBalancedRecursive(t.Root)
}

func (t *AVLTree) isBalancedRecursive(node *AVLNode) bool {
	if node == nil {
		return true
	}
	balance := t.getBalance(node)
	if balance < -1 || balance > 1 {
		return false
	}
	return t.isBalancedRecursive(node.Left) && t.isBalancedRecursive(node.Right)
}

func main() {
	rand.Seed(42)

	avl := NewAVLTree()
	for key := 1; key <= 50; key++ {
		avl.Insert(key)
	}
	if !avl.IsBalanced() {
		fmt.Fprintln(os.Stderr, "sequential insert broke the AVL balance invariant")
		os.Exit(1)
	}
	if avl.Root.Height > 8 {
		fmt.Fprintf(os.Stderr, "50 nodes must fit in AVL height <=8, got %d (chain?)\n", avl.Root.Height)
		os.Exit(1)
	}
	if sliceEqual(avl.InorderTraversal(), rangeSlice(1, 51)) == false {
		fmt.Fprintln(os.Stderr, "inorder not sorted")
		os.Exit(1)
	}
	sum := 0
	for _, v := range avl.InorderTraversal() {
		sum += v
	}
	if sum != 1275 {
		fmt.Fprintln(os.Stderr, "1..50 must sum to 1275")
		os.Exit(1)
	}
	if !(avl.Search(25) && avl.Search(1) && avl.Search(50)) {
		fmt.Fprintln(os.Stderr, "search failed for present keys")
		os.Exit(1)
	}
	if avl.Search(100) || avl.Search(0) {
		fmt.Fprintln(os.Stderr, "search returned true for absent keys")
		os.Exit(1)
	}

	avl.Insert(25)
	if sliceEqual(avl.InorderTraversal(), rangeSlice(1, 51)) == false {
		fmt.Fprintln(os.Stderr, "duplicate insert changed the tree")
		os.Exit(1)
	}

	for _, key := range []int{10, 20, 30} {
		avl.Delete(key)
	}
	if !avl.IsBalanced() {
		fmt.Fprintln(os.Stderr, "delete broke the balance invariant")
		os.Exit(1)
	}
	remaining := avl.InorderTraversal()
	wantRemaining := []int{}
	for k := 1; k <= 50; k++ {
		if k != 10 && k != 20 && k != 30 {
			wantRemaining = append(wantRemaining, k)
		}
	}
	if !sliceEqual(remaining, wantRemaining) {
		fmt.Fprintln(os.Stderr, "remaining keys after delete mismatch")
		os.Exit(1)
	}
	if avl.Search(10) || !avl.Search(11) {
		fmt.Fprintln(os.Stderr, "search after delete mismatch")
		os.Exit(1)
	}

	fuzz := NewAVLTree()
	oracle := map[int]struct{}{}
	for step := 0; step < 600; step++ {
		k := rand.Intn(81)
		if rand.Float64() < 0.6 {
			fuzz.Insert(k)
			oracle[k] = struct{}{}
		} else if _, ok := oracle[k]; ok {
			fuzz.Delete(k)
			delete(oracle, k)
		}
		if !fuzz.IsBalanced() {
			fmt.Fprintf(os.Stderr, "balance invariant broken at step %d\n", step)
			os.Exit(1)
		}
	}
	if sliceEqual(fuzz.InorderTraversal(), sortedKeys(oracle)) == false {
		fmt.Fprintln(os.Stderr, "final tree diverged from set oracle")
		os.Exit(1)
	}
	if fuzz.Root != nil && fuzz.Root.Height > 10 {
		fmt.Fprintf(os.Stderr, "fuzz tree degenerated: height %d\n", fuzz.Root.Height)
		os.Exit(1)
	}

	fmt.Printf("avl_tree: 50 sequential inserts height %d (<=8) balanced, deletes rebalanced, 600-op set oracle agreed — PASS\n", avl.Root.Height)
}

func sliceEqual(a, b []int) bool {
	if len(a) != len(b) {
		return false
	}
	for i := range a {
		if a[i] != b[i] {
			return false
		}
	}
	return true
}

func rangeSlice(start, end int) []int {
	res := make([]int, 0, end-start)
	for i := start; i < end; i++ {
		res = append(res, i)
	}
	return res
}

func sortedKeys(m map[int]struct{}) []int {
	keys := make([]int, 0, len(m))
	for k := range m {
		keys = append(keys, k)
	}
	// simple insertion sort
	for i := 1; i < len(keys); i++ {
		j := i
		for j > 0 && keys[j-1] > keys[j] {
			keys[j-1], keys[j] = keys[j], keys[j-1]
			j--
		}
	}
	return keys
}
