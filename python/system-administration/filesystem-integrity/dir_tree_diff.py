"""
dir_tree_diff: compute a diff between two directory trees (file presence, size, content hash).
Failure simulated: create two similar trees; modify one file; diff trees and assert
the difference is detected (changed file flagged, unchanged files not).
Recovery asserted: diff correctly identifies added, removed, modified, and unchanged files.
Pattern's own diff function is called.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import os
import tempfile
import sys
import hashlib
from pathlib import Path


def tree_checksum_index(root_dir):
    """
    Build an index of (path, size, checksum) for all files in root_dir.
    Returns a dict: {relative_path: (size, checksum)}.
    """
    index = {}
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for fname in sorted(filenames):
            full_path = os.path.join(dirpath, fname)
            rel_path = os.path.relpath(full_path, root_dir)
            size = os.path.getsize(full_path)
            h = hashlib.sha256()
            with open(full_path, "rb") as f:
                while True:
                    chunk = f.read(65536)
                    if not chunk:
                        break
                    h.update(chunk)
            checksum = h.hexdigest()
            index[rel_path] = (size, checksum)
    return index


def tree_diff(tree1_index, tree2_index):
    """
    Compare two tree indexes.
    Returns: {added: [], removed: [], modified: [], unchanged: []}.
    """
    all_paths = set(tree1_index.keys()) | set(tree2_index.keys())
    diff = {"added": [], "removed": [], "modified": [], "unchanged": []}

    for path in sorted(all_paths):
        in_tree1 = path in tree1_index
        in_tree2 = path in tree2_index

        if in_tree1 and not in_tree2:
            diff["removed"].append(path)
        elif in_tree2 and not in_tree1:
            diff["added"].append(path)
        elif tree1_index[path] == tree2_index[path]:
            diff["unchanged"].append(path)
        else:
            diff["modified"].append(path)

    return diff


if __name__ == "__main__":
    tmpdir = tempfile.mkdtemp()
    tree1 = os.path.join(tmpdir, "tree1")
    tree2 = os.path.join(tmpdir, "tree2")

    os.makedirs(tree1)
    os.makedirs(tree2)

    # Seed: create identical trees
    expected_files = {
        "file_a.txt": b"content_a_" + (b"x" * 256),
        "file_b.txt": b"content_b_" + (b"y" * 256),
        "subdir/file_c.txt": b"content_c_" + (b"z" * 256),
    }

    for rel_path, content in expected_files.items():
        path1 = os.path.join(tree1, rel_path)
        path2 = os.path.join(tree2, rel_path)
        os.makedirs(os.path.dirname(path1), exist_ok=True)
        os.makedirs(os.path.dirname(path2), exist_ok=True)
        Path(path1).write_bytes(content)
        Path(path2).write_bytes(content)

    # Build indexes
    index1 = tree_checksum_index(tree1)
    index2 = tree_checksum_index(tree2)

    # RECOVERY assert 1: identical trees have no diff
    expected_unchanged_count = len(expected_files)
    diff = tree_diff(index1, index2)
    assert len(diff["added"]) == 0, f"unexpected added: {diff['added']}"
    assert len(diff["removed"]) == 0, f"unexpected removed: {diff['removed']}"
    assert len(diff["modified"]) == 0, f"unexpected modified: {diff['modified']}"
    assert len(diff["unchanged"]) == expected_unchanged_count, f"unchanged count wrong: {len(diff['unchanged'])}"

    # FAILURE SIM: modify one file in tree2
    modified_content = b"modified_content_" + (b"m" * 512)
    Path(os.path.join(tree2, "file_b.txt")).write_bytes(modified_content)

    # Rebuild index2
    index2 = tree_checksum_index(tree2)

    # RECOVERY assert 2: diff detects the modification
    diff = tree_diff(index1, index2)
    assert "file_b.txt" in diff["modified"], f"modified file not detected: {diff['modified']}"
    assert len(diff["modified"]) == 1, f"too many modified: {diff['modified']}"
    assert len(diff["added"]) == 0, f"unexpected added: {diff['added']}"
    assert len(diff["removed"]) == 0, f"unexpected removed: {diff['removed']}"
    assert len(diff["unchanged"]) == 2, f"unchanged count wrong: {len(diff['unchanged'])}"

    # FAILURE SIM: add a new file to tree2
    new_content = b"new_file_" + (b"n" * 128)
    Path(os.path.join(tree2, "new_file.txt")).write_bytes(new_content)

    # Rebuild index2
    index2 = tree_checksum_index(tree2)

    # RECOVERY assert 3: diff detects the addition
    diff = tree_diff(index1, index2)
    assert "new_file.txt" in diff["added"], f"added file not detected: {diff['added']}"
    assert len(diff["added"]) == 1, f"too many added: {diff['added']}"
    assert len(diff["modified"]) == 1, f"modified count changed: {diff['modified']}"

    # FAILURE SIM: remove a file from tree2
    os.unlink(os.path.join(tree2, "file_a.txt"))

    # Rebuild index2
    index2 = tree_checksum_index(tree2)

    # RECOVERY assert 4: diff detects the removal
    diff = tree_diff(index1, index2)
    assert "file_a.txt" in diff["removed"], f"removed file not detected: {diff['removed']}"
    assert len(diff["removed"]) == 1, f"too many removed: {diff['removed']}"

    # Clean up
    import shutil
    shutil.rmtree(tmpdir)

    print(f"dir_tree_diff: files={len(expected_files)}, added=1, modified=1, removed=1")
    print("dir_tree_diff PASS")
    sys.exit(0)
