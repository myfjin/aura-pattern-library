#!/usr/bin/env python3
"""build_patterns_index.py — regenerate PATTERNS_INDEX.md.

One clickable row per pattern FILE: name -> relative link, plus its own description and the
other languages that share its ID.

The description is read from the file itself under the FROZEN 07-18 ruler (the same rule the
audit sheet uses), so the index can never drift from what the code actually says:
  python : the module docstring (ast.get_docstring)
  others : the first real comment block, skipping watermark and structural lines
A pattern with no description shows `—` rather than an invented summary.

Run after adding/removing patterns:  python3 build_patterns_index.py
"""
import ast, os, re, glob, collections

ROOT = os.path.dirname(os.path.abspath(__file__))
EXT = {"python": "py", "cpp": "cpp", "rust": "rs", "go": "go", "r": "R", "javascript": "js"}
LANG_LABEL = {"python": "Python", "cpp": "C++", "rust": "Rust", "go": "Go", "r": "R",
              "javascript": "JavaScript"}
MAXDESC = 180

WM = "AURA Pattern Library"
MARKS = ("_AURA_MARK", "_auraMark", "_aura_mark", ".aura_mark")


def is_watermark(line):
    s = line.strip()
    if WM in s:
        return True
    if any(m in s for m in MARKS) and ("=" in s or "<-" in s):
        return True
    body = s.lstrip("/#").strip()
    if body and all(0x2000 < ord(c) < 0x2070 or ord(c) in (0x200b, 0x200c, 0x2060, 0x2063)
                    for c in body):
        return True
    return False


def is_structural(line, lang):
    s = line.strip()
    if not s:
        return True
    if s.startswith("#!") and lang != "r":
        return True
    if lang == "rust" and (s.startswith("#![") or s.startswith("use ") or s.startswith("extern ")):
        return True
    if lang == "go" and (s.startswith("package ") or s.startswith("import ") or s in ("import (", ")")
                         or (s.startswith('"') and s.endswith('"'))):
        return True
    if lang == "cpp" and s.startswith(("#include", "#pragma", "#define")):
        return True
    # javascript: `// @forge-family <name>` is a Forge Gate provenance TAG, not a description.
    # Skipping it lets the /* */ handler below reach the JSDoc block, which is where the claim
    # actually lives. Without this the tag would be read as the description — or, since the
    # `//` branch does not list javascript, no description would be found at all.
    if lang == "javascript" and s.startswith("// @forge-family"):
        return True
    return False


def extract_claim(path, lang):
    text = open(path, encoding="utf-8", errors="replace").read()
    if lang == "python":
        try:
            tree = ast.parse(text)
        except SyntaxError:
            return ""
        doc = ast.get_docstring(tree)
        if doc:
            return " ".join(doc.split())
        # FALLBACK — a string literal that is NOT the first statement.
        # Python treats a string as the module docstring ONLY when it is the first statement.
        # Put an import above it and __doc__ is None: a human reading the file sees a perfectly
        # good description, every docstring-reading tool sees nothing. 35 files were in exactly
        # that shape until 2026-07-28 (`95ebea9` relocated them; the index was byte-identical
        # before and after, which is what proved this fallback read the right text).
        # KEPT as a safety net — the shape is easy to reintroduce and silent when it happens.
        for node in tree.body[:6]:
            if isinstance(node, ast.Expr) and isinstance(node.value, ast.Constant) \
                    and isinstance(node.value.value, str):
                return " ".join(node.value.value.split())
        return ""
    lines = text.splitlines()
    i, n, block = 0, len(lines), []
    while i < n:
        raw = lines[i]
        s = raw.strip()
        if is_watermark(raw) or is_structural(raw, lang):
            i += 1
            continue
        if s.startswith("/*"):
            buf = []
            while i < n:
                seg = lines[i].strip()
                cleaned = seg.replace("/*", "").replace("*/", "").lstrip("*").strip()
                if cleaned:
                    buf.append(cleaned)
                if "*/" in lines[i]:
                    break
                i += 1
            return " ".join(" ".join(buf).split())
        if (lang in ("cpp", "go", "rust") and s.startswith("//")) or (lang == "r" and s.startswith("#")):
            while i < n:
                cur = lines[i]
                cs = cur.strip()
                if is_watermark(cur):
                    i += 1
                    continue
                if (lang in ("cpp", "go", "rust") and cs.startswith("//")) or (lang == "r" and cs.startswith("#")):
                    block.append(cs.lstrip("/#").strip() if lang != "r" else cs.lstrip("#").strip())
                    i += 1
                else:
                    break
            return " ".join(" ".join(block).split())
        break
    return ""


