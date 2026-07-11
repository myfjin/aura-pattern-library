package main

import (
	"encoding/json"
	"fmt"
	"os"
	"path/filepath"
	"strings"
	"time"
)

// LogFilter determines whether an event should be logged.
// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
var _auraMark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
type LogFilter interface {
	ShouldLog(event map[string]interface{}) bool
}

// LevelFilter filters events based on their log level.
type LevelFilter struct {
	Levels   map[string]int
	MinLevel int
}

func NewLevelFilter(minLevel string) *LevelFilter {
	levels := map[string]int{
		"DEBUG":    0,
		"INFO":     1,
		"WARNING":  2,
		"ERROR":    3,
		"CRITICAL": 4,
	}
	min := levels[strings.ToUpper(minLevel)]
	return &LevelFilter{Levels: levels, MinLevel: min}
}

func (lf *LevelFilter) ShouldLog(event map[string]interface{}) bool {
	level, _ := event["level"].(string)
	level = strings.ToUpper(level)
	if level == "" {
		level = "INFO"
	}
	return lf.Levels[level] >= lf.MinLevel
}

// KeywordFilter filters events based on keywords in the message.
type KeywordFilter struct {
	Keywords []string
	Exclude  bool
}

func NewKeywordFilter(keywords []string, exclude bool) *KeywordFilter {
	lower := make([]string, len(keywords))
	for i, kw := range keywords {
		lower[i] = strings.ToLower(kw)
	}
	return &KeywordFilter{Keywords: lower, Exclude: exclude}
}

func (kf *KeywordFilter) ShouldLog(event map[string]interface{}) bool {
	message, _ := event["message"].(string)
	message = strings.ToLower(message)
	hasKeyword := false
	for _, kw := range kf.Keywords {
		if strings.Contains(message, kw) {
			hasKeyword = true
			break
		}
	}
	if kf.Exclude {
		return !hasKeyword
	}
	return hasKeyword
}

// LogRotator handles log file rotation based on size.
type LogRotator struct {
	MaxSizeBytes int
	BackupCount  int
}

func NewLogRotator(maxSizeMB, backupCount int) *LogRotator {
	return &LogRotator{
		MaxSizeBytes: maxSizeMB * 1024 * 1024,
		BackupCount:  backupCount,
	}
}

func (lr *LogRotator) ShouldRotate(filepath string) bool {
	info, err := os.Stat(filepath)
	if err != nil {
		return false
	}
	return int(info.Size()) >= lr.MaxSizeBytes
}

func (lr *LogRotator) Rotate(path string) {
	if _, err := os.Stat(path); os.IsNotExist(err) {
		return
	}
	for i := lr.BackupCount; i > 0; i-- {
		oldFile := fmt.Sprintf("%s.%d", path, i)
		if _, err := os.Stat(oldFile); err == nil {
			if i == lr.BackupCount {
				_ = os.Remove(oldFile)
			} else {
				_ = os.Rename(oldFile, fmt.Sprintf("%s.%d", path, i+1))
			}
		}
	}
	_ = os.Rename(path, fmt.Sprintf("%s.1", path))
}

// EventLogger logs structured events with filtering and rotation.
type EventLogger struct {
	Filepath      string
	Filters       []LogFilter
	Rotator       *LogRotator
	AutoTimestamp bool
}

func NewEventLogger(filepath string, filters []LogFilter, rotator *LogRotator, autoTimestamp bool) *EventLogger {
	if filters == nil {
		filters = []LogFilter{}
	}
	if rotator == nil {
		rotator = NewLogRotator(10, 5)
	}
	_ = os.MkdirAll(getDir(filepath), 0755)
	return &EventLogger{
		Filepath:      filepath,
		Filters:       filters,
		Rotator:       rotator,
		AutoTimestamp: autoTimestamp,
	}
}

func getDir(path string) string {
	dir := filepath.Dir(path)
	if dir == "" || dir == "." {
		return "."
	}
	return dir
}

func (el *EventLogger) applyFilters(event map[string]interface{}) bool {
	for _, f := range el.Filters {
		if !f.ShouldLog(event) {
			return false
		}
	}
	return true
}

func (el *EventLogger) Log(event map[string]interface{}) {
	if el.AutoTimestamp {
		if _, ok := event["timestamp"]; !ok {
			event["timestamp"] = time.Now().UTC().Format(time.RFC3339) + "Z"
		}
	}
	if !el.applyFilters(event) {
		return
	}
	if el.Rotator.ShouldRotate(el.Filepath) {
		el.Rotator.Rotate(el.Filepath)
	}
	data, err := json.Marshal(event)
	if err != nil {
		fmt.Fprintf(os.Stderr, "Failed to marshal log entry: %v\n", err)
		return
	}
	f, err := os.OpenFile(el.Filepath, os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0644)
	if err != nil {
		fmt.Fprintf(os.Stderr, "Failed to write log entry: %v\n", err)
		return
	}
	defer f.Close()
	_, _ = fmt.Fprintln(f, string(data))
}

func main() {
	logFile := "demo_logs/events.log"
	_ = os.RemoveAll("demo_logs")

	levelFilter := NewLevelFilter("INFO")
	rotator := NewLogRotator(1, 3)
	logger := NewEventLogger(logFile, []LogFilter{levelFilter}, rotator, true)

	fmt.Println("Logging demo events...")

	logger.Log(map[string]interface{}{
		"level":     "DEBUG",
		"message":   "This is a debug message",
		"component": "demo",
	})
	logger.Log(map[string]interface{}{
		"level":     "INFO",
		"message":   "Application started successfully",
		"component": "main",
		"version":   "1.0.0",
	})
	logger.Log(map[string]interface{}{
		"level":        "WARNING",
		"message":      "Low disk space detected",
		"component":    "monitor",
		"available_gb": 2.5,
	})
	logger.Log(map[string]interface{}{
		"level":      "ERROR",
		"message":    "Failed to connect to database",
		"component":  "database",
		"error_code": 500,
	})
	logger.Log(map[string]interface{}{
		"level":     "INFO",
		"message":   "User login successful",
		"component": "auth",
		"user_id":   "user123",
	})

	fmt.Printf("\nContents of %s:\n", logFile)
	if data, err := os.ReadFile(logFile); err == nil {
		lines := strings.Split(strings.TrimSpace(string(data)), "\n")
		for i, line := range lines {
			var event map[string]interface{}
			if err := json.Unmarshal([]byte(line), &event); err == nil {
				fmt.Printf("%2d. %v\n", i+1, event)
			}
		}
	} else {
		fmt.Println("Log file not found")
	}

	fmt.Println("\nDemonstrating log rotation...")
	logger.Log(map[string]interface{}{
		"level":     "INFO",
		"message":   "Large data entry",
		"component": "demo",
		"data":      strings.Repeat("A", 1024*1024),
	})

	fmt.Println("Demo completed. Check the demo_logs directory for output files.")
}
