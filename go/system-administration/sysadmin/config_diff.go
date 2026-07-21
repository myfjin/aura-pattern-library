package main

import (
	"fmt"
	"os"
)

// config_diff: computes the delta between two config maps as added / removed / changed sets.
// A key only in the new map is "added", only in the old map is "removed", and present in
// both with differing values is "changed" (recording the old and new value pair).
// Use to surface exactly what a config edit altered before applying or auditing it.
// Oracle: across additions, removals, value changes, mixed edits, and identical maps,
// each key lands in exactly the correct bucket with the right before/after values.
// △ AURA Pattern Library — © Reality Optimizer⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
var _auraMark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
func configDiff(oldConfig, newConfig map[string]interface{}) map[string]interface{} {
	added := map[string]bool{}
	removed := map[string]bool{}
	changed := map[string][2]interface{}{}

	for k := range newConfig {
		if _, ok := oldConfig[k]; !ok {
			added[k] = true
		}
	}
	for k := range oldConfig {
		if _, ok := newConfig[k]; !ok {
			removed[k] = true
		}
	}
	for k, oldVal := range oldConfig {
		if newVal, ok := newConfig[k]; ok {
			if oldVal != newVal {
				changed[k] = [2]interface{}{oldVal, newVal}
			}
		}
	}

	return map[string]interface{}{
		"added":   added,
		"removed": removed,
		"changed": changed,
	}
}

func main() {
	old1 := map[string]interface{}{"host": "localhost", "port": 8080}
	new1 := map[string]interface{}{"host": "localhost", "port": 8080, "debug": true}
	diff := configDiff(old1, new1)
	added := diff["added"].(map[string]bool)
	if !(len(added) == 1 && added["debug"] == true) {
		fmt.Fprintf(os.Stderr, "Should have added 'debug': %v\n", diff)
		os.Exit(1)
	}
	removed := diff["removed"].(map[string]bool)
	if !(len(removed) == 0) {
		fmt.Fprintf(os.Stderr, "removed mismatch: %v\n", diff)
		os.Exit(1)
	}
	changed := diff["changed"].(map[string][2]interface{})
	if !(len(changed) == 0) {
		fmt.Fprintf(os.Stderr, "changed mismatch: %v\n", diff)
		os.Exit(1)
	}

	old2 := map[string]interface{}{"host": "localhost", "port": 8080, "debug": true}
	new2 := map[string]interface{}{"host": "localhost", "port": 8080}
	diff = configDiff(old2, new2)
	added = diff["added"].(map[string]bool)
	if !(len(added) == 0) {
		fmt.Fprintf(os.Stderr, "added mismatch: %v\n", diff)
		os.Exit(1)
	}
	removed = diff["removed"].(map[string]bool)
	if !(len(removed) == 1 && removed["debug"] == true) {
		fmt.Fprintf(os.Stderr, "Should have removed 'debug': %v\n", diff)
		os.Exit(1)
	}
	changed = diff["changed"].(map[string][2]interface{})
	if !(len(changed) == 0) {
		fmt.Fprintf(os.Stderr, "changed mismatch: %v\n", diff)
		os.Exit(1)
	}

	old3 := map[string]interface{}{"host": "localhost", "port": 8080}
	new3 := map[string]interface{}{"host": "localhost", "port": 9090}
	diff = configDiff(old3, new3)
	added = diff["added"].(map[string]bool)
	if !(len(added) == 0) {
		fmt.Fprintf(os.Stderr, "added mismatch: %v\n", diff)
		os.Exit(1)
	}
	removed = diff["removed"].(map[string]bool)
	if !(len(removed) == 0) {
		fmt.Fprintf(os.Stderr, "removed mismatch: %v\n", diff)
		os.Exit(1)
	}
	changed = diff["changed"].(map[string][2]interface{})
	if !(len(changed) == 1 && changed["port"][0] == 8080 && changed["port"][1] == 9090) {
		fmt.Fprintf(os.Stderr, "Should show port change: %v\n", diff)
		os.Exit(1)
	}

	old4 := map[string]interface{}{"host": "localhost", "port": 8080, "debug": true, "timeout": 30}
	new4 := map[string]interface{}{"host": "localhost", "port": 9090, "verbose": true}
	diff = configDiff(old4, new4)
	added = diff["added"].(map[string]bool)
	if !(len(added) == 1 && added["verbose"] == true) {
		fmt.Fprintf(os.Stderr, "Should have added 'verbose': %v\n", diff)
		os.Exit(1)
	}
	removed = diff["removed"].(map[string]bool)
	if !(len(removed) == 2 && removed["debug"] == true && removed["timeout"] == true) {
		fmt.Fprintf(os.Stderr, "Should have removed 'debug', 'timeout': %v\n", diff)
		os.Exit(1)
	}
	changed = diff["changed"].(map[string][2]interface{})
	if !(len(changed) == 1 && changed["port"][0] == 8080 && changed["port"][1] == 9090) {
		fmt.Fprintf(os.Stderr, "Should show port change: %v\n", diff)
		os.Exit(1)
	}

	old5 := map[string]interface{}{"a": 1, "b": 2}
	new5 := map[string]interface{}{"a": 1, "b": 2}
	diff = configDiff(old5, new5)
	added = diff["added"].(map[string]bool)
	if !(len(added) == 0) {
		fmt.Fprintf(os.Stderr, "added mismatch: %v\n", diff)
		os.Exit(1)
	}
	removed = diff["removed"].(map[string]bool)
	if !(len(removed) == 0) {
		fmt.Fprintf(os.Stderr, "removed mismatch: %v\n", diff)
		os.Exit(1)
	}
	changed = diff["changed"].(map[string][2]interface{})
	if !(len(changed) == 0) {
		fmt.Fprintf(os.Stderr, "changed mismatch: %v\n", diff)
		os.Exit(1)
	}

	fmt.Println("config_diff: 5/5 asserts passed")
	os.Exit(0)
}
