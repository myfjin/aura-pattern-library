# shared_ptr_reference_cycle_leak

**Pattern:** shared_ptr_reference_cycle_leak

**Why you would reach for this:** `shared_ptr` frees when the count hits zero, and two nodes pointing at each other keep each other's count at one forever — reference counting does not collect cycles. When you build bidirectional links between `shared_ptr`-owned nodes, both nodes leak because neither count ever reaches zero. This pattern is the rule that exactly one leg of a cycle must be `weak_ptr` — the non-owning one.

**Entry fn:** `std::weak_ptr<NodeWeak> back;` — the non-owning back-link in a cycle, with `std::shared_ptr<NodeWeak> fwd;` as the owning forward-link.

**Valid input:** Two nodes linked in a cycle, each holding a value (`EXPECT = 4242`). Exactly one leg of the cycle must be a `weak_ptr` so the cycle can be broken.

**Core:** Two `shared_ptr`s pointing at each other keep each other's reference count at one forever, so neither node is ever freed — a reference cycle that reference counting cannot collect. The unsafe arm links two `shared_ptr` nodes in both directions; leaving scope leaves both counts at one and both leak. The safe arm makes one leg a `weak_ptr`, which does not own; when the owning links are released, the counts drop to zero and both nodes are destroyed. A `weak_ptr` on one leg is the mechanism — it breaks the cycle so the counts can reach zero.

**Assert:** The planted truth is that the `weak_ptr` breaks the cycle, recovering `EXPECT = 4242` and destroying exactly 2 nodes. Real SUCCESS line from the evidence file:
```
PASS: weak_ptr broke cycle recovered 4242 destroyed 2 and the cycle leak was caught as detected memory leaks
```

**⚠️ Defect it prevents:** The disaster is both nodes leaking because neither count ever reaches zero — a memory leak. Real FAILURE line from the evidence file:
```
==1431526==ERROR: LeakSanitizer: detected memory leaks
```
