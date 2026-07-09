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


def main() -> None:
    """Demo the diff engine with sample texts."""
    # Sample texts
    old_text = """Hello World
This is a sample text.
It has multiple lines.
Some lines will be changed.
Others will remain the same.
This line will be deleted.
Another unchanged line."""

    new_text = """Hello World
This is a sample text.
It has multiple lines.
Some lines have been changed.
Others will remain the same.
This is a new line.
Another unchanged line.
And another new line."""

    # Create diff engine and compute diff
    engine = DiffEngine(old_text, new_text)
    diff = engine.compute_diff()
    
    print("=== Edit Operations ===")
    for edit in diff:
        line_info = ""
        if edit.old_line_number is not None:
            line_info += f"old:{edit.old_line_number} "
        if edit.new_line_number is not None:
            line_info += f"new:{edit.new_line_number} "
        print(f"{edit.edit_type.value} {line_info}{edit.line.rstrip()}")
    
    print("\n=== Unified Diff ===")
    unified = engine.format_unified_diff(context_lines=2)
    if unified:
        print(unified)
    else:
        print("No differences found")


if __name__ == "__main__":
    main()