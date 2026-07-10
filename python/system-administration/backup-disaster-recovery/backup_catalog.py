#!/usr/bin/env python3
"""backup_catalog: maintain and search backup metadata."""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import os
import sys
import tempfile
import json
from pathlib import Path

def create_backup_entry(backup_id, metadata):
    """Create backup catalog entry."""
    return {
        "id": backup_id,
        "timestamp": metadata.get("timestamp"),
        "size_bytes": metadata.get("size_bytes"),
        "file_count": metadata.get("file_count"),
        "retention_tag": metadata.get("retention_tag"),
        "status": "complete"
    }

def build_backup_catalog(backup_dir, catalog_dir):
    """Scan backup directory and build catalog index."""
    Path(catalog_dir).mkdir(parents=True, exist_ok=True)

    catalog = {}
    total_size = 0

    for backup_path in sorted(Path(backup_dir).glob("backup_*")):
        if not backup_path.is_dir():
            continue

        backup_id = backup_path.name
        size = 0
        file_count = 0

        for root, dirs, files in os.walk(backup_path):
            for fname in files:
                fpath = Path(root) / fname
                size += fpath.stat().st_size
                file_count += 1

        entry = create_backup_entry(
            backup_id,
            {
                "timestamp": int(backup_path.stat().st_mtime),
                "size_bytes": size,
                "file_count": file_count,
                "retention_tag": "default"
            }
        )

        catalog[backup_id] = entry
        total_size += size

    # Save catalog
    with open(Path(catalog_dir) / "catalog.json", 'w') as f:
        json.dump(catalog, f, indent=2)

    # Save summary
    summary = {
        "total_backups": len(catalog),
        "total_size_bytes": total_size,
        "backups": list(catalog.keys())
    }
    with open(Path(catalog_dir) / "summary.json", 'w') as f:
        json.dump(summary, f, indent=2)

    return catalog

def search_catalog(catalog_dir, query):
    """Search catalog by backup ID or metadata."""
    with open(Path(catalog_dir) / "catalog.json", 'r') as f:
        catalog = json.load(f)

    results = []
    for backup_id, entry in catalog.items():
        # Search by ID substring
        if query.lower() in backup_id.lower():
            results.append((backup_id, entry))
        # Search by retention tag
        elif query.lower() == entry.get("retention_tag", "").lower():
            results.append((backup_id, entry))

    return results

def get_backup_stats(catalog_dir):
    """Get catalog statistics."""
    with open(Path(catalog_dir) / "summary.json", 'r') as f:
        summary = json.load(f)

    return summary

def test_backup_catalog():
    """Test: create backups, build catalog, search, verify stats."""
    with tempfile.TemporaryDirectory() as tmpdir:
        backup_base = Path(tmpdir) / "backups"
        backup_base.mkdir()
        catalog_base = Path(tmpdir) / "catalog"

        # Create test backups
        for i in range(1, 4):
            backup_dir = backup_base / f"backup_{i}"
            backup_dir.mkdir()

            # Create files of different sizes
            (backup_dir / "data.bin").write_bytes(b"X" * (1024 * i))  # i KB each
            (backup_dir / "config.json").write_text(f'{{"id": {i}}}')

        # Build catalog
        catalog = build_backup_catalog(backup_base, catalog_base)

        # Verify catalog has all backups
        assert len(catalog) == 3, f"Catalog should have 3 backups, got {len(catalog)}"
        assert "backup_1" in catalog, "Backup 1 should be in catalog"
        assert "backup_2" in catalog, "Backup 2 should be in catalog"
        assert "backup_3" in catalog, "Backup 3 should be in catalog"

        # Verify metadata
        backup1_entry = catalog["backup_1"]
        assert backup1_entry["status"] == "complete"
        assert backup1_entry["file_count"] == 2  # data.bin + config.json
        assert backup1_entry["size_bytes"] > 0, "Backup should have nonzero size"

        # Verify file counts
        assert catalog["backup_1"]["file_count"] == 2
        assert catalog["backup_2"]["file_count"] == 2
        assert catalog["backup_3"]["file_count"] == 2

        # Verify sizes are proportional (backup_i has i KB of data)
        size1 = catalog["backup_1"]["size_bytes"]
        size2 = catalog["backup_2"]["size_bytes"]
        size3 = catalog["backup_3"]["size_bytes"]
        assert size2 > size1, f"Backup 2 should be larger: {size2} vs {size1}"
        assert size3 > size2, f"Backup 3 should be larger: {size3} vs {size2}"

        # Test search
        results = search_catalog(catalog_base, "backup_2")
        assert len(results) == 1, f"Search for 'backup_2' should return 1 result, got {len(results)}"
        assert results[0][0] == "backup_2", "Search result should be backup_2"

        # Test wildcard search
        results = search_catalog(catalog_base, "backup")
        assert len(results) == 3, f"Search for 'backup' should return 3 results, got {len(results)}"

        # Test stats
        stats = get_backup_stats(catalog_base)
        assert stats["total_backups"] == 3, f"Stats should show 3 backups, got {stats['total_backups']}"
        assert stats["total_size_bytes"] > 0, "Total size should be positive"
        assert len(stats["backups"]) == 3, "Backups list should have 3 entries"

        # Verify summary accuracy
        total_size = sum(entry["size_bytes"] for entry in catalog.values())
        assert stats["total_size_bytes"] == total_size, f"Summary total should match: {stats['total_size_bytes']} vs {total_size}"

if __name__ == "__main__":
    test_backup_catalog()
    print("✓ backup_catalog passed")
