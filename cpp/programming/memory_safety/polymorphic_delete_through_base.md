# polymorphic_delete_through_base

**Pattern:** polymorphic_delete_through_base

**Why you would reach for this:** Deleting a derived object through a base pointer tells `delete` to release an object of the base's size and to run the base's destructor. If the derived part is bigger or owns anything, both are wrong. This pattern is the rule that any class deleted through a base pointer needs a virtual destructor.

**Entry fn:** `virtual ~BaseVirtual()` — a virtual destructor that makes `delete` ask the object what it actually is.

**Valid input:** A class hierarchy (`Base`/`Derived`, where `Derived` adds a 16-int pad, `1..16`) deleted through a base pointer. The base must have a virtual destructor so the correct destructor chain and size are used.

**Core:** Deleting a derived object through a base pointer without a virtual destructor tells `delete` to release an object of the base's size and run the base's destructor — both wrong when the derived part is bigger. The unsafe arm deletes a `Derived` through a non-virtual `Base*`; the deallocation size and destructor chain are taken from the static type, and the sanitizer reports a size mismatch. The safe arm's base has a virtual destructor, so `delete` dispatches to the derived destructor and the correct size. A virtual destructor is the mechanism — it makes `delete` ask the object what it actually is.

**Assert:** The planted truth is that the virtual destructor sums to `EXPECT_SUM = 136` and destroys both derived and base (1+1). Real SUCCESS line from the evidence file:
```
PASS: virtual destructor summed 136 destroyed 1+1 and the size mismatch was caught as new-delete-type-mismatch
```

**⚠️ Defect it prevents:** The disaster is the deallocation size and destructor chain being taken from the static type, not the dynamic type — a new-delete-type-mismatch. Real FAILURE line from the evidence file:
```
==1435267==ERROR: AddressSanitizer: new-delete-type-mismatch on 0x507000000100 in thread T0:
```
