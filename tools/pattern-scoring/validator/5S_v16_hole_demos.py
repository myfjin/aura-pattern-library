"""5S v1.6: demonstrations of two new holes.

1. R3 false-FLAG: a function with two numeric params where equal values are VALID.
2. Set-shape miss: dedup_pipeline shingles(k=0) returns {''}, not counted as acceptance.
"""
import executor
from executor import build_baseline, attack_fixtures, _finite_or_full
import inspect


# Hole 1: a function where p1==p2 is perfectly valid
print("=" * 78)
print("HOLE 1: R3 treats valid equal params as silent acceptance")
print("=" * 78)

def compare_ratios(p1: float, p2: float) -> float:
    """Return p1 / p2. Equal params is a valid 1.0 ratio."""
    return p1 / p2

sig = inspect.signature(compare_ratios)
params = list(sig.parameters.values())
baseline, ok = build_baseline(params)
print(f"compare_ratios baseline={baseline} (equal is valid)")
for recipe, args, ec, idx in attack_fixtures(params, baseline):
    if recipe == "R3_degenerate_equal":
        out = compare_ratios(*args)
        print(f"  {recipe}: args={args} -> out={out!r}")
        print(f"  _finite_or_full(out)={_finite_or_full(out)}  (so generic executor counts as 'silent accept' -> FLAG)")
        print(f"  HONEST verdict should be: PASS (1.0 is a meaningful, correct result)")

# Hole 2: set output not counted as finite_or_full
print()
print("=" * 78)
print("HOLE 2: set/dict degenerate output not counted as 'full'")
print("=" * 78)

examples = [
    ("set {''}", {""}),
    ("dict {}", {}),
    ("list ['']", [""]),
    ("str ''", ""),
    ("int 0", 0),
]
for label, val in examples:
    print(f"  {label:15} _finite_or_full={_finite_or_full(val):5}  len_ok={bool(val) if isinstance(val,(list,dict,set,str)) else 'n/a'}")

print("\n  dedup_pipeline.shingles(k=0) returns {' '} -> _finite_or_full=False -> not counted as silent accept")
print("  Yet it IS a degenerate output from a degenerate param (E009).")
print("=" * 78)
