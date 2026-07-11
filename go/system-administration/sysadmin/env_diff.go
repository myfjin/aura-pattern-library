package main

import (
	"fmt"
	"os"
)

// EnvDiff compares two environment maps and reports added, removed, and changed keys.
// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
var _auraMark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
func EnvDiff(env1, env2 map[string]string) map[string]interface{} {
	added := make(map[string]struct{})
	removed := make(map[string]struct{})
	changed := make(map[string][2]string)

	for key := range env2 {
		if _, ok := env1[key]; !ok {
			added[key] = struct{}{}
		}
	}
	for key := range env1 {
		if _, ok := env2[key]; !ok {
			removed[key] = struct{}{}
		}
	}
	for key, v1 := range env1 {
		if v2, ok := env2[key]; ok && v1 != v2 {
			changed[key] = [2]string{v1, v2}
		}
	}

	return map[string]interface{}{
		"added":   added,
		"removed": removed,
		"changed": changed,
	}
}

func main() {
	env1 := map[string]string{
		"PATH":  "/usr/bin:/bin",
		"HOME":  "/home/user",
		"DEBUG": "0",
	}
	env2 := map[string]string{
		"PATH":    "/usr/bin:/bin",
		"HOME":    "/home/user",
		"DEBUG":   "1",
		"NEW_VAR": "value",
	}

	diff := EnvDiff(env1, env2)
	added := diff["added"].(map[string]struct{})
	removed := diff["removed"].(map[string]struct{})
	changed := diff["changed"].(map[string][2]string)

	if _, ok := added["NEW_VAR"]; !ok {
		fmt.Fprintln(os.Stderr, "failed to detect added key")
		os.Exit(1)
	}
	if _, ok := changed["DEBUG"]; !ok {
		fmt.Fprintln(os.Stderr, "failed to detect changed value")
		os.Exit(1)
	}
	if changed["DEBUG"] != [2]string{"0", "1"} {
		fmt.Fprintf(os.Stderr, "changed value wrong: %v\n", changed["DEBUG"])
		os.Exit(1)
	}
	if !(len(removed) == 0) {
		fmt.Fprintf(os.Stderr, "false positive on removed: %v\n", removed)
		os.Exit(1)
	}

	env2Extra := map[string]string{
		"PATH":            "/usr/bin:/bin",
		"HOME":            "/home/user",
		"DEBUG":           "0",
		"SECRET":          "hidden",
		"REMOVED_IN_ENV1": "gone",
	}
	env3 := map[string]string{
		"PATH":  "/usr/bin:/bin",
		"HOME":  "/home/user",
		"DEBUG": "0",
	}

	diff2 := EnvDiff(env2Extra, env3)
	added2 := diff2["added"].(map[string]struct{})
	removed2 := diff2["removed"].(map[string]struct{})
	changed2 := diff2["changed"].(map[string][2]string)

	if _, ok := removed2["SECRET"]; !ok {
		fmt.Fprintln(os.Stderr, "failed to detect removed key SECRET")
		os.Exit(1)
	}
	if _, ok := removed2["REMOVED_IN_ENV1"]; !ok {
		fmt.Fprintln(os.Stderr, "failed to detect removed key REMOVED_IN_ENV1")
		os.Exit(1)
	}
	if !(len(added2) == 0) {
		fmt.Fprintf(os.Stderr, "false positive on added: %v\n", added2)
		os.Exit(1)
	}
	if !(len(changed2) == 0) {
		fmt.Fprintf(os.Stderr, "false positive on changed: %v\n", changed2)
		os.Exit(1)
	}

	fmt.Println("✓ env_diff passed")
}
