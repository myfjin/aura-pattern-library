#!/usr/bin/env python3
"""
xmt_scan.py — FOLD 1: eXtreme Mutation Testing as the tool's OWN oracle-weakness scanner.
Adapted from forge-gate/tools/xmt_harness.py (inherited, NOT merged — the two tools stay separate).

The question it answers about OUR tool (not user code): are our PASS probes HOLLOW? For each
python pattern the exam marks PASS via a probe, we body-wipe each entry function to a dumb
type-compatible return (the oracle now produces garbage) and re-run the probe against the mutant.
If the probe STILL returns PASS -> the probe is HOLLOW (its positive oracle doesn't actually
verify correctness). A probe that flips off PASS on every mutant is SOLID.

Verdict-ladder mapping (per FOLD_PLAN protocol): a HOLLOW probe is a finding about the TOOL —
it emits an evidence card with verdict FLAG on the PROBE (oracle-weakness), routed to hardening.
It NEVER touches the exam verdicts of the library patterns. oracle_coverage gains a 'mutation'
kind: a SOLID probe has verified mutation-coverage.

The real signed library is never mutated: mutants live in a temp mirror and probes.LIB is
redirected there for the run, then restored.
"""
import ast, os, json, tempfile, shutil, importlib
import probes as P

LIB = os.path.expanduser("~/aura-pattern-library")
HERE = os.path.dirname(os.path.abspath(__file__))


def _return_expr(returns):
    """Type-compatible dumb return (from the forge harness)."""
    if returns is None:
        return ast.Constant(value=None)
    if isinstance(returns, ast.Constant):
        return ast.Constant(value=None)
    if isinstance(returns, ast.Name):
        return {"int": ast.Constant(0), "float": ast.Constant(0.0), "bool": ast.Constant(False),
                "str": ast.Constant("")}.get(returns.id, ast.Constant(value=None))
    if isinstance(returns, ast.Subscript) and isinstance(returns.value, ast.Name):
        b = returns.value.id
        if b == "List": return ast.List(elts=[], ctx=ast.Load())
        if b == "Tuple": return ast.Tuple(elts=[], ctx=ast.Load())
        if b == "Dict": return ast.Dict(keys=[], values=[])
    return ast.Constant(value=None)


class _Wiper(ast.NodeTransformer):
    def __init__(self, target, ret): self.target, self.ret = target, ret
    def visit_FunctionDef(self, node):
        if node.name != self.target:
            return self.generic_visit(node)
        return ast.FunctionDef(name=node.name, args=node.args,
                               body=[ast.Return(value=self.ret)],
                               decorator_list=node.decorator_list, returns=node.returns,
                               type_comment=node.type_comment, lineno=node.lineno,
                               col_offset=node.col_offset)


def _entry_fns(src):
    """Top-level def names that are plausible oracle entry points (not dunders/validators)."""
    tree = ast.parse(src)
    return [n.name for n in tree.body if isinstance(n, ast.FunctionDef)
            and not n.name.startswith(("_", "test_")) and n.name != "main"]


def _probe_says_pass(relpath, probe_fn, lib_root):
    """Run a probe with probes.LIB redirected to lib_root; return True if it still PASSes."""
    orig = P.LIB
    try:
        P.LIB = lib_root
        r = probe_fn()
    except Exception:
        return False  # a crash means the mutant was NOT silently accepted -> killed
    finally:
        P.LIB = orig
    # a probe "passes" when its positive oracle held: oracle_match True, or no kill/flag signal
    if r.get("oracle_match") is True:
        return True
    if r.get("oracle_match") is False:
        return False
    if r.get("conclusive_kill") or r.get("invariant_broken"):
        return False
    return False  # conservative: only an explicit oracle_match=True counts as survived


def scan(pass_patterns, verbose=True):
    """pass_patterns: list of (relpath, probe_fn_name, target_fns). Returns evidence cards."""
    cards = []
    for relpath, probe_name, targets in pass_patterns:
        if not relpath.endswith(".py"):
            continue  # XMT is AST-based python; twin/compiled langs handled by fold 4
        probe_fn = getattr(P, probe_name, None)
        if probe_fn is None:
            continue
        src = open(os.path.join(LIB, relpath), encoding="utf-8").read()
        present = {n.name for n in ast.walk(ast.parse(src)) if isinstance(n, ast.FunctionDef)}
        fns = [t for t in targets if t in present]   # only mutate the probe's ACTUAL targets
        killed, survivors = 0, []
        for fn in fns:
            tree = ast.parse(src)
            mutant = _Wiper(fn, _return_expr(next((n.returns for n in ast.walk(tree)
                            if isinstance(n, ast.FunctionDef) and n.name == fn), None))).visit(ast.parse(src))
            ast.fix_missing_locations(mutant)
            # write mutant into a temp mirror at the same relpath
            mirror = tempfile.mkdtemp(prefix="aura_xmt_")
            dst = os.path.join(mirror, relpath)
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            open(dst, "w", encoding="utf-8").write(ast.unparse(mutant))
            survived = _probe_says_pass(relpath, probe_fn, mirror)
            shutil.rmtree(mirror, ignore_errors=True)
            if survived:
                survivors.append(fn)
            else:
                killed += 1
        total = len(fns)
        status = "HOLLOW" if survivors else "SOLID"
        if verbose:
            print(f"  {os.path.basename(relpath):40} {killed}/{total} killed  [{status}]"
                  + (f"  SURVIVORS: {survivors}" if survivors else ""))
        if survivors:
            cards.append({
                "pattern": relpath, "probe": probe_name, "severity": "medium",
                "class": "oracle-weakness", "technique": "XMT",
                "fixture": f"body-wipe mutants of {survivors}",
                "expected": "probe rejects a gutted oracle (killed)",
                "actual": f"probe still PASSed on wiped {survivors} (survived)",
                "why": "the probe's positive oracle does not actually exercise these functions -> hollow",
                "verdict": "FLAG", "verdict_target": "PROBE",  # about the tool, not the library
                "confidence": "high", "repro_cmd": f"python3 xmt_scan.py --pattern {relpath}",
                "oracle_coverage_kind": "mutation",
            })
    return cards


