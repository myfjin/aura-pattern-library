# use_after_move_contract

**Pattern:** use_after_move_contract

**Why you would reach for this:** You captured a pointer into a container and then moved the container. The buffer went with the destination, so your pointer now tracks something you do not control — and if the destination is destroyed, the old pointer reads freed memory. This pattern is the rule for re-acquiring the pointer from the destination after the move.

**Entry fn:** `int* p = dst->data();` — re-acquiring the pointer from the destination after the move.

**Valid input:** A `std::vector<int>` with 100 elements (all `7`) that has been moved into a destination vector. The pointer must be re-acquired from the destination after the move, and the source (now empty) may be safely deleted.

**Core:** Moving a `std::vector` transfers its buffer to the destination; the source is left empty. The unsafe arm captures `src->data()`, moves the vector into `dst`, deletes `dst`, and then reads through the old pointer — the buffer was freed with the destination. The safe arm re-acquires the pointer from `dst` after the move, deletes the now-empty source, and reads through the live destination buffer. Re-acquiring from the destination is the mechanism — the pointer follows the buffer, which now belongs to the destination.

**Assert:** The planted truth is that the re-acquired pointer from the destination sums to `EXPECT = 700`. Real SUCCESS line from the evidence file:
```
PASS: re-acquired pointer from destination summed 700 and the moved-buffer dangling was caught as heap-use-after-free
```

**⚠️ Defect it prevents:** The disaster is the destination being destroyed and the old pointer reading freed memory — a heap-use-after-free. Real FAILURE line from the evidence file:
```
==1423062==ERROR: AddressSanitizer: heap-use-after-free on address 0x514000000040 at pc 0x62c29f04d949 bp 0x7ffe13aec050 sp 0x7ffe13aec040
```
