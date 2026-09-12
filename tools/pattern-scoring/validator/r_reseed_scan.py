#!/usr/bin/env python3
"""
r_reseed_scan.py — WAVE 2: an independent oracle for the R sphere (reseed robustness).

THE PROBLEM. R was oracle-bare (0 axioms before today) for a STRUCTURAL reason, not a tool gap:
  - xlang needs >=2 language twins; R patterns are R-native -> impossible without building twins.
  - the inherited metamorphic relations are bound to named PYTHON entry points
    (getattr(mod,"linear_regression_gd")...) and R patterns expose NO callable function at all —
    they are straight-line scripts that plant their own data and stopifnot() on it.

THE LEVER. Every R pattern plants its data under a single `set.seed(N)`, and most then check
themselves against a BASE-R REFERENCE (lm/t.test/prcomp/...). That reference check is real, but it
only ever runs on the ONE dataset the author chose. So: regenerate the data under seeds the author
never picked and require the pattern's own checks to keep holding. That converts a built-in
reference comparison into evidence INDEPENDENT of the author's single green run — and it needs
zero edits to the signed library (source is copied to temp; the library is never mutated).

WHY THIS IS NOT JUST RE-RUNNING THE SELF-TEST (the GREEN-RUN != VERIFIED-AXIOM line):
  same seed  -> same data -> green-run, ZERO new information (correctly excluded).
  unseen seed-> data the author never tested; holding across N of them shows the MECHANISM
                generalizes rather than that one memorized case passes.

VERDICT LADDER (deliberately conservative — a statistical assert MAY fail legitimately):
  holds N/N unseen seeds  -> PASS, earns oracle kind 'reseed'
  holds k/N (0<k<N)       -> FLAG "seed-fragile". NOT a kill: a 95% CI is *designed* to miss ~5%
                             of the time, so partial failure can be correct behaviour. Routed to
                             human review, never auto-INVALID (fold law: a failing relation may
                             mean the RELATION is miscalibrated, not the pattern).
  holds 0/N               -> FLAG (harness/pattern error), investigate.

TIER (mirrors how roundtrip vs positive are tiered elsewhere):
  'hard'      - the pattern validates against a BASE-R REFERENCE implementation (external truth)
                AND holds on unseen data.
  'consensus' - the pattern only self-checks (no external reference); reseed proves robustness,
                not correctness against a standard.

Observation-only: the signed library is never mutated; the exam grader is never touched.

  python3 r_reseed_scan.py            # all R patterns
  python3 r_reseed_scan.py <name>...  # named patterns
"""
from __future__ import annotations
import glob, json, os, re, subprocess, sys, tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
LIB = Path(os.path.expanduser("~/aura-pattern-library"))
R_DIR = LIB / "r"
REPORT = HERE / "r_reseed_report.json"

# seeds the authors did not choose (fixed list -> the scan is deterministic and reproducible)
SEEDS = [7, 101, 555, 2024, 88, 31337, 12345, 9001, 4242, 6180]
SEED_RE = re.compile(r"set\.seed\(\s*\d+\s*\)")
TIMEOUT = 90

# base-R reference implementations: if the pattern checks itself against one of these, its
# internal comparison is against EXTERNAL truth, not just self-consistency.
BASE_R_REFERENCE = [
    "lm(", "glm(", "t.test(", "wilcox.test(", "chisq.test(", "ks.test(", "shapiro.test(",
    "cor.test(", "aov(", "TukeyHSD(", "prcomp(", "kmeans(", "dist(", "ecdf(", "quantile(",
    "fisher.test(", "binom.test(", "var.test(", "poisson.test(", "acf(", "arima(", "spec.pgram(",
    "predict(", "residuals(", "coef(", "anova(", "nls(", "optim(", "integrate(", "density(",
]


def _run_r(src: str, workdir: str) -> subprocess.CompletedProcess:
    p = os.path.join(workdir, "probe.R")
    with open(p, "w", encoding="utf-8") as fh:
        fh.write(src)
    return subprocess.run(["Rscript", p], capture_output=True, text=True, timeout=TIMEOUT)


def _reseed(src: str, seed: int) -> str:
    """Replace ONLY the first set.seed(...) — the data generator."""
    return SEED_RE.sub(f"set.seed({seed})", src, count=1)


def _uses_reference(src: str) -> list:
    return sorted({r.rstrip("(") for r in BASE_R_REFERENCE if r in src})


