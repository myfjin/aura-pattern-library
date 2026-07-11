package main

import (
	"fmt"
	"math"
	"os"
)

// Block represents a memory block.
// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
var _auraMark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
type Block struct {
	Start  int
	Size   int
	IsFree bool
	Next   *Block
	Prev   *Block
}

// FreeList manages free memory blocks.
type FreeList struct {
	Head *Block
}

func newFreeList() *FreeList {
	return &FreeList{}
}

func (fl *FreeList) insert(block *Block) {
	if fl.Head == nil {
		fl.Head = block
		return
	}
	if block.Start < fl.Head.Start {
		block.Next = fl.Head
		fl.Head.Prev = block
		fl.Head = block
		return
	}
	current := fl.Head
	for current.Next != nil && current.Next.Start < block.Start {
		current = current.Next
	}
	block.Next = current.Next
	if current.Next != nil {
		current.Next.Prev = block
	}
	current.Next = block
	block.Prev = current
}

func (fl *FreeList) remove(block *Block) {
	if block.Prev != nil {
		block.Prev.Next = block.Next
	} else {
		fl.Head = block.Next
	}
	if block.Next != nil {
		block.Next.Prev = block.Prev
	}
}

func (fl *FreeList) findBestFit(size int) *Block {
	var best *Block
	current := fl.Head
	for current != nil {
		if current.IsFree && current.Size >= size {
			if best == nil || current.Size < best.Size {
				best = current
			}
		}
		current = current.Next
	}
	return best
}

func (fl *FreeList) coalesce() {
	current := fl.Head
	for current != nil && current.Next != nil {
		if current.IsFree && current.Next.IsFree && current.Start+current.Size == current.Next.Start {
			current.Size += current.Next.Size
			nextBlock := current.Next
			current.Next = nextBlock.Next
			if nextBlock.Next != nil {
				nextBlock.Next.Prev = current
			}
		} else {
			current = current.Next
		}
	}
}

// Allocator manages memory using best-fit.
type Allocator struct {
	TotalSize       int
	FreeList        *FreeList
	AllocatedBlocks []*Block
}

func newAllocator(totalSize int) (*Allocator, error) {
	if totalSize <= 0 {
		return nil, fmt.Errorf("total size must be positive")
	}
	alloc := &Allocator{
		TotalSize:       totalSize,
		FreeList:        newFreeList(),
		AllocatedBlocks: []*Block{},
	}
	initialBlock := &Block{Start: 0, Size: totalSize, IsFree: true}
	alloc.FreeList.insert(initialBlock)
	return alloc, nil
}

func (a *Allocator) allocate(size int) (int, error) {
	if size <= 0 {
		return 0, fmt.Errorf("allocation size must be positive")
	}
	freeBlock := a.FreeList.findBestFit(size)
	if freeBlock == nil {
		return -1, nil
	}
	a.FreeList.remove(freeBlock)
	if freeBlock.Size > size {
		remaining := &Block{
			Start:  freeBlock.Start + size,
			Size:   freeBlock.Size - size,
			IsFree: true,
		}
		a.FreeList.insert(remaining)
	}
	freeBlock.Size = size
	freeBlock.IsFree = false
	a.AllocatedBlocks = append(a.AllocatedBlocks, freeBlock)
	return freeBlock.Start, nil
}

func (a *Allocator) free(address int) bool {
	var blockToFree *Block
	for _, block := range a.AllocatedBlocks {
		if block.Start == address {
			blockToFree = block
			break
		}
	}
	if blockToFree == nil {
		return false
	}
	blockToFree.IsFree = true
	// Remove from allocated list
	newAllocated := a.AllocatedBlocks[:0]
	for _, block := range a.AllocatedBlocks {
		if block.Start != address {
			newAllocated = append(newAllocated, block)
		}
	}
	a.AllocatedBlocks = newAllocated
	a.FreeList.insert(blockToFree)
	a.FreeList.coalesce()
	return true
}

func (a *Allocator) fragmentationReport() (int, int, float64) {
	freeBlocksCount := 0
	freeMemory := 0
	current := a.FreeList.Head
	for current != nil {
		if current.IsFree {
			freeBlocksCount++
			freeMemory += current.Size
		}
		current = current.Next
	}
	if freeMemory == 0 {
		return freeBlocksCount, freeMemory, 0.0
	}
	largestFree := 0
	current = a.FreeList.Head
	for current != nil {
		if current.IsFree && current.Size > largestFree {
			largestFree = current.Size
		}
		current = current.Next
	}
	fragmentationRatio := float64(freeMemory-largestFree) / float64(freeMemory)
	return freeBlocksCount, freeMemory, fragmentationRatio
}

