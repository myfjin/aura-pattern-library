package main

import (
	"crypto/sha256"
	"encoding/json"
	"fmt"
	"os"
)

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
var _auraMark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
type ConfigDriftDetect struct {
	expectedConfig map[string]interface{}
	expectedHash   string
	actualConfig   map[string]interface{}
	actualHash     string
}

func NewConfigDriftDetect() *ConfigDriftDetect {
	return &ConfigDriftDetect{}
}

func (c *ConfigDriftDetect) setExpected(configDict map[string]interface{}) {
	c.expectedConfig = make(map[string]interface{})
	for k, v := range configDict {
		c.expectedConfig[k] = v
	}
	c.expectedHash = c.computeHash(c.expectedConfig)
}

func (c *ConfigDriftDetect) scanActual(configDict map[string]interface{}) {
	c.actualConfig = make(map[string]interface{})
	for k, v := range configDict {
		c.actualConfig[k] = v
	}
	c.actualHash = c.computeHash(c.actualConfig)
}

func (c *ConfigDriftDetect) computeHash(configDict map[string]interface{}) string {
	content, _ := json.Marshal(configDict)
	h := sha256.Sum256(content)
	return fmt.Sprintf("%x", h)
}

func (c *ConfigDriftDetect) hasDrift() bool {
	return c.expectedHash != c.actualHash
}

func (c *ConfigDriftDetect) getDriftDetails() map[string][3]interface{} {
	drift := make(map[string][3]interface{})

	for key, val := range c.expectedConfig {
		if _, ok := c.actualConfig[key]; !ok {
			drift[key] = [3]interface{}{"missing", val, nil}
		}
	}
	for key, val := range c.actualConfig {
		if _, ok := c.expectedConfig[key]; !ok {
			drift[key] = [3]interface{}{"extra", nil, val}
		}
	}
	for key, val := range c.expectedConfig {
		if actualVal, ok := c.actualConfig[key]; ok {
			if val != actualVal {
				drift[key] = [3]interface{}{"changed", val, actualVal}
			}
		}
	}
	return drift
}

