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
		metricsHistory:             make([]Metrics, 0, metricsWindowSize),
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

// CurrentBatchSize returns the current recommended batch size.
func (c *BatchController) CurrentBatchSize() int {
	return c.currentBatchSize
}

// InSlowStart reports whether the controller is still in slow-start mode.
func (c *BatchController) InSlowStart() bool {
	return c.inSlowStart
}

// SimulateProcessing generates deterministic metrics for a given batch size.
func SimulateProcessing(batchSize int, baselineTimePerItem float64) Metrics {
	now := float64(time.Now().UnixNano()) / 1e9
	variability := 0.2*float64(int64(now*100)%100)/100.0 - 0.1
	degradationFactor := 1.0 + (float64(batchSize)/1000.0)*0.5
	processingTime := float64(batchSize) * baselineTimePerItem * (1 + variability) * degradationFactor
	return Metrics{
		BatchSize:      batchSize,
		ProcessingTime: processingTime,
		ItemsProcessed: batchSize,
		Timestamp:      now,
	}
}

func mk(throughput float64, batch int) Metrics {
	return Metrics{BatchSize: batch, ProcessingTime: 1.0,
		ItemsProcessed: int(throughput), Timestamp: 0.0}
}

func main() {
	// Throughput math is exact arithmetic.
	if mk(25.0, 10).Throughput() != 25.0 {
		fmt.Fprintf(os.Stderr, "50 items / 2s must be 25/s: got %v\n",
			mk(25.0, 10).Throughput())
		os.Exit(1)
	}
	if (Metrics{BatchSize: 1, ProcessingTime: 0.0, ItemsProcessed: 10, Timestamp: 0.0}).Throughput() != 0.0 {
		fmt.Fprintln(os.Stderr, "zero-time throughput must be 0")
		os.Exit(1)
	}

	c, err := NewBatchController(1, 128, 1, 16, 2.0, 0.5, 5)
	if err != nil {
		fmt.Fprintf(os.Stderr, "controller init: %v\n", err)
		os.Exit(1)
	}

	err = c.RecordMetrics(mk(1000.0, 10))
	if err != nil {
		fmt.Fprintf(os.Stderr, "record metrics: %v\n", err)
		os.Exit(1)
	}
	err = c.RecordMetrics(mk(1000.0, 10))
	if err != nil {
		fmt.Fprintf(os.Stderr, "record metrics: %v\n", err)
		os.Exit(1)
	}
	if c.AdjustBatchSize() != 2 {
		fmt.Fprintf(os.Stderr, "expected batch size 2 in trace, got %d\n", c.AdjustBatchSize())
		os.Exit(1)
	}
	if c.InSlowStart() != true {
		fmt.Fprintf(os.Stderr, "slow-start flag wrong at size 2: %v\n", c.InSlowStart())
		os.Exit(1)
	}

	err = c.RecordMetrics(mk(1000.0, 10))
	if err != nil {
		fmt.Fprintf(os.Stderr, "record metrics: %v\n", err)
		os.Exit(1)
	}
	err = c.RecordMetrics(mk(1000.0, 10))
	if err != nil {
		fmt.Fprintf(os.Stderr, "record metrics: %v\n", err)
		os.Exit(1)
	}
	if c.AdjustBatchSize() != 4 {
		fmt.Fprintf(os.Stderr, "expected batch size 4 in trace, got %d\n", c.AdjustBatchSize())
		os.Exit(1)
	}
	if c.InSlowStart() != true {
		fmt.Fprintf(os.Stderr, "slow-start flag wrong at size 4: %v\n", c.InSlowStart())
		os.Exit(1)
	}

	err = c.RecordMetrics(mk(1000.0, 10))
	if err != nil {
		fmt.Fprintf(os.Stderr, "record metrics: %v\n", err)
		os.Exit(1)
	}
	err = c.RecordMetrics(mk(1000.0, 10))
	if err != nil {
		fmt.Fprintf(os.Stderr, "record metrics: %v\n", err)
		os.Exit(1)
	}
	if c.AdjustBatchSize() != 8 {
		fmt.Fprintf(os.Stderr, "expected batch size 8 in trace, got %d\n", c.AdjustBatchSize())
		os.Exit(1)
	}
	if c.InSlowStart() != true {
		fmt.Fprintf(os.Stderr, "slow-start flag wrong at size 8: %v\n", c.InSlowStart())
		os.Exit(1)
	}

	err = c.RecordMetrics(mk(1000.0, 10))
	if err != nil {
		fmt.Fprintf(os.Stderr, "record metrics: %v\n", err)
		os.Exit(1)
	}
	err = c.RecordMetrics(mk(1000.0, 10))
	if err != nil {
		fmt.Fprintf(os.Stderr, "record metrics: %v\n", err)
		os.Exit(1)
	}
	if c.AdjustBatchSize() != 16 {
		fmt.Fprintf(os.Stderr, "expected batch size 16 in trace, got %d\n", c.AdjustBatchSize())
		os.Exit(1)
	}
	if c.InSlowStart() != true {
		fmt.Fprintf(os.Stderr, "slow-start flag wrong at size 16: %v\n", c.InSlowStart())
		os.Exit(1)
	}

	err = c.RecordMetrics(mk(1000.0, 10))
	if err != nil {
		fmt.Fprintf(os.Stderr, "record metrics: %v\n", err)
		os.Exit(1)
	}
	err = c.RecordMetrics(mk(1000.0, 10))
	if err != nil {
		fmt.Fprintf(os.Stderr, "record metrics: %v\n", err)
		os.Exit(1)
	}
	if c.AdjustBatchSize() != 32 {
		fmt.Fprintf(os.Stderr, "expected batch size 32 in trace, got %d\n", c.AdjustBatchSize())
		os.Exit(1)
	}
	if c.InSlowStart() != false {
		fmt.Fprintf(os.Stderr, "slow-start flag wrong at size 32: %v\n", c.InSlowStart())
		os.Exit(1)
	}

	err = c.RecordMetrics(mk(1000.0, 10))
	if err != nil {
		fmt.Fprintf(os.Stderr, "record metrics: %v\n", err)
		os.Exit(1)
	}
	err = c.RecordMetrics(mk(1000.0, 10))
	if err != nil {
		fmt.Fprintf(os.Stderr, "record metrics: %v\n", err)
		os.Exit(1)
	}
	if c.AdjustBatchSize() != 33 {
		fmt.Fprintf(os.Stderr, "expected batch size 33 in trace, got %d\n", c.AdjustBatchSize())
		os.Exit(1)
	}
	if c.InSlowStart() != false {
		fmt.Fprintf(os.Stderr, "slow-start flag wrong at size 33: %v\n", c.InSlowStart())
		os.Exit(1)
	}

	err = c.RecordMetrics(mk(1000.0, 10))
	if err != nil {
		fmt.Fprintf(os.Stderr, "record metrics: %v\n", err)
		os.Exit(1)
	}
	err = c.RecordMetrics(mk(1000.0, 10))
	if err != nil {
		fmt.Fprintf(os.Stderr, "record metrics: %v\n", err)
		os.Exit(1)
	}
	if c.AdjustBatchSize() != 34 {
		fmt.Fprintf(os.Stderr, "expected batch size 34 in trace, got %d\n", c.AdjustBatchSize())
		os.Exit(1)
	}
	if c.InSlowStart() != false {
		fmt.Fprintf(os.Stderr, "slow-start flag wrong at size 34: %v\n", c.InSlowStart())
		os.Exit(1)
	}

	// Throughput collapse (1000 → 200 < 0.7x) must HALVE the batch, not grow it: 34 → 17.
	err = c.RecordMetrics(mk(1000.0, 10))
	if err != nil {
		fmt.Fprintf(os.Stderr, "record metrics: %v\n", err)
		os.Exit(1)
	}
	err = c.RecordMetrics(mk(200.0, 10))
	if err != nil {
		fmt.Fprintf(os.Stderr, "record metrics: %v\n", err)
		os.Exit(1)
	}
	if c.AdjustBatchSize() != 17 {
		fmt.Fprintf(os.Stderr, "congestion must decay 34*0.5=17, got %d\n", c.AdjustBatchSize())
		os.Exit(1)
	}
	if c.InSlowStart() != false {
		fmt.Fprintf(os.Stderr, "slow-start flag should be false after congestion: %v\n", c.InSlowStart())
		os.Exit(1)
	}

	// Repeated collapses decay to the floor and NEVER below min_batch_size:
	// 17 → 8 → 4 → 2 → 1 → 1 → 1.
	err = c.RecordMetrics(mk(1000.0, 10))
	if err != nil {
		fmt.Fprintf(os.Stderr, "record metrics: %v\n", err)
		os.Exit(1)
	}
	err = c.RecordMetrics(mk(100.0, 10))
	if err != nil {
		fmt.Fprintf(os.Stderr, "record metrics: %v\n", err)
		os.Exit(1)
	}
	if c.AdjustBatchSize() != 8 {
		fmt.Fprintf(os.Stderr, "decay trace expected 8, got %d\n", c.AdjustBatchSize())
		os.Exit(1)
	}

	err = c.RecordMetrics(mk(1000.0, 10))
	if err != nil {
		fmt.Fprintf(os.Stderr, "record metrics: %v\n", err)
		os.Exit(1)
	}
	err = c.RecordMetrics(mk(100.0, 10))
	if err != nil {
		fmt.Fprintf(os.Stderr, "record metrics: %v\n", err)
		os.Exit(1)
	}
	if c.AdjustBatchSize() != 4 {
		fmt.Fprintf(os.Stderr, "decay trace expected 4, got %d\n", c.AdjustBatchSize())
		os.Exit(1)
	}

	err = c.RecordMetrics(mk(1000.0, 10))
	if err != nil {
		fmt.Fprintf(os.Stderr, "record metrics: %v\n", err)
		os.Exit(1)
	}
	err = c.RecordMetrics(mk(100.0, 10))
	if err != nil {
		fmt.Fprintf(os.Stderr, "record metrics: %v\n", err)
		os.Exit(1)
	}
	if c.AdjustBatchSize() != 2 {
		fmt.Fprintf(os.Stderr, "decay trace expected 2, got %d\n", c.AdjustBatchSize())
		os.Exit(1)
	}

	err = c.RecordMetrics(mk(1000.0, 10))
	if err != nil {
		fmt.Fprintf(os.Stderr, "record metrics: %v\n", err)
		os.Exit(1)
	}
	err = c.RecordMetrics(mk(100.0, 10))
	if err != nil {
		fmt.Fprintf(os.Stderr, "record metrics: %v\n", err)
		os.Exit(1)
	}
	if c.AdjustBatchSize() != 1 {
		fmt.Fprintf(os.Stderr, "decay trace expected 1, got %d\n", c.AdjustBatchSize())
		os.Exit(1)
	}

	err = c.RecordMetrics(mk(1000.0, 10))
	if err != nil {
		fmt.Fprintf(os.Stderr, "record metrics: %v\n", err)
		os.Exit(1)
	}
	err = c.RecordMetrics(mk(100.0, 10))
	if err != nil {
		fmt.Fprintf(os.Stderr, "record metrics: %v\n", err)
		os.Exit(1)
	}
	if c.AdjustBatchSize() != 1 {
		fmt.Fprintf(os.Stderr, "decay trace expected 1, got %d\n", c.AdjustBatchSize())
		os.Exit(1)
	}

	err = c.RecordMetrics(mk(1000.0, 10))
	if err != nil {
		fmt.Fprintf(os.Stderr, "record metrics: %v\n", err)
		os.Exit(1)
	}
	err = c.RecordMetrics(mk(100.0, 10))
	if err != nil {
		fmt.Fprintf(os.Stderr, "record metrics: %v\n", err)
		os.Exit(1)
	}
	if c.AdjustBatchSize() != 1 {
		fmt.Fprintf(os.Stderr, "decay trace expected 1, got %d\n", c.AdjustBatchSize())
		os.Exit(1)
	}
	if c.currentBatchSize != 1 {
		fmt.Fprintf(os.Stderr, "decay went below min_batch_size: %d\n", c.currentBatchSize)
		os.Exit(1)
	}

	// reset() restores the initial state completely.
	c.Reset()
	if c.currentBatchSize != 1 || c.InSlowStart() != true || len(c.metricsHistory) != 0 {
		fmt.Fprintln(os.Stderr, "reset left stale state")
		os.Exit(1)
	}

	// Invalid construction and invalid metrics are refused.
	_, err = NewBatchController(0, 128, 1, 16, 2.0, 0.5, 5)
	if err == nil {
		fmt.Fprintln(os.Stderr, "BatchController accepted invalid arguments: initial_batch_size=0")
		os.Exit(1)
	}
	_, err = NewBatchController(1, 0, 1, 16, 2.0, 0.5, 5)
	if err == nil {
		fmt.Fprintln(os.Stderr, "BatchController accepted invalid arguments: max_batch_size=0")
		os.Exit(1)
	}
	_, err = NewBatchController(1, 128, 1, 16, 1.0, 0.5, 5)
	if err == nil {
		fmt.Fprintln(os.Stderr, "BatchController accepted invalid arguments: congestion_window_multiplier=1.0")
		os.Exit(1)
	}
	_, err = NewBatchController(1, 128, 1, 16, 2.0, 1.0, 5)
	if err == nil {
		fmt.Fprintln(os.Stderr, "BatchController accepted invalid arguments: decay_factor=1.0")
		os.Exit(1)
	}
	err = c.RecordMetrics(Metrics{BatchSize: 0, ProcessingTime: 1.0, ItemsProcessed: 1, Timestamp: 0.0})
	if err == nil {
		fmt.Fprintln(os.Stderr, "batch_size=0 metrics accepted")
		os.Exit(1)
	}

	fmt.Println("batch_controller: slow-start 1→32 exact, congestion 34→17, " +
		"floor held at 1, reset clean — PASS")
}
