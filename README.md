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
| `python/data-science` | 370 | run-gated | Ed25519 signed |
| `r/` | 60 | run-gated | Ed25519 signed |
| `cpp/`, `go/` | 0 (empty-ready) | — | twins ingest on approval |

**529 shippable patterns · 527 unique IDs.** Four data-science patterns are held in
`_quarantine/` (assert-linter REJECTs) and are **not** shipped.

## Layout

```
python/{programming,data-science}/<category>/<pattern>.py
r/<category>/<pattern>.R
cpp/  go/                      # language twins (ingested only when final-approved)
_quarantine/                   # excluded, with reason + date
CATALOG.md                     # ID-keyed master: pattern ID -> languages + category
MANIFEST.json                  # machine-readable index
library_verify.py              # the library's CI (run it)
SYNC.md                        # how the snapshot re-pulls from its sources
```

The **basename is the canonical pattern ID**: a future `cpp/data-science/hyperloglog_distinct.cpp`
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
