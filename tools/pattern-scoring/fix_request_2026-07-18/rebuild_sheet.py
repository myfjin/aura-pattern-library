#!/usr/bin/env python3
"""Rebuild DESCRIPTIONS_SHEET.csv under the FROZEN 07-18 ruler.

Ruler: claim = first real comment/docstring block above code.
  python: ast.get_docstring(module)
  cpp/rust/go/r: first contiguous comment block, skipping watermark lines and
                 structural lines (package/import/use/#include/#![..]/shebang/blank).
Emits columns: file,lang,category,claim,claim_missing  (claim_missing = "YES" when none).
"""
import ast, csv, sys
from pathlib import Path

LIB = Path.home() / "aura-pattern-library"
SUBTREES = ["python/programming", "python/data-science", "python/system-administration",
            "r", "cpp", "rust", "go"]
EXT2LANG = {".py": "python", ".R": "r", ".cpp": "cpp", ".go": "go", ".rs": "rust"}

WM_MARK = "AURA Pattern Library"          # the △ trademark comment line
WM_ASSIGN = ("_AURA_MARK", "_auraMark", "_aura_mark")


def is_watermark(line: str) -> bool:
    s = line.strip()
    if WM_MARK in s:
        return True
    if any(a in s for a in WM_ASSIGN) and "=" in s:
        return True
    # zero-width watermark line: a comment whose payload is only invisible chars
    body = s.lstrip("/#").strip()
    if body and all(ord(ch) > 0x2000 and ord(ch) < 0x2070 or ch == "⁣" or ord(ch) in (0x200b, 0x200c, 0x2060, 0x2061, 0x2062) for ch in body):
        return True
    return False


def is_structural(line: str, lang: str) -> bool:
    s = line.strip()
    if s == "":
        return True
    if s.startswith("#!") and lang != "r":       # shebang (py)
        return True
    if lang == "rust" and s.startswith("#!["):    # inner attribute
        return True
    if lang == "go" and (s.startswith("package ") or s.startswith("import ") or s == "import (" or s == ")"):
        return True
    if lang == "rust" and (s.startswith("use ") or s.startswith("extern ")):
        return True
    if lang == "cpp" and (s.startswith("#include") or s.startswith("#pragma") or s.startswith("#define")):
        return True
    # inside a go grouped import block: bare quoted paths
    if lang == "go" and (s.startswith('"') and s.endswith('"')):
        return True
    return False


def strip_comment(line: str, lang: str) -> str:
    s = line.strip()
    if lang == "r":
        return s.lstrip("#").strip()
    if s.startswith("//"):
        return s[2:].strip()
    return s


def extract_claim(path: Path, lang: str) -> str:
    text = path.read_text(encoding="utf-8", errors="replace")
    if lang == "python":
        try:
            doc = ast.get_docstring(ast.parse(text))
        except SyntaxError:
            doc = None
        return " ".join((doc or "").split()).strip()

    lines = text.splitlines()
    i, n = 0, len(lines)
    block = []
    while i < n:
        raw = lines[i]
        s = raw.strip()
        if is_watermark(raw) or is_structural(raw, lang):
            i += 1
            continue
        # C-style block comment /* ... */
        if s.startswith("/*"):
            buf = []
            while i < n:
                seg = lines[i].strip()
                cleaned = seg.replace("/*", "").replace("*/", "").lstrip("*").strip()
                if cleaned:
                    buf.append(cleaned)
                if "*/" in lines[i]:
                    i += 1
                    break
                i += 1
            return " ".join(" ".join(buf).split()).strip()
        # line comment block (// or #)
        if (lang in ("cpp", "go", "rust") and s.startswith("//")) or (lang == "r" and s.startswith("#")):
            while i < n:
                cur = lines[i]
                cs = cur.strip()
                if is_watermark(cur):
                    i += 1
                    continue
                if (lang in ("cpp", "go", "rust") and cs.startswith("//")) or (lang == "r" and cs.startswith("#")):
                    block.append(strip_comment(cur, lang))
                    i += 1
                else:
                    break
            return " ".join(" ".join(block).split()).strip()
        # hit real code before any comment block
        break
    return ""


def main():
    rows = []
    for st in SUBTREES:
        base = LIB / st
        if not base.exists():
            continue
        for p in sorted(base.rglob("*")):
            if p.suffix not in EXT2LANG or "_quarantine" in p.parts:
                continue
            lang = EXT2LANG[p.suffix]
            rel = str(p.relative_to(LIB))
            cat = str(p.parent.relative_to(LIB / lang)) if (LIB / lang) in p.parents else p.parent.name
            claim = extract_claim(p, lang)[:400]
            rows.append({"file": rel, "lang": lang, "category": cat,
                         "claim": claim, "claim_missing": "" if claim else "YES"})
    out = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("/dev/stdout")
    with open(out, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["file", "lang", "category", "claim", "claim_missing"])
        w.writeheader()
        w.writerows(rows)
    miss = sum(1 for r in rows if r["claim_missing"] == "YES")
    short = sum(1 for r in rows if r["claim_missing"] == "" and len(r["claim"]) < 40)
    print(f"rows={len(rows)} claim_missing={miss} short(<40)={short}", file=sys.stderr)


if __name__ == "__main__":
    main()
