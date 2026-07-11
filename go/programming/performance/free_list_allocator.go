package main

import (
	"fmt"
	"os"
)

// Block represents a memory block with size and allocation status.
// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
var _auraMark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
type Block struct {
	start  int
	size   int
	isFree bool
	next   *Block
	prev   *Block
}

// FreeList manages a list of free memory blocks.
type FreeList struct {
	head *Block
}

func NewFreeList() *FreeList {
	return &FreeList{}
}

func (fl *FreeList) insert(block *Block) {
	if fl.head == nil {
		fl.head = block
		return
	}

	if block.start < fl.head.start {
		block.next = fl.head
		fl.head.prev = block
		fl.head = block
		return
	}

	current := fl.head
	for current.next != nil && current.next.start < block.start {
		current = current.next
	}

	block.next = current.next
	if current.next != nil {
		current.next.prev = block
	}
	current.next = block
	block.prev = current
}

func (fl *FreeList) remove(block *Block) {
	if block.prev != nil {
		block.prev.next = block.next
	} else {
		fl.head = block.next
	}

	if block.next != nil {
		block.next.prev = block.prev
	}
}

func (fl *FreeList) findBestFit(size int) *Block {
	var best *Block
	current := fl.head

	for current != nil {
		if current.isFree && current.size >= size {
			if best == nil || current.size < best.size {
				best = current
			}
		}
		current = current.next
	}

	return best
}

func (fl *FreeList) coalesce() {
	current := fl.head
	for current != nil && current.next != nil {
		if current.isFree && current.next.isFree && current.start+current.size == current.next.start {
			current.size += current.next.size
			nextBlock := current.next
			current.next = nextBlock.next
			if nextBlock.next != nil {
				nextBlock.next.prev = current
			}
		} else {
			current = current.next
		}
	}
}

// Allocator is a simple memory allocator simulator using best-fit algorithm.
type Allocator struct {
	totalSize       int
	freeList        *FreeList
	allocatedBlocks []*Block
}

func NewAllocator(totalSize int) (*Allocator, error) {
	if totalSize <= 0 {
		return nil, fmt.Errorf("total size must be positive")
	}

	allocator := &Allocator{
		totalSize:       totalSize,
		freeList:        NewFreeList(),
		allocatedBlocks: []*Block{},
	}
	initialBlock := &Block{start: 0, size: totalSize, isFree: true}
	allocator.freeList.insert(initialBlock)
	return allocator, nil
}

func (a *Allocator) Allocate(size int) (int, error) {
	if size <= 0 {
		return -1, fmt.Errorf("allocation size must be positive")
	}

	freeBlock := a.freeList.findBestFit(size)
	if freeBlock == nil {
		return -1, nil
	}

	a.freeList.remove(freeBlock)

	if freeBlock.size > size {
		remaining := &Block{
			start:  freeBlock.start + size,
			size:   freeBlock.size - size,
			isFree: true,
		}
		a.freeList.insert(remaining)
	}

	freeBlock.size = size
	freeBlock.isFree = false
	a.allocatedBlocks = append(a.allocatedBlocks, freeBlock)

	return freeBlock.start, nil
}

func (a *Allocator) Free(address int) bool {
	var target *Block
	for _, block := range a.allocatedBlocks {
		if block.start == address {
			target = block
			break
		}
	}

	if target == nil {
		return false
	}

	target.isFree = true
	a.freeList.insert(target)
	a.freeList.coalesce()

	for i, block := range a.allocatedBlocks {
		if block == target {
			a.allocatedBlocks = append(a.allocatedBlocks[:i], a.allocatedBlocks[i+1:]...)
			break
		}
	}

	return true
}

