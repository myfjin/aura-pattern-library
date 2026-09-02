# reference_into_erased_map_node

**Pattern:** reference_into_erased_map_node

**Why you would reach for this:** You cached a reference to a map entry for speed, then erased that key. A reference obtained from a map stays pointing at that element's node, and erasing the key deallocates the node — so the reference is freed memory, not stale-but-readable. This pattern is the rule for taking an owning copy before the erase.

**Entry fn:** `std::string owned = m.at(7);` — an owning copy taken before `m.erase(7)`.

**Valid input:** An `std::unordered_map<int, std::string>` with 50 entries, each a 64-char string of `'h'`, from which key 7 is about to be erased. The copy must be made while the node is still alive.

**Core:** A reference obtained from a map points into that element's node. The unsafe arm binds `const std::string& r = m.at(7)`, erases key 7, and then reads through `r` — the erase deallocated the node, so the read hits freed memory. The safe arm copies the value into an owning `std::string` before the erase, so the data lives in a separate buffer that survives the node's deallocation. Taking an owning copy before the erase is the mechanism — a reference into a removed node is freed memory.

**Assert:** The planted truth is that the owning copy sums to `EXPECT_SUM = 6656` and key 7 is no longer present in the map. Real SUCCESS line from the evidence file:
```
PASS: owning copy summed 6656 and the erased-map-node reference was caught as heap-use-after-free
```

**⚠️ Defect it prevents:** The disaster is the reference reading the freed node's memory after the key is erased — a heap-use-after-free. Real FAILURE line from the evidence file:
```
==1422121==ERROR: AddressSanitizer: heap-use-after-free on address 0x507000000410 at pc 0x5ca70dc9ddbc bp 0x7ffc3b65b1c0 sp 0x7ffc3b65b1b0
```
