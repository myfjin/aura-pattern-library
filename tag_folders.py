#!/usr/bin/env python3
"""tag_folders.py — semantic identity for every folder in the Grand Library.

Writes a meaningful `.folder-nature` (identity / being / purpose / tags / memory)
into EVERY directory, plus the root declaration `.folder-nature-root.yaml` with
`require_nature: true`, so `folder-nature verify --root` fails loudly if any
folder is ever missing its identity — the library self-checks its own tagging.

Dogfoods the installed `folder_nature` API — no hand-written YAML.

RE-RUNNABLE + IDEMPOTENT: purposes/tags are regenerated from what is on disk
(pattern counts, CATALOG.md titles); `memory.created` and accumulated
`notable_events` are preserved from an existing file.

THE ORDER LAW (from SYNC.md): run this AFTER copy+stamp and BEFORE re-signing.
A `.folder-nature` added to an already-signed subtree breaks manifest↔disk
parity until that subtree is re-signed.
"""
import argparse
import re
import sys
from datetime import date
from pathlib import Path

from _check_folder_nature import add_dev_checkout as _dev, require as _require  # noqa: E402

_dev()
from folder_nature import FolderNature, write_folder_nature
from folder_nature.core import NATURE_FILENAME, read_folder_nature
from folder_nature.schema import Identity, Memory

_require()

ROOT = Path(__file__).resolve().parent
SRC_EXT = (".py", ".R", ".cpp", ".go", ".rs")
MAX_TAG_LEN = 30                       # schema limit — tags longer than this are rejected
SKIP_DIRS = {".git", ".hg", ".svn", "__pycache__", ".pytest_cache", ".venv",
              "node_modules", ".mypy_cache"}   # mirrors orchestrator._SKIP_DIRS

# Human names for structural directories the CATALOG can't title.
SPHERE_NAMES = {
    "python": "Python", "r": "R", "cpp": "C++", "go": "Go", "rust": "Rust",
    "programming": "Programming", "data-science": "Data Science",
    "system-administration": "System Administration", "sysadmin": "Sysadmin",
}
ACRONYMS = {"ii": "II", "iii": "III", "nlp": "NLP", "eda": "EDA", "ml": "ML",
            "io": "IO", "ds": "DS", "ab": "A/B", "svd": "SVD", "pca": "PCA"}

ROOT_NATURE = dict(
    being="director",
    purpose=("AURA Pattern Library — verified, attributed, multi-language reference "
             "patterns; every file run-gated, watermarked, Ed25519-signed. "
             "© Reality Optimizer."),
    tags=["aura", "patterns", "verified", "signed", "multi-language"],
    rules=["Every file is run-gated, watermarked, and Ed25519-signed",
           "Nothing ships that fails the honesty gate"],
)

ROOT_SPEC = """\
# Root declaration — makes `folder-nature verify --root` a single-verdict gate.
# require_nature: EVERY folder must carry a .folder-nature, or the verdict is RED.
orchestrator: true
expect_dirs: [python, r, cpp, rust, go]
require_nature: true
require_mark: true
require_watermark: true
"""


def catalog_titles() -> dict:
    """slug -> human category title, parsed from CATALOG.md (both slug variants:
    with and without 'and', since sphere slugs differ, e.g.
    bayesian_iii_modeling_and_selection vs bayesian_iii_modeling_selection)."""
    out = {}
    cat = ROOT / "CATALOG.md"
    if not cat.exists():
        return out
    for m in re.finditer(r"^\| `[^`]+` \| [^|]+ \| ([^|]+) \|", cat.read_text(), re.M):
        title = m.group(1).strip()
        tokens = re.findall(r"[a-z0-9]+", title.lower().replace("&", " and "))
        for variant in ("_".join(tokens), "_".join(t for t in tokens if t != "and")):
            out.setdefault(variant, title)
    return out


