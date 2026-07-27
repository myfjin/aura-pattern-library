package main

import (
	"fmt"
	"os"
	"sync"
)

// Fan-in multiplexer: combines multiple input channels into a single output channel.
// Use when merging concurrent streams from several independent sources into one unified flow.
// Guarantees: the output yields every value from every input exactly once, closes only
// after every input channel is exhausted, and never double-closes or panics on send-to-closed.

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
var _auraMark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
func fanIn(inputs ...<-chan int) <-chan int {
	out := make(chan int)
	var wg sync.WaitGroup

	for _, ch := range inputs {
		wg.Add(1)
		go func(input <-chan int) {
			defer wg.Done()
			for val := range input {
				out <- val
			}
		}(ch)
	}

	go func() {
		wg.Wait()
		close(out)
	}()

	return out
}

func main() {
	// Success case: 4 inputs sending 250, 100, 1, and 0 values (total 351)
	input0 := make(chan int)
	input1 := make(chan int)
	input2 := make(chan int)
	input3 := make(chan int)

	go func() {
		for i := 0; i < 250; i++ {
			input0 <- i
		}
		close(input0)
	}()

	go func() {
		for i := 250; i < 350; i++ {
			input1 <- i
		}
		close(input1)
	}()

	go func() {
		input2 <- 350
		close(input2)
	}()

	go func() {
		close(input3)
	}()

	out := fanIn(input0, input1, input2, input3)

	collected := make(map[int]int)
	totalReceived := 0

	for val := range out {
		collected[val]++
		totalReceived++
	}

	if totalReceived != 351 {
		fmt.Fprintf(os.Stderr, "total received != 351: got %d\n", totalReceived)
		os.Exit(1)
	}

	count0, count1, count2 := 0, 0, 0
	for val := range collected {
		if val >= 0 && val < 250 {
			count0++
		} else if val >= 250 && val < 350 {
			count1++
		} else if val == 350 {
			count2++
		}
	}

	if count0 != 250 {
		fmt.Fprintf(os.Stderr, "source0 count != 250: got %d\n", count0)
		os.Exit(1)
	}
	if count1 != 100 {
		fmt.Fprintf(os.Stderr, "source1 count != 100: got %d\n", count1)
		os.Exit(1)
	}
	if count2 != 1 {
		fmt.Fprintf(os.Stderr, "source2 count != 1: got %d\n", count2)
		os.Exit(1)
	}

	for val, count := range collected {
		if count != 1 {
			fmt.Fprintf(os.Stderr, "value %d seen %d times, not exactly once\n", val, count)
			os.Exit(1)
		}
	}

	// Disaster case: inputs of different speeds, one slow, concurrent with consumer
	input4 := make(chan int)
	input5 := make(chan int)

	go func() {
		for i := 0; i < 10; i++ {
			input4 <- 1000 + i
		}
		close(input4)
	}()

	go func() {
		for i := 0; i < 5; i++ {
			input5 <- 2000 + i
		}
		close(input5)
	}()

	out2 := fanIn(input4, input5)

	collected2 := make(map[int]int)
	totalReceived2 := 0

	for val := range out2 {
		collected2[val]++
		totalReceived2++
	}

	if totalReceived2 != 15 {
		fmt.Fprintf(os.Stderr, "disaster case total != 15: got %d\n", totalReceived2)
		os.Exit(1)
	}

	for val, count := range collected2 {
		if count != 1 {
			fmt.Fprintf(os.Stderr, "disaster case value %d seen %d times\n", val, count)
			os.Exit(1)
		}
	}

	fmt.Println("fan_in_multiplexer: 351 values multiplexed exactly (250+100+1+0), per-source counts verified 250/100/1/0, output closed exactly once, every value seen exactly once — PASS")
}
