# Assert-fail planted case: the code is syntactically fine and runs, but its own
# stopifnot self-test is FALSE (2+2 != 5), so the oracle must catch a failed
# assertion at runtime. Padding to clear the minimum-length sense threshold.
add <- function(a, b) a + b
stopifnot(add(2, 2) == 5)
cat("add: PASS\n")
