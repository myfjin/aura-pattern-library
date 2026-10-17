# `ingest*.py` — the 4-tool ingest flow

Four scripts share one contract: **stamp the watermark, sign the subtree, update `CATALOG.md`** — atomically, with no half-states left behind. They are the only tools that *add* patterns to the signed library.

| Script | Role |
|---|---|
| `ingest.py` | python ingest (programming / data-science / system-administration) |
| `ingest_cpp_native.py` | native cpp pattern ingest (not a conversion twin — a cpp-first pattern) |
| `ingest_go.py` | go twin ingest (a go version of a python/r source) |
| `ingest_go_native.py` | native go pattern ingest (a go-first pattern) |

---

## What question does it answer?

> *"How does a candidate pattern that passed harvest_gate become a signed, shippable member of the library?"*

The answer involves watermarks, signatures, and the catalog — in a specific order, with specific atomicity guarantees. These four scripts encapsulate that order so a human cannot do it wrong by hand.

---

## Dependencies

- Python ≥ 3.10
- **[folder-nature](https://github.com/myfjin/folder-nature)** — provides the signing primitives
- The target subtree's existing signing key material (handled through folder-nature, never exposed in CLI)
- For cpp/go: the respective toolchains, used to compile+run the self-test as a sanity check before accepting the pattern

---

## The contract (shared by all four scripts)

Each ingest operation is a **three-phase atomic transaction**:

1. **Stamp** — insert the watermark block into the file. Language-specific slot (see the "description slot" table in `.claude/skills/library-operations/SKILL.md`). The stamp happens **once at ingest and never again** — re-stamping is how you corrupt a mark that was fine.
2. **Sign** — re-sign the whole subtree the pattern just entered. The signature covers every file in that subtree; adding one changes the subtree hash, which requires a new signature. Any failure here leaves the pattern on disk but reports FAIL; `library_verify.py` would then go RED.
3. **Catalog** — update `CATALOG.md` with the new pattern's ID, languages, and category. The catalog is append-only in the "patterns added" direction; removals go through a different flow with explicit tombstoning.

If any phase fails, the whole ingest fails: the file is removed, the subtree is not re-signed, and the catalog is not touched. **Half-states are not allowed.**

---

## CLI — common shape

All four scripts share the same CLI shape:

```
ingest<_variant>.py <source-file> --sphere <sphere> --category <category>
```

| Arg | Meaning |
|---|---|
| `<source-file>` | path to the candidate pattern file (usually from `aura-pattern-library-pending/` or a harvest workspace) |
| `--sphere` | one of: `programming`, `data-science`, `system-administration` (python/go); or the language name for native (cpp, go) |
| `--category` | the category directory the pattern lands in (must match an existing category or be explicitly declared new) |

Variants add their own flags for toolchain-specific checks:

| Script | Extra flag(s) |
|---|---|
| `ingest.py` | `--doc` (expected description path, for cross-check) |
| `ingest_cpp_native.py` | `--std` (c++ standard, default `c++17`), `--opt` (optimization level) |
| `ingest_go.py` | `--source-id` (the python/r source ID this is a twin of) |
| `ingest_go_native.py` | nothing extra |

---

## Who runs ingest

**Only Illia.** From `.claude/skills/library-operations/SKILL.md`:

> "a pattern enters this library via `ingest.py` / `ingest_cpp_native.py` (**Illia's yes only**) and gets signed here."

The `pending/` tree is where salvage lives waiting for his review. Harvest workspaces are where the harvester explores. Neither is canonical. The ingest scripts are the gate between those staging areas and the signed library, and the gate's authority is Illia's.

Agents can prepare the inputs — generate the pattern, write the self-test, run `harvest_gate.py` to get a PASS verdict, write the description in the right slot per language, propose the sphere + category. But the ingest call itself needs human review.

---

## Why four scripts, not one

**The signing step is subtree-specific.** Python's ingest knows the python subtree's layout, python's description slot (`ast.get_docstring`), python's toolchain. The cpp native script knows cpp's slot (first `/* */` after the mark), cpp's compile+run sanity check (g++ -std=c++17), cpp's native-lane declaration in `MANIFEST.json`.

A single ingest tool would branch on language in every method. Four small scripts keep each one's logic linear and the signing-key handling identical in shape per subtree. Changes to one language's ingest don't risk the others.

**The twin/native distinction is a verdict, not a parameter.** `ingest_go.py` and `ingest_go_native.py` are different tools because the pattern is a different thing in each case: a twin inherits a python/r source's proven claims (same assert, same tolerance, coupling-pinned to the source hash); a native is a deliberate standalone. The script name forces the author to pick before they ingest.

---

## Guarantees after a successful ingest

- `library_verify.py` prints GREEN (signature + watermark + catalog + census all honest).
- `PATTERNS_INDEX.md` **does not** auto-regenerate — follow ingest with `python3 build_patterns_index.py` to refresh the browse surface.
- Any native pattern is declared in `MANIFEST.json["native_patterns"]`; `library_verify.py` rule (f) enforces this on the next run.
- The twin contract divergence number in `MANIFEST.json["twin_contract_divergence"]` is updated if the ingest changed it.

---

## When to run it

- **When a candidate pattern has passed `harvest_gate.py`** with a PASS or FLAG verdict (not INVALID, not CONTRADICTION).
- **When Illia says yes** to ingest after reviewing the harvest-gate output + the self-test.
- **One pattern at a time** — never batch an ingest run; the atomicity contract is per-operation, and batching obscures which pattern caused a RED.

---

## Known limits

- **Does not run attack probes.** The ingest's sanity check is compile+run clean, not attack-survival. For deep validation, see [`library_audit.md`](library_audit.md) and the Layer-2 pattern-scoring validators (`polyglot`, `executor`, `chaos_scan`, etc.).
- **Native-pattern declaration is manual.** The ingest does not infer native-vs-twin; the author picks the script name and must update `MANIFEST.json` if the pattern is native.
- **No bulk/undo.** Removing a pattern after ingest requires explicit tombstoning + re-sign + catalog edit; this is deliberate (public history is immutable).
- **Twin-of-source consistency** is not automatically checked here — a go twin ingested with a wrong `--source-id` will pass ingest and then be flagged by `library_verify.py`'s rule (f) on the next run. The author should pre-check before ingest.

---

## Related

- [`library_verify.md`](library_verify.md) — the gate that enforces ingest atomicity after the fact.
- [`library_audit.md`](library_audit.md) — the second-layer check that runs on the ingested pattern.
- [`harvest_gate.md`](harvest_gate.md) — the Phase A proposer whose PASS verdict is the entry criterion.
- [`.claude/skills/library-operations/SKILL.md`](https://github.com) — operator-side rules (the per-language description slot, the three lanes, the ONE LAW).
