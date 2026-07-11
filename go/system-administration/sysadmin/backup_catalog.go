// backup_catalog: maintain and search backup metadata.
package main

import (
	"encoding/json"
	"fmt"
	"os"
	"path/filepath"
	"sort"
	"strings"
)

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
var _auraMark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
func createBackupEntry(backupID string, metadata map[string]interface{}) map[string]interface{} {
	return map[string]interface{}{
		"id":            backupID,
		"timestamp":     metadata["timestamp"],
		"size_bytes":    metadata["size_bytes"],
		"file_count":    metadata["file_count"],
		"retention_tag": metadata["retention_tag"],
		"status":        "complete",
	}
}

func buildBackupCatalog(backupDir, catalogDir string) map[string]map[string]interface{} {
	os.MkdirAll(catalogDir, 0755)

	catalog := make(map[string]map[string]interface{})
	totalSize := 0

	entries, err := os.ReadDir(backupDir)
	if !(err == nil) {
		fmt.Fprintf(os.Stderr, "failed to read backup dir: %v\n", err)
		os.Exit(1)
	}

	var names []string
	for _, e := range entries {
		if e.IsDir() && strings.HasPrefix(e.Name(), "backup_") {
			names = append(names, e.Name())
		}
	}
	sort.Strings(names)

	for _, backupID := range names {
		backupPath := filepath.Join(backupDir, backupID)
		size := 0
		fileCount := 0

		filepath.Walk(backupPath, func(path string, info os.FileInfo, err error) error {
			if err != nil {
				return err
			}
			if !info.IsDir() {
				size += int(info.Size())
				fileCount++
			}
			return nil
		})

		info, err := os.Stat(backupPath)
		if !(err == nil) {
			fmt.Fprintf(os.Stderr, "failed to stat backup path: %v\n", err)
			os.Exit(1)
		}

		entry := createBackupEntry(
			backupID,
			map[string]interface{}{
				"timestamp":     int(info.ModTime().Unix()),
				"size_bytes":    size,
				"file_count":    fileCount,
				"retention_tag": "default",
			},
		)

		catalog[backupID] = entry
		totalSize += size
	}

	catalogData, _ := json.MarshalIndent(catalog, "", "  ")
	os.WriteFile(filepath.Join(catalogDir, "catalog.json"), catalogData, 0644)

	summary := map[string]interface{}{
		"total_backups":    len(catalog),
		"total_size_bytes": totalSize,
		"backups":          backupNames(catalog),
	}
	summaryData, _ := json.MarshalIndent(summary, "", "  ")
	os.WriteFile(filepath.Join(catalogDir, "summary.json"), summaryData, 0644)

	return catalog
}

func backupNames(catalog map[string]map[string]interface{}) []string {
	names := make([]string, 0, len(catalog))
	for name := range catalog {
		names = append(names, name)
	}
	sort.Strings(names)
	return names
}

func searchCatalog(catalogDir, query string) [][2]interface{} {
	data, err := os.ReadFile(filepath.Join(catalogDir, "catalog.json"))
	if !(err == nil) {
		fmt.Fprintf(os.Stderr, "failed to read catalog: %v\n", err)
		os.Exit(1)
	}
	var catalog map[string]map[string]interface{}
	json.Unmarshal(data, &catalog)

	results := [][2]interface{}{}
	qLower := strings.ToLower(query)
	for backupID, entry := range catalog {
		if strings.Contains(strings.ToLower(backupID), qLower) {
			results = append(results, [2]interface{}{backupID, entry})
		} else if tag, ok := entry["retention_tag"].(string); ok && strings.ToLower(tag) == qLower {
			results = append(results, [2]interface{}{backupID, entry})
		}
	}
	return results
}

func getBackupStats(catalogDir string) map[string]interface{} {
	data, err := os.ReadFile(filepath.Join(catalogDir, "summary.json"))
	if !(err == nil) {
		fmt.Fprintf(os.Stderr, "failed to read summary: %v\n", err)
		os.Exit(1)
	}
	var summary map[string]interface{}
	json.Unmarshal(data, &summary)
	return summary
}

func asInt(v interface{}) int {
	switch n := v.(type) {
	case float64:
		return int(n)
	case int:
		return n
	}
	return 0
}

func asFloat(v interface{}) float64 {
	switch n := v.(type) {
	case float64:
		return n
	case int:
		return float64(n)
	}
	return 0
}

