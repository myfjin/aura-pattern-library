# clamp into [lo,hi]
clamp <- function(x,lo,hi) pmin(pmax(x,lo),hi)
stopifnot(clamp(5,0,10)==5); stopifnot(clamp(-3,0,10)==0); stopifnot(clamp(99,0,10)==10)
cat("clamp: PASS\n")