def negative_control(workdir: str) -> bool:
    """Test-of-the-test: a SEED-MEMORIZED pattern (its reference comparison replaced by values
    hardcoded from seed 42) must pass on 42 and FAIL on unseen seeds. If reseed cannot catch
    that, the whole lane is cosmetic and we abort — same discipline as metamorphic_scan."""
    f = R_DIR / "regression_and_glm" / "linear_regression_normal_eq.R"
    if not f.exists():
        print("negative control: anchor pattern missing -> ABORT")
        return False
    src = f.read_text(encoding="utf-8", errors="replace")
    probe = src.replace('cat("linear_regression_normal_eq.R PASS\\n")',
                        'cat(sprintf("BETA %.10f %.10f %.10f\\n",'
                        ' beta_manual[1], beta_manual[2], beta_manual[3]))')
    out = _run_r(probe, workdir).stdout.strip().split()
    if len(out) < 4:
        print("negative control: could not capture seed-42 beta -> ABORT")
        return False
    b = out[1:4]
    memo = src.replace(
        "stopifnot(all.equal(as.numeric(beta_manual), as.numeric(beta_lm), tolerance=1e-8))",
        f"stopifnot(all.equal(as.numeric(beta_manual), c({b[0]},{b[1]},{b[2]}), tolerance=1e-8))")
    if _run_r(memo, workdir).returncode != 0:
        print("negative control: memorized version fails its OWN seed -> harness broken, ABORT")
        return False
    caught = sum(1 for s in SEEDS if _run_r(_reseed(memo, s), workdir).returncode != 0)
    ok = caught == len(SEEDS)
    print(f"negative control: seed-memorized pattern caught on {caught}/{len(SEEDS)} unseen seeds "
          f"-> {'DETECTION WORKS' if ok else 'COSMETIC (ABORT)'}")
    return ok


def _card(relpath, name, held, total, refs, err=None):
    tier = "hard" if refs else "consensus"
    common = {"pattern": relpath, "technique": "reseed-robustness",
              "fixture": f"{total} unseen seeds (author's seed replaced)",
              "confidence": "high", "repro_cmd": f"python3 r_reseed_scan.py {name}",
              "oracle_coverage_kind": "reseed", "reference_oracles": refs, "tier": tier,
              "held": held, "total": total}
    if err:
        return {**common, "severity": "medium", "class": "reseed-harness-error",
                "verdict": "FLAG", "actual": err,
                "why": "pattern could not be driven under reseed"}
    if held == total:
        return {**common, "severity": "info", "class": "reseed-coverage", "verdict": "PASS",
                "expected": "the pattern's own checks hold on data the author never chose",
                "actual": f"{held}/{total} unseen seeds hold",
                "why": ("internal checks (vs base-R reference: " + ", ".join(refs) + ") hold on "
                        "unseen data -> independent positive oracle" if refs else
                        "self-consistency holds across unseen data -> robustness oracle")}
    return {**common, "severity": "medium", "class": "reseed-fragility", "verdict": "FLAG",
            "expected": "checks hold on unseen data", "actual": f"only {held}/{total} seeds hold",
            "why": ("assertion did not survive unseen data. NOT auto-INVALID: a probabilistic "
                    "assert (CI coverage, sampling test) may legitimately fail some fraction of "
                    "the time — human review decides fragility vs correct stochastic behaviour"),
            "verdict_target": "HUMAN-REVIEW"}


def scan(names=None, verbose=True):
    files = sorted(glob.glob(str(R_DIR / "**" / "*.R"), recursive=True))
    if names:
        files = [f for f in files if Path(f).stem in set(names)]
    cards = []
    with tempfile.TemporaryDirectory(prefix="aura_rseed_") as wd:
        for f in files:
            rel = str(Path(f).relative_to(LIB))
            name = Path(f).stem
            src = open(f, encoding="utf-8", errors="replace").read()
            refs = _uses_reference(src)
            if not SEED_RE.search(src):
                cards.append(_card(rel, name, 0, len(SEEDS), refs, err="no set.seed() to vary"))
                if verbose:
                    print(f"  {name:42s} SKIP (no set.seed)")
                continue
            held, err = 0, None
            for s in SEEDS:
                try:
                    if _run_r(_reseed(src, s), wd).returncode == 0:
                        held += 1
                except subprocess.TimeoutExpired:
                    err = f"timeout at seed {s}"
                    break
            card = _card(rel, name, held, len(SEEDS), refs, err=err)
            cards.append(card)
            if verbose:
                mark = "PASS" if card["verdict"] == "PASS" else "FLAG"
                print(f"  {name:42s} {held}/{len(SEEDS)} [{mark}]"
                      f"{'  ref=' + ','.join(refs[:3]) if refs else '  (self-check only)'}")
    json.dump({"cards": cards}, open(REPORT, "w"), indent=1)
    return cards


def main():
    names = sys.argv[1:] or None
    print("R RESEED-ROBUSTNESS ORACLE (wave 2) — do R patterns hold on data the author never chose?")
    print("=" * 92)
    with tempfile.TemporaryDirectory(prefix="aura_rnc_") as wd:
        if not negative_control(wd):
            print("ABORT: reseed detection is cosmetic.")
            return 1
    print("-" * 92)
    cards = scan(names)
    print("=" * 92)
    p = [c for c in cards if c["verdict"] == "PASS"]
    hard = [c for c in p if c["tier"] == "hard"]
    flag = [c for c in cards if c["verdict"] == "FLAG"]
    print(f"reseed PASS: {len(p)}/{len(cards)}  (hard={len(hard)} vs base-R reference, "
          f"consensus={len(p)-len(hard)} self-check)  ·  FLAG: {len(flag)}")
    if flag:
        print("REVIEW (fragile vs correct stochastic behaviour):",
              [c["pattern"].split("/")[-1] for c in flag])
    return 0


if __name__ == "__main__":
    sys.exit(main())
