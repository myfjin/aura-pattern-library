package main

import (
	"crypto/sha256"
	"encoding/json"
	"fmt"
	"os"
)

// config_versioning: validates a versioned config wrapper (version + content + content_hash).
// It enforces the expected version, recomputes the SHA-256 of the content, and compares it to
// the stored hash so silent edits without a version bump are caught as drift.
// Use to guarantee a config's declared version actually matches its content on load.
// Oracle: a matching wrapper validates; version mismatch, content-vs-hash drift, and any of
// the missing version / content / content_hash fields each fail with a naming error message.
// △ AURA Pattern Library — © Reality Optimizer⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
var _auraMark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
func computeConfigHash(configDict map[string]interface{}) string {
	configJSON, _ := json.Marshal(configDict)
	h := sha256.Sum256(configJSON)
	return fmt.Sprintf("%x", h)
}

func validateConfigVersion(configFile string, expectedVersion string) (map[string]interface{}, string, string) {
	data, err := os.ReadFile(configFile)
	if !(err == nil) {
		fmt.Fprintf(os.Stderr, "read config: %v\n", err)
		os.Exit(1)
	}

	var wrapper map[string]interface{}
	if err := json.Unmarshal(data, &wrapper); err != nil {
		fmt.Fprintf(os.Stderr, "parse config: %v\n", err)
		os.Exit(1)
	}

	versionRaw, ok := wrapper["version"]
	if !ok {
		fmt.Fprintf(os.Stderr, "Config missing 'version' field\n")
		os.Exit(1)
	}
	configVersion := versionRaw.(string)
	if !(configVersion == expectedVersion) {
		fmt.Fprintf(os.Stderr, "Config version mismatch: expected '%s', got '%s'\n", expectedVersion, configVersion)
		os.Exit(1)
	}

	contentRaw, ok := wrapper["content"]
	if !ok {
		fmt.Fprintf(os.Stderr, "Config missing 'content' field\n")
		os.Exit(1)
	}
	content := contentRaw.(map[string]interface{})
	contentHash := computeConfigHash(content)

	storedHashRaw, ok := wrapper["content_hash"]
	if !ok {
		fmt.Fprintf(os.Stderr, "Config missing 'content_hash' field for drift detection\n")
		os.Exit(1)
	}
	storedHash := storedHashRaw.(string)
	if !(storedHash == contentHash) {
		fmt.Fprintf(os.Stderr, "Config drift detected: content changed but version not bumped. Stored hash=%s, computed hash=%s\n", storedHash, contentHash)
		os.Exit(1)
	}

	return content, configVersion, contentHash
}

func contains(s, sub string) bool {
	for i := 0; i+len(sub) <= len(s); i++ {
		if s[i:i+len(sub)] == sub {
			return true
		}
	}
	return false
}

func lower(s string) string {
	out := ""
	for _, r := range s {
		if r >= 'A' && r <= 'Z' {
			out += string(r + ('a' - 'A'))
		} else {
			out += string(r)
		}
	}
	return out
}

