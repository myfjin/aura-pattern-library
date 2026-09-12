# R SIGNATURE REFERENCE (COPY VERBATIM) — no Rscript on .8, sig+defect verified

## data_wrangling_and_feature_engineering
### date_features.R
```r
```
### factor_onehot.R
```r
```
### group_aggregate.R
```r
```
### hash_join.R
```r
```
### long_wide_reshape.R
```r
```
### missing_pattern_matrix.R
```r
```
### na_imputation.R
```r
```
### rolling_stats.R
```r
```

## distributions_and_resampling
### bootstrap_ci.R
```r
```
### ecdf_dkw_bands.R
```r
```
### kde_gaussian.R
```r
```
### outlier_iqr_mad.R
```r
```
### quantile_type7.R
```r
quantile_type7 <- function(x, p)
```

## hypothesis_testing_parametric
### ab_power_analysis.R
```r
```
### anova_tukey.R
```r
```
### correlation_tests.R
```r
```
### ks_one_sample.R
```r
```
### one_way_anova.R
```r
```
### prop_test_two_sample.R
```r
```
### welch_t_test.R
```r
```

## multivariate_and_applied_modeling
### km_survival_lite.R
```r
```
### kmeans_lloyd.R
```r
```
### pca_power_iteration.R
```r
power_iterate <- function(C, iters = 1000, tol = 1e-12)
align <- function(v, oracle) if (sum(v * oracle) < 0) -v else v
```
### stratified_split.R
```r
```
### weighted_survey_mean.R
```r
```

## nonparametric_and_categorical
### chi_square_independence.R
```r
```
### cramers_v_effect.R
```r
cramers_v <- function(contingency_table)
```
### fisher_exact_2x2.R
```r
hypergeo_prob <- function(a_val, m1, m2, n1, N)
```
### kruskal_wallis.R
```r
```
### table_margins.R
```r
```
### wilcoxon_rank_sum.R
```r
```

## regression_and_glm
### bootstrap_regression.R
```r
```
### cv_model_selection.R
```r
```
### hosmer_lemeshow_lite.R
```r
hl_test <- function(y_true, y_pred, n_groups = 10)
```
### linear_regression_normal_eq.R
```r
```
### lm_diagnostics.R
```r
```
### logistic_regression_irls.R
```r
```
### poisson_regression_irls.R
```r
```
### ridge_regression.R
```r
```

## sampling_and_simulation
### box_muller.R
```r
```
### inverse_cdf_sampling.R
```r
```
### mvn_cholesky.R
```r
```
### order_statistics.R
```r
```
### poisson_process_thinning.R
```r
lambda_t <- function(t) 2 + sin(pi * t / T)
```
### probability_integral_transform.R
```r
```
### rejection_sampling_beta.R
```r
beta_density <- function(x) x^(alpha-1) * (1-x)^(beta_param-1)
```
### truncated_normal.R
```r
```

## time_series_models_and_autocorrelation
### acf_pacf_from_scratch.R
```r
```
### ar1_fit_forecast.R
```r
```
### ar_yule_walker.R
```r
```
### ccf_lag_detection.R
```r
```
### holt_winters_lite.R
```r
```
### ljung_box.R
```r
```
### seasonal_decompose.R
```r
```

## time_series_trend_spectral_and_smoothing
### diff_seasonality_test.R
```r
compute_acf <- function(x, max_lag)
```
### hampel_ts_outliers.R
```r
hampel_outliers <- function(x, win = window, threshold = 3.5)
```
### mann_kendall_trend.R
```r
mk_test <- function(time, value)
```
### periodogram_spectral.R
```r
```
### rolling_origin_cv.R
```r
```
### sma_wma_filter.R
```r
```

