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
    """Self-test: exact address arithmetic, best-fit choice, fragmentation
    failure, and full coalescing back to one block."""
    a = Allocator(1000)

    # Sequential allocation carves from address 0 upward — addresses are exact.
    assert a.allocate(100) == 0, "first allocation must start at 0"
    assert a.allocate(200) == 100, "second allocation must start at 100"
    assert a.allocate(50) == 300, "third allocation must start at 300"

    # Free the middle 200-byte block: two holes now exist (200 @100, 650 @350).
    assert a.free(100) is True
    blocks, free_mem, frag = a.fragmentation_report()
    assert blocks == 2 and free_mem == 850, f"expected 2 holes/850 free, got {blocks}/{free_mem}"
    assert abs(frag - 200.0 / 850.0) < 1e-12, f"fragmentation must be 200/850, got {frag}"

    # BEST-fit: a 150-byte request must take the 200-hole (@100), not the 650 tail.
    addr = a.allocate(150)
    assert addr == 100, f"best-fit must choose the 200-byte hole at 100, got {addr}"
    blocks, free_mem, _ = a.fragmentation_report()
    assert blocks == 2 and free_mem == 700, "split must leave a 50-byte remainder + tail"

    # THE DISASTER fragmentation causes: 700 bytes are free, but no contiguous
    # hole fits 700 — the allocation must fail honestly, not corrupt.
    assert a.allocate(700) is None, "allocator satisfied a request no hole can hold"

    # Freeing everything must coalesce back to ONE block of exactly 1000.
    assert a.free(100) is True   # 150-block; merges with the 50-remainder
    assert a.free(300) is True   # 50-block; bridges to the tail
    assert a.free(0) is True     # first 100-block; completes the merge
    blocks, free_mem, frag = a.fragmentation_report()
    assert (blocks, free_mem, frag) == (1, 1000, 0.0), \
        f"full coalesce must yield (1, 1000, 0.0), got ({blocks}, {free_mem}, {frag})"

    # After coalescing, the full arena is allocatable again.
    assert a.allocate(1000) == 0, "coalesced arena must satisfy a full-size allocation"
    assert a.allocate(1) is None, "empty arena granted an allocation"
    assert a.free(0) is True

    # Refusals: double free, unknown address, invalid sizes.
    assert a.free(9999) is False, "freeing an unknown address reported success"
    assert a.free(0) is False, "double free reported success"
    for ctor_arg in (0, -100):
        try:
            Allocator(ctor_arg)
            assert False, f"Allocator({ctor_arg}) accepted"
        except ValueError:
            pass
    try:
        a.allocate(-50)
        assert False, "negative allocation accepted"
    except ValueError:
        pass

    print("free_list_allocator: exact addresses, best-fit @100, frag 200/850, "
          "700-in-700-free refused, coalesce → (1, 1000, 0.0) — PASS")


if __name__ == "__main__":
    main()