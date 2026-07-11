# AURA Pattern Library

> Verified, attributed, multi-language reference patterns. Every file runs; every
> file is marked and signed. **© Reality Optimizer.**

The AURA Pattern Library is a curated set of implementation patterns across
languages and spheres. Its distinguishing discipline: **verification is the entry
criterion** — every pattern is independently run-gated, and nothing that fails the
honesty gate ships. Each file carries a visible attribution mark, invisible
tracing channels, and a cryptographic signature.

## What's inside

| Language / sphere | Patterns | Gate | Signature |
|---|---|---|---|
| `python/programming` | 99 | run-gated | Ed25519 signed |
| `python/data-science` | 377 | run-gated | Ed25519 signed |
| `python/system-administration` | 200 | run-gated | Ed25519 signed |
| `r/` | 60 | run-gated | Ed25519 signed |
| `cpp/` | 370 | g++ **and** clang, `-std=c++17 -pedantic` | Ed25519 signed |
| `rust/` | 200 | `rustc -O -D warnings` | Ed25519 signed |
| `go/` | 93 | `go build` + run + 3× determinism | Ed25519 signed |

**934 unique patterns · 1,399 verified files across five languages · 463 patterns in
two or more languages.** Language twins are strictly downstream of their Python/R source:
each carries the source's proven claims (same assert, same tolerance) and is coupling-pinned
to the source's hash. Four data-science patterns are held in `_quarantine/` (assert-linter
REJECTs) and are **not** shipped.

## Layout

```
python/{programming,data-science,system-administration}/<category>/<pattern>.py
r/<category>/<pattern>.R
cpp/data-science/<category>/<pattern>.cpp      # language twins, final-approved only
rust/<category>/<pattern>.rs
go/<shelf>/<category>/<pattern>.go
_quarantine/                   # excluded, with reason + date
CATALOG.md                     # ID-keyed master: pattern ID -> languages + category
MANIFEST.json                  # machine-readable index
library_verify.py              # the library's CI (run it)
SYNC.md                        # how the snapshot re-pulls from its sources
```

The **basename is the canonical pattern ID**: `cpp/data-science/streaming_and_sketches/hyperloglog_distinct.cpp`
shares the ID of `python/data-science/streaming_and_sketches/hyperloglog_distinct.py`.

## Attribution, not prevention (the honest boundary)

- The **watermark** answers *who* holds this copy — visible mark + invisible
  redundant channels that survive reformatting, for leak-tracing.
- The **signature** answers whether files are *genuinely ours and unaltered*.
- Neither prevents copying — you cannot prevent copying on someone's own disk.
  They make a copy **checkable**. That is the whole claim, and the only one.

Marks and signatures are produced by [folder-nature](https://github.com/myfjin/folder-nature).

## Verify it yourself

```bash
python3 library_verify.py            # signatures + watermarks + catalog parity
python3 library_verify.py --gate     # also compile/run every file (slow)
```

## Tiers & licensing

Standard single-sphere 100-lists · composed/unique lists · **free for
universities/teaching with attribution**. Copy-count tiers (cooperative limiter):
Personal 1–3 · Team 0–9 · Enterprise (alphanumeric >10). See `CATALOG.md`.

## License

Apache-2.0 (see `LICENSE`). Attribution required; the trademark/owner mark is
reserved (Apache §6 grants no trademark rights).
