# aligned_storage_lifetime

**Pattern:** aligned_storage_lifetime

**Why you would reach for this:** This is the mirror image of placement new. Once you call the destructor explicitly, the object's lifetime is over — but the storage is still there, still readable, and the pointer still looks good. Nothing about the type or the compiler marks the moment. This pattern is the rule that an explicit destructor call ends the object's lifetime, and every access after it is undefined.

**Entry fn:** `bool engaged` — a flag saying whether the slot is engaged, preventing use-after-destroy.

**Valid input:** An `Own` (owning an 8-int buffer, `1..8`) constructed in `aligned_storage` and explicitly destroyed. Access after destroy must be refused via the engaged flag.

**Core:** An explicit destructor call ends the object's lifetime, but the storage remains readable and the pointer still looks valid — nothing marks the moment. The unsafe arm constructs an `Own` in `aligned_storage`, calls `~Own()` (which frees the owned buffer), and then reads through the pointer into freed memory. The safe arm tracks an `engaged` flag: set true after construction, set false after the explicit destroy, and any access after destroy is refused. The engaged flag is the mechanism — it marks the moment the lifetime ends and prevents use-after-destroy.

**Assert:** The planted truth is that the engaged flag guards the slot, summing to `EXPECT_SUM = 36` and refusing access after destroy. Real SUCCESS line from the evidence file:
```
PASS: engaged flag guarded slot summing 36 refused after destroy and the freed read was caught as heap-use-after-free
```

**⚠️ Defect it prevents:** The disaster is the owned array being freed by the destructor, then the pointer reading freed memory — a heap-use-after-free. Real FAILURE line from the evidence file:
```
==1440385==ERROR: AddressSanitizer: heap-use-after-free on address 0x503000000040 at pc 0x56a7075d5744 bp 0x7ffdc836e170 sp 0x7ffdc836e160
```
