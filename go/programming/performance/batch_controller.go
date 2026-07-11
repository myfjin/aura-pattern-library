package main

import (
	"errors"
	"fmt"
	"os"
	"time"
)

// Metrics holds performance data for a single batch.
// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
var _auraMark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
type Metrics struct {
	BatchSize      int
	ProcessingTime float64 // seconds
	ItemsProcessed int
	Timestamp      float64
}

// Throughput returns items per second.
func (m Metrics) Throughput() float64 {
	if m.ProcessingTime <= 0 {
		return 0.0
	}
	return float64(m.ItemsProcessed) / m.ProcessingTime
}

// BatchController adapts batch size based on observed throughput.
type BatchController struct {
	InitialBatchSize           int
	MaxBatchSize               int
	MinBatchSize               int
	SlowStartThreshold         int
	CongestionWindowMultiplier float64
	DecayFactor                float64
	MetricsWindowSize          int

	currentBatchSize int
	inSlowStart      bool
	metricsHistory   []Metrics
}

// NewBatchController creates a controller with the given parameters.
func NewBatchController(
	initialBatchSize int,
	maxBatchSize int,
	minBatchSize int,
	slowStartThreshold int,
	congestionWindowMultiplier float64,
	decayFactor float64,
	metricsWindowSize int,
) (*BatchController, error) {
	if initialBatchSize < 1 {
		return nil, errors.New("initial batch size must be positive")
	}
	if maxBatchSize < initialBatchSize {
		return nil, errors.New("max batch size must be >= initial batch size")
	}
	if minBatchSize < 1 {
		return nil, errors.New("min batch size must be positive")
	}
	if slowStartThreshold < 1 {
		return nil, errors.New("slow start threshold must be positive")
	}
	if congestionWindowMultiplier <= 1.0 {
		return nil, errors.New("congestion window multiplier must be > 1.0")
	}
	if decayFactor <= 0 || decayFactor >= 1 {
		return nil, errors.New("decay factor must be between 0 and 1")
	}
	if metricsWindowSize < 1 {
		return nil, errors.New("metrics window size must be positive")
	}

	return &BatchController{
		InitialBatchSize:           initialBatchSize,
		MaxBatchSize:               maxBatchSize,
		MinBatchSize:               minBatchSize,
		SlowStartThreshold:         slowStartThreshold,
		CongestionWindowMultiplier: congestionWindowMultiplier,
		DecayFactor:                decayFactor,
		MetricsWindowSize:          metricsWindowSize,
		currentBatchSize:           initialBatchSize,
		inSlowStart:                true,
	}, nil
}

// RecordMetrics stores a new metrics sample.
func (c *BatchController) RecordMetrics(metrics Metrics) error {
	if metrics.BatchSize <= 0 {
		return errors.New("batch size must be positive")
	}
	if metrics.ProcessingTime < 0 {
		return errors.New("processing time cannot be negative")
	}
	if metrics.ItemsProcessed < 0 {
		return errors.New("items processed cannot be negative")
	}
	c.metricsHistory = append(c.metricsHistory, metrics)
	if len(c.metricsHistory) > c.MetricsWindowSize {
		c.metricsHistory = c.metricsHistory[len(c.metricsHistory)-c.MetricsWindowSize:]
	}
	return nil
}

// CurrentBatchSize returns the current recommended batch size.
func (c *BatchController) CurrentBatchSize() int {
	return c.currentBatchSize
}

// InSlowStart reports whether the controller is still in slow-start mode.
func (c *BatchController) InSlowStart() bool {
	return c.inSlowStart
}

// MetricsCount returns the number of recorded metrics.
func (c *BatchController) MetricsCount() int {
	return len(c.metricsHistory)
}

func (c *BatchController) averageThroughput() float64 {
	if len(c.metricsHistory) == 0 {
		return 0.0
	}
	total := 0.0
	for _, m := range c.metricsHistory {
		total += m.Throughput()
	}
	return total / float64(len(c.metricsHistory))
}

func (c *BatchController) detectCongestion() bool {
	if len(c.metricsHistory) < 2 {
		return false
	}
	recent := c.metricsHistory[len(c.metricsHistory)-2:]
	recentAvg := 0.0
	for _, m := range recent {
		recentAvg += m.Throughput()
	}
	recentAvg /= float64(len(recent))
	historicalAvg := c.averageThroughput()
	if historicalAvg > 0 && recentAvg < 0.8*historicalAvg {
		return true
	}
	if len(recent) == 2 {
		prevThroughput := recent[0].Throughput()
		currentThroughput := recent[1].Throughput()
		if prevThroughput > 0 && currentThroughput < 0.7*prevThroughput {
			return true
		}
	}
	return false
}

