#!/usr/bin/env python3
"""
oracle_sizer.py — size the POSITIVE-oracle gap honestly. A pattern is "green" (compiles +
self-test passes) but that is NOT correctness. A PASS needs a positive oracle proving the
pattern right on its domain. This tool statically classifies every pattern by what KIND of
positive oracle its own code affords — which decides auto-generatable vs needs-hand-audit.

Buckets (most-automatable first):
  ROUNDTRIP   paired inverse fns (encode/decode, serialize/recover, forward/inverse, to_/from_)
              -> auto: assert decode(encode(x)) == x over random x. Cheapest, strongest.
  SELF_REF    self-test ALREADY compares against an independent reference (2nd computation /
              stdlib / brute force) -> auto: lift that comparison into a probe (like the R pair).
  INVARIANT   code/docstring states a hard property (sum->1, monotonic, never false-neg,
              exactly-once, >=0) -> semi-auto: encode the named invariant as a check.
  NUMERIC     numeric fn with NO reference and NO stated invariant -> needs a hand-derived
              closed-form/brute-force truth (the bayes_factor / log_rank class). HAND.
  OPAQUE      no clear oracle affordance (side-effecting, plumbing, config) -> HAND or N/A.

This is a STATIC estimate of affordance, not a guarantee any auto-oracle will pass — it sizes
the work, it doesn't do it.
"""
import os, re, ast, glob, json, sys
from collections import Counter, defaultdict

LIB = os.path.expanduser("~/aura-pattern-library")
HERE = os.path.dirname(os.path.abspath(__file__))

def _exam_and_hardened():
    ex = json.load(open(os.path.join(HERE, "exam.json")))
    exam = {e["file"] for e in ex["frozen"] + ex["expansion"]}
    hardened = set()
    for p in glob.glob(os.path.join(LIB, "python/data-science", "**", "*.py"), recursive=True):
        try:
            if "AuraInputError" in open(p, encoding="utf-8", errors="replace").read():
                hardened.add(os.path.relpath(p, LIB))
        except OSError:
            pass
    return exam, hardened

# --- affordance signals (language-agnostic text + python AST where available) ---
ROUNDTRIP_PAIRS = [
    ("encode", "decode"), ("serialize", "deserialize"), ("serialize", "recover"),
    ("marshal", "unmarshal"), ("compress", "decompress"), ("dump", "load"),
    ("forward", "inverse"), ("to_", "from_"), ("pack", "unpack"), ("sign", "verify"),
    ("write", "read"), ("push", "pop"), ("insert", "delete"), ("enqueue", "dequeue"),
]
REF_TOKENS = re.compile(r"\b(lm|t\.test|glm|numpy|np\.|scipy|reference|oracle|brute|"
                        r"closed[_\s-]?form|analytic|ground[_\s-]?truth|vs\s+stdlib|expected)\b", re.I)
INVARIANT_TOKENS = re.compile(r"\b(sum(s|med)?\s*(to|=|->)\s*1|monoton|invariant|guarantee|"
                              r"never\s+(false|negativ|los)|exactly[_\s-]?once|must\s+(hold|equal|be)|"
                              r"conserv|idempoten|no\s+false|preserve|>=\s*0|non[_\s-]?negativ)\b", re.I)
ASSERT_CMP = re.compile(r"(assert|stopifnot|if\s*!?\().{0,80}(==|all\.equal|isclose|abs\s*\(.*-)")
NUMERIC_HINT = re.compile(r"\b(float|double|mean|variance|probability|likelihood|estimate|"
                          r"score|coefficient|gradient|matrix|integral|density|distribution)\b", re.I)


