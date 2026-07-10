#!/usr/bin/env python3
"""
merge_sorted_streams: Merge N sorted streams into one sorted stream.
THE ONE LAW: Merge streams, assert exact global sortedness and no data loss.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import heapq

def merge_sorted_streams(streams, key=None):
    """
    Merge multiple sorted streams into one sorted stream.
    streams: list of iterables (each sorted).
    key: function to extract sort key (default: identity).
    Return merged sorted list.
    """
    if not streams:
        return []

    result = []
    # Create iterators for each stream.
    stream_iters = [iter(stream) for stream in streams]

    # Create a min-heap with (key_val, stream_idx, item).
    heap = []

    # Initialize heap with first item from each stream.
    for idx, stream_iter in enumerate(stream_iters):
        try:
            item = next(stream_iter)
            key_val = key(item) if key else item
            heapq.heappush(heap, (key_val, idx, item))
        except StopIteration:
            pass

    # Extract items in sorted order.
    while heap:
        key_val, idx, item = heapq.heappop(heap)
        result.append(item)

        # Try to get next item from the same stream.
        try:
            next_item = next(stream_iters[idx])
            next_key = key(next_item) if key else next_item
            heapq.heappush(heap, (next_key, idx, next_item))
        except StopIteration:
            pass

    return result

def verify_sorted(items, key=None):
    """Verify that items are in sorted order. Return True or False."""
    for i in range(len(items) - 1):
        val_curr = key(items[i]) if key else items[i]
        val_next = key(items[i+1]) if key else items[i+1]
        if val_curr > val_next:
            return False
    return True

def main():
    # Synthetic sorted streams.
    stream1 = [1, 4, 7]
    stream2 = [2, 5, 8]
    stream3 = [3, 6, 9]

    merged = merge_sorted_streams([stream1, stream2, stream3])

    # Verify exact merged result.
    assert merged == [1, 2, 3, 4, 5, 6, 7, 8, 9], f"Expected 1-9 sorted, got {merged}"

    # Verify global sortedness.
    assert verify_sorted(merged), "Merged list should be sorted"

    # FAILURE SIMULATION: Not merging correctly.
    def merge_sorted_streams_broken(streams):
        """Broken: just concatenates streams."""
        result = []
        for stream in streams:
            result.extend(stream)
        return result

    broken = merge_sorted_streams_broken([stream1, stream2, stream3])
    assert broken == [1, 4, 7, 2, 5, 8, 3, 6, 9], "Broken should concatenate"
    assert not verify_sorted(broken), "Broken merge should NOT be sorted"

    # Test with overlapping ranges.
    stream_a = [1, 3, 5, 9]
    stream_b = [2, 4, 6, 8]
    merged_overlap = merge_sorted_streams([stream_a, stream_b])
    assert merged_overlap == [1, 2, 3, 4, 5, 6, 8, 9], f"Overlapping merge failed: {merged_overlap}"
    assert verify_sorted(merged_overlap), "Overlapping merge should be sorted"

    # Edge case: Empty streams.
    empty = merge_sorted_streams([[], []])
    assert empty == [], "Merging empty streams should give empty result"

    # Edge case: Single stream.
    single = merge_sorted_streams([[5, 3, 1]])
    assert single == [5, 3, 1], "Single unsorted stream should be returned as-is (no sorting)"

    # Edge case: Streams with duplicate values.
    dup_stream1 = [1, 3, 3, 5]
    dup_stream2 = [2, 3, 4, 4]
    merged_dup = merge_sorted_streams([dup_stream1, dup_stream2])
    assert merged_dup == [1, 2, 3, 3, 3, 4, 4, 5], f"Duplicates should be preserved, got {merged_dup}"
    assert verify_sorted(merged_dup), "Merge with duplicates should be sorted"

    # Test with key function (sort by absolute value).
    # Streams must be sorted by the key function.
    keyed_stream1 = [1, -2, -5]  # Sorted by abs: 1, 2, 5
    keyed_stream2 = [-1, 3, 4]   # Sorted by abs: 1, 3, 4
    merged_keyed = merge_sorted_streams([keyed_stream1, keyed_stream2], key=abs)
    # Merged by absolute value: 1 (abs=1), -1 (abs=1), -2 (abs=2), 3 (abs=3), 4 (abs=4), -5 (abs=5)
    assert verify_sorted(merged_keyed, key=abs), "Keyed merge should be sorted by key"
    # Check that all items are present.
    assert sorted(merged_keyed, key=abs) == [1, -1, -2, 3, 4, -5], f"Items should all be present, got {merged_keyed}"

    # Verify no data loss: count items before and after.
    all_items = [1, 4, 7, 2, 5, 8, 3, 6, 9]
    streams = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    merged_check = merge_sorted_streams(streams)
    assert len(merged_check) == len(all_items), "Merge should not lose items"
    assert sorted(merged_check) == sorted(all_items), "Merge should preserve all items"

    print("✓ merge_sorted_streams passed")

if __name__ == '__main__':
    main()
