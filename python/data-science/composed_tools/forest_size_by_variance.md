# forest size by variance

**Language:** Python · **Category:** composed tools

## What it does

Forest Size by Variance — stop hiring trees when the crew is steady enough.

FUSED-BRIDGE COMPOSED PATTERN: bias_variance_decomposition (Model Diagnostics) x
random_forest (Ensembles & Robust) — proposed by BOTH signals 2026-07-10:
structural edge `matrix` (a data matrix flows into the diagnostic that wraps the
forest) + semantic 0.429. Practitioners guess n_trees (a default 100) or grid-
search it. The composition runs the bias-variance decomposition's bootstrap
estimator ACROSS forest sizes: bias stays flat (more trees don't change what the
forest is biased toward) while ensemble variance falls as ~1/n. HONEST PHYSICS:
independent trees give NO hard plateau — variance keeps decaying 1/n; a true
plateau needs correlated trees (variance -> rho*sigma^2). So the data-driven size
is the DIMINISHING-RETURNS knee: the smallest forest that captures most of the
achievable variance reduction, past which each doubling buys little.

Human logic of the name: you keep adding workers until the crew is steady
enough — the point where one more worker barely reduces the wobble.

---
*△ AURA Pattern Library — © Reality Optimizer*
