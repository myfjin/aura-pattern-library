package main

import (
	"fmt"
	"os"
	"os/exec"
	"path/filepath"
	"sort"
	"strings"
	"syscall"
	"time"
)

// childScript is the Go source code we compile and run as a subprocess. It creates
// three versioned backup files, fsyncs them, signals readiness, then performs the
// atomic rotation sequence with pauses so the parent can SIGKILL it mid-rotation.
// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
var _auraMark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
const childScript = `package main
import (
	"fmt"
	"os"
	"time"
)
func main() {
	d := os.Args[1]
	p := func(v int) string { return filepath.Join(d, fmt.Sprintf("backup.v%d.txt", v)) }
	for i := 1; i <= 3; i++ {
		f, err := os.Create(p(i))
		if err != nil { panic(err) }
		_, _ = f.WriteString(fmt.Sprintf("backup_data_version_%d\n", i))
		_ = f.Sync()
		_ = f.Close()
	}
	ready := filepath.Join(d, "ready")
	_, _ = os.Create(ready)
	time.Sleep(150 * time.Millisecond)
	_ = os.Remove(p(1))
	time.Sleep(150 * time.Millisecond)
	_ = os.Rename(p(2), p(1))
	time.Sleep(150 * time.Millisecond)
	_ = os.Rename(p(3), p(2))
}
`

func survivingBackups(d string) [][2]string {
	files, err := os.ReadDir(d)
	if err != nil {
		return nil
	}
	sort.Slice(files, func(i, j int) bool { return files[i].Name() < files[j].Name() })
	out := make([][2]string, 0)
	for _, f := range files {
		name := f.Name()
		if strings.HasPrefix(name, "backup.v") && strings.HasSuffix(name, ".txt") {
			content, err := os.ReadFile(filepath.Join(d, name))
			if err != nil {
				continue
			}
			out = append(out, [2]string{name, string(content)})
		}
	}
	return out
}

func main() {
	tmpdir, err := os.MkdirTemp("", "backup_rotation_*")
	if !(err == nil) {
		fmt.Fprintf(os.Stderr, "temp dir: %v\n", err)
		os.Exit(1)
	}
	defer os.RemoveAll(tmpdir)
	bdir := filepath.Join(tmpdir, "backups")
	if err := os.MkdirAll(bdir, 0o755); err != nil {
		fmt.Fprintf(os.Stderr, "mkdir: %v\n", err)
		os.Exit(1)
	}

	// Write and build the child program. The child imports path/filepath and fmt,
	// so we include them in the source.
	childSrc := filepath.Join(tmpdir, "child.go")
	fullChildScript := strings.Replace(childScript, `import (
	"fmt"
	"os"
	"time"
)`, `import (
	"fmt"
	"os"
	"path/filepath"
	"time"
)`, 1)
	if err := os.WriteFile(childSrc, []byte(fullChildScript), 0o644); err != nil {
		fmt.Fprintf(os.Stderr, "write child source: %v\n", err)
		os.Exit(1)
	}
	childBin := filepath.Join(tmpdir, "child")
	cmdBuild := exec.Command("go", "build", "-o", childBin, childSrc)
	if err := cmdBuild.Run(); err != nil {
		fmt.Fprintf(os.Stderr, "build child: %v\n", err)
		os.Exit(1)
	}

	child := exec.Command(childBin, bdir)
	if err := child.Start(); err != nil {
		fmt.Fprintf(os.Stderr, "start child: %v\n", err)
		os.Exit(1)
	}

	readyPath := filepath.Join(bdir, "ready")
	for {
		_, err := os.Stat(readyPath)
		if err == nil {
			break
		}
		time.Sleep(5 * time.Millisecond)
	}
	time.Sleep(200 * time.Millisecond)
	if err := child.Process.Kill(); err != nil {
		_ = child.Process.Signal(syscall.SIGKILL)
	}
	_, _ = child.Process.Wait()

	survivors := survivingBackups(bdir)

	if len(survivors) == 0 {
		fmt.Fprintln(os.Stderr, "rotation crash lost ALL backups")
		os.Exit(1)
	}
	for _, sc := range survivors {
		content := sc[1]
		if !(strings.HasPrefix(content, "backup_data_version_") && strings.HasSuffix(content, "\n")) {
			fmt.Fprintf(os.Stderr, "%s is TORN/incomplete: %q\n", sc[0], content)
			os.Exit(1)
		}
	}

	allContent := strings.Builder{}
	for _, sc := range survivors {
		allContent.WriteString(sc[1])
	}
	if !strings.Contains(allContent.String(), "backup_data_version_3") {
		fmt.Fprintln(os.Stderr, "the NEWEST backup was lost during rotation")
		os.Exit(1)
	}

	fmt.Printf("backup_rotation: crash mid-rotation left %d complete backup(s), newest preserved\n", len(survivors))
	fmt.Println("backup_rotation PASS")
}
