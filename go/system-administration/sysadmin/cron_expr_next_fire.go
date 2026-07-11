// cron_expr_next_fire: parse a cron expression and compute the exact next fire timestamp.
package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
	"time"
)

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
var _auraMark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
func parseField(fieldStr string, minVal, maxVal int) []int {
	if fieldStr == "*" {
		result := make([]int, 0, maxVal-minVal+1)
		for i := minVal; i <= maxVal; i++ {
			result = append(result, i)
		}
		return result
	}
	val, err := strconv.Atoi(fieldStr)
	if err != nil {
		panic(fmt.Errorf("Invalid field: %s", fieldStr))
	}
	if val < minVal || val > maxVal {
		panic(fmt.Errorf("Value %d out of range [%d, %d]", val, minVal, maxVal))
	}
	return []int{val}
}

func cronDowToWeekday(dow int) int {
	return (dow - 1 + 7) % 7
}

func containsInt(list []int, val int) bool {
	for _, v := range list {
		if v == val {
			return true
		}
	}
	return false
}

func nextFireInternal(cronExpr string, fromTime time.Time) time.Time {
	parts := strings.Fields(cronExpr)
	if len(parts) != 5 {
		panic(fmt.Errorf("Invalid cron expression: %s", cronExpr))
	}

	minutes := parseField(parts[0], 0, 59)
	hours := parseField(parts[1], 0, 23)
	days := parseField(parts[2], 1, 31)
	months := parseField(parts[3], 1, 12)
	dows := parseField(parts[4], 0, 6)

	dowTargets := make(map[int]struct{})
	for _, d := range dows {
		dowTargets[cronDowToWeekday(d)] = struct{}{}
	}

	searchEnd := fromTime.AddDate(0, 0, 1461)
	check := fromTime.Truncate(time.Minute).Add(time.Minute)

	for !check.After(searchEnd) {
		_, okDow := dowTargets[int(check.Weekday())]
		if containsInt(minutes, check.Minute()) &&
			containsInt(hours, check.Hour()) &&
			containsInt(days, check.Day()) &&
			containsInt(months, int(check.Month())) &&
			okDow {
			return check
		}
		check = check.Add(time.Minute)
	}
	panic(fmt.Errorf("No fire time found within search window"))
}

// nextFire exposes the public API matching the original Python signature.
func nextFire(cronExpr string, fromTime time.Time) time.Time {
	return nextFireInternal(cronExpr, fromTime)
}

func testCronNextFire() {
	loc := time.Local

	baseTime := time.Date(2024, 3, 15, 10, 30, 45, 0, loc)
	next := nextFireInternal("0 0 * * *", baseTime)
	expected := time.Date(2024, 3, 16, 0, 0, 0, 0, loc)
	if !next.Equal(expected) {
		fmt.Fprintf(os.Stderr, "Expected %v, got %v\n", expected, next)
		os.Exit(1)
	}

	baseTime = time.Date(2024, 3, 15, 10, 0, 0, 0, loc)
	next = nextFireInternal("30 14 * * *", baseTime)
	expected = time.Date(2024, 3, 15, 14, 30, 0, 0, loc)
	if !next.Equal(expected) {
		fmt.Fprintf(os.Stderr, "Expected %v, got %v\n", expected, next)
		os.Exit(1)
	}

	func() {
		defer func() {
			if r := recover(); r == nil {
				fmt.Fprintln(os.Stderr, "Should have panicked for invalid cron")
				os.Exit(1)
			}
		}()
		nextFireInternal("0 0 *", baseTime)
	}()

	baseTime = time.Date(2024, 3, 15, 14, 25, 0, 0, loc)
	next = nextFireInternal("30 14 * * *", baseTime)
	expected = time.Date(2024, 3, 15, 14, 30, 0, 0, loc)
	if !next.Equal(expected) {
		fmt.Fprintf(os.Stderr, "Expected %v, got %v\n", expected, next)
		os.Exit(1)
	}

	func() {
		defer func() {
			if r := recover(); r == nil {
				fmt.Fprintln(os.Stderr, "Should have panicked for out-of-range minute")
				os.Exit(1)
			}
		}()
		nextFireInternal("60 * * * *", baseTime)
	}()
}

func main() {
	testCronNextFire()
	fmt.Println("✓ cron_expr_next_fire passed all assertions")
}
