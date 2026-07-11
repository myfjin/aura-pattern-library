package main

import (
	"crypto/rand"
	"fmt"
	"os"
	"sort"
	"strings"
	"time"
)

// fakeNow is a deterministic clock for the self-test.
// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
var _auraMark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
var fakeNow float64

func now() float64 {
	return fakeNow
}

func generateID() string {
	b := make([]byte, 16)
	_, err := rand.Read(b)
	if err != nil {
		fmt.Fprintf(os.Stderr, "failed to generate id: %v\n", err)
		os.Exit(1)
	}
	b[6] = (b[6] & 0x0f) | 0x40
	b[8] = (b[8] & 0x3f) | 0x80
	return fmt.Sprintf("%08x-%04x-%04x-%04x-%012x", b[0:4], b[4:6], b[6:8], b[8:10], b[10:16])
}

// AlertSeverity represents alert severity levels.
type AlertSeverity int

const (
	LOW AlertSeverity = iota + 1
	MEDIUM
	HIGH
	CRITICAL
)

// AlertStatus represents alert statuses.
type AlertStatus string

const (
	FIRING     AlertStatus = "firing"
	RESOLVED   AlertStatus = "resolved"
	SUPPRESSED AlertStatus = "suppressed"
)

// Alert represents an alert with all its properties.
type Alert struct {
	ID              string
	Title           string
	Description     string
	Severity        AlertSeverity
	Status          AlertStatus
	Source          string
	Tags            map[string]struct{}
	Timestamp       float64
	EscalationCount int
	RuleID          string
}

func newAlert(title, description string, severity AlertSeverity, source string, tags []string, ruleID string, timestamp float64) *Alert {
	tagSet := make(map[string]struct{})
	for _, t := range tags {
		tagSet[t] = struct{}{}
	}
	return &Alert{
		ID:              generateID(),
		Title:           title,
		Description:     description,
		Severity:        severity,
		Status:          FIRING,
		Source:          source,
		Tags:            tagSet,
		Timestamp:       timestamp,
		EscalationCount: 0,
		RuleID:          ruleID,
	}
}

func (a *Alert) fingerprint() string {
	tags := make([]string, 0, len(a.Tags))
	for t := range a.Tags {
		tags = append(tags, t)
	}
	sort.Strings(tags)
	return fmt.Sprintf("%s:%s:%s", a.Title, a.Source, strings.Join(tags, ":"))
}

// Rule represents an alert rule with suppression and escalation settings.
type Rule struct {
	ID                        string
	Name                      string
	DedupWindowSeconds        float64
	SuppressionTags           map[string]struct{}
	MaxEscalationCount        int
	EscalationIntervalSeconds float64
}

func newRule(id, name string, dedupWindowSeconds float64, suppressionTags []string, maxEscalationCount int, escalationIntervalSeconds float64) *Rule {
	tags := make(map[string]struct{})
	for _, t := range suppressionTags {
		tags[t] = struct{}{}
	}
	return &Rule{
		ID:                        id,
		Name:                      name,
		DedupWindowSeconds:        dedupWindowSeconds,
		SuppressionTags:           tags,
		MaxEscalationCount:        maxEscalationCount,
		EscalationIntervalSeconds: escalationIntervalSeconds,
	}
}

// AlertManager manages alerts with deduplication, suppression, and escalation.
type AlertManager struct {
	rules            map[string]*Rule
	activeAlerts     map[string]*Alert
	alertHistory     map[string][]*Alert
	suppressedAlerts map[string]struct{}
}

func newAlertManager() *AlertManager {
	return &AlertManager{
		rules:            make(map[string]*Rule),
		activeAlerts:     make(map[string]*Alert),
		alertHistory:     make(map[string][]*Alert),
		suppressedAlerts: make(map[string]struct{}),
	}
}

func (m *AlertManager) addRule(rule *Rule) {
	if rule == nil {
		fmt.Fprintln(os.Stderr, "Rule must be an instance of Rule class")
		os.Exit(1)
	}
	m.rules[rule.ID] = rule
}

