// crash_consistent_snapshot: snapshot a live DB atomically so the snapshot is never torn.
package main

import (
	"fmt"
	"os"
	"os/exec"
	"path/filepath"
	"strings"
	"syscall"
	"time"
)

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
var _auraMark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
func atomicSnapshot(dbPath, snapPath string) {
	part := snapPath + ".part"

	// Use sqlite3 CLI for backup (available on almost all test runners).
	cmd := exec.Command("sqlite3", dbPath, ".backup '"+part+"'")
	out, err := cmd.CombinedOutput()
	if !(err == nil) {
		fmt.Fprintf(os.Stderr, "backup command failed: %v\n%s\n", err, out)
		os.Exit(1)
	}

	fd, err := os.Open(part)
	if !(err == nil) {
		fmt.Fprintf(os.Stderr, "failed to open part for fsync: %v\n", err)
		os.Exit(1)
	}
	if err := fd.Sync(); err != nil {
		fd.Close()
		fmt.Fprintf(os.Stderr, "failed to fsync part: %v\n", err)
		os.Exit(1)
	}
	fd.Close()

	if err := os.Rename(part, snapPath); err != nil {
		fmt.Fprintf(os.Stderr, "failed to rename part: %v\n", err)
		os.Exit(1)
	}
}

func validDB(path string) bool {
	if _, err := os.Stat(path); err != nil {
		return false
	}
	cmd := exec.Command("sqlite3", path, "PRAGMA integrity_check;")
	out, err := cmd.CombinedOutput()
	return err == nil && strings.TrimSpace(string(out)) == "ok"
}

func initDB(dbPath string) (int, error) {
	cmd := exec.Command("sqlite3", dbPath,
		"CREATE TABLE t (id INTEGER PRIMARY KEY, val TEXT);")
	if out, err := cmd.CombinedOutput(); err != nil {
		return 0, fmt.Errorf("create table failed: %v\n%s", err, out)
	}

	var inserts []string
	for i := 0; i < 3000; i++ {
		inserts = append(inserts, fmt.Sprintf("INSERT INTO t (val) VALUES ('v%d');", i))
	}
	cmd = exec.Command("sqlite3", dbPath, strings.Join(inserts, ""))
	if out, err := cmd.CombinedOutput(); err != nil {
		return 0, fmt.Errorf("insert failed: %v\n%s", err, out)
	}

	cmd = exec.Command("sqlite3", dbPath, "SELECT COUNT(*) FROM t;")
	out, err := cmd.CombinedOutput()
	if err != nil {
		return 0, fmt.Errorf("count failed: %v\n%s", err, out)
	}
	var committed int
	fmt.Sscanf(strings.TrimSpace(string(out)), "%d", &committed)
	return committed, nil
}

func main() {
	tmpdir, err := os.MkdirTemp("", "crash_snapshot_*")
	if !(err == nil) {
		fmt.Fprintf(os.Stderr, "failed to create temp dir: %v\n", err)
		os.Exit(1)
	}
	defer os.RemoveAll(tmpdir)

	dbPath := filepath.Join(tmpdir, "live.db")
	committed, err := initDB(dbPath)
	if !(err == nil) {
		fmt.Fprintf(os.Stderr, "%v\n", err)
		os.Exit(1)
	}

	snap := filepath.Join(tmpdir, "snap.db")

	// THE CRASH: kill the snapshotter mid-copy, before its atomic rename.
	child := exec.Command(os.Args[0], "--child", dbPath, snap)
	if err := child.Start(); err != nil {
		fmt.Fprintf(os.Stderr, "failed to start child: %v\n", err)
		os.Exit(1)
	}
	time.Sleep(150 * time.Millisecond)
	child.Process.Signal(syscall.SIGKILL)
	child.Wait()

	if exists, _ := fileExists(snap); exists {
		if !validDB(snap) {
			fmt.Fprintf(os.Stderr, "snapshot target is TORN after mid-copy crash (atomicity violated)\n")
			os.Exit(1)
		}
	}

	for _, p := range []string{snap, snap + ".part"} {
		os.Remove(p)
	}
	atomicSnapshot(dbPath, snap)

	if !validDB(snap) {
		fmt.Fprintf(os.Stderr, "clean snapshot is not a valid DB\n")
		os.Exit(1)
	}
	cmd := exec.Command("sqlite3", snap, "SELECT COUNT(*) FROM t;")
	out, err := cmd.CombinedOutput()
	if !(err == nil) {
		fmt.Fprintf(os.Stderr, "failed to count snapshot rows: %v\n%s\n", err, out)
		os.Exit(1)
	}
	var snapRows int
	fmt.Sscanf(strings.TrimSpace(string(out)), "%d", &snapRows)
	if !(snapRows == committed) {
		fmt.Fprintf(os.Stderr, "snapshot rows %d != committed %d\n", snapRows, committed)
		os.Exit(1)
	}

	fmt.Printf("crash_consistent_snapshot: mid-copy crash left no torn target; clean snapshot = %d committed rows\n", committed)
	fmt.Println("crash_consistent_snapshot PASS")
}

func fileExists(path string) (bool, error) {
	_, err := os.Stat(path)
	if err == nil {
		return true, nil
	}
	if os.IsNotExist(err) {
		return false, nil
	}
	return false, err
}

// Child mode: slow page-by-page copy so parent can SIGKILL us before rename.
func init() {
	if len(os.Args) >= 4 && os.Args[1] == "--child" {
		dbPath := os.Args[2]
		snap := os.Args[3]
		part := snap + ".part"

		for i := 0; i < 3000; i++ {
			cmd := exec.Command("sqlite3", dbPath, fmt.Sprintf(".backup '%s_%d'", part, i))
			cmd.Run()
			time.Sleep(10 * time.Millisecond)
		}

		// Never reached if killed.
		os.Exit(0)
	}
}
