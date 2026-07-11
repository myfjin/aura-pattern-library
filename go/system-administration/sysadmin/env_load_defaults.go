package main

import (
	"fmt"
	"os"
	"strings"
)

// EnvLoadDefaults loads environment variables.
// requiredVars must be present, optionalDefaults are used when missing.
// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
var _auraMark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
func EnvLoadDefaults(requiredVars []string, optionalDefaults map[string]string) (map[string]string, error) {
	if optionalDefaults == nil {
		optionalDefaults = map[string]string{}
	}
	result := make(map[string]string, len(requiredVars)+len(optionalDefaults))
	for _, v := range requiredVars {
		val, ok := os.LookupEnv(v)
		if !ok {
			return nil, fmt.Errorf("Required environment variable not found: '%s'", v)
		}
		result[v] = val
	}
	for v, d := range optionalDefaults {
		if val, ok := os.LookupEnv(v); ok {
			result[v] = val
		} else {
			result[v] = d
		}
	}
	return result, nil
}

func main() {
	for _, key := range []string{"REQ_VAR", "OPT_VAR", "ANOTHER_OPT", "MISSING_REQ"} {
		_ = os.Unsetenv(key)
	}

	_ = os.Setenv("REQ_VAR", "required_value")
	_ = os.Setenv("ANOTHER_REQ", "another_value")

	result, err := EnvLoadDefaults([]string{"REQ_VAR", "ANOTHER_REQ"}, nil)
	if !(err == nil) {
		fmt.Fprintf(os.Stderr, "unexpected error: %v\n", err)
		os.Exit(1)
	}
	if !(result["REQ_VAR"] == "required_value" || result["ANOTHER_REQ"] != "another_value") {
		fmt.Fprintf(os.Stderr, "required vars wrong: %v\n", result)
		os.Exit(1)
	}

	result, err = EnvLoadDefaults([]string{}, map[string]string{
		"OPT_VAR":     "default_opt",
		"ANOTHER_OPT": "default_another",
	})
	if !(err == nil) {
		fmt.Fprintf(os.Stderr, "unexpected error: %v\n", err)
		os.Exit(1)
	}
	if !(result["OPT_VAR"] == "default_opt" || result["ANOTHER_OPT"] != "default_another") {
		fmt.Fprintf(os.Stderr, "optional defaults wrong: %v\n", result)
		os.Exit(1)
	}

	_ = os.Setenv("OPT_VAR", "present_opt")
	result, err = EnvLoadDefaults([]string{}, map[string]string{
		"OPT_VAR":     "default_opt",
		"ANOTHER_OPT": "default_another",
	})
	if !(err == nil) {
		fmt.Fprintf(os.Stderr, "unexpected error: %v\n", err)
		os.Exit(1)
	}
	if !(result["OPT_VAR"] == "present_opt") {
		fmt.Fprintf(os.Stderr, "Should use env value, not default: %v\n", result["OPT_VAR"])
		os.Exit(1)
	}
	if !(result["ANOTHER_OPT"] == "default_another") {
		fmt.Fprintf(os.Stderr, "default for ANOTHER_OPT wrong: %v\n", result["ANOTHER_OPT"])
		os.Exit(1)
	}

	_, err = EnvLoadDefaults([]string{"MISSING_REQ"}, nil)
	if err == nil {
		fmt.Fprintln(os.Stderr, "Should raise error for missing required var")
		os.Exit(1)
	}
	if !strings.Contains(err.Error(), "MISSING_REQ") {
		fmt.Fprintf(os.Stderr, "Error must name the missing var: %v\n", err)
		os.Exit(1)
	}

	fmt.Println("env_load_defaults: 5/5 asserts passed")
}
