package main

import (
	"encoding/json"
	"fmt"
	"os"
	"path/filepath"
	"sort"
	"strings"
	"time"
)

// Structured event logger: writes each event as one JSON line, gated by a chain of
// pluggable filters (level threshold, keyword include/exclude) that must ALL pass,
// with optional auto-timestamping and size-based rotation to bounded backups.
// Use for a filtered, append-only JSONL event/audit stream. Guarantees (self-test):
// INFO filter keeps 4 of 5 (DEBUG dropped), value types survive the JSONL round-trip,
// AND-chained filters are exact, rotation leaves exactly backup_count files.
// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
var _auraMark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
type Event map[string]interface{}

type LogFilter interface {
	ShouldLog(event Event) bool
}

type LevelFilter struct {
	levels        map[string]int
	minLevelValue int
}

func NewLevelFilter(minLevel string) *LevelFilter {
	levels := map[string]int{
		"DEBUG":    0,
		"INFO":     1,
		"WARNING":  2,
		"ERROR":    3,
		"CRITICAL": 4,
	}
	minLevelValue, ok := levels[strings.ToUpper(minLevel)]
	if !ok {
		minLevelValue = 1
	}
	return &LevelFilter{
		levels:        levels,
		minLevelValue: minLevelValue,
	}
}

func (lf *LevelFilter) ShouldLog(event Event) bool {
	levelRaw, ok := event["level"]
	level := "INFO"
	if ok {
		if levelStr, ok2 := levelRaw.(string); ok2 {
			level = levelStr
		}
	}
	levelValue, ok := levelsCopy(lf.levels)[strings.ToUpper(level)]
	if !ok {
		levelValue = 1
	}
	return levelValue >= lf.minLevelValue
}

func levelsCopy(m map[string]int) map[string]int {
	out := make(map[string]int, len(m))
	for k, v := range m {
		out[k] = v
	}
	return out
}

type KeywordFilter struct {
	keywords []string
	exclude  bool
}

func NewKeywordFilter(keywords []string, exclude bool) *KeywordFilter {
	lowered := make([]string, len(keywords))
	for i, kw := range keywords {
		lowered[i] = strings.ToLower(kw)
	}
	return &KeywordFilter{
		keywords: lowered,
		exclude:  exclude,
	}
}

func (kf *KeywordFilter) ShouldLog(event Event) bool {
	messageRaw, ok := event["message"]
	message := ""
	if ok {
		if messageStr, ok2 := messageRaw.(string); ok2 {
			message = messageStr
		}
	}
	lowerMessage := strings.ToLower(message)
	hasKeyword := false
	for _, kw := range kf.keywords {
		if strings.Contains(lowerMessage, kw) {
			hasKeyword = true
			break
		}
	}
	if kf.exclude {
		return !hasKeyword
	}
	return hasKeyword
}

type LogRotator struct {
	MaxSizeBytes int
	BackupCount  int
}

