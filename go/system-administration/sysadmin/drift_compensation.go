package main

import (
	"fmt"
	"os"
)

// DriftCompensator tracks and corrects for clock drift.
// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
var _auraMark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
type DriftCompensator struct {
	DriftRate     float64
	ReferenceTime float64
	ReferenceReal float64
}

// NewDriftCompensator creates a compensator with the given drift rate.
// drift_rate > 1.0: clock fast; drift_rate < 1.0: clock slow.
func NewDriftCompensator(driftRate float64) *DriftCompensator {
	return &DriftCompensator{DriftRate: driftRate}
}

// Calibrate sets the calibration point (what real time should be at clock time).
func (dc *DriftCompensator) Calibrate(realTime, clockTime float64) {
	dc.ReferenceTime = clockTime
	dc.ReferenceReal = realTime
}

// Correct returns the corrected (real) time for a given clock reading.
func (dc *DriftCompensator) Correct(clockTime float64) float64 {
	clockElapsed := clockTime - dc.ReferenceTime
	realElapsed := clockElapsed / dc.DriftRate
	return dc.ReferenceReal + realElapsed
}

// ErrorAt returns the error (uncorrected - corrected) at this clock time.
func (dc *DriftCompensator) ErrorAt(clockTime float64) float64 {
	return clockTime - dc.Correct(clockTime)
}

func testFastClockCompensation() {
	comp := NewDriftCompensator(1.10)
	comp.Calibrate(1000.0, 1000.0)
	corrected := comp.Correct(1110.0)
	expected := 1100.0
	if !(corrected == expected) {
		fmt.Fprintf(os.Stderr, "Expected %v, got %v\n", expected, corrected)
		os.Exit(1)
	}
}

func testSlowClockCompensation() {
	comp := NewDriftCompensator(0.90)
	comp.Calibrate(1000.0, 1000.0)
	corrected := comp.Correct(1090.0)
	expected := 1100.0
	if !(corrected == expected) {
		fmt.Fprintf(os.Stderr, "Expected %v, got %v\n", expected, corrected)
		os.Exit(1)
	}
}

func testErrorCalculation() {
	comp := NewDriftCompensator(1.20)
	comp.Calibrate(1000.0, 1000.0)
	errorVal := comp.ErrorAt(1120.0)
	expected := 20.0
	if !(errorVal == expected) {
		fmt.Fprintf(os.Stderr, "Expected error %v, got %v\n", expected, errorVal)
		os.Exit(1)
	}
}

func testSimulationFastClockCausesWrongMeasure() {
	comp := NewDriftCompensator(1.15)
	comp.Calibrate(2000.0, 2000.0)
	clockReading := 2115.0
	corrected := comp.Correct(clockReading)
	realElapsed := corrected - 2000.0
	if !(realElapsed == 100.0) {
		fmt.Fprintf(os.Stderr, "Real elapsed should be 100, got %v\n", realElapsed)
		os.Exit(1)
	}
	uncorrectedElapsed := clockReading - 2000.0
	if !(uncorrectedElapsed == 115.0) {
		fmt.Fprintf(os.Stderr, "Uncorrected elapsed should be 115, got %v\n", uncorrectedElapsed)
		os.Exit(1)
	}
	if uncorrectedElapsed == realElapsed {
		fmt.Fprintln(os.Stderr, "Uncorrected and real elapsed should differ")
		os.Exit(1)
	}
}

func main() {
	testFastClockCompensation()
	testSlowClockCompensation()
	testErrorCalculation()
	testSimulationFastClockCausesWrongMeasure()
	fmt.Println("✓ drift_compensation passed")
}