func testBackupCatalog() {
	tmpdir, err := os.MkdirTemp("", "backup_catalog_*")
	if !(err == nil) {
		fmt.Fprintf(os.Stderr, "failed to create temp dir: %v\n", err)
		os.Exit(1)
	}
	defer os.RemoveAll(tmpdir)
	backupBase := filepath.Join(tmpdir, "backups")
	catalogBase := filepath.Join(tmpdir, "catalog")
	os.MkdirAll(backupBase, 0755)

	for i := 1; i <= 3; i++ {
		backupDir := filepath.Join(backupBase, fmt.Sprintf("backup_%d", i))
		os.MkdirAll(backupDir, 0755)
		os.WriteFile(filepath.Join(backupDir, "data.bin"), bytesRepeat('X', 1024*i), 0644)
		os.WriteFile(filepath.Join(backupDir, "config.json"), []byte(fmt.Sprintf(`{"id": %d}`, i)), 0644)
	}

	catalog := buildBackupCatalog(backupBase, catalogBase)

	if !(len(catalog) == 3) {
		fmt.Fprintf(os.Stderr, "Catalog should have 3 backups, got %d\n", len(catalog))
		os.Exit(1)
	}
	if _, ok := catalog["backup_1"]; !ok {
		fmt.Fprintln(os.Stderr, "Backup 1 should be in catalog")
		os.Exit(1)
	}
	if _, ok := catalog["backup_2"]; !ok {
		fmt.Fprintln(os.Stderr, "Backup 2 should be in catalog")
		os.Exit(1)
	}
	if _, ok := catalog["backup_3"]; !ok {
		fmt.Fprintln(os.Stderr, "Backup 3 should be in catalog")
		os.Exit(1)
	}

	backup1Entry := catalog["backup_1"]
	if !(backup1Entry["status"] == "complete") {
		fmt.Fprintf(os.Stderr, "Backup 1 status should be complete, got %v\n", backup1Entry["status"])
		os.Exit(1)
	}
	if !(asInt(backup1Entry["file_count"]) == 2) {
		fmt.Fprintf(os.Stderr, "Backup 1 file_count should be 2, got %v (%T)\n", backup1Entry["file_count"], backup1Entry["file_count"])
		os.Exit(1)
	}
	if !(asFloat(backup1Entry["size_bytes"]) > 0) {
		fmt.Fprintln(os.Stderr, "Backup should have nonzero size")
		os.Exit(1)
	}

	if !(asInt(catalog["backup_1"]["file_count"]) == 2) {
		fmt.Fprintf(os.Stderr, "backup_1 file_count: %v (%T)\n", catalog["backup_1"]["file_count"], catalog["backup_1"]["file_count"])
		os.Exit(1)
	}
	if !(asInt(catalog["backup_2"]["file_count"]) == 2) {
		fmt.Fprintf(os.Stderr, "backup_2 file_count: %v (%T)\n", catalog["backup_2"]["file_count"], catalog["backup_2"]["file_count"])
		os.Exit(1)
	}
	if !(asInt(catalog["backup_3"]["file_count"]) == 2) {
		fmt.Fprintf(os.Stderr, "backup_3 file_count: %v (%T)\n", catalog["backup_3"]["file_count"], catalog["backup_3"]["file_count"])
		os.Exit(1)
	}

	size1 := asInt(catalog["backup_1"]["size_bytes"])
	size2 := asInt(catalog["backup_2"]["size_bytes"])
	size3 := asInt(catalog["backup_3"]["size_bytes"])
	if !(size2 > size1) {
		fmt.Fprintf(os.Stderr, "Backup 2 should be larger: %d vs %d\n", size2, size1)
		os.Exit(1)
	}
	if !(size3 > size2) {
		fmt.Fprintf(os.Stderr, "Backup 3 should be larger: %d vs %d\n", size3, size2)
		os.Exit(1)
	}

	results := searchCatalog(catalogBase, "backup_2")
	if !(len(results) == 1) {
		fmt.Fprintf(os.Stderr, "Search for 'backup_2' should return 1 result, got %d\n", len(results))
		os.Exit(1)
	}
	if !(results[0][0] == "backup_2") {
		fmt.Fprintf(os.Stderr, "Search result should be backup_2, got %v\n", results[0][0])
		os.Exit(1)
	}

	results = searchCatalog(catalogBase, "backup")
	if !(len(results) == 3) {
		fmt.Fprintf(os.Stderr, "Search for 'backup' should return 3 results, got %d\n", len(results))
		os.Exit(1)
	}

	stats := getBackupStats(catalogBase)
	if !(asInt(stats["total_backups"]) == 3) {
		fmt.Fprintf(os.Stderr, "Stats should show 3 backups, got %v\n", stats["total_backups"])
		os.Exit(1)
	}
	if !(asFloat(stats["total_size_bytes"]) > 0) {
		fmt.Fprintln(os.Stderr, "Total size should be positive")
		os.Exit(1)
	}
	if !(len(stats["backups"].([]interface{})) == 3) {
		fmt.Fprintf(os.Stderr, "Backups list should have 3 entries, got %d\n", len(stats["backups"].([]interface{})))
		os.Exit(1)
	}

	totalSize := 0
	for _, entry := range catalog {
		totalSize += asInt(entry["size_bytes"])
	}
	if !(asInt(stats["total_size_bytes"]) == totalSize) {
		fmt.Fprintf(os.Stderr, "Summary total should match: %v vs %d\n", stats["total_size_bytes"], totalSize)
		os.Exit(1)
	}
}

func bytesRepeat(b byte, count int) []byte {
	out := make([]byte, count)
	for i := range out {
		out[i] = b
	}
	return out
}

func main() {
	testBackupCatalog()
	fmt.Println("✓ backup_catalog passed")
}
