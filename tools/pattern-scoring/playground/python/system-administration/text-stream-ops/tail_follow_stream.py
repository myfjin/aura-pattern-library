#!/usr/bin/env python3
"""
tail_follow_stream: Simulate tail -f behavior (read from file position, follow new lines).
THE ONE LAW: Track file position, read only new lines, handle file rotation edge case.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import tempfile
import os
import time

class TailFollower:
    """Follow a file like tail -f. Track position and read only new content."""

    def __init__(self, file_path):
        self.file_path = file_path
        self.file_size = 0
        if os.path.exists(file_path):
            self.file_size = os.path.getsize(file_path)

    def read_new_lines(self):
        """Read lines that appeared since last position. Return list of lines."""
        if not os.path.exists(self.file_path):
            return []

        current_size = os.path.getsize(self.file_path)
        if current_size < self.file_size:
            # File rotated/truncated. Start from beginning.
            self.file_size = 0

        new_lines = []
        try:
            with open(self.file_path) as f:
                f.seek(self.file_size)
                new_lines = [line.rstrip('\n') for line in f.readlines()]
                self.file_size = f.tell()
        except IOError:
            pass

        return new_lines

def main():
    # Create temp file and follow it.
    with tempfile.NamedTemporaryFile(mode='w', suffix='.log', delete=False) as f:
        temp_file = f.name
        f.write("Line 1\n")

    try:
        # Reset file_size to 0 to read from beginning (simulate fresh tail).
        follower = TailFollower(temp_file)
        follower.file_size = 0  # Force read from start.

        # First read: should get Line 1.
        lines = follower.read_new_lines()
        assert lines == ['Line 1'], f"First read should be ['Line 1'], got {lines}"

        # Second read: nothing new yet.
        lines = follower.read_new_lines()
        assert lines == [], f"Second read should be empty, got {lines}"

        # Append new lines.
        with open(temp_file, 'a') as f:
            f.write("Line 2\nLine 3\n")

        # Third read: should get new lines only.
        lines = follower.read_new_lines()
        assert lines == ['Line 2', 'Line 3'], f"Expected new lines, got {lines}"

        # FAILURE SIMULATION: Re-reading without new content should be empty.
        lines = follower.read_new_lines()
        assert lines == [], f"Fourth read should be empty, got {lines}"

        # Simulate file rotation: truncate and write new content.
        with open(temp_file, 'w') as f:
            f.write("Rotated line 1\n")

        # Should detect rotation and start from new beginning.
        lines = follower.read_new_lines()
        assert lines == ['Rotated line 1'], f"After rotation, should read from start, got {lines}"

        # Verify position tracking (no infinite loops or missing lines).
        with open(temp_file, 'a') as f:
            for i in range(100):
                f.write(f"Line {i+2}\n")

        all_new = []
        all_new.extend(follower.read_new_lines())
        assert len(all_new) == 100, f"Should read all 100 new lines, got {len(all_new)}"
        assert all_new[0].startswith('Line 2'), f"Should start with Line 2, got {all_new[0]}"

    finally:
        os.unlink(temp_file)

    print("✓ tail_follow_stream passed")

if __name__ == '__main__':
    main()
