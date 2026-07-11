package main

import (
	"fmt"
	"os"
	"path/filepath"
	"strings"
)

// EnvSecretLoad loads a secret from an environment variable safely.
// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
var _auraMark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
func EnvSecretLoad(envKey string, defaultValue *string) (string, error) {
	val, ok := os.LookupEnv(envKey)
	if !ok {
		if defaultValue != nil {
			return *defaultValue, nil
		}
		return "", fmt.Errorf("Env var %s not set and no default", envKey)
	}
	return val, nil
}

// LoadSecretsSafe loads multiple secrets from env vars and writes a usage log (not secrets).
func LoadSecretsSafe(envKeys []string, outputFile string) (map[string]string, error) {
	secrets := make(map[string]string, len(envKeys))
	for _, key := range envKeys {
		secret, err := EnvSecretLoad(key, nil)
		if err != nil {
			return nil, err
		}
		secrets[key] = secret
	}
	if outputFile != "" {
		var sb strings.Builder
		for _, key := range envKeys {
			sb.WriteString(fmt.Sprintf("Loaded secret for %s\n", key))
		}
		if err := os.WriteFile(outputFile, []byte(sb.String()), 0644); err != nil {
			return nil, err
		}
	}
	return secrets, nil
}

func main() {
	tmpdir, err := os.MkdirTemp("", "env_secret_load_*")
	if !(err == nil) {
		fmt.Fprintf(os.Stderr, "tmpdir: %v\n", err)
		os.Exit(1)
	}
	defer os.RemoveAll(tmpdir)

	secretDB := "password_db_hunter2_xyz"
	secretAPI := "api_key_sk_live_12345678"
	secretToken := "oauth_ghp_secret_token"

	_ = os.Setenv("DB_PASSWORD", secretDB)
	_ = os.Setenv("API_KEY", secretAPI)
	_ = os.Setenv("OAUTH_TOKEN", secretToken)

	// Capture stdout/stderr by redirecting to files.
	oldStdout := os.Stdout
	oldStderr := os.Stderr

	rStdout, wStdout, err := os.Pipe()
	if !(err == nil) {
		fmt.Fprintf(os.Stderr, "pipe stdout: %v\n", err)
		os.Exit(1)
	}
	rStderr, wStderr, err := os.Pipe()
	if !(err == nil) {
		fmt.Fprintf(os.Stderr, "pipe stderr: %v\n", err)
		os.Exit(1)
	}

	os.Stdout = wStdout
	os.Stderr = wStderr

	logFile := filepath.Join(tmpdir, "usage.log")
	secrets, err := LoadSecretsSafe([]string{"DB_PASSWORD", "API_KEY", "OAUTH_TOKEN"}, logFile)

	_ = wStdout.Close()
	_ = wStderr.Close()
	os.Stdout = oldStdout
	os.Stderr = oldStderr

	if !(err == nil) {
		fmt.Fprintf(os.Stderr, "load secrets: %v\n", err)
		os.Exit(1)
	}

	stdoutText := readAllString(rStdout)
	stderrText := readAllString(rStderr)

	for _, secret := range []string{secretDB, secretAPI, secretToken} {
		if strings.Contains(stdoutText, secret) {
			fmt.Fprintf(os.Stderr, "%s leaked to stdout\n", secret)
			os.Exit(1)
		}
		if strings.Contains(stderrText, secret) {
			fmt.Fprintf(os.Stderr, "%s leaked to stderr\n", secret)
			os.Exit(1)
		}
	}

	logContent, err := os.ReadFile(logFile)
	if !(err == nil) {
		fmt.Fprintf(os.Stderr, "read log: %v\n", err)
		os.Exit(1)
	}
	logText := string(logContent)
	for _, secret := range []string{secretDB, secretAPI, secretToken} {
		if strings.Contains(logText, secret) {
			fmt.Fprintf(os.Stderr, "%s in usage log\n", secret)
			os.Exit(1)
		}
	}
	for _, key := range []string{"DB_PASSWORD", "API_KEY", "OAUTH_TOKEN"} {
		if !strings.Contains(logText, key) {
			fmt.Fprintf(os.Stderr, "Log should mention %s\n", key)
			os.Exit(1)
		}
	}

	if !(secrets["DB_PASSWORD"] == secretDB || secrets["API_KEY"] != secretAPI || secrets["OAUTH_TOKEN"] != secretToken) {
		fmt.Fprintln(os.Stderr, "Secrets not loaded correctly")
		os.Exit(1)
	}

	fmt.Println("env_secret_load PASS")
}

func readAllString(r *os.File) string {
	data := make([]byte, 0, 4096)
	buf := make([]byte, 1024)
	for {
		n, err := r.Read(buf)
		if n > 0 {
			data = append(data, buf[:n]...)
		}
		if err != nil {
			break
		}
	}
	_ = r.Close()
	return string(data)
}
