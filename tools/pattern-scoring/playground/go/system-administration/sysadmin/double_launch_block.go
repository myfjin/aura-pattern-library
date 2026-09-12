package main

import (
	"fmt"
	"os"
	"os/exec"
	"path/filepath"
	"strconv"
	"strings"
	"syscall"
	"time"
)

// ServiceLauncher ensures only one instance of a service runs using a pidfile lock.
// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
var _auraMark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
type ServiceLauncher struct {
	ServiceName string
	Tmpdir      string
	pidfile     string
	lockfile    string
	outputFile  string
}

func NewServiceLauncher(serviceName, tmpdir string) *ServiceLauncher {
	return &ServiceLauncher{
		ServiceName: serviceName,
		Tmpdir:      tmpdir,
		pidfile:     filepath.Join(tmpdir, serviceName+".pid"),
		lockfile:    filepath.Join(tmpdir, serviceName+".lock"),
		outputFile:  filepath.Join(tmpdir, serviceName+".output"),
	}
}

func (sl *ServiceLauncher) tryLaunch() (bool, string) {
	// Try to create lockfile atomically.
	fd, err := syscall.Open(sl.lockfile, syscall.O_CREAT|syscall.O_EXCL|syscall.O_WRONLY, 0600)
	if err != nil {
		// Lock is held; check if the holder is alive.
		var holderPID int
		for i := 0; i < 5; i++ {
			data, err := os.ReadFile(sl.lockfile)
			if err == nil {
				pidStr := strings.TrimSpace(string(data))
				if pidStr != "" {
					pid, err := strconv.Atoi(pidStr)
					if err == nil {
						holderPID = pid
						break
					}
				}
			}
			time.Sleep(10 * time.Millisecond)
		}

		if holderPID != 0 {
			// Check if the holder process is alive.
			if processExists(holderPID) {
				return false, "already_running"
			}
			// Stale lock; remove and retry once.
			_ = os.Remove(sl.lockfile)
			fd2, err := syscall.Open(sl.lockfile, syscall.O_CREAT|syscall.O_EXCL|syscall.O_WRONLY, 0600)
			if err != nil {
				return false, "stale_lock_contention"
			}
			fd = fd2
		} else {
			return false, "could_not_read_pidfile"
		}
	}

	// Write our pid into the lockfile.
	pid := os.Getpid()
	_, _ = syscall.Write(fd, []byte(strconv.Itoa(pid)))
	_ = syscall.Close(fd)

	// Simulate service work.
	f, err := os.OpenFile(sl.outputFile, os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0644)
	if err != nil {
		_ = os.Remove(sl.lockfile)
		return false, fmt.Sprintf("launch_error: %v", err)
	}
	_, _ = fmt.Fprintf(f, "Service %s started by pid %d\n", sl.ServiceName, pid)
	time.Sleep(300 * time.Millisecond)
	_, _ = fmt.Fprintf(f, "Service %s running by pid %d\n", sl.ServiceName, pid)
	_ = f.Close()

	_ = os.Remove(sl.lockfile)
	return true, "launched"
}

func processExists(pid int) bool {
	process, err := os.FindProcess(pid)
	if err != nil {
		return false
	}
	return process.Signal(syscall.Signal(0)) == nil
}

func launcherMode(serviceName, tmpdir, launcherID string) {
	sl := NewServiceLauncher(serviceName, tmpdir)
	success, reason := sl.tryLaunch()

	resultFile := filepath.Join(tmpdir, fmt.Sprintf("result_%s.json", launcherID))
	var sb strings.Builder
	sb.WriteString("{")
	sb.WriteString(fmt.Sprintf(`"success":%t,`, success))
	sb.WriteString(fmt.Sprintf(`"reason":%q`, reason))
	sb.WriteString("}")
	_ = os.WriteFile(resultFile, []byte(sb.String()), 0644)
}