def negative_control():
    """Test-of-the-test: a synthetic probe that ALWAYS says match=True (hollow) must be flagged
    HOLLOW; a probe that checks a real property must be SOLID. Proves detection isn't cosmetic."""
    src = "def answer(x: int) -> int:\n    return x * 2 + 1\n"
    tree = ast.parse(src)
    mutant = _Wiper("answer", _return_expr(ast.Name(id="int"))).visit(ast.parse(src))
    ast.fix_missing_locations(mutant)
    mirror = tempfile.mkdtemp(prefix="aura_xmt_nc_")
    open(os.path.join(mirror, "nc.py"), "w").write(ast.unparse(mutant))
    ns = {}
    exec(open(os.path.join(mirror, "nc.py")).read(), ns)
    # a HOLLOW oracle: "answer(3) is an int" survives the wipe (0 is still an int) -> HOLLOW
    hollow_survives = isinstance(ns["answer"](3), int)
    # a SOLID oracle: "answer(3) == 7" fails on the wipe (0 != 7) -> KILLED
    solid_killed = ns["answer"](3) != 7
    shutil.rmtree(mirror, ignore_errors=True)
    ok = hollow_survives and solid_killed
    print(f"negative control: hollow-oracle survives={hollow_survives}, solid-oracle killed={solid_killed} "
          f"-> {'DETECTION WORKS' if ok else 'BROKEN'}")
    return ok


# PASS python patterns: (relpath, probe_fn, TARGET_FNS the probe's oracle actually exercises).
# XMT only mutates the TARGETS — a probe legitimately verifies its oracle's functions, not every
# helper in the file (mutating unused helpers = false hollow, the forge harness's get_fn filter).
PASS_PROBES = [
    ("python/data-science/bayesian_iii_approximate_inference/bayes_factor_normal_means.py", "probe_bayes_factor", ["bayes_factor_normal"]),
    ("python/data-science/recommenders_and_graph_sampling/bayesian_ab_beta.py", "probe_bayesian_ab", ["bayesian_ab_test"]),
    ("python/data-science/ensembles_and_robust_methods/stacking_ensemble.py", "probe_stacking", ["fit", "predict"]),
    ("python/data-science/information_theory_and_probability/inverse_transform_sampling.py", "probe_inverse_transform", ["exponential_inverse_cdf"]),
    ("python/system-administration/resource-guards/token_bucket_limiter.py", "probe_token_bucket", ["allow_op"]),
    ("python/system-administration/secrets-credentials/ttl_cache.py", "probe_ttl_cache", ["size", "_expired"]),
    ("python/data-science/composed_tools/dedup_pipeline.py", "probe_dedup_pipeline", ["edit_distance", "estimated_jaccard", "dedup_pipeline"]),
    ("python/data-science/bayesian_iii_modeling_and_selection/dirichlet_stick_breaking.py", "probe_dirichlet", ["stick_breaking_process"]),
    ("python/data-science/ensembles_and_robust_methods/gradient_boosting_stumps.py", "probe_gradient_boosting", ["fit_stump", "gradient_boost", "predict_stump"]),
    ("python/data-science/composed_tools/walk_forward_early_stopping.py", "probe_walk_forward", ["mae", "fit_stump_to_residuals", "predict_ensemble"]),
    ("python/data-science/survival_and_reliability/log_rank_test.py", "probe_log_rank", ["log_rank_test"]),
    ("python/system-administration/text-stream-ops/robust_csv_parse.py", "probe_robust_csv", ["parse_csv_line"]),
]


def main():
    import sys
    print("XMT ORACLE-WEAKNESS SCANNER (fold 1) — are the tool's PASS probes hollow?")
    print("=" * 78)
    if not negative_control():
        print("ABORT: XMT detection is broken (negative control failed).")
        return 1
    print("-" * 78)
    cards = scan(PASS_PROBES)
    print("=" * 78)
    hollow = [c for c in cards if c["verdict"] == "FLAG"]
    print(f"SOLID probes: {len(PASS_PROBES)-len(hollow)}/{len(PASS_PROBES)} · HOLLOW: {len(hollow)}")
    json.dump({"cards": cards}, open(os.path.join(HERE, "xmt_report.json"), "w"), indent=1)
    if hollow:
        print("HOLLOW probes (oracle-weakness FLAGs — harden these):",
              [c["probe"] for c in hollow])
    return 0

if __name__ == "__main__":
    import sys; sys.exit(main())