func main() {
	a, err := newAllocator(1000)
	if err != nil {
		fmt.Fprintf(os.Stderr, "allocator create: %v\n", err)
		os.Exit(1)
	}

	addr0, err := a.allocate(100)
	if err != nil || !(addr0 == 0) {
		fmt.Fprintf(os.Stderr, "first allocation must start at 0, got %d err %v\n", addr0, err)
		os.Exit(1)
	}
	addr1, err := a.allocate(200)
	if err != nil || !(addr1 == 100) {
		fmt.Fprintf(os.Stderr, "second allocation must start at 100, got %d err %v\n", addr1, err)
		os.Exit(1)
	}
	addr2, err := a.allocate(50)
	if err != nil || !(addr2 == 300) {
		fmt.Fprintf(os.Stderr, "third allocation must start at 300, got %d err %v\n", addr2, err)
		os.Exit(1)
	}
	if !(a.AllocatedBlocks[2].Size == 50) {
		fmt.Fprintf(os.Stderr, "third allocated block size must be 50\n")
		os.Exit(1)
	}

	if !(a.free(100)) {
		fmt.Fprintf(os.Stderr, "free 100 reported failure\n")
		os.Exit(1)
	}
	blocks, freeMem, frag := a.fragmentationReport()
	if !(blocks == 2 && freeMem == 850) {
		fmt.Fprintf(os.Stderr, "expected 2 holes/850 free, got %d/%d\n", blocks, freeMem)
		os.Exit(1)
	}
	if !(math.Abs(frag-200.0/850.0) < 1e-12) {
		fmt.Fprintf(os.Stderr, "fragmentation must be 200/850, got %v\n", frag)
		os.Exit(1)
	}

	addr, err := a.allocate(150)
	if err != nil || !(addr == 100) {
		fmt.Fprintf(os.Stderr, "best-fit must choose the 200-byte hole at 100, got %d err %v\n", addr, err)
		os.Exit(1)
	}
	blocks, freeMem, _ = a.fragmentationReport()
	if !(blocks == 2 && freeMem == 700) {
		fmt.Fprintf(os.Stderr, "split must leave a 50-byte remainder + tail, got %d/%d\n", blocks, freeMem)
		os.Exit(1)
	}

	addr700, err := a.allocate(700)
	if err != nil || !(addr700 == -1) {
		fmt.Fprintf(os.Stderr, "allocator satisfied a request no hole can hold\n")
		os.Exit(1)
	}

	if !(a.free(100)) {
		fmt.Fprintf(os.Stderr, "free 100 (150-block) reported failure\n")
		os.Exit(1)
	}
	if !(a.free(300)) {
		fmt.Fprintf(os.Stderr, "free 300 reported failure\n")
		os.Exit(1)
	}
	if !(a.free(0)) {
		fmt.Fprintf(os.Stderr, "free 0 reported failure\n")
		os.Exit(1)
	}
	blocks, freeMem, frag = a.fragmentationReport()
	if !((blocks == 1) && (freeMem == 1000) && (frag == 0.0)) {
		fmt.Fprintf(os.Stderr, "full coalesce must yield (1, 1000, 0.0), got (%d, %d, %v)\n", blocks, freeMem, frag)
		os.Exit(1)
	}

	addrFull, err := a.allocate(1000)
	if err != nil || !(addrFull == 0) {
		fmt.Fprintf(os.Stderr, "coalesced arena must satisfy a full-size allocation, got %d err %v\n", addrFull, err)
		os.Exit(1)
	}
	addrOne, err := a.allocate(1)
	if err != nil || !(addrOne == -1) {
		fmt.Fprintf(os.Stderr, "empty arena granted an allocation\n")
		os.Exit(1)
	}
	if !(a.free(0)) {
		fmt.Fprintf(os.Stderr, "free 0 (full block) reported failure\n")
		os.Exit(1)
	}

	if !(a.free(9999) == false) {
		fmt.Fprintf(os.Stderr, "freeing an unknown address reported success\n")
		os.Exit(1)
	}
	if !(a.free(0) == false) {
		fmt.Fprintf(os.Stderr, "double free reported success\n")
		os.Exit(1)
	}
	for _, ctorArg := range []int{0, -100} {
		_, err := newAllocator(ctorArg)
		if err == nil {
			fmt.Fprintf(os.Stderr, "Allocator(%d) accepted\n", ctorArg)
			os.Exit(1)
		}
	}
	_, err = a.allocate(-50)
	if err == nil {
		fmt.Fprintf(os.Stderr, "negative allocation accepted\n")
		os.Exit(1)
	}

	fmt.Println("free_list_allocator: exact addresses, best-fit @100, frag 200/850, 700-in-700-free refused, coalesce -> (1, 1000, 0.0) -- PASS")
}