def cell(text):
    """Make a string safe inside a markdown table cell."""
    t = " ".join((text or "").split()).replace("|", "\\|")
    if len(t) > MAXDESC:
        t = t[:MAXDESC].rsplit(" ", 1)[0] + "…"
    return t or "—"


def anchor(title):
    a = title.lower()
    a = re.sub(r"[^\w\s-]", "", a)
    return re.sub(r"\s+", "-", a.strip())


def main():
    files = []
    for lang, ext in EXT.items():
        for p in sorted(glob.glob(os.path.join(ROOT, lang, "**", f"*.{ext}"), recursive=True)):
            rel = os.path.relpath(p, ROOT)
            if "_quarantine" in rel.split(os.sep):
                continue
            files.append((rel, lang))

    # stem -> languages, for the twin column
    stems = collections.defaultdict(set)
    for rel, lang in files:
        stems[os.path.basename(rel).rsplit(".", 1)[0]].add(lang)

    # shelf -> category -> rows
    tree = collections.defaultdict(lambda: collections.defaultdict(list))
    for rel, lang in files:
        parts = rel.split(os.sep)
        shelf = f"{parts[0]}/{parts[1]}" if parts[0] in ("python", "go") else parts[0]
        category = os.sep.join(parts[1:-1]) if parts[0] not in ("python", "go") else os.sep.join(parts[2:-1])
        category = category or "(root)"
        name = os.path.basename(rel).rsplit(".", 1)[0]
        others = sorted(LANG_LABEL[l] for l in stems[name] if l != lang)
        tree[shelf][category].append((name, rel, extract_claim(os.path.join(ROOT, rel), lang), others))

    total = len(files)
    L = []
    L.append("# AURA Pattern Library — Pattern Index")
    L.append("")
    # Derived, not written down: the language count was hardcoded as "five" and would have
    # silently become a lie the moment a sixth lane landed. Count the lanes actually present.
    langs_present = sorted({lang for _, lang in files})
    L.append(f"Direct link and description for every one of the **{total:,} pattern files** "
             f"({len(stems):,} unique pattern IDs across {len(langs_present)} languages).")
    L.append("")
    L.append("Descriptions are extracted from each file at generation time under the frozen ruler "
             "(python = module docstring; others = first real comment block), so this index cannot "
             "drift from the code. `—` means the file carries no description.")
    L.append("")
    L.append("Regenerate with `python3 build_patterns_index.py`. "
             "For the ID-keyed master (twins, tiers, licensing) see [CATALOG.md](CATALOG.md).")
    L.append("")
    L.append("## Contents")
    L.append("")
    for shelf in sorted(tree):
        n = sum(len(v) for v in tree[shelf].values())
        L.append(f"- [`{shelf}`](#{anchor(shelf)}) — {n} files, {len(tree[shelf])} categories")
    L.append("")
    for shelf in sorted(tree):
        n = sum(len(v) for v in tree[shelf].values())
        L.append(f"## {shelf}")
        L.append("")
        L.append(f"*{n} files across {len(tree[shelf])} categories.*")
        L.append("")
        for cat in sorted(tree[shelf]):
            rows = sorted(tree[shelf][cat])
            L.append(f"### {cat}")
            L.append("")
            L.append("| Pattern | Description | Also in |")
            L.append("|---|---|---|")
            for name, rel, desc, others in rows:
                link = rel.replace(os.sep, "/")
                L.append(f"| [`{name}`]({link}) | {cell(desc)} | {', '.join(others) or '—'} |")
            L.append("")
    out = os.path.join(ROOT, "PATTERNS_INDEX.md")
    open(out, "w", encoding="utf-8").write("\n".join(L) + "\n")
    missing = sum(1 for s in tree.values() for c in s.values() for r in c if not r[2])
    print(f"wrote {out}")
    cats = sum(len(v) for v in tree.values())
    print(f"  {total} files · {len(stems)} unique IDs · {len(tree)} shelves · "
          f"{cats} categories · no-description: {missing}")


if __name__ == "__main__":
    main()