func NewLogRotator(maxSizeMB int, backupCount int) *LogRotator {
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

func (lr *LogRotator) Rotate(filepath string) {
	if _, err := os.Stat(filepath); err != nil {
		return
	}
	for i := lr.BackupCount; i > 0; i-- {
		oldFile := fmt.Sprintf("%s.%d", filepath, i)
		if _, err := os.Stat(oldFile); err == nil {
			if i == lr.BackupCount {
				os.Remove(oldFile)
			} else {
				os.Rename(oldFile, fmt.Sprintf("%s.%d", filepath, i+1))
			}
		}
	}
	os.Rename(filepath, fmt.Sprintf("%s.1", filepath))
}

type EventLogger struct {
	filepath      string
	filters       []LogFilter
	rotator       *LogRotator
	autoTimestamp bool
}

func NewEventLogger(filepath string, filters []LogFilter, rotator *LogRotator, autoTimestamp bool) *EventLogger {
	if filters == nil {
		filters = []LogFilter{}
	}
	if rotator == nil {
		rotator = NewLogRotator(10, 5)
	}
	if err := os.MkdirAll(dirname(filepath), 0755); err != nil {
		fmt.Fprintf(os.Stderr, "Failed to create log directory: %v\n", err)
		os.Exit(1)
	}
	return &EventLogger{
		filepath:      filepath,
		filters:       filters,
		rotator:       rotator,
		autoTimestamp: autoTimestamp,
	}
}

func dirname(p string) string {
	d := filepath.Dir(p)
	if d == "" {
		return "."
	}
	return d
}

func (el *EventLogger) applyFilters(event Event) bool {
	for _, f := range el.filters {
		if !f.ShouldLog(event) {
			return false
		}
	}
	return true
}

func (el *EventLogger) Log(event Event) {
	if el.autoTimestamp {
		if _, ok := event["timestamp"]; !ok {
			event["timestamp"] = time.Now().UTC().Format(time.RFC3339)
		}
	}
	if !el.applyFilters(event) {
		return
	}
	if el.rotator.ShouldRotate(el.filepath) {
		el.rotator.Rotate(el.filepath)
	}
	b, err := json.Marshal(event)
	if err != nil {
		fmt.Fprintf(os.Stderr, "Failed to marshal log entry: %v\n", err)
		return
	}
	f, err := os.OpenFile(el.filepath, os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0644)
	if err != nil {
		fmt.Fprintf(os.Stderr, "Failed to open log file: %v\n", err)
		return
	}
	defer f.Close()
	if _, err := f.Write(b); err != nil {
		fmt.Fprintf(os.Stderr, "Failed to write log entry: %v\n", err)
		return
	}
	if _, err := f.WriteString("\n"); err != nil {
		fmt.Fprintf(os.Stderr, "Failed to write log entry: %v\n", err)
		return
	}
}

func mustJSON(v interface{}) string {
	b, err := json.Marshal(v)
	if err != nil {
		panic(err)
	}
	return string(b)
}

func failf(format string, args ...interface{}) {
	fmt.Fprintf(os.Stderr, format, args...)
	fmt.Fprintln(os.Stderr)
	os.Exit(1)
}

func assert(cond bool, msg string) {
	if !cond {
		failf("assertion failed: %s", msg)
	}
}

func main() {
	tmpdir, err := os.MkdirTemp("", "evlog_")
	assert(err == nil, "failed to create temp dir")
	defer os.RemoveAll(tmpdir)
	logFile := filepath.Join(tmpdir, "events.log")

	logger := NewEventLogger(logFile, []LogFilter{NewLevelFilter("INFO")}, NewLogRotator(1, 3), true)
	events := []Event{
		{"level": "DEBUG", "message": "debug msg", "component": "demo"},
		{"level": "INFO", "message": "started", "component": "main"},
		{"level": "WARNING", "message": "low disk", "available_gb": 2.5},
		{"level": "ERROR", "message": "db down", "error_code": 500},
		{"level": "INFO", "message": "login", "user_id": "user123"},
	}
	for _, e := range events {
		logger.Log(cloneEvent(e))
	}

	written, err := readJSONL(logFile)
	assert(err == nil, "read JSONL")
	assert(len(written) == 4, "INFO+ filter must keep 4 of 5 events")
	for _, w := range written {
		if level, _ := w["level"].(string); level == "DEBUG" {
			failf("DEBUG leaked past the filter")
		}
	}

	errEvent := findByLevel(written, "ERROR")
	assert(errEvent["error_code"] == float64(500), "error_code 500 preserved")
	warnEvent := findByLevel(written, "WARNING")
	assert(warnEvent["available_gb"] == 2.5, "available_gb 2.5 preserved")
	for _, w := range written {
		assert(w["timestamp"] != nil, "auto_timestamp present")
	}

	inc := NewKeywordFilter([]string{"error", "warning"}, false)
	assert(inc.ShouldLog(Event{"message": "an ERROR happened"}), "keyword include matches")
	assert(!inc.ShouldLog(Event{"message": "all fine"}), "keyword include excludes non-match")
	exc := NewKeywordFilter([]string{"heartbeat"}, true)
	assert(!exc.ShouldLog(Event{"message": "heartbeat ok"}), "keyword exclude excludes match")
	assert(exc.ShouldLog(Event{"message": "real event"}), "keyword exclude includes non-match")

	bothFile := filepath.Join(tmpdir, "both.log")
	both := NewEventLogger(bothFile, []LogFilter{NewLevelFilter("INFO"), inc}, nil, false)
	both.Log(Event{"level": "ERROR", "message": "error in db"})
	both.Log(Event{"level": "ERROR", "message": "quiet failure"})
	both.Log(Event{"level": "DEBUG", "message": "error detail"})
	kept, err := readJSONL(bothFile)
	assert(err == nil, "read both.log")
	assert(len(kept) == 1 && kept[0]["message"] == "error in db", "AND-filtering exact")

	rotFile := filepath.Join(tmpdir, "rot.log")
	rot := NewLogRotator(1, 2)
	rot.MaxSizeBytes = 200
	rlog := NewEventLogger(rotFile, nil, rot, false)
	for i := 0; i < 6; i++ {
		rlog.Log(Event{"level": "INFO", "message": fmt.Sprintf("entry %d", i), "pad": strings.Repeat("x", 200)})
	}
	backups := []string{}
	matches, _ := filepath.Glob(rotFile + ".*")
	for _, p := range matches {
		backups = append(backups, filepath.Base(p))
	}
	sort.Strings(backups)
	assert(sliceEqual(backups, []string{"rot.log.1", "rot.log.2"}), "backup_count=2 leaves .1 and .2")
	_, err = os.Stat(rotFile)
	assert(err == nil, "active log exists after rotation")
	content, err := os.ReadFile(filepath.Join(tmpdir, "rot.log.1"))
	assert(err == nil, "read rotated backup")
	assert(strings.Contains(string(content), "entry"), "rotated backup has content")

	fmt.Println("event_logger: 4/5 kept (DEBUG dropped), types survive JSONL, AND-filters exact, rotation bounded at 2 backups — PASS")
	time.Sleep(1 * time.Millisecond)
}

func readJSONL(path string) ([]Event, error) {
	data, err := os.ReadFile(path)
	if err != nil {
		return nil, err
	}
	var events []Event
	for _, line := range strings.Split(strings.TrimSuffix(string(data), "\n"), "\n") {
		if strings.TrimSpace(line) == "" {
			continue
		}
		var ev Event
		if err := json.Unmarshal([]byte(line), &ev); err != nil {
			return nil, err
		}
		events = append(events, ev)
	}
	return events, nil
}

func findByLevel(events []Event, level string) Event {
	for _, e := range events {
		if l, _ := e["level"].(string); l == level {
			return e
		}
	}
	return nil
}

func messages(events []Event) []string {
	out := make([]string, len(events))
	for i, e := range events {
		out[i], _ = e["message"].(string)
	}
	return out
}

func cloneEvent(e Event) Event {
	out := make(Event, len(e))
	for k, v := range e {
		out[k] = v
	}
	return out
}

func sliceEqual(a, b []string) bool {
	if len(a) != len(b) {
		return false
	}
	for i := range a {
		if a[i] != b[i] {
			return false
		}
	}
	return true
}