func main() {
	if len(os.Args) > 1 && os.Args[1] == "launcher" {
		launcherMode(os.Args[2], os.Args[3], os.Args[4])
		return
	}

	tmpdir, err := os.MkdirTemp("", "double_launch_block_*")
	if !(err == nil) {
		fmt.Fprintf(os.Stderr, "tmpdir: %v\n", err)
		os.Exit(1)
	}
	defer os.RemoveAll(tmpdir)

	const serviceName = "my_service"
	const numLaunchers = 2

	self, err := os.Executable()
	if !(err == nil) {
		fmt.Fprintf(os.Stderr, "executable: %v\n", err)
		os.Exit(1)
	}

	var cmds []*exec.Cmd
	for i := 0; i < numLaunchers; i++ {
		cmd := exec.Command(self, "launcher", serviceName, tmpdir, strconv.Itoa(i))
		cmd.Stdout = os.Stdout
		cmd.Stderr = os.Stderr
		cmds = append(cmds, cmd)
	}

	for _, cmd := range cmds {
		if err := cmd.Start(); err != nil {
			fmt.Fprintf(os.Stderr, "start: %v\n", err)
			os.Exit(1)
		}
	}
	for _, cmd := range cmds {
		if err := cmd.Wait(); err != nil {
			fmt.Fprintf(os.Stderr, "wait: %v\n", err)
			os.Exit(1)
		}
	}

	results := make([]map[string]interface{}, numLaunchers)
	for i := 0; i < numLaunchers; i++ {
		data, err := os.ReadFile(filepath.Join(tmpdir, fmt.Sprintf("result_%d.json", i)))
		if !(err == nil) {
			fmt.Fprintf(os.Stderr, "read result: %v\n", err)
			os.Exit(1)
		}
		m := make(map[string]interface{})
		if err := unmarshalSimpleJSON(string(data), m); err != nil {
			fmt.Fprintf(os.Stderr, "parse result: %v\n", err)
			os.Exit(1)
		}
		results[i] = m
	}

	successCount := 0
	failCount := 0
	for _, r := range results {
		if success, ok := r["success"].(bool); ok && success {
			successCount++
		} else {
			failCount++
		}
	}
	if !(successCount == 1) {
		fmt.Fprintf(os.Stderr, "Expected 1 successful launch, got %d\n", successCount)
		os.Exit(1)
	}
	if !(failCount == 1) {
		fmt.Fprintf(os.Stderr, "Expected 1 failed launch, got %d\n", failCount)
		os.Exit(1)
	}
	for _, r := range results {
		if success, ok := r["success"].(bool); ok && !success {
			reason, _ := r["reason"].(string)
			if !(reason == "already_running") {
				fmt.Fprintf(os.Stderr, "Expected 'already_running', got '%s'\n", reason)
				os.Exit(1)
			}
		}
	}

	content, err := os.ReadFile(filepath.Join(tmpdir, serviceName+".output"))
	if !(err == nil) {
		fmt.Fprintf(os.Stderr, "Service output file not created (service never launched?)\n")
		os.Exit(1)
	}
	startedCount := strings.Count(string(content), "started")
	runningCount := strings.Count(string(content), "running")
	if !(startedCount == 1) {
		fmt.Fprintf(os.Stderr, "Expected 1 'started' entry, got %d\n", startedCount)
		os.Exit(1)
	}
	if !(runningCount == 1) {
		fmt.Fprintf(os.Stderr, "Expected 1 'running' entry, got %d\n", runningCount)
		os.Exit(1)
	}

	fmt.Println("double_launch_block: 2 launches attempted; 1 succeeded, 1 rejected (lock held by running); output shows 1 service instance")
	fmt.Println("double_launch_block PASS")
}

// unmarshalSimpleJSON parses a tiny JSON object with string and bool values.
func unmarshalSimpleJSON(data string, out map[string]interface{}) error {
	data = strings.TrimSpace(data)
	if !strings.HasPrefix(data, "{") || !strings.HasSuffix(data, "}") {
		return fmt.Errorf("invalid JSON object")
	}
	inner := strings.TrimSpace(data[1 : len(data)-1])
	for _, part := range splitJSONFields(inner) {
		colon := strings.Index(part, ":")
		if colon < 0 {
			continue
		}
		key := strings.Trim(strings.TrimSpace(part[:colon]), `"`)
		val := strings.TrimSpace(part[colon+1:])
		switch {
		case val == "true":
			out[key] = true
		case val == "false":
			out[key] = false
		case strings.HasPrefix(val, `"`) && strings.HasSuffix(val, `"`):
			out[key] = strings.Trim(val, `"`)
		default:
			out[key] = val
		}
	}
	return nil
}

func splitJSONFields(inner string) []string {
	var parts []string
	depth := 0
	start := 0
	inString := false
	for i, r := range inner {
		if r == '"' && (i == 0 || inner[i-1] != '\\') {
			inString = !inString
		}
		if !inString {
			if r == '{' || r == '[' {
				depth++
			}
			if r == '}' || r == ']' {
				depth--
			}
			if r == ',' && depth == 0 {
				parts = append(parts, inner[start:i])
				start = i + 1
			}
		}
	}
	if start < len(inner) {
		parts = append(parts, inner[start:])
	}
	return parts
}