def classify(relpath):
    path = os.path.join(LIB, relpath)
    try:
        src = open(path, encoding="utf-8", errors="replace").read()
    except OSError:
        return "OPAQUE"
    low = src.lower()
    names = set()
    if relpath.endswith(".py"):
        try:
            names = {n.name.lower() for n in ast.walk(ast.parse(src))
                     if isinstance(n, ast.FunctionDef)}
        except SyntaxError:
            names = set(re.findall(r"def\s+(\w+)", low))
    else:
        names = set(re.findall(r"(?:fn|func|def)\s+(\w+)", low))
    joined = " ".join(names)

    # ROUNDTRIP: both halves of an inverse pair present as function names
    for a, b in ROUNDTRIP_PAIRS:
        if any(a in n for n in names) and any(b in n for n in names):
            return "ROUNDTRIP"

    # SELF_REF: self-test compares a computed value against an independent reference
    if ASSERT_CMP.search(src) and REF_TOKENS.search(src):
        return "SELF_REF"

    # INVARIANT: a hard property is stated (docstring/comment/name)
    if INVARIANT_TOKENS.search(src):
        return "INVARIANT"

    # NUMERIC: numeric surface but no reference / no stated invariant -> hand-derived truth
    if NUMERIC_HINT.search(src):
        return "NUMERIC"

    return "OPAQUE"


def main():
    exam, hardened = _exam_and_hardened()
    known = exam | hardened
    files = sorted(os.path.relpath(p, LIB) for p in
                   glob.glob(os.path.join(LIB, "**", "*.*"), recursive=True)
                   if p.endswith((".py", ".R", ".cpp", ".go", ".rs")))
    by_bucket = Counter()
    by_lang_bucket = defaultdict(Counter)
    rows = []
    for f in files:
        if f in known:
            continue
        b = classify(f)
        lang = f.split("/")[0]
        by_bucket[b] += 1
        by_lang_bucket[lang][b] += 1
        rows.append({"file": f, "bucket": b, "lang": lang})

    total_unknown = sum(by_bucket.values())
    print("=" * 78)
    print(f"POSITIVE-ORACLE GAP — {total_unknown} health-only patterns "
          f"(excludes {len(exam)} exam + {len(hardened)} input-hardened)")
    print("=" * 78)
    order = ["ROUNDTRIP", "SELF_REF", "INVARIANT", "NUMERIC", "OPAQUE"]
    auto = by_bucket["ROUNDTRIP"] + by_bucket["SELF_REF"]
    semi = by_bucket["INVARIANT"]
    hand = by_bucket["NUMERIC"] + by_bucket["OPAQUE"]
    labels = {"ROUNDTRIP": "auto (inverse round-trip)",
              "SELF_REF": "auto (lift existing reference)",
              "INVARIANT": "semi-auto (encode stated invariant)",
              "NUMERIC": "HAND (derive numeric truth)",
              "OPAQUE": "HAND / N-A (no clear oracle)"}
    for b in order:
        n = by_bucket[b]
        print(f"  {b:10} {n:4}  ({100*n//total_unknown:2}%)  {labels[b]}")
    print("-" * 78)
    print(f"  AUTO-GENERATABLE : {auto:4}  ({100*auto//total_unknown}%)  round-trip + reference-lift")
    print(f"  SEMI-AUTO        : {semi:4}  ({100*semi//total_unknown}%)  invariant encode (needs a human to name it)")
    print(f"  HAND-AUDIT       : {hand:4}  ({100*hand//total_unknown}%)  numeric truth or opaque")
    print("\nby language:")
    for lang in ("python", "cpp", "rust", "go", "r"):
        c = by_lang_bucket[lang]
        tot = sum(c.values())
        if tot:
            print(f"  {lang:7} {tot:4}  " + " ".join(f"{k}:{c[k]}" for k in order if c[k]))
    json.dump({"by_bucket": dict(by_bucket), "rows": rows},
              open(os.path.join(HERE, "oracle_gap_report.json"), "w"), indent=1)
    print(f"\nreport: {os.path.join(HERE, 'oracle_gap_report.json')}")
    print("\nCAVEAT: STATIC affordance estimate — sizes the work, does not prove any auto-oracle passes.")

if __name__ == "__main__":
    main()