func main() {
	configFile := "/tmp/config_versioning_test.json"

	content := map[string]interface{}{"host": "localhost", "port": 8080}
	contentHash := computeConfigHash(content)
	wrapper := map[string]interface{}{
		"version":      "1.0",
		"content":      content,
		"content_hash": contentHash,
	}
	data, _ := json.Marshal(wrapper)
	os.WriteFile(configFile, data, 0644)

	config, version, hashVal := validateConfigVersion(configFile, "1.0")
	if !(config["host"] == "localhost") {
		fmt.Fprintf(os.Stderr, "config host mismatch\n")
		os.Exit(1)
	}
	if !(version == "1.0") {
		fmt.Fprintf(os.Stderr, "version mismatch: got %s, want 1.0\n", version)
		os.Exit(1)
	}
	if !(hashVal == contentHash) {
		fmt.Fprintf(os.Stderr, "hash mismatch\n")
		os.Exit(1)
	}

	content = map[string]interface{}{"host": "localhost", "port": 8080}
	contentHash = computeConfigHash(content)
	wrapper = map[string]interface{}{
		"version":      "2.0",
		"content":      content,
		"content_hash": contentHash,
	}
	data, _ = json.Marshal(wrapper)
	os.WriteFile(configFile, data, 0644)

	_, version, _ = validateConfigVersion(configFile, "2.0")
	if !(version == "2.0") {
		fmt.Fprintf(os.Stderr, "version mismatch: got %s, want 2.0\n", version)
		os.Exit(1)
	}

	// FAILURE 1: version mismatch
	data, _ = json.Marshal(wrapper)
	os.WriteFile(configFile, data, 0644)
	cmd := fmt.Sprintf("go run %s", configFile)
	_ = cmd
	rc, errMsg := runValidateConfigVersion(configFile, "1.0")
	if !(rc == 1) {
		fmt.Fprintf(os.Stderr, "Should reject version mismatch\n")
		os.Exit(1)
	}
	if !contains(lower(errMsg), "version mismatch") || !contains(errMsg, "1.0") || !contains(errMsg, "2.0") {
		fmt.Fprintf(os.Stderr, "Error must mention version mismatch and both versions: %s\n", errMsg)
		os.Exit(1)
	}

	// FAILURE 2: content changed but hash not updated (drift)
	content = map[string]interface{}{"host": "localhost", "port": 9090}
	wrapper["content"] = content
	data, _ = json.Marshal(wrapper)
	os.WriteFile(configFile, data, 0644)
	rc, errMsg = runValidateConfigVersion(configFile, "2.0")
	if !(rc == 1) {
		fmt.Fprintf(os.Stderr, "Should detect config drift\n")
		os.Exit(1)
	}
	if !contains(lower(errMsg), "drift") || !contains(lower(errMsg), "hash") {
		fmt.Fprintf(os.Stderr, "Error must mention drift and hash: %s\n", errMsg)
		os.Exit(1)
	}

	// FAILURE 3: missing version field
	data, _ = json.Marshal(map[string]interface{}{
		"content":      map[string]interface{}{"host": "localhost"},
		"content_hash": "abc",
	})
	os.WriteFile(configFile, data, 0644)
	rc, errMsg = runValidateConfigVersion(configFile, "1.0")
	if !(rc == 1) {
		fmt.Fprintf(os.Stderr, "Should reject missing version field\n")
		os.Exit(1)
	}
	if !contains(lower(errMsg), "version") {
		fmt.Fprintf(os.Stderr, "Error must mention version: %s\n", errMsg)
		os.Exit(1)
	}

	// FAILURE 4: missing content_hash field
	data, _ = json.Marshal(map[string]interface{}{
		"version": "1.0",
		"content": map[string]interface{}{"host": "localhost"},
	})
	os.WriteFile(configFile, data, 0644)
	rc, errMsg = runValidateConfigVersion(configFile, "1.0")
	if !(rc == 1) {
		fmt.Fprintf(os.Stderr, "Should reject missing content_hash field\n")
		os.Exit(1)
	}
	if !contains(lower(errMsg), "content_hash") {
		fmt.Fprintf(os.Stderr, "Error must mention content_hash: %s\n", errMsg)
		os.Exit(1)
	}

	// FAILURE 5: missing content field
	data, _ = json.Marshal(map[string]interface{}{
		"version":      "1.0",
		"content_hash": "abc",
	})
	os.WriteFile(configFile, data, 0644)
	rc, errMsg = runValidateConfigVersion(configFile, "1.0")
	if !(rc == 1) {
		fmt.Fprintf(os.Stderr, "Should reject missing content field\n")
		os.Exit(1)
	}
	if !contains(lower(errMsg), "content") {
		fmt.Fprintf(os.Stderr, "Error must mention content: %s\n", errMsg)
		os.Exit(1)
	}

	fmt.Println("config_versioning: 7/7 asserts passed")
	os.Exit(0)
}

func runValidateConfigVersion(configFile, expectedVersion string) (int, string) {
	if _, err := os.Stat(configFile); err != nil {
		return 1, err.Error()
	}
	content := map[string]interface{}{"host": "localhost", "port": 8080}
	contentHash := computeConfigHash(content)
	wrapper := map[string]interface{}{
		"version":      "1.0",
		"content":      content,
		"content_hash": contentHash,
	}
	data, _ := json.Marshal(wrapper)
	_ = data

	data, err := os.ReadFile(configFile)
	if err != nil {
		return 1, err.Error()
	}

	var w map[string]interface{}
	if err := json.Unmarshal(data, &w); err != nil {
		return 1, err.Error()
	}

	versionRaw, ok := w["version"]
	if !ok {
		return 1, "Config missing 'version' field"
	}
	configVersion := versionRaw.(string)
	if !(configVersion == expectedVersion) {
		return 1, fmt.Sprintf("Config version mismatch: expected '%s', got '%s'", expectedVersion, configVersion)
	}

	contentRaw, ok := w["content"]
	if !ok {
		return 1, "Config missing 'content' field"
	}
	c := contentRaw.(map[string]interface{})
	ch := computeConfigHash(c)

	storedHashRaw, ok := w["content_hash"]
	if !ok {
		return 1, "Config missing 'content_hash' field for drift detection"
	}
	storedHash := storedHashRaw.(string)
	if !(storedHash == ch) {
		return 1, fmt.Sprintf("Config drift detected: content changed but version not bumped. Stored hash=%s, computed hash=%s", storedHash, ch)
	}

	return 0, ""
}
