package main

import (
	"fmt"
	"os"
)

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
var _auraMark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
type SkewDetector struct {
	lastWall    *float64
	skewSamples []float64
}

func NewSkewDetector() *SkewDetector {
	return &SkewDetector{
		skewSamples: []float64{},
	}
}

func (sd *SkewDetector) Sample(wallTime float64) bool {
	if sd.lastWall == nil {
		sd.lastWall = &wallTime
		return false
	}

	skewAmount := *sd.lastWall - wallTime
	hasSkew := skewAmount > 0

	if hasSkew {
		sd.skewSamples = append(sd.skewSamples, skewAmount)
	}

	sd.lastWall = &wallTime
	return hasSkew
}

func (sd *SkewDetector) GetSkewCount() int {
	return len(sd.skewSamples)
}

func (sd *SkewDetector) GetTotalSkew() float64 {
	var total float64
	for _, v := range sd.skewSamples {
		total += v
	}
	return total
}

func testDetectBackwardJump() {
	detector := NewSkewDetector()

	if !(detector.Sample(1000.0) == false) {
		fmt.Fprintln(os.Stderr, "first sample should not detect skew")
		os.Exit(1)
	}
	if !(detector.Sample(1001.0) == false) {
		fmt.Fprintln(os.Stderr, "forward sample should not detect skew")
		os.Exit(1)
	}
	if !(detector.Sample(1002.0) == false) {
		fmt.Fprintln(os.Stderr, "forward sample should not detect skew")
		os.Exit(1)
	}

	skewDetected := detector.Sample(1997.0)
	if !(skewDetected == false) {
		fmt.Fprintln(os.Stderr, "forward jump should not detect skew")
		os.Exit(1)
	}

	skewDetected = detector.Sample(1990.0)
	if !(skewDetected == true) {
		fmt.Fprintln(os.Stderr, "backward jump should detect skew")
		os.Exit(1)
	}
	if !(detector.GetSkewCount() == 1) {
		fmt.Fprintf(os.Stderr, "skew count should be 1, got %d\n", detector.GetSkewCount())
		os.Exit(1)
	}
	if !(detector.GetTotalSkew() == 7.0) {
		fmt.Fprintf(os.Stderr, "total skew should be 7.0, got %f\n", detector.GetTotalSkew())
		os.Exit(1)
	}
}

func testMultipleSkews() {
	detector := NewSkewDetector()

	detector.Sample(1000.0)
	detector.Sample(1010.0)
	detector.Sample(1005.0)
	if !(detector.GetSkewCount() == 1) {
		fmt.Fprintf(os.Stderr, "skew count should be 1, got %d\n", detector.GetSkewCount())
		os.Exit(1)
	}
	if !(detector.GetTotalSkew() == 5.0) {
		fmt.Fprintf(os.Stderr, "total skew should be 5.0, got %f\n", detector.GetTotalSkew())
		os.Exit(1)
	}

	detector.Sample(1002.0)
	if !(detector.GetSkewCount() == 2) {
		fmt.Fprintf(os.Stderr, "skew count should be 2, got %d\n", detector.GetSkewCount())
		os.Exit(1)
	}
	if !(detector.GetTotalSkew() == 8.0) {
		fmt.Fprintf(os.Stderr, "total skew should be 8.0, got %f\n", detector.GetTotalSkew())
		os.Exit(1)
	}
}

func testNoFalsePositive() {
	detector := NewSkewDetector()

	for i := 0; i < 10; i++ {
		if !(detector.Sample(1000.0+float64(i)) == false) {
			fmt.Fprintf(os.Stderr, "forward sample %d should not detect skew\n", i)
			os.Exit(1)
		}
	}
	if !(detector.GetSkewCount() == 0) {
		fmt.Fprintf(os.Stderr, "skew count should be 0, got %d\n", detector.GetSkewCount())
		os.Exit(1)
	}
}

func main() {
	testDetectBackwardJump()
	testMultipleSkews()
	testNoFalsePositive()
	fmt.Println("✓ clock_skew_detect passed")
}
