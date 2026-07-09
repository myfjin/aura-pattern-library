#!/usr/bin/env python3
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

from typing import List, Optional, Tuple
import sys


class Block:
    """Represents a memory block with size and allocation status."""
    
    def __init__(self, start: int, size: int, is_free: bool = True):
        self.start = start
        self.size = size
        self.is_free = is_free
        self.next: Optional['Block'] = None
        self.prev: Optional['Block'] = None
    
    def __repr__(self):
        return f"Block(start={self.start}, size={self.size}, is_free={self.is_free})"


class FreeList:
    """Manages a list of free memory blocks."""
    
    def __init__(self):
        self.head: Optional[Block] = None
    
    def insert(self, block: Block) -> None:
        """Insert a block into the free list, keeping it sorted by address."""
        if not self.head:
            self.head = block
            return
        
        # Insert at beginning if block is before head
        if block.start < self.head.start:
            block.next = self.head
            self.head.prev = block
            self.head = block
            return
        
        # Find insertion point
        current = self.head
        while current.next and current.next.start < block.start:
            current = current.next
        
        # Insert block
        block.next = current.next
        if current.next:
            current.next.prev = block
        current.next = block
        block.prev = current
    
    def remove(self, block: Block) -> None:
        """Remove a block from the free list."""
        if block.prev:
            block.prev.next = block.next
        else:
            self.head = block.next
        
        if block.next:
            block.next.prev = block.prev
    
    def find_best_fit(self, size: int) -> Optional[Block]:
        """Find the best fitting free block for the requested size."""
        best_block: Optional[Block] = None
        current = self.head
        
        while current:
            if current.is_free and current.size >= size:
                if not best_block or current.size < best_block.size:
                    best_block = current
            current = current.next
        
        return best_block
    
    def coalesce(self) -> None:
        """Merge adjacent free blocks."""
        current = self.head
        while current and current.next:
            # If both blocks are free and adjacent
            if (current.is_free and current.next.is_free and 
                current.start + current.size == current.next.start):
                # Merge blocks
                current.size += current.next.size
                # Remove next block from list
                next_block = current.next
                current.next = next_block.next
                if next_block.next:
                    next_block.next.prev = current
            else:
                current = current.next


class Allocator:
    """Simple memory allocator simulator using best-fit algorithm."""
    
    def __init__(self, total_size: int):
        if total_size <= 0:
            raise ValueError("Total size must be positive")
        
        self.total_size = total_size
        self.free_list = FreeList()
        # Initialize with one large free block
        initial_block = Block(0, total_size)
        self.free_list.insert(initial_block)
        self.allocated_blocks: List[Block] = []
    
    def allocate(self, size: int) -> Optional[int]:
        """Allocate a block of memory of the given size.
        
        Args:
            size: Size of memory to allocate
            
        Returns:
            Starting address of allocated block, or None if allocation fails
        """
        if size <= 0:
            raise ValueError("Allocation size must be positive")
        
        # Find best fitting free block
        free_block = self.free_list.find_best_fit(size)
        if not free_block:
            return None  # Not enough free space
        
        # Remove the block from free list
        self.free_list.remove(free_block)
        
        # If block is larger than needed, split it
        if free_block.size > size:
            # Create new free block with remaining space
            remaining_block = Block(
                start=free_block.start + size,
                size=free_block.size - size,
                is_free=True
            )
            self.free_list.insert(remaining_block)
        
        # Update the allocated block
        free_block.size = size
        free_block.is_free = False
        self.allocated_blocks.append(free_block)
        
        return free_block.start
    
    def free(self, address: int) -> bool:
        """Free a previously allocated block.
        
        Args:
            address: Starting address of block to free
            
        Returns:
            True if successful, False if address not found
        """
        # Find the allocated block
        block_to_free: Optional[Block] = None
        for block in self.allocated_blocks:
            if block.start == address:
                block_to_free = block
                break
        
        if not block_to_free:
            return False
        
        # Mark as free and move to free list
        block_to_free.is_free = True
        self.allocated_blocks.remove(block_to_free)
        self.free_list.insert(block_to_free)
        
        # Coalesce adjacent free blocks
        self.free_list.coalesce()
        
        return True
    
    def fragmentation_report(self) -> Tuple[int, int, float]:
        """Generate fragmentation statistics.
        
        Returns:
            Tuple of (free_blocks_count, free_memory, fragmentation_ratio)
        """
        free_blocks_count = 0
        free_memory = 0
        current = self.free_list.head
        
        while current:
            if current.is_free:
                free_blocks_count += 1
                free_memory += current.size
            current = current.next
        
        if free_memory == 0:
            fragmentation_ratio = 0.0
        else:
            # Fragmentation = (free_memory - size_of_largest_free_block) / free_memory
            largest_free = 0
            current = self.free_list.head
            while current:
                if current.is_free and current.size > largest_free:
                    largest_free = current.size
                current = current.next
            fragmentation_ratio = (free_memory - largest_free) / free_memory if free_memory > 0 else 0.0
        
        return free_blocks_count, free_memory, fragmentation_ratio
    
    def __str__(self) -> str:
        """String representation of current memory state."""
        result = "Memory State:\n"
        current = self.free_list.head
        while current:
            status = "FREE" if current.is_free else "ALLOCATED"
            result += f"  {status}: start={current.start}, size={current.size}\n"
            current = current.next
        return result


def main():
    """Demonstrate the memory allocator functionality."""
    print("Memory Allocator Simulator Demo")
    print("=" * 40)
    
    # Create allocator with 1000 bytes
    allocator = Allocator(1000)
    print(f"Initialized allocator with {allocator.total_size} bytes")
    
    # Allocate some blocks
    allocations = []
    sizes = [100, 200, 50, 300, 75, 150]
    
    print("\nAllocating blocks:")
    for i, size in enumerate(sizes):
        addr = allocator.allocate(size)
        if addr is not None:
            allocations.append((addr, size))
            print(f"  Allocated {size} bytes at address {addr}")
        else:
            print(f"  Failed to allocate {size} bytes")
    
    print(f"\n{allocator}")
    
    # Free some blocks
    print("Freeing some blocks:")
    # Free every other allocation
    for i in range(0, len(allocations), 2):
        addr, size = allocations[i]
        if allocator.free(addr):
            print(f"  Freed block of {size} bytes at address {addr}")
        else:
            print(f"  Failed to free block at address {addr}")
    
    print(f"\n{allocator}")
    
    # Try to allocate more memory
    print("Trying to allocate more memory:")
    new_sizes = [80, 250, 60]
    for size in new_sizes:
        addr = allocator.allocate(size)
        if addr is not None:
            print(f"  Allocated {size} bytes at address {addr}")
        else:
            print(f"  Failed to allocate {size} bytes")
    
    # Final state and fragmentation report
    print(f"\n{allocator}")
    free_blocks, free_mem, frag_ratio = allocator.fragmentation_report()
    print(f"Fragmentation Report:")
    print(f"  Free blocks: {free_blocks}")
    print(f"  Free memory: {free_mem} bytes")
    print(f"  Fragmentation ratio: {frag_ratio:.2%}")
    
    # Test error conditions
    print("\nTesting error conditions:")
    try:
        Allocator(-100)
    except ValueError as e:
        print(f"  Caught expected error: {e}")
    
    try:
        allocator.allocate(-50)
    except ValueError as e:
        print(f"  Caught expected error: {e}")
    
    success = allocator.free(9999)  # Non-existent address
    print(f"  Freeing non-existent block: {'Success' if success else 'Failed'}")


if __name__ == "__main__":
    main()