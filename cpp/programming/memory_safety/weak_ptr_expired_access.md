# weak_ptr_expired_access

**Pattern:** weak_ptr_expired_access

**Why you would reach for this:** `weak_ptr` exists so an observer can ask "is it still there?" before touching it — and the answer is only honest if you ask through `lock()`. A raw pointer cached out of the owner carries no expiry information and cannot tell you it has died. This pattern is the rule that an observer must re-acquire through `lock()` at every use.

**Entry fn:** `auto locked = w.lock();` — re-acquiring a `shared_ptr` from the `weak_ptr` at every use.

**Valid input:** A `weak_ptr<Buf>` observing a `shared_ptr<Buf>`-owned object with a 16-int buffer (`1..16`). The observer must lock before each use and check the lock result.

**Core:** A raw pointer cached out of a `shared_ptr`'s internal object carries no expiry information — when the owner releases, the cached pointer reads freed memory. The unsafe arm caches `sp->d` and reads it after the owner dies. The safe arm holds a `weak_ptr` and re-acquires through `lock()` at every use; after the owner dies, `expired()` is true and `lock()` returns null. Re-acquiring through `lock()` is the mechanism — it is the only honest way to ask whether the object is still there.

**Assert:** The planted truth is that the `weak_ptr` lock sums to `EXPECT_SUM = 136` while the owner is alive and is expired after the owner dies. Real SUCCESS line from the evidence file:
```
PASS: weak_ptr lock summed 136 and expired after owner died, cached pointer caught as heap-use-after-free
```

**⚠️ Defect it prevents:** The disaster is the cached pointer reading freed memory after the `shared_ptr` releases — a heap-use-after-free. Real FAILURE line from the evidence file:
```
==1435783==ERROR: AddressSanitizer: heap-use-after-free on address 0x506000000020 at pc 0x59d1f4e5186b bp 0x7ffd22957320 sp 0x7ffd22957310
```
