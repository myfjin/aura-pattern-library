# Linear Regression via Normal Equations (R)
#
# WHAT IT DOES: The most fundamental question in statistics — "given data points,
# what's the best-fit line (or plane)?" Ordinary least squares. This does it the
# textbook way: beta = (X'X)^{-1} X' y, then PROVES its answer matches R's trusted
# lm() to 1e-8. Use it to understand what lm() does under the hood, or when you need
# the coefficients in a setting where you can't depend on lm().
#
# WHEN TO USE: You want to understand what lm() does under the hood, or you need the
# coefficients in a setting where you can't depend on lm(). The self-check against
# R's built-in lm() is the trust anchor — if the manual path ever diverges, the
# assert catches it.
#
# GUARANTEES: The manual normal-equations solution matches R's lm() coefficients to
# within 1e-8. Collinear columns produce an honest "system is exactly singular" error
# from solve(). Coefficients are recovered within sampling error of the true values.
#
# NOT: A robust regression function. NA in y propagates silently through matrix
# operations, producing all-NA coefficients with no warning (caught only by the lm()
# cross-check). R's weak typing means this is a language-level hazard, not a code bug.
