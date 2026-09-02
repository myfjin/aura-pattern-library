# partially_constructed_cleanup

**Pattern:** partially_constructed_cleanup

**Why you would reach for this:** If a constructor throws, the object never existed so its destructor never runs — but members already constructed are destroyed. Raw pointer members are not members that clean up, so a raw pointer allocated before the throw is never freed. This pattern is the rule for making members themselves owners (`unique_ptr`) so they are destroyed correctly even on the throwing path.

**Entry fn:** `std::unique_ptr<int[]> a;` — a member that is itself an owner, so it cleans up when the constructor throws.

**Valid input:** A class whose constructor allocates a 32-int member (`0..31`) and then throws after the first allocation. The already-constructed members must be owners so they are destroyed during the failed construction.

**Core:** When a constructor throws, the object never fully exists, so its destructor never runs — but every member already constructed is destroyed. The unsafe arm's `HalfUnsafe` has raw `int*` members and a destructor that never runs; the `a` block allocated before the throw leaks. The safe arm's `HalfSafe` holds its members in `std::unique_ptr`; when the constructor throws, the already-constructed `unique_ptr` member is destroyed and releases its block. Members that are themselves owners is the mechanism — they clean up correctly even on the throwing path.

**Assert:** The planted truth is that the `unique_ptr` member is cleaned up on the throwing constructor and the success path sums to `EXPECT_SUM = 496`. Real SUCCESS line from the evidence file:
```
PASS: unique_ptr member cleaned up on throwing ctor summing 496 and the raw leak was caught as detected memory leaks
```

**⚠️ Defect it prevents:** The disaster is a raw pointer member allocated before the throw never being freed — a memory leak. Real FAILURE line from the evidence file:
```
==1422034==ERROR: LeakSanitizer: detected memory leaks
```
