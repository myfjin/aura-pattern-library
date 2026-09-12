# Syntax-error planted case: this file is deliberately malformed to prove the
# oracle reports a parse/syntax failure rather than passing it. Padding to clear
# the minimum-length sense threshold so we actually reach the Rscript run stage.
f <- function(x) { x + }
stopifnot(f(2) == 4)
cat("f: PASS\n")
