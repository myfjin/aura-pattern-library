# allocation_failure_path

**Pattern:** allocation_failure_path

**Why you would reach for this:** Allocation failure is a path almost nobody exercises, so it is where cleanup code goes to die. A pool that returns `nullptr` when exhausted does not throw, does not warn, and does not undo anything — and the natural reaction, an early return, walks away from every block already taken. The failure is silent and it is a leak, not a crash. This pattern is the rule that the failure path must release everything acquired so far.

**Entry fn:** the failure-path loop that frees every block acquired so far when the pool runs out.

**Valid input:** A fixed-capacity pool (capacity 3) from which 5 blocks are requested. When the pool returns `nullptr`, the failure path must free the 3 blocks already taken.

**Core:** A pool that returns `nullptr` when exhausted does not throw, warn, or undo anything — so an early return walks away from every block already taken. The unsafe arm's `do_leak` returns early when the pool runs out, abandoning the 3 blocks already allocated. The safe arm's failure path frees every block acquired so far and resets the pool's taken count. Releasing everything on the failure path is the mechanism — partial success is not success; a function that acquires N resources must free them on the way out of any exit.

**Assert:** The planted truth is that the failure path frees `CAP = 3` blocks and resets `taken` to 0. Real SUCCESS line from the evidence file:
```
PASS: failure path freed 3 blocks taken 3 and the early-return leak was caught as detected memory leaks
```

**⚠️ Defect it prevents:** The disaster is the blocks already taken from the pool being abandoned when the loop returns early — a memory leak. Real FAILURE line from the evidence file:
```
==1440406==ERROR: LeakSanitizer: detected memory leaks
```
