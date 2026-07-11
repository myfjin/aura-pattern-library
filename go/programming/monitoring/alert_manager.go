package main

import (
	"crypto/rand"
	"fmt"
	"os"
	"sort"
	"strings"
	"time"
)

// randRead is a thin alias so the generateID body matches Go's crypto/rand.Read signature.
// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
var _auraMark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
func randRead(b []byte) (int, error) {
	return rand.Read(b)
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

// NewAlert creates a new Alert with a unique ID and current timestamp.
func NewAlert(title, description string, severity AlertSeverity, source string, tags []string, ruleID string) *Alert {
	tagSet := make(map[string]struct{})
	for _, t := range tags {
		tagSet[t] = struct{}{}
	}
	return &Alert{
		ID:          generateID(),
		Title:       title,
		Description: description,
		Severity:    severity,
		Status:      FIRING,
		Source:      source,
		Tags:        tagSet,
		Timestamp:   float64(time.Now().UnixNano()) / 1e9,
		RuleID:      ruleID,
	}
}

func generateID() string {
	// emulate uuid4 via crypto/rand for uniqueness
	b := make([]byte, 16)
	_, err := randRead(b)
	if !(err == nil) {
		fmt.Fprintf(os.Stderr, "failed to generate id: %v\n", err)
		os.Exit(1)
	}
	b[6] = (b[6] & 0x0f) | 0x40
	b[8] = (b[8] & 0x3f) | 0x80
	return fmt.Sprintf("%08x-%04x-%04x-%04x-%012x", b[0:4], b[4:6], b[6:8], b[8:10], b[10:16])
}

// Fingerprint generates a fingerprint for deduplication based on key attributes.
func (a *Alert) Fingerprint() string {
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

// AlertManager manages alerts with deduplication, suppression, and escalation.
type AlertManager struct {
	rules            map[string]*Rule
	activeAlerts     map[string]*Alert
	alertHistory     map[string][]*Alert
	suppressedAlerts map[string]struct{}
}

// NewAlertManager initializes an AlertManager.
func NewAlertManager() *AlertManager {
	return &AlertManager{
		rules:            make(map[string]*Rule),
		activeAlerts:     make(map[string]*Alert),
		alertHistory:     make(map[string][]*Alert),
		suppressedAlerts: make(map[string]struct{}),
	}
}

// AddRule adds a rule to the manager.
func (m *AlertManager) AddRule(rule *Rule) {
	if rule == nil {
		fmt.Fprintf(os.Stderr, "Rule must be an instance of Rule\n")
		os.Exit(1)
	}
	m.rules[rule.ID] = rule
}

// ProcessAlert processes an incoming alert.
// Returns true if alert was processed (not deduplicated), false if deduplicated.
func (m *AlertManager) ProcessAlert(alert *Alert) bool {
	if alert == nil {
		fmt.Fprintf(os.Stderr, "Alert must be an instance of Alert\n")
		os.Exit(1)
	}

	// Assign rule if not already assigned
	if alert.RuleID == "" {
		if len(m.rules) == 1 {
			for id := range m.rules {
				alert.RuleID = id
			}
		} else {
			fmt.Fprintf(os.Stderr, "Alert must have a rule_id or exactly one rule must exist\n")
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
	if !(duplicateID == "") {
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
	m.alertHistory[alert.Fingerprint()] = append(m.alertHistory[alert.Fingerprint()], alert)
	return true
}

// ResolveAlert resolves an active alert.
func (m *AlertManager) ResolveAlert(alertID string) bool {
	alert, ok := m.activeAlerts[alertID]
	if !ok {
		return false
	}
	alert.Status = RESOLVED
	alert.Timestamp = float64(time.Now().UnixNano()) / 1e9
	delete(m.activeAlerts, alertID)
	return true
}

// GetActiveAlerts returns all currently active alerts.
func (m *AlertManager) GetActiveAlerts() []*Alert {
	alerts := make([]*Alert, 0, len(m.activeAlerts))
	for _, alert := range m.activeAlerts {
		alerts = append(alerts, alert)
	}
	return alerts
}

// GetSuppressedAlerts returns all currently suppressed alerts.
func (m *AlertManager) GetSuppressedAlerts() []*Alert {
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
	fingerprint := alert.Fingerprint()
	currentTime := float64(time.Now().UnixNano()) / 1e9

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
	fingerprint := alert.Fingerprint()
	currentTime := float64(time.Now().UnixNano()) / 1e9

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

func main() {
	manager := NewAlertManager()

	rule := &Rule{
		ID:                        "service_rule",
		Name:                      "Service Alert Rule",
		DedupWindowSeconds:        10.0,
		SuppressionTags:           map[string]struct{}{"maintenance": {}},
		MaxEscalationCount:        2,
		EscalationIntervalSeconds: 30.0,
	}
	manager.AddRule(rule)

	alert1 := NewAlert("High CPU Usage", "CPU usage exceeded 90%", HIGH, "server01", []string{"production", "cpu"}, "service_rule")
	alert2 := NewAlert("High CPU Usage", "CPU usage still high", HIGH, "server01", []string{"production", "cpu"}, "service_rule")
	alert3 := NewAlert("High Memory Usage", "Memory usage exceeded 95%", CRITICAL, "server01", []string{"production", "memory"}, "service_rule")
	suppressedAlert := NewAlert("Disk Warning", "Disk usage at 85%", MEDIUM, "server02", []string{"maintenance", "disk"}, "service_rule")

	fmt.Println("Processing alerts...")
	result1 := manager.ProcessAlert(alert1)
	fmt.Printf("Alert 1 processed: %v\n", result1)

	time.Sleep(100 * time.Millisecond)

	result2 := manager.ProcessAlert(alert2)
	fmt.Printf("Alert 2 processed: %v\n", result2)

	result3 := manager.ProcessAlert(alert3)
	fmt.Printf("Alert 3 processed: %v\n", result3)

	suppressedResult := manager.ProcessAlert(suppressedAlert)
	fmt.Printf("Suppressed alert processed: %v\n", suppressedResult)

	active := manager.GetActiveAlerts()
	fmt.Printf("\nActive alerts: %d\n", len(active))
	for _, alert := range active {
		fmt.Printf("  - %s (%s)\n", alert.Title, alert.Status)
	}

	suppressed := manager.GetSuppressedAlerts()
	fmt.Printf("\nSuppressed alerts: %d\n", len(suppressed))
	for _, alert := range suppressed {
		fmt.Printf("  - %s\n", alert.Title)
	}

	resolved := manager.ResolveAlert(alert1.ID)
	fmt.Printf("\nAlert 1 resolved: %v\n", resolved)

	activeAfterResolve := manager.GetActiveAlerts()
	fmt.Printf("Active alerts after resolve: %d\n", len(activeAfterResolve))

	fmt.Println("\nTesting escalation...")
	for i := 0; i < 4; i++ {
		escalationTest := NewAlert("Recurring Error", fmt.Sprintf("Error occurred %d times", i+1), MEDIUM, "serviceA", []string{"error"}, "service_rule")
		processed := manager.ProcessAlert(escalationTest)
		fmt.Printf("Escalation test %d processed: %v\n", i+1, processed)
		if !processed && i > 0 {
			fmt.Println("  Alert was deduplicated")
		}
		time.Sleep(100 * time.Millisecond)
	}
}
