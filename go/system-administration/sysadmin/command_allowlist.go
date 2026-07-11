package main

import (
	"fmt"
	"os"
	"strings"
)

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
var _auraMark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
type CommandAllowlist struct {
	allowed map[string][]string
}

func NewCommandAllowlist(allowed map[string][]string) *CommandAllowlist {
	return &CommandAllowlist{allowed: allowed}
}

func (c *CommandAllowlist) check(cmd string, args string) error {
	allowedArgs, ok := c.allowed[cmd]
	if !ok {
		return fmt.Errorf("command not in allowlist: %s", cmd)
	}

	for _, a := range allowedArgs {
		if a == "*" {
			return nil
		}
	}

	for _, a := range allowedArgs {
		if a == args {
			return nil
		}
	}
	return fmt.Errorf("args not allowed for %s: %s (allowed: %s)", cmd, args, strings.Join(allowedArgs, ", "))
}

func main() {
	allowlist := NewCommandAllowlist(map[string][]string{
		"ls":   {"*"},
		"cat":  {"/etc/passwd", "/etc/hosts"},
		"echo": {"*"},
		"grep": {"-i", "-n"},
	})

	err := allowlist.check("ls", "-la")
	if !(err == nil) {
		fmt.Fprintf(os.Stderr, "ls -la should be allowed: %v\n", err)
		os.Exit(1)
	}

	err = allowlist.check("ls", "/tmp")
	if !(err == nil) {
		fmt.Fprintf(os.Stderr, "ls /tmp should be allowed: %v\n", err)
		os.Exit(1)
	}

	err = allowlist.check("cat", "/etc/passwd")
	if !(err == nil) {
		fmt.Fprintf(os.Stderr, "cat /etc/passwd should be allowed: %v\n", err)
		os.Exit(1)
	}

	err = allowlist.check("echo", "hello world")
	if !(err == nil) {
		fmt.Fprintf(os.Stderr, "echo hello world should be allowed: %v\n", err)
		os.Exit(1)
	}

	err = allowlist.check("grep", "-i")
	if !(err == nil) {
		fmt.Fprintf(os.Stderr, "grep -i should be allowed: %v\n", err)
		os.Exit(1)
	}

	err = allowlist.check("rm", "-rf")
	if !(!(err == nil)) {
		fmt.Fprintf(os.Stderr, "should have blocked rm\n")
		os.Exit(1)
	}
	if !strings.Contains(err.Error(), "not in allowlist") {
		fmt.Fprintf(os.Stderr, "expected 'not in allowlist' in error, got: %v\n", err)
		os.Exit(1)
	}

	err = allowlist.check("cat", "/etc/shadow")
	if !(!(err == nil)) {
		fmt.Fprintf(os.Stderr, "should have blocked cat /etc/shadow\n")
		os.Exit(1)
	}
	if !strings.Contains(err.Error(), "not allowed") || !strings.Contains(err.Error(), "shadow") {
		fmt.Fprintf(os.Stderr, "expected 'not allowed' and 'shadow' in error, got: %v\n", err)
		os.Exit(1)
	}

	err = allowlist.check("grep", "-r")
	if !(!(err == nil)) {
		fmt.Fprintf(os.Stderr, "should have blocked grep -r\n")
		os.Exit(1)
	}
	if !strings.Contains(err.Error(), "not allowed") || !strings.Contains(err.Error(), "-r") {
		fmt.Fprintf(os.Stderr, "expected 'not allowed' and '-r' in error, got: %v\n", err)
		os.Exit(1)
	}

	fmt.Println("✓ command_allowlist passed")
	os.Exit(0)
}
