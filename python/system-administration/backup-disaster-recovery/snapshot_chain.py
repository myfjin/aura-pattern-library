#!/usr/bin/env python3
"""snapshot_chain: maintain chain of snapshots with parent references."""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import os
import sys
import tempfile
import hashlib
import json
from pathlib import Path

def create_snapshot(src_dir, snapshot_dir, snapshot_id, parent_id=None):
    """Create snapshot with optional parent reference for deduplication."""
    snap_path = Path(snapshot_dir) / f"snap_{snapshot_id}"
    snap_path.mkdir(parents=True, exist_ok=True)

    manifest = {
        "id": snapshot_id,
        "parent": parent_id,
        "files": {}
    }

    for root, dirs, files in os.walk(src_dir):
        for fname in files:
            src_path = Path(root) / fname
            rel = src_path.relative_to(src_dir)
            content = src_path.read_bytes()
            content_hash = hashlib.sha256(content).hexdigest()

            # Only store file if it's new (different from parent)
            # In real impl, this would check parent snapshot's manifest
            dst_path = snap_path / content_hash
            if not dst_path.exists():
                dst_path.write_bytes(content)

            manifest["files"][str(rel)] = content_hash

    # Store manifest
    with open(snap_path / "manifest.json", 'w') as f:
        json.dump(manifest, f)

    return manifest

def restore_from_snapshot(snapshot_dir, snapshot_id, restore_dir):
    """Restore from snapshot by following parent chain."""
    Path(restore_dir).mkdir(parents=True, exist_ok=True)

    # Collect all snapshots in chain
    current_id = snapshot_id
    chain = []
    visited = set()

    while current_id:
        if current_id in visited:
            break  # Cycle detection
        visited.add(current_id)

        snap_path = Path(snapshot_dir) / f"snap_{current_id}"
        if not snap_path.exists():
            break

        with open(snap_path / "manifest.json", 'r') as f:
            manifest = json.load(f)

        chain.append((current_id, manifest))
        current_id = manifest.get("parent")

    # Reverse to apply oldest first
    chain.reverse()

    # Apply snapshots in order
    for snap_id, manifest in chain:
        snap_path = Path(snapshot_dir) / f"snap_{snap_id}"
        for rel_path, content_hash in manifest.get("files", {}).items():
            content_file = snap_path / content_hash
            if content_file.exists():
                content = content_file.read_bytes()
                dst_path = Path(restore_dir) / rel_path
                dst_path.parent.mkdir(parents=True, exist_ok=True)
                dst_path.write_bytes(content)

    return True

def test_snapshot_chain():
    """Test: create snapshot chain, verify parent links, restore from middle snapshot."""
    with tempfile.TemporaryDirectory() as tmpdir:
        src = Path(tmpdir) / "src"
        src.mkdir()
        snapshot_base = Path(tmpdir) / "snapshots"

        # Snapshot 1: initial state
        (src / "file1.txt").write_text("content_v1")
        (src / "file2.txt").write_text("shared_content")
        snap1 = create_snapshot(src, snapshot_base, "snap1", parent_id=None)
        assert snap1["id"] == "snap1", "Snapshot ID mismatch"
        assert snap1["parent"] is None, "First snapshot should have no parent"
        assert len(snap1["files"]) == 2, f"Snapshot 1 should have exactly 2 files, got {len(snap1['files'])}"
        assert "file1.txt" in snap1["files"] and "file2.txt" in snap1["files"], "Should have both files"

        # Snapshot 2: modify file1, keep file2
        (src / "file1.txt").write_text("content_v2")
        snap2 = create_snapshot(src, snapshot_base, "snap2", parent_id="snap1")
        assert snap2["parent"] == "snap1"

        # Snapshot 3: add file3, modify file2
        (src / "file2.txt").write_text("shared_content_modified")
        (src / "file3.txt").write_text("new_file_content")
        snap3 = create_snapshot(src, snapshot_base, "snap3", parent_id="snap2")
        assert snap3["parent"] == "snap2"
        assert len(snap3["files"]) == 3, f"Snapshot 3 should reference 3 files, got {len(snap3['files'])}"

        # Restore from snap1 (initial state)
        restore1 = Path(tmpdir) / "restore1"
        restore_from_snapshot(snapshot_base, "snap1", restore1)
        assert (restore1 / "file1.txt").read_text() == "content_v1"
        assert (restore1 / "file2.txt").read_text() == "shared_content"
        assert not (restore1 / "file3.txt").exists(), "snap1 should not have file3"

        # Restore from snap2 (via parent chain)
        restore2 = Path(tmpdir) / "restore2"
        restore_from_snapshot(snapshot_base, "snap2", restore2)
        assert (restore2 / "file1.txt").read_text() == "content_v2", "snap2 should have modified file1"
        assert (restore2 / "file2.txt").read_text() == "shared_content", "snap2 should have original file2"
        assert not (restore2 / "file3.txt").exists(), "snap2 should not have file3"

        # Restore from snap3 (full chain)
        restore3 = Path(tmpdir) / "restore3"
        restore_from_snapshot(snapshot_base, "snap3", restore3)
        assert (restore3 / "file1.txt").read_text() == "content_v2", "snap3 inherited from snap2"
        assert (restore3 / "file2.txt").read_text() == "shared_content_modified", "snap3 has modified file2"
        assert (restore3 / "file3.txt").read_text() == "new_file_content", "snap3 has new file3"

        # Verify snapshots are chained correctly
        snap1_manifest = json.loads((Path(snapshot_base) / "snap_snap1" / "manifest.json").read_text())
        snap2_manifest = json.loads((Path(snapshot_base) / "snap_snap2" / "manifest.json").read_text())
        snap3_manifest = json.loads((Path(snapshot_base) / "snap_snap3" / "manifest.json").read_text())

        assert snap1_manifest["parent"] is None
        assert snap2_manifest["parent"] == "snap1"
        assert snap3_manifest["parent"] == "snap2"

if __name__ == "__main__":
    test_snapshot_chain()
    print("✓ snapshot_chain passed")