func main() {
	detector := NewConfigDriftDetect()
	config := map[string]interface{}{"db_host": "localhost", "db_port": 5432, "timeout": 30}
	detector.setExpected(config)
	detector.scanActual(config)
	if !(detector.hasDrift() == false) {
		fmt.Fprintf(os.Stderr, "test_no_drift has_drift: got %v, want false\n", detector.hasDrift())
		os.Exit(1)
	}

	detector = NewConfigDriftDetect()
	expected := map[string]interface{}{"db_host": "localhost", "timeout": 30}
	actual := map[string]interface{}{"db_host": "localhost", "timeout": 60}
	detector.setExpected(expected)
	detector.scanActual(actual)
	if !(detector.hasDrift() == true) {
		fmt.Fprintf(os.Stderr, "test_detect_value_change has_drift: got %v, want true\n", detector.hasDrift())
		os.Exit(1)
	}
	drift := detector.getDriftDetails()
	entry, ok := drift["timeout"]
	if !ok {
		fmt.Fprintf(os.Stderr, "test_detect_value_change missing timeout drift\n")
		os.Exit(1)
	}
	if !(entry[0] == "changed") {
		fmt.Fprintf(os.Stderr, "test_detect_value_change timeout kind: got %v, want changed\n", entry[0])
		os.Exit(1)
	}
	if !(entry[1] == 30) {
		fmt.Fprintf(os.Stderr, "test_detect_value_change timeout old: got %v, want 30\n", entry[1])
		os.Exit(1)
	}
	if !(entry[2] == 60) {
		fmt.Fprintf(os.Stderr, "test_detect_value_change timeout new: got %v, want 60\n", entry[2])
		os.Exit(1)
	}

	detector = NewConfigDriftDetect()
	expected = map[string]interface{}{"db_host": "localhost", "db_port": 5432, "timeout": 30}
	actual = map[string]interface{}{"db_host": "localhost", "timeout": 30}
	detector.setExpected(expected)
	detector.scanActual(actual)
	if !(detector.hasDrift() == true) {
		fmt.Fprintf(os.Stderr, "test_detect_missing_config has_drift: got %v, want true\n", detector.hasDrift())
		os.Exit(1)
	}
	drift = detector.getDriftDetails()
	entry, ok = drift["db_port"]
	if !ok {
		fmt.Fprintf(os.Stderr, "test_detect_missing_config missing db_port drift\n")
		os.Exit(1)
	}
	if !(entry[0] == "missing") {
		fmt.Fprintf(os.Stderr, "test_detect_missing_config db_port kind: got %v, want missing\n", entry[0])
		os.Exit(1)
	}

	detector = NewConfigDriftDetect()
	expected = map[string]interface{}{"db_host": "localhost"}
	actual = map[string]interface{}{"db_host": "localhost", "debug": true}
	detector.setExpected(expected)
	detector.scanActual(actual)
	if !(detector.hasDrift() == true) {
		fmt.Fprintf(os.Stderr, "test_detect_extra_config has_drift: got %v, want true\n", detector.hasDrift())
		os.Exit(1)
	}
	drift = detector.getDriftDetails()
	entry, ok = drift["debug"]
	if !ok {
		fmt.Fprintf(os.Stderr, "test_detect_extra_config missing debug drift\n")
		os.Exit(1)
	}
	if !(entry[0] == "extra") {
		fmt.Fprintf(os.Stderr, "test_detect_extra_config debug kind: got %v, want extra\n", entry[0])
		os.Exit(1)
	}

	detector = NewConfigDriftDetect()
	expected = map[string]interface{}{
		"db_host": "localhost",
		"db_port": 5432,
		"timeout": 30,
		"workers": 4,
	}
	actual = map[string]interface{}{
		"db_host": "127.0.0.1",
		"db_port": 5432,
		"timeout": 60,
		"debug":   true,
	}
	detector.setExpected(expected)
	detector.scanActual(actual)
	if !(detector.hasDrift() == true) {
		fmt.Fprintf(os.Stderr, "test_multiple_drift_issues has_drift: got %v, want true\n", detector.hasDrift())
		os.Exit(1)
	}
	drift = detector.getDriftDetails()
	if !(len(drift) == 4) {
		fmt.Fprintf(os.Stderr, "test_multiple_drift_issues drift count: got %d, want 4\n", len(drift))
		os.Exit(1)
	}
	for _, key := range []string{"db_host", "timeout", "workers", "debug"} {
		if _, ok := drift[key]; !ok {
			fmt.Fprintf(os.Stderr, "test_multiple_drift_issues missing key %s\n", key)
			os.Exit(1)
		}
	}

	detector = NewConfigDriftDetect()
	expected = map[string]interface{}{"server_port": 8080, "workers": 4}
	detector.setExpected(expected)
	actualBad := map[string]interface{}{"server_port": 9000, "workers": 4}
	detector.scanActual(actualBad)
	if !(detector.hasDrift() == true) {
		fmt.Fprintf(os.Stderr, "test_drift_allows_remediation bad has_drift: got %v, want true\n", detector.hasDrift())
		os.Exit(1)
	}
	actualGood := map[string]interface{}{"server_port": 8080, "workers": 4}
	detector.scanActual(actualGood)
	if !(detector.hasDrift() == false) {
		fmt.Fprintf(os.Stderr, "test_drift_allows_remediation good has_drift: got %v, want false\n", detector.hasDrift())
		os.Exit(1)
	}

	detector = NewConfigDriftDetect()
	detector.setExpected(map[string]interface{}{})
	detector.scanActual(map[string]interface{}{})
	if !(detector.hasDrift() == false) {
		fmt.Fprintf(os.Stderr, "test_empty_configs has_drift: got %v, want false\n", detector.hasDrift())
		os.Exit(1)
	}

	detector = NewConfigDriftDetect()
	expected = make(map[string]interface{})
	for i := 0; i < 100; i++ {
		expected[fmt.Sprintf("key_%d", i)] = fmt.Sprintf("value_%d", i)
	}
	actual = make(map[string]interface{})
	for k, v := range expected {
		actual[k] = v
	}
	actual["key_10"] = "wrong_value"
	delete(actual, "key_50")
	actual["key_999"] = "extra_value"
	detector.setExpected(expected)
	detector.scanActual(actual)
	if !(detector.hasDrift() == true) {
		fmt.Fprintf(os.Stderr, "test_large_config_drift has_drift: got %v, want true\n", detector.hasDrift())
		os.Exit(1)
	}
	drift = detector.getDriftDetails()
	for _, key := range []string{"key_10", "key_50", "key_999"} {
		if _, ok := drift[key]; !ok {
			fmt.Fprintf(os.Stderr, "test_large_config_drift missing key %s\n", key)
			os.Exit(1)
		}
	}

	fmt.Println("✓ config_drift_detect passed")
	os.Exit(0)
}