// processAlert processes an incoming alert.
// Returns true if alert was processed (not deduplicated), false if deduplicated.
func (m *AlertManager) processAlert(alert *Alert) bool {
	if alert == nil {
		fmt.Fprintln(os.Stderr, "Alert must be an instance of Alert class")
		os.Exit(1)
	}

	// Assign rule if not already assigned
	if alert.RuleID == "" {
		if len(m.rules) == 1 {
			for id := range m.rules {
				alert.RuleID = id
			}
		} else {
			fmt.Fprintln(os.Stderr, "Alert must have a rule_id or exactly one rule must exist")
			os.Exit(1)
		}
	}

	rule, ok := m.rules[alert.RuleID]
	if !ok || rule == nil {
		fmt.Fprintf(os.Stderr, "Rule with ID %s not found\n", alert.RuleID)
		os.Exit(1)
	}

	// Check for suppression
	if m.isSuppressed(alert, rule) {
		alert.Status = SUPPRESSED
		m.suppressedAlerts[alert.ID] = struct{}{}
		m.activeAlerts[alert.ID] = alert
		return true
	}

	// Check for deduplication
	duplicateID := m.findDuplicate(alert, rule)
	if duplicateID != "" {
		existingAlert, ok := m.activeAlerts[duplicateID]
		if !ok {
			fmt.Fprintf(os.Stderr, "duplicate alert %s not found in active alerts\n", duplicateID)
			os.Exit(1)
		}
		existingAlert.Timestamp = alert.Timestamp
		existingAlert.Description = alert.Description
		existingAlert.EscalationCount = alert.EscalationCount
		return false
	}

	// New alert - check for escalation
	if m.shouldEscalate(alert, rule) {
		alert.EscalationCount++
	}

	m.activeAlerts[alert.ID] = alert
	m.alertHistory[alert.fingerprint()] = append(m.alertHistory[alert.fingerprint()], alert)
	return true
}

func (m *AlertManager) resolveAlert(alertID string) bool {
	alert, ok := m.activeAlerts[alertID]
	if !ok {
		return false
	}
	alert.Status = RESOLVED
	alert.Timestamp = now()
	delete(m.activeAlerts, alertID)
	return true
}

func (m *AlertManager) getActiveAlerts() []*Alert {
	alerts := make([]*Alert, 0, len(m.activeAlerts))
	for _, alert := range m.activeAlerts {
		if _, suppressed := m.suppressedAlerts[alert.ID]; !suppressed {
			alerts = append(alerts, alert)
		}
	}
	return alerts
}

func (m *AlertManager) getSuppressedAlerts() []*Alert {
	alerts := make([]*Alert, 0, len(m.suppressedAlerts))
	for id := range m.suppressedAlerts {
		if alert, ok := m.activeAlerts[id]; ok {
			alerts = append(alerts, alert)
		}
	}
	return alerts
}

func (m *AlertManager) isSuppressed(alert *Alert, rule *Rule) bool {
	for tag := range rule.SuppressionTags {
		if _, ok := alert.Tags[tag]; ok {
			return true
		}
	}
	return false
}

func (m *AlertManager) findDuplicate(alert *Alert, rule *Rule) string {
	fingerprint := alert.fingerprint()
	currentTime := now()

	history := m.alertHistory[fingerprint]
	for i := len(history) - 1; i >= 0; i-- {
		historicalAlert := history[i]
		if _, ok := m.activeAlerts[historicalAlert.ID]; !ok {
			continue
		}
		if currentTime-historicalAlert.Timestamp <= rule.DedupWindowSeconds {
			return historicalAlert.ID
		}
		break
	}
	return ""
}

func (m *AlertManager) shouldEscalate(alert *Alert, rule *Rule) bool {
	if rule.MaxEscalationCount <= 0 {
		return false
	}
	fingerprint := alert.fingerprint()
	currentTime := now()

	recentCount := 0
	history := m.alertHistory[fingerprint]
	for i := len(history) - 1; i >= 0; i-- {
		historicalAlert := history[i]
		if currentTime-historicalAlert.Timestamp <= rule.EscalationIntervalSeconds {
			recentCount++
		} else {
			break
		}
	}
	return recentCount >= rule.MaxEscalationCount
}

