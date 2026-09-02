# erase_loses_owned_resource

**Pattern:** erase_loses_owned_resource

**Why you would reach for this:** You are storing raw owning pointers in a container and erasing elements. Erasing an element destroys the pointer and abandons the pointee — the container shrinks, the memory does not. This pattern is the rule for using owning handles so that erase releases the resource.

**Entry fn:** `std::vector<OwnerSafe>` — a container whose elements own their buffers via `std::unique_ptr`.

**Valid input:** A vector of three elements, each owning a 16-int buffer (`1..16`), from which the middle element is erased. The elements must own their buffers so erase releases them.

**Core:** Erasing an element from a container of raw owning pointers destroys the pointer value but not the pointee — the erased element's buffer is abandoned and unreachable. The unsafe arm's `OwnerUnsafe` has no destructor, so erasing the middle element leaks its buffer. The safe arm's `OwnerSafe` holds its buffer in a `std::unique_ptr`; when the element is erased, the `unique_ptr` destructor releases the buffer. Owning handles in the container is the mechanism — erase releases the resource because the element owns it.

**Assert:** The planted truth is that after erasing the middle element the vector has size `EXPECT_SIZE_AFTER = 2` and the first element sums to `EXPECT_SUM = 136`. Real SUCCESS line from the evidence file:
```
PASS: unique_ptr erase released and first element summed 136 size 2, leak caught as detected memory leaks
```

**⚠️ Defect it prevents:** The disaster is the erased element's buffer being abandoned and unreachable — a memory leak. Real FAILURE line from the evidence file:
```
==1421916==ERROR: LeakSanitizer: detected memory leaks
```