func (a *Allocator) FragmentationReport() (int, int, float64) {
	freeBlocksCount := 0
	freeMemory := 0
	largestFree := 0

	current := a.freeList.head
	for current != nil {
		if current.isFree {
			freeBlocksCount++
			freeMemory += current.size
			if current.size > largestFree {
				largestFree = current.size
			}
		}
		current = current.next
	}

	fragmentationRatio := 0.0
	if freeMemory > 0 {
		fragmentationRatio = float64(freeMemory-largestFree) / float64(freeMemory)
	}

	return freeBlocksCount, freeMemory, fragmentationRatio
}

func (a *Allocator) String() string {
	result := "Memory State:\n"
	current := a.freeList.head
	for current != nil {
		status := "FREE"
		if !current.isFree {
			status = "ALLOCATED"
		}
		result += fmt.Sprintf("  %s: start=%d, size=%d\n", status, current.start, current.size)
		current = current.next
	}
	return result
}

func main() {
	fmt.Println("Memory Allocator Simulator Demo")
	fmt.Println("=============================")

	allocator, err := NewAllocator(1000)
	if !(err == nil) {
		fmt.Fprintf(os.Stderr, "failed to create allocator: %v\n", err)
		os.Exit(1)
	}
	fmt.Printf("Initialized allocator with %d bytes\n", allocator.totalSize)

	var allocations [][2]int
	sizes := []int{100, 200, 50, 300, 75, 150}

	fmt.Println("\nAllocating blocks:")
	for _, size := range sizes {
		addr, err := allocator.Allocate(size)
		if !(err == nil) {
			fmt.Fprintf(os.Stderr, "allocation error: %v\n", err)
			os.Exit(1)
		}
		if addr >= 0 {
			allocations = append(allocations, [2]int{addr, size})
			fmt.Printf("  Allocated %d bytes at address %d\n", size, addr)
		} else {
			fmt.Printf("  Failed to allocate %d bytes\n", size)
		}
	}

	fmt.Printf("\n%s", allocator)

	fmt.Println("Freeing some blocks:")
	for i := 0; i < len(allocations); i += 2 {
		addr, size := allocations[i][0], allocations[i][1]
		if allocator.Free(addr) {
			fmt.Printf("  Freed block of %d bytes at address %d\n", size, addr)
		} else {
			fmt.Printf("  Failed to free block at address %d\n", addr)
		}
	}

	fmt.Printf("\n%s", allocator)

	fmt.Println("Trying to allocate more memory:")
	newSizes := []int{80, 250, 60}
	for _, size := range newSizes {
		addr, err := allocator.Allocate(size)
		if !(err == nil) {
			fmt.Fprintf(os.Stderr, "allocation error: %v\n", err)
			os.Exit(1)
		}
		if addr >= 0 {
			fmt.Printf("  Allocated %d bytes at address %d\n", size, addr)
		} else {
			fmt.Printf("  Failed to allocate %d bytes\n", size)
		}
	}

	fmt.Printf("\n%s", allocator)
	freeBlocks, freeMem, fragRatio := allocator.FragmentationReport()
	fmt.Println("Fragmentation Report:")
	fmt.Printf("  Free blocks: %d\n", freeBlocks)
	fmt.Printf("  Free memory: %d bytes\n", freeMem)
	fmt.Printf("  Fragmentation ratio: %.2f%%\n", fragRatio*100)

	fmt.Println("\nTesting error conditions:")
	if _, err := NewAllocator(-100); err != nil {
		fmt.Printf("  Caught expected error: %v\n", err)
	} else {
		fmt.Fprintln(os.Stderr, "Expected error for negative total size")
		os.Exit(1)
	}

	if _, err := allocator.Allocate(-50); err != nil {
		fmt.Printf("  Caught expected error: %v\n", err)
	} else {
		fmt.Fprintln(os.Stderr, "Expected error for negative allocation size")
		os.Exit(1)
	}

	success := allocator.Free(9999)
	fmt.Printf("  Freeing non-existent block: %s\n", map[bool]string{true: "Success", false: "Failed"}[success])

	fmt.Println("free_list_allocator PASS")
}