def prettify(name: str) -> str:
    if name in SPHERE_NAMES:
        return SPHERE_NAMES[name]
    words = re.split(r"[_\-]+", name)
    return " ".join(ACRONYMS.get(w, w.capitalize()) for w in words if w)


def slug_tag(component: str) -> str:
    return re.sub(r"[^a-z0-9\-]+", "-", component.lower()).strip("-")[:MAX_TAG_LEN]


def walk_dirs(root: Path):
    """Every directory below root, mirroring the orchestrator's walk rules."""
    for p in sorted(root.rglob("*")):
        if not p.is_dir():
            continue
        parts = p.relative_to(root).parts
        if any(part in SKIP_DIRS for part in parts):
            continue
        if any(part.startswith(".") for part in parts):
            continue
        yield p


def preserved_memory(d: Path, today: str) -> Memory:
    """Keep created/notable_events across re-runs; seed them on first tagging."""
    nf = d / NATURE_FILENAME
    if nf.exists():
        try:
            old = read_folder_nature(nf)
            if old.memory and (old.memory.created or old.memory.notable_events):
                return Memory(created=old.memory.created or today,
                              last_significant_change=today,
                              notable_events=list(old.memory.notable_events))
        except Exception:
            pass    # unreadable old nature — regenerate from scratch
    return Memory(created=today,
                  notable_events=[f"{today}: semantic identity layer added "
                                  "(REQ-tag-library-folders)"])


def nature_for(d: Path, root: Path, titles: dict, today: str) -> FolderNature:
    rel = d.relative_to(root)
    name = d.name

    if d == root:
        return FolderNature(
            identity=Identity(name="aura-pattern-library",
                              being=ROOT_NATURE["being"],
                              purpose=ROOT_NATURE["purpose"]),
            director=True, tags=ROOT_NATURE["tags"], rules=ROOT_NATURE["rules"],
            memory=preserved_memory(d, today))

    if name == "_quarantine":
        return FolderNature(
            identity=Identity(name=name, being="private",
                              purpose="Excluded assert-linter REJECTs — not shipped"),
            tags=["quarantine", "excluded"],
            memory=preserved_memory(d, today))

    n_patterns = sum(1 for p in d.rglob("*") if p.suffix in SRC_EXT)
    n_subdirs = sum(1 for p in d.iterdir() if p.is_dir() and p.name not in SKIP_DIRS)
    human = titles.get(name) or prettify(name)
    if name == "tools":
        purpose = "Library maintenance tooling (census) — not patterns"
    else:
        purpose = f"{human} — {n_patterns} patterns"
        if n_subdirs:
            purpose += f" / {n_subdirs} subfolders"

    tags = [slug_tag(c) for c in rel.parts] + ["verified"]
    return FolderNature(
        identity=Identity(name=name, being="collector", purpose=purpose),
        tags=tags, memory=preserved_memory(d, today))


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--root", default=str(ROOT))
    args = ap.parse_args()
    root = Path(args.root).resolve()
    today = date.today().isoformat()
    titles = catalog_titles()

    created = refreshed = 0
    for d in [root] + list(walk_dirs(root)):
        existed = (d / NATURE_FILENAME).exists()
        write_folder_nature(d, nature_for(d, root, titles, today))
        created += (not existed)
        refreshed += existed

    spec = root / ".folder-nature-root.yaml"
    spec.write_text(ROOT_SPEC, encoding="utf-8")

    print(f"tagged {created + refreshed} folders ({created} created, {refreshed} refreshed)")
    print(f"root spec written: {spec.name} (require_nature: true)")
    print("NOW RE-SIGN every signed subtree, or parity is broken (the order law):")
    print("  for st in python/programming python/data-science python/system-administration r cpp rust go;")
    print("    do folder-nature sign <lib>/$st --key ~/.config/folder-nature/aura-signing.key; done")
    return 0


if __name__ == "__main__":
    sys.exit(main())
