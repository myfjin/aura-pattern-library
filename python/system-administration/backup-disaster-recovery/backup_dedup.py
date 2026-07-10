#!/usr/bin/env python3
"""backup_dedup: detect and skip duplicate content in backups."""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import os
import sys
import tempfile
import hashlib
from pathlib import Path

def chunk_file(path, chunk_size=4096):
    """Yield (chunk_hash, chunk_data) for a file."""
    with open(path, 'rb') as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            yield hashlib.sha256(chunk).hexdigest(), chunk

def backup_with_dedup(src_dir, backup_dir, chunk_size=4096):
    """Backup files, storing only unique chunks. Return chunk_store and file_refs."""
    chunk_store = Path(backup_dir) / "chunks"
    refs_dir = Path(backup_dir) / "refs"
    chunk_store.mkdir(parents=True, exist_ok=True)
    refs_dir.mkdir(parents=True, exist_ok=True)

    chunk_count = {}  # hash -> count of references
    file_refs = {}    # filename -> list of (chunk_hash, offset)

    for root, dirs, files in os.walk(src_dir):
        for fname in files:
            src_path = Path(root) / fname
            rel = src_path.relative_to(src_dir)
            file_refs[str(rel)] = []

            for chunk_hash, chunk_data in chunk_file(src_path, chunk_size):
                chunk_path = chunk_store / chunk_hash
                if not chunk_path.exists():
                    chunk_path.write_bytes(chunk_data)
                chunk_count[chunk_hash] = chunk_count.get(chunk_hash, 0) + 1
                file_refs[str(rel)].append(chunk_hash)

    # Save refs
    import json
    with open(refs_dir / "manifest.json", 'w') as f:
        json.dump(file_refs, f)

    return chunk_count, file_refs

def restore_from_dedup(backup_dir, restore_dir):
    """Restore files from deduplicated backup."""
    Path(restore_dir).mkdir(parents=True, exist_ok=True)
    chunk_store = Path(backup_dir) / "chunks"
    refs_dir = Path(backup_dir) / "refs"

    import json
    with open(refs_dir / "manifest.json", 'r') as f:
        file_refs = json.load(f)

    for fname, chunk_hashes in file_refs.items():
        dst_path = Path(restore_dir) / fname
        dst_path.parent.mkdir(parents=True, exist_ok=True)
        with open(dst_path, 'wb') as out:
            for chunk_hash in chunk_hashes:
                chunk_path = chunk_store / chunk_hash
                if chunk_path.exists():
                    out.write(chunk_path.read_bytes())
                else:
                    raise FileNotFoundError(f"Chunk {chunk_hash} missing in store")

def test_backup_dedup():
    """Test: create files with duplicate content, backup with dedup, verify chunk reuse, restore."""
    with tempfile.TemporaryDirectory() as tmpdir:
        src = Path(tmpdir) / "src"
        src.mkdir()
        backup_base = Path(tmpdir) / "backup"
        restore_base = Path(tmpdir) / "restore"

        # Create files with overlapping content (4KB chunks)
        chunk_data = b"X" * 4096
        (src / "file1.txt").write_bytes(chunk_data + b"_file1")
        (src / "file2.txt").write_bytes(chunk_data + b"_file2")
        (src / "file3.txt").write_bytes(chunk_data + b"_file3")

        # Backup with dedup
        chunk_count, file_refs = backup_with_dedup(src, backup_base, chunk_size=4096)

        # Verify actual chunk reuse
        stored_chunks_list = list((Path(backup_base) / "chunks").glob("*"))
        # 3 files with same 4KB chunk = 1 chunk stored, 3 references
        assert len(stored_chunks_list) >= 1, f"Should have at least 1 stored chunk, got {len(stored_chunks_list)}"
        max_refs = max(chunk_count.values()) if chunk_count else 0
        assert max_refs == 3, f"Expected 3 chunk refs (reused), got {max_refs}"

        # Restore and verify
        restore_from_dedup(backup_base, restore_base)
        assert (restore_base / "file1.txt").read_bytes() == chunk_data + b"_file1"
        assert (restore_base / "file2.txt").read_bytes() == chunk_data + b"_file2"
        assert (restore_base / "file3.txt").read_bytes() == chunk_data + b"_file3"

        # Failure case: corrupt the SHARED chunk (the one all 3 files reference) and
        # prove the corruption is both DETECTABLE and PROPAGATES — the real risk dedup
        # carries. (The earlier version asserted True here, which proved nothing.)
        shared_hash = max(chunk_count, key=chunk_count.get)
        assert chunk_count[shared_hash] == 3, "the shared 4KB chunk should back all 3 files"
        chunk_path = Path(backup_base) / "chunks" / shared_hash
        chunk_path.write_bytes(b"CORRUPTED")

        # (a) Content-addressed invariant is broken: the chunk no longer hashes to its
        #     own name, so a verifying store can DETECT the corruption.
        rehash = hashlib.sha256(chunk_path.read_bytes()).hexdigest()
        assert rehash != shared_hash, "corruption must break the content-address invariant (detectable)"

        # (b) The corruption PROPAGATES: every file built from that chunk now differs
        #     from its source — assert it for all three, unconditionally.
        restore_base2 = Path(tmpdir) / "restore2"
        restore_from_dedup(backup_base, restore_base2)
        for fname in ["file1.txt", "file2.txt", "file3.txt"]:
            restored = (restore_base2 / fname).read_bytes()
            assert restored != (src / fname).read_bytes(), \
                f"{fname} must reflect the corrupted shared chunk"

if __name__ == "__main__":
    test_backup_dedup()
    print("✓ backup_dedup passed")
