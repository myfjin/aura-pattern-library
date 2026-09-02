# dangling_string_view_owner

**Pattern:** dangling_string_view_owner

**Why you would reach for this:** You are returning a `std::string_view` from a function, storing one past the owner's scope, or binding a view to a temporary — and you need to remember that a view is a borrow, not a copy. It does not keep its owner alive. This pattern is the rule for taking real ownership when the data must outlive the original owner.

**Entry fn:** `std::string owned_copy(*owner)` — copying the owner into a `std::string` takes ownership of the data.

**Valid input:** A heap-allocated `std::string` owner (length ≥ 80 to force heap allocation) whose contents you want to keep after the owner is destroyed. The copy must be made while the owner is still alive.

**Core:** `std::string_view` is a non-owning window over another object's buffer; it never extends the owner's lifetime. The unsafe arm creates a view into a heap `std::string`, deletes the owner, and then reads through the view — the buffer is already freed. The safe arm copies the owner into a new `std::string` before deleting the original, so the copy owns its own buffer and survives independently. Ownership transfer by copy is the mechanism; a view alone is never enough to keep data alive.

**Assert:** The planted truth is that the owning copy preserves the size `EXPECT_SIZE = 80` and every character is still `'x'`. Real SUCCESS line from the evidence file:
```
PASS: owning copy preserved size 80 and the dangling string_view was caught as heap-use-after-free
```

**⚠️ Defect it prevents:** The disaster is the view outliving its owner and reading freed heap memory — a heap-use-after-free. Real FAILURE line from the evidence file:
```
==1421812==ERROR: AddressSanitizer: heap-use-after-free on address 0x508000000020 at pc 0x5bb6ca02495b bp 0x7ffee9943700 sp 0x7ffee99436f0
```
