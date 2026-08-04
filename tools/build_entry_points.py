#!/usr/bin/env python3
"""build_entry_points — the shared entry-point registry for every downstream sweep.

WHY THIS EXISTS. Both planned sweeps (mutation ruler, input-robustness prober) need the same
answer first: *what do I call, and with what shape?* 904 of 1,500 patterns have no documented
entry function. If each harness invents its own discovery they will disagree, and every
disagreement will look like a defect in a pattern rather than in the tools. So discovery happens
ONCE, here, and the harnesses consume the result.

⛔ NOTHING IS IMPORTED OR EXECUTED. Python is parsed with `ast`. All 676 python patterns carry a
__main__ guard so importing would be *probably* safe — "probably safe" is not a thing this library
does, and a parser cannot be sabotaged by the file it reads.

⛔ NEVER INFER. A pattern whose entry point cannot be derived is recorded with
`derived_from: "none"` and is COUNTED, not skipped. The gap is the most useful thing in the file:
it is the exact denominator of what any sweep can honestly cover.

Output: tools/entry_points.jsonl — one record per pattern FILE (census law: a stem in two spheres
is two patterns). tools/ is not a signed subtree, so writing here needs no re-sign.
"""
import ast, json, re, sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "tools" / "entry_points.jsonl"

LANES = {"python": "*.py", "r": "*.R", "cpp": "*.cpp",
         "go": "*.go", "rust": "*.rs", "javascript": "*.js"}

# Helpers the retrofit injected — never a pattern's entry point.
SKIP_FN = re.compile(r"^(_aura_validate_|_?test_|main$|__)")
# A matrix-shaped parameter, in any of the library's annotation dialects.
MATRIX_ANN = re.compile(r"list\s*\[\s*list|List\s*\[\s*List|\[\]\[\]|Vec<\s*Vec|float\s*\*\s*\*", re.I)
MATRIX_NAME = re.compile(r"^(X|A|mat|matrix|data|features|design)$", re.I)

DOC_ENTRY = re.compile(r"^\*\*Entry fn:\*\*\s*(.+)$", re.M)

# A 1-D sequence a prober CAN synthesise (targets, labels, a sample). Distinct from `matrix`
# and from `other` — an `other` required parameter (k, alpha, a prior, a callable) is the thing
# that makes a function undrivable, and it must be named as such rather than guessed at.
VECTOR_ANN = re.compile(r"list\s*\[\s*(float|int)|List\s*\[\s*(float|int)|\[\]float|Vec<\s*f64", re.I)
VECTOR_NAME = re.compile(r"^(y|labels?|target|targets|values|samples?|obs|observations)$", re.I)


def param_role(name: str, ann) -> str:
    """matrix | vector | other. `other` required => the prober cannot drive this function."""
    if (ann and MATRIX_ANN.search(ann)) or MATRIX_NAME.match(name):
        return "matrix"
    if (ann and VECTOR_ANN.search(ann)) or VECTOR_NAME.match(name):
        return "vector"
    return "other"


def domain_of(shelf: str, category: str, fns) -> str:
    """Classify what KIND of input this pattern takes. The robustness sweep's six classes are
    numerical-linear-algebra classes; applying them outside `numeric-matrix` produces noise."""
    blob = f"{shelf} {category}".lower()
    if any(f["matrix_param"] for f in fns):
        return "numeric-matrix"
    if "system-administration" in blob or "sysadmin" in blob:
        return "sysadmin"
    if any(k in blob for k in ("concurren", "resilience", "scheduling", "process")):
        return "concurrency"
    if any(k in blob for k in ("data_structure", "data-structure", "programming", "algorithm")):
        return "data-structure"
    if "data-science" in blob or "statistic" in blob:
        return "numeric-scalar"
    return "unclassified"