func alertTitles(alerts []*Alert) []string {
	out := make([]string, len(alerts))
	for i, a := range alerts {
		out[i] = a.Title
	}
	return out
}

func containsString(slice []string, s string) bool {
	for _, v := range slice {
		if v == s {
			return true
		}
	}
	return false
}

func main() {
	fakeNow = 50000.0

	manager := newAlertManager()
	manager.addRule(newRule("service_rule", "Service Alert Rule",
		10.0,
		[]string{"maintenance"},
		2,
		30.0))

	mkAlert := func(title string, severity AlertSeverity, source string, tags []string, ts float64) *Alert {
		return newAlert(title, title, severity, source, tags, "service_rule", ts)
	}

	assert := func(cond bool, msg string) {
		if !cond {
			fmt.Fprintf(os.Stderr, "assertion failed: %s\n", msg)
			os.Exit(1)
		}
	}

	// First alert accepted; identical fingerprint inside 10s deduped.
	a1 := mkAlert("High CPU", HIGH, "server01", []string{"prod", "cpu"}, fakeNow)
	assert(manager.processAlert(a1), "first alert rejected")
	fakeNow += 1.0
	dup := mkAlert("High CPU", HIGH, "server01", []string{"prod", "cpu"}, fakeNow)
	assert(!manager.processAlert(dup), "duplicate inside window accepted")

	// Different fingerprint is NOT deduped.
	a3 := mkAlert("High Memory", CRITICAL, "server01", []string{"prod"}, fakeNow)
	assert(manager.processAlert(a3), "distinct alert wrongly deduped")

	// PAST the window the same fingerprint alerts again.
	fakeNow += 11.0
	again := mkAlert("High CPU", HIGH, "server01", []string{"prod", "cpu"}, fakeNow)
	assert(manager.processAlert(again), "re-alert after the dedup window was swallowed")

	// Suppression: maintenance-tagged alert is accepted but SUPPRESSED.
	supp := mkAlert("Disk Warning", MEDIUM, "server02", []string{"maintenance", "disk"}, fakeNow)
	assert(manager.processAlert(supp), "suppressed alert was not processed")
	suppressed := alertTitles(manager.getSuppressedAlerts())
	assert(len(suppressed) == 1 && suppressed[0] == "Disk Warning", fmt.Sprintf("suppressed set wrong: %v", suppressed))
	activeTitles := alertTitles(manager.getActiveAlerts())
	assert(!containsString(activeTitles, "Disk Warning"), "suppressed alert is active")

	// Resolve removes from active, reports honestly.
	nActiveBefore := len(manager.getActiveAlerts())
	assert(nActiveBefore == 3, fmt.Sprintf("exactly 3 alerts must be active, got %d", nActiveBefore))
	assert(manager.resolveAlert(a1.ID), "resolve a1 failed")
	assert(!manager.resolveAlert(a1.ID), "double resolve reported success")
	assert(!manager.resolveAlert("ghost-id"), "resolve ghost-id reported success")
	assert(len(manager.getActiveAlerts()) == nActiveBefore-1, "resolve did not shrink the active set by exactly 1")

	// Dedup applies per-fingerprint: 4 rapid repeats -> 1 accepted, 3 deduped.
	accepted := 0
	for i := 0; i < 4; i++ {
		e := mkAlert("Recurring Error", MEDIUM, "serviceA", []string{"error"}, fakeNow)
		if manager.processAlert(e) {
			accepted++
		}
		fakeNow += 0.5
	}
	assert(accepted == 1, fmt.Sprintf("4 repeats in 2s must accept exactly 1, accepted %d", accepted))

	fmt.Println("alert_manager: dedup in-window, re-alert at +11s, maintenance suppressed, resolve exact, 4 repeats -> 1 accepted — PASS")
	time.Sleep(1 * time.Millisecond)
}
