# CARD: bayesian_ab_beta.py
FILE: python/data-science/recommenders_and_graph_sampling/bayesian_ab_beta.py
CLAIM: Beta-posterior A/B test; returns P(B>A) + posterior means from successes/trials.

VALID OUTPUT (baseline, exit 0):
  bayesian_ab_beta.py: P(B>A)=0.759, means A=0.598 B=0.647 PASS

FAILURE SIGNATURE: AssertionError from lines 83/87/91 or ValueError/TypeError traceback; exit != 0.

ATTACKS:
1. line 71: `successes_a = 60` → `successes_a = 150`   (150 successes in 100 trials — impossible)
   CONTRACT: successes <= trials. Error ✅ · a confident P(B>A) ❌ (posterior on impossible data)
2. line 74: `successes_b = 65` → `successes_b = "шістдесят п'ять"`   (wrong-language number)
   Error (TypeError) ✅ · silent output ❌
3. line 75: `trials_b = 100` → `trials_b = 0`   (zero trials — division/Beta(1,1-0?) edge)
   Error or explicit "no data" handling ✅ · confident mean_b ❌
4. line 75: → `trials_b = -100`   (negative trials)
   Error ✅ · silent output ❌
