#!/usr/bin/env python3
"""
A simple diff engine for text comparison.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

from typing import List, Tuple, Optional, Iterator
from enum import Enum
from dataclasses import dataclass


class EditType(Enum):
    """Types of edits in a diff."""
    EQUAL = " "
    INSERT = "+"
    DELETE = "-"


@dataclass
class Edit:
    """Represents a single edit operation."""
    edit_type: EditType
    line: str
    old_line_number: Optional[int] = None
    new_line_number: Optional[int] = None

    def __str__(self) -> str:
        """String representation of the edit."""
        return f"{self.edit_type.value}{self.line}"


class DiffEngine:
    """A simple diff engine for comparing text lines."""

    def __init__(self, old_text: str, new_text: str) -> None:
        """
        Initialize the diff engine with old and new text.
        
        Args:
            old_text: The original text
            new_text: The modified text
        """
        self.old_lines = old_text.splitlines(keepends=True) if old_text else []
        self.new_lines = new_text.splitlines(keepends=True) if new_text else []
        self._lcs_table: Optional[List[List[int]]] = None
        self._edits: Optional[List[Edit]] = None

    def _compute_lcs_table(self) -> List[List[int]]:
        """Compute the longest common subsequence table."""
        if self._lcs_table is not None:
            return self._lcs_table
            
        m, n = len(self.old_lines), len(self.new_lines)
        # Initialize table with zeros
        table = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Fill the table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if self.old_lines[i-1] == self.new_lines[j-1]:
                    table[i][j] = table[i-1][j-1] + 1
                else:
                    table[i][j] = max(table[i-1][j], table[i][j-1])
        
        self._lcs_table = table
        return table

    def _backtrack_lcs(self) -> List[Tuple[int, int]]:
        """Backtrack through the LCS table to find matching lines."""
        table = self._compute_lcs_table()
        matches = []
        i, j = len(self.old_lines), len(self.new_lines)
        
        while i > 0 and j > 0:
            if self.old_lines[i-1] == self.new_lines[j-1]:
                matches.append((i-1, j-1))
                i -= 1
                j -= 1
            elif table[i-1][j] > table[i][j-1]:
                i -= 1
            else:
                j -= 1
                
        matches.reverse()
        return matches

    def compute_diff(self) -> List[Edit]:
        """Compute the diff between old and new text."""
        if self._edits is not None:
            return self._edits
            
        matches = self._backtrack_lcs()
        edits: List[Edit] = []
        
        i = j = 0
        old_line_num = new_line_num = 1
        
        for old_idx, new_idx in matches:
            # Add deletions for lines between current position and match
            while i < old_idx:
                edits.append(Edit(EditType.DELETE, self.old_lines[i], old_line_num, None))
                i += 1
                old_line_num += 1
                
            # Add insertions for lines between current position and match
            while j < new_idx:
                edits.append(Edit(EditType.INSERT, self.new_lines[j], None, new_line_num))
                j += 1
                new_line_num += 1
                
            # Add equal line
            edits.append(Edit(EditType.EQUAL, self.old_lines[old_idx], old_line_num, new_line_num))
            i += 1
            j += 1
            old_line_num += 1
            new_line_num += 1
            
        # Handle remaining lines
        while i < len(self.old_lines):
            edits.append(Edit(EditType.DELETE, self.old_lines[i], old_line_num, None))
            i += 1
            old_line_num += 1
            
        while j < len(self.new_lines):
            edits.append(Edit(EditType.INSERT, self.new_lines[j], None, new_line_num))
            j += 1
            new_line_num += 1
            
        self._edits = edits
        return edits

    def format_unified_diff(self, context_lines: int = 3) -> str:
        """
        Format the diff in unified diff format.
        
        Args:
            context_lines: Number of context lines to show around changes
            
        Returns:
            Unified diff formatted string
        """
        edits = self.compute_diff()
        if not edits:
            return ""
            
        result = []
        i = 0
        
        while i < len(edits):
            # Find next change
            while i < len(edits) and edits[i].edit_type == EditType.EQUAL:
                i += 1
                
            if i >= len(edits):
                break
                
            # Found a change, collect context before
            start = max(0, i - context_lines)
            while start < i and edits[start].edit_type != EditType.EQUAL:
                start += 1
                
            # Collect changes and context after
            end = i
            # Include changes
            while end < len(edits) and edits[end].edit_type != EditType.EQUAL:
                end += 1
            # Include context after
            post_context_end = min(len(edits), end + context_lines)
            
            # Determine line numbers for the hunk
            old_start = edits[start].old_line_number or 1
            new_start = edits[start].new_line_number or 1
            
            # Count lines in old and new versions for this hunk
            old_count = 0
            new_count = 0
            for edit in edits[start:post_context_end]:
                if edit.edit_type in (EditType.EQUAL, EditType.DELETE):
                    old_count += 1
                if edit.edit_type in (EditType.EQUAL, EditType.INSERT):
                    new_count += 1
                    
            # Add hunk header
            result.append(f"@@ -{old_start},{old_count} +{new_start},{new_count} @@")
            
            # Add lines
            for edit in edits[start:post_context_end]:
                result.append(str(edit))
                
            i = post_context_end
            
        return "\n".join(result) if result else ""


def _reconstruct(edits):
    """Rebuild (old_lines, new_lines) from an edit script — the diff invariant."""
    old = [e.line for e in edits if e.edit_type in (EditType.EQUAL, EditType.DELETE)]
    new = [e.line for e in edits if e.edit_type in (EditType.EQUAL, EditType.INSERT)]
    return old, new


def main() -> None:
    """Self-test: THE diff invariant (edits reconstruct both texts exactly),
    exact edit counts on a planted change, fuzz over random line soups."""
    import random
    random.seed(42)

    # Planted change: one line replaced, one deleted+inserted, one appended.
    old_text = "Hello World\nkeep one\nchange me\nkeep two\ndelete me\nkeep three"
    new_text = "Hello World\nkeep one\nchanged!\nkeep two\nkeep three\nappended"
    engine = DiffEngine(old_text, new_text)
    edits = engine.compute_diff()

    # The invariant: replaying the script yields both sides verbatim
    # (the engine keeps line endings, so compare with keepends).
    old_r, new_r = _reconstruct(edits)
    assert old_r == old_text.splitlines(keepends=True), \
        "edit script does not reconstruct the OLD text"
    assert new_r == new_text.splitlines(keepends=True), \
        "edit script does not reconstruct the NEW text"

    # Exact operation counts for the planted change. Note keepends: the old
    # text's final "keep three" has no trailing newline while the new one
    # does, so that pair counts as a change, not a match — 3 of each.
    kinds = [e.edit_type for e in edits]
    assert kinds.count(EditType.EQUAL) == 3, f"3 shared lines expected, got {kinds.count(EditType.EQUAL)}"
    assert kinds.count(EditType.DELETE) == 3, "changed+deleted+eol-changed = 3 DELETEs expected"
    assert kinds.count(EditType.INSERT) == 3, "changed+appended+eol-changed = 3 INSERTs expected"

    # Identical texts: all EQUAL, empty unified diff.
    same = DiffEngine("a\nb\nc", "a\nb\nc")
    assert all(e.edit_type == EditType.EQUAL for e in same.compute_diff())
    assert same.format_unified_diff() == "", "no-change diff must be empty"

    # Unified diff carries hunk headers for real changes.
    unified = engine.format_unified_diff(context_lines=2)
    assert unified.startswith("@@ -"), f"unified diff missing hunk header: {unified[:30]!r}"
    assert "changed!" in unified and "delete me" in unified

    # Degenerate shapes: all-insert and all-delete (empty text = no lines).
    ins = DiffEngine("", "x\ny").compute_diff()
    o, n = _reconstruct(ins)
    assert n == ["x\n", "y"] and o == [], "insert-only script broken"
    dele = DiffEngine("x\ny", "").compute_diff()
    o, n = _reconstruct(dele)
    assert o == ["x\n", "y"] and n == [], "delete-only script broken"

    # Fuzz: 60 random pairs of line-soups; the invariant must never break.
    vocab = ["alpha", "beta", "gamma", "delta", "epsilon"]
    for trial in range(60):
        a_text = "\n".join(random.choice(vocab) for _ in range(random.randint(0, 12)))
        b_text = "\n".join(random.choice(vocab) for _ in range(random.randint(0, 12)))
        script = DiffEngine(a_text, b_text).compute_diff()
        got_a, got_b = _reconstruct(script)
        assert got_a == a_text.splitlines(keepends=True), \
            f"trial {trial}: old reconstruction diverged"
        assert got_b == b_text.splitlines(keepends=True), \
            f"trial {trial}: new reconstruction diverged"

    print("diff_engine: reconstruction invariant held (planted + 60 fuzz pairs), "
          "counts 3=/3-/3+ (keepends), hunk headers present — PASS")


if __name__ == "__main__":
    main()