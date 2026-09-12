# Token Bucket Rate Limiter

**File:** `python/system-administration/resource-guards/token_bucket_limiter.py`
**Sphere:** System Administration — Resource Guards
**Status:** ❌/⚠ ILLIA-TO-RULE (audit 2026-07-19)

---

## What it solves

Stop a flood. An API, a login endpoint, a disk writer — anything that must serve a *steady* rate and reject the rest. The token bucket: tokens drip into a bucket at a fixed rate; each request spends one; empty bucket → request denied. Steady service, bursts absorbed up to the bucket size.

**When to use:** You need to rate-limit access to a resource — API calls per second, logins per minute, disk writes per second. The token bucket allows short bursts (up to its capacity) while enforcing a steady long-term rate.

---

## ⚠️ The defect (a stateful bug, invisible in a return value — the first of its kind in this audit)

- Real token buckets have a **capacity** (burst size). This code: `tokens += elapsed * rate` with NO upper bound. Idle the limiter and tokens accumulate forever.
- **Proven:** rate=10, idle 100s → next 200 requests ALL granted instantly, 800 tokens still in hand. A rate limiter that permits a 200-op burst is not limiting during exactly the traffic spike it exists to stop. The name "limiter" is a claim the code doesn't honor after idle.
- This is why sysadmin patterns need a different audit lens than DS: the bug isn't in any number the function returns — it's in **behavior accumulated over time**.

---

## Valid inputs (the contract — to be enforced per fix #10)

| Input | Domain | Today → |
|---|---|---|
| `tokens_per_sec` | > 0 | 0 → never grants (defensible, undeclared) · **-10 → tokens go increasingly NEGATIVE, silent** |
| (missing param) | burst capacity / max tokens | absent — the root defect |

---

## How inputs shape the output

- **rate = tokens per second granted** in steady state (demo: 10/sec → ~20 granted in 2s, 980 denied).
- **After idle, rate stops bounding anything** until the accumulated tokens drain — the flaw. A correct bucket caps accumulation at its burst size.
- **negative rate** makes the token balance drift down forever — a nonsense state with no guard.

---

## Worked example — and the SILENT-SUCCESS defect

```
$ python3 python/system-administration/resource-guards/token_bucket_limiter.py
$ echo $?
0
```

**There is no output.** Success and "the script never ran" are identical to the eye — a direct violation of Illia's requirement ② (know what output you get on success/failure). Every sysadmin harness in the library shares this; the retrofit adds a receipts line: `token_bucket: granted=20 denied=980 over 2.0s PASS`.

---

## Failure modes (audited by hand)

| Trigger | What happens today | Meaning |
|---|---|---|
| 100s idle then burst | **200/200 granted** — no cap | the limiter doesn't limit after idle (functional ❌) |
| `rate = -10` | tokens go negative silently | B5, no guard |
| `rate = 0` | all denied (never refills) | correct but undeclared |
| baseline success | **zero output** | silent success — violates requirement ② |

---

## Provenance

Machine-VERIFIED (frozen ruler) · Illia's audit 2026-07-19: missing-capacity behavioral defect (Fable-proven) + silent-success harness defect; severity ruling pending · evidence: `output/manual_audit_2026-07-19.csv` · fixes: queue #10 + sysadmin-wide CLASS fix