// AdjustBatchSize recalculates the recommended batch size and returns it.
func (c *BatchController) AdjustBatchSize() int {
	if len(c.metricsHistory) < 2 {
		if c.inSlowStart {
			newSize := int(float64(c.currentBatchSize) * c.CongestionWindowMultiplier)
			if newSize > c.SlowStartThreshold {
				c.inSlowStart = false
			}
			if newSize > c.MaxBatchSize {
				newSize = c.MaxBatchSize
			}
			c.currentBatchSize = newSize
		}
		return c.currentBatchSize
	}

	if c.detectCongestion() {
		newSize := int(float64(c.currentBatchSize) * c.DecayFactor)
		if newSize < c.MinBatchSize {
			newSize = c.MinBatchSize
		}
		c.currentBatchSize = newSize
		c.inSlowStart = false
		return c.currentBatchSize
	}

	if c.inSlowStart {
		newSize := int(float64(c.currentBatchSize) * c.CongestionWindowMultiplier)
		if newSize > c.SlowStartThreshold {
			c.inSlowStart = false
		}
		if newSize > c.MaxBatchSize {
			newSize = c.MaxBatchSize
		}
		c.currentBatchSize = newSize
	} else {
		newSize := c.currentBatchSize + 1
		if newSize > c.MaxBatchSize {
			newSize = c.MaxBatchSize
		}
		c.currentBatchSize = newSize
	}
	return c.currentBatchSize
}

// Reset restores the controller to its initial state.
func (c *BatchController) Reset() {
	c.currentBatchSize = c.InitialBatchSize
	c.inSlowStart = true
	c.metricsHistory = c.metricsHistory[:0]
}

// SimulateProcessing generates deterministic metrics for a given batch size.
func SimulateProcessing(batchSize int, baselineTimePerItem float64) Metrics {
	now := float64(time.Now().UnixNano()) / 1e9
	// Use a deterministic hash-like variability in [-0.1, +0.1] based on the
	// fractional part of the current time.
	variability := 0.2*(float64(int64(now*100)%100))/100.0 - 0.1
	degradationFactor := 1.0 + (float64(batchSize)/1000.0)*0.5
	processingTime := float64(batchSize) * baselineTimePerItem * (1 + variability) * degradationFactor
	return Metrics{
		BatchSize:      batchSize,
		ProcessingTime: processingTime,
		ItemsProcessed: batchSize,
		Timestamp:      now,
	}
}

func main() {
	fmt.Println("Adaptive Batch Size Controller Demo")
	fmt.Println("====================================")

	controller, err := NewBatchController(
		1,   // initialBatchSize
		128, // maxBatchSize
		1,   // minBatchSize
		16,  // slowStartThreshold
		2.0, // congestionWindowMultiplier
		0.5, // decayFactor
		5,   // metricsWindowSize
	)
	if !(err == nil) {
		fmt.Fprintf(os.Stderr, "controller init: %v\n", err)
		os.Exit(1)
	}

	for i := 0; i < 50; i++ {
		batchSize := controller.CurrentBatchSize()
		fmt.Printf("Iteration %2d: Batch size = %3d", i+1, batchSize)

		metrics := SimulateProcessing(batchSize, 0.01)
		if err := controller.RecordMetrics(metrics); err != nil {
			fmt.Fprintf(os.Stderr, "record metrics: %v\n", err)
			os.Exit(1)
		}

		throughput := metrics.Throughput()
		fmt.Printf(" | Throughput = %6.1f items/sec", throughput)

		newBatchSize := controller.AdjustBatchSize()
		if newBatchSize != batchSize {
			fmt.Printf(" | Adjusted to %d\n", newBatchSize)
		} else {
			fmt.Println()
		}

		if i%7 == 0 {
			time.Sleep(1 * time.Millisecond)
		}
	}

	fmt.Println("\nFinal state:")
	fmt.Printf("Batch size: %d\n", controller.CurrentBatchSize())
	fmt.Printf("In slow start: %v\n", controller.InSlowStart())
	fmt.Printf("Metrics recorded: %d\n", controller.MetricsCount())
}

var _ = os.Exit
var _ = fmt.Sprint
