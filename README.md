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
| `go/programming` | 45 | `go build` + run + 3× determinism | Ed25519 signed |
| `go/system-administration` | 58 | `go build` + run + 3× determinism | Ed25519 signed |
| `javascript/` | 91 | `node` (exit 0) | Ed25519 signed |

**1,035 patterns · 1,500 verified files across six languages · 466 patterns in
two or more languages.** (1,024 unique IDs — 11 catalog rows share a stem across
spheres, e.g. `circuit_breaker` lives in programming, sysadmin *and* rust-systems;
by the census law a stem in two spheres is two patterns.) Nine shelves, 144
categories. **JavaScript, like Python and R, is a source lane** — its patterns were
written directly in the language and have no twins, which is why the
two-or-more-languages count is unchanged. Language twins are strictly downstream of their Python/R source:
each carries the source's proven claims (same assert, same tolerance) and is coupling-pinned
to the source's hash. Four data-science patterns are excluded from the tree entirely
(assert-linter REJECTs, listed in `_quarantine/QUARANTINE.md`) and are **not** shipped.

## Browse every pattern

**[PATTERNS_INDEX.md](PATTERNS_INDEX.md)** — a direct link and a description for every one
of the 1,500 files, grouped by shelf and category, with each pattern's language twins named.
Descriptions are extracted from the files themselves at generation time, so the index cannot
drift from the code; regenerate with `python3 build_patterns_index.py`.

**JavaScript lane — measured limits.** Every JS pattern has a companion `.md` recording what
its self-test actually proves and its known defects, plus
[`javascript/ROBUSTNESS.md`](javascript/ROBUSTNESS.md) — the measured behaviour of all 91
patterns on six input classes beyond their own fixtures. **This sweep has been run on the
JavaScript lane only**; the other lanes carry generated verification evidence and have not
been measured this way.

## Layout

```
python/{programming,data-science,system-administration}/<category>/<pattern>.py
r/<category>/<pattern>.R
cpp/data-science/<category>/<pattern>.cpp      # language twins, final-approved only
rust/<category>/<pattern>.rs
go/<shelf>/<category>/<pattern>.go
javascript/<category>/<pattern>.js
_quarantine/                   # excluded, with reason + date
PATTERNS_INDEX.md              # every pattern: direct link + description + twins
CATALOG.md                     # ID-keyed master: pattern ID -> languages + category
MANIFEST.json                  # machine-readable index
library_verify.py              # the library's CI (run it)
build_patterns_index.py        # regenerates PATTERNS_INDEX.md from the files themselves
tag_folders.py                 # semantic identity: a .folder-nature in every folder
SYNC.md                        # how the snapshot re-pulls from its sources
```

Every folder also carries a `.folder-nature` — machine-readable semantic identity
(being / purpose / tags) — enforced tree-wide by `.folder-nature-root.yaml`
(`require_nature: true`), so the full folder-nature stack is live here:
**identity + mark + signature**.

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
folder-nature verify . --root --pubkey aura-signing.pub   # one-verdict tree self-check
```

## Tiers & licensing

Standard single-sphere 100-lists · composed/unique lists · **free for
universities/teaching with attribution**. Copy-count tiers (cooperative limiter):
Personal 1–3 · Team 0–9 · Enterprise (alphanumeric >10). See `CATALOG.md`.

## Adjacent trees

**`../aura-pattern-library-pending/`** — an *unsigned* queue of patterns salvaged from harvest-workspace dup folders that (a) are not in this library and (b) have real value worth review before ingest. Each candidate carries its own `.md` note explaining tier (A = ingest-ready modulo review; B = needs listed fixes), origin folder, and the specific defects blocking canonical entry. When a pattern there is fixed + reviewer-approved, it enters this library via `ingest.py` / `ingest_cpp_native.py` (Illia's yes only) and gets signed here.

## License

Apache-2.0 (see `LICENSE`). Attribution required; the trademark/owner mark is
reserved (Apache §6 grants no trademark rights).