def py_entries(p: Path):
    """Top-level callables, from the AST. Returns [] when the file will not parse."""
    try:
        tree = ast.parse(p.read_text(encoding="utf-8", errors="replace"))
    except SyntaxError:
        return None
    out = []
    for node in tree.body:                       # top level only — nested defs are helpers
        if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            continue
        if SKIP_FN.match(node.name):
            continue
        # Defaults bind to the LAST n positional args. Without this, a prober cannot tell a
        # parameter it MUST supply from one it may omit — which is precisely why the 172-pattern
        # run produced 549 TypeErrors and read them as a robustness finding.
        n_req = len(node.args.args) - len(node.args.defaults)
        params = []
        for i, a in enumerate(node.args.args):
            ann = ast.unparse(a.annotation) if a.annotation is not None else None
            params.append({"name": a.arg, "annotation": ann, "required": i < n_req,
                           "role": param_role(a.arg, ann)})
        matrix = any(q["role"] == "matrix" for q in params)
        drivable = all((not q["required"]) or q["role"] in ("matrix", "vector")
                       for q in params) and matrix
        out.append({"name": node.name, "params": params,
                    "matrix_param": matrix, "drivable": drivable})
    return out


def doc_entries(card: Path):
    """Fall back to the audited doc's `Entry fn:` line for lanes we cannot parse."""
    if not card.exists():
        return []
    m = DOC_ENTRY.search(card.read_text(encoding="utf-8", errors="replace"))
    if not m:
        return []
    out = []
    for chunk in m.group(1).split("`"):
        chunk = chunk.strip()
        if not chunk or chunk in (",", "·"):
            continue
        name = re.search(r"(?:def|func|fn)?\s*([A-Za-z_]\w*)\s*\(", chunk)
        if name and not SKIP_FN.match(name.group(1)):
            # Doc-derived entries carry no parsed signature, so drivability is UNKNOWN — and
            # unknown must never read as drivable. Fail closed.
            out.append({"name": name.group(1), "params": [],
                        "matrix_param": bool(MATRIX_ANN.search(chunk)), "drivable": False})
    return out


def main() -> int:
    records, stats = [], Counter()
    for lane, glob in LANES.items():
        for p in sorted((ROOT / lane).rglob(glob)):
            if "__pycache__" in p.parts:
                continue
            rel = p.relative_to(ROOT)
            parts = rel.parts
            shelf = parts[1] if len(parts) > 2 else lane
            category = parts[-2] if len(parts) > 2 else ""

            if lane == "python":
                fns = py_entries(p)
                if fns is None:
                    derived, fns = "parse-error", []
                elif fns:
                    derived = "ast"
                else:
                    fns, derived = doc_entries(p.with_suffix(".md")), "doc"
            else:
                fns = doc_entries(p.with_suffix(".md"))
                derived = "doc" if fns else "none"
            if not fns:
                derived = "parse-error" if derived == "parse-error" else "none"

            dom = domain_of(shelf, category, fns)
            stats[f"{lane}:{derived}"] += 1
            stats[f"domain:{dom}"] += 1
            if derived != "none" and dom == "numeric-matrix":
                stats["SWEEPABLE"] += 1
            records.append({
                "file": str(rel), "lane": lane, "shelf": shelf, "category": category,
                "id": p.stem, "domain": dom, "derived_from": derived,
                "callable": lane in ("python", "r", "javascript"),
                "entry_fns": fns,
            })

    OUT.write_text("\n".join(json.dumps(r, ensure_ascii=False) for r in records) + "\n",
                   encoding="utf-8")

    print(f"wrote {OUT.relative_to(ROOT)} — {len(records)} pattern files\n")
    print("derivation, per lane:")
    for lane in LANES:
        row = {k.split(":")[1]: v for k, v in stats.items() if k.startswith(f"{lane}:")}
        tot = sum(row.values())
        none = row.get("none", 0)
        print(f"  {lane:<11} {tot:>5} files — " +
              " · ".join(f"{k}:{v}" for k, v in sorted(row.items())) +
              f"   [NO ENTRY POINT: {none}]")
    print("\ndomain:")
    for k, v in sorted(((k, v) for k, v in stats.items() if k.startswith("domain:")),
                       key=lambda x: -x[1]):
        print(f"  {k.split(':')[1]:<18} {v:>5}")
    print(f"\n⭐ SWEEPABLE (entry point known AND numeric-matrix): {stats['SWEEPABLE']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
