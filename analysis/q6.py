import pandas as pd
import os
import sys
import numpy as np
import statsmodels.formula.api as smf

script_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(script_dir, '..'))

from data_code.load_clean_data import full_data as full_data

#creating subsets to run on
data_06 = full_data[(full_data['year'] == 2006) & (full_data['window_06'] == 1) & (full_data['e_ben'] == 0)]
data_07 = full_data[(full_data['year'] == 2007) & (full_data['window_06'] == 1) & (full_data['e_ben'] == 0)]
data_08 = full_data[(full_data['year'] == 2008) & (full_data['window_06'] == 1) & (full_data['e_ben'] == 0)]
data_09 = full_data[(full_data['year'] == 2009) & (full_data['window_06'] == 1) & (full_data['e_ben'] == 0)]
data_10 = full_data[(full_data['year'] == 2010) & (full_data['window_06'] == 1) & (full_data['e_ben'] == 0)]

#panel A results
lin_2006 = smf.ols(formula = 'ln_share ~ below_bench_2 + lis_prem_pos + lis_prem_neg', data = data_06).fit(cov_type='cluster', cov_kwds={'groups': data_06['uniqueID']})
lin_2007 = smf.ols(formula = 'ln_share ~ below_bench_2 + lis_prem_pos + lis_prem_neg', data = data_07).fit(cov_type='cluster', cov_kwds={'groups': data_07['uniqueID']})
lin_2008 = smf.ols(formula = 'ln_share ~ below_bench_2 + lis_prem_pos + lis_prem_neg', data = data_08).fit(cov_type='cluster', cov_kwds={'groups': data_08['uniqueID']})
lin_2009 = smf.ols(formula = 'ln_share ~ below_bench_2 + lis_prem_pos + lis_prem_neg', data = data_09).fit(cov_type='cluster', cov_kwds={'groups': data_09['uniqueID']})
lin_2010 = smf.ols(formula = 'ln_share ~ below_bench_2 + lis_prem_pos + lis_prem_neg', data = data_10).fit(cov_type='cluster', cov_kwds={'groups': data_10['uniqueID']})

#putting results in table
data_year_lin = [lin_2006, lin_2007, lin_2008, lin_2009, lin_2010]
results = []
for lin_year in data_year_lin:
    result = {"Below benchmark, 2006" : lin_year.params.below_bench_2.round(3), "se_1" : lin_year.bse.below_bench_2.round(3), "Below Benchmark" : lin_year.params.lis_prem_neg.round(3), "se_2" : lin_year.bse.lis_prem_neg.round(3), "Above Benchmark" : lin_year.params.lis_prem_pos.round(3), "se_3" : lin_year.bse.lis_prem_pos.round(3), "Observations" : lin_year.nobs, "R^2" : lin_year.rsquared.round(3)}
    results.append(result)
results_df = pd.DataFrame(results)
results_df.index = [2006, 2007, 2008, 2009, 2010]
results_df['se_1'] = results_df['se_1'].apply(lambda x: f'({x})')
results_df['se_2'] = results_df['se_2'].apply(lambda x: f'({x})')
results_df['se_3'] = results_df['se_3'].apply(lambda x: f'({x})')
table_3_a = results_df.T
table_3_a.index = ['Below benchmark, 2006', ' ', 'Below Benchmark', ' ', 'Above Benchmark', ' ', 'Observations', 'R^2']
panel_a = pd.DataFrame(index=['Panel A. Local linear, bandwidth $4'])
table_3_A = pd.concat([panel_a, table_3_a])

#panel B results
quad_2006 = smf.ols(formula = 'ln_share ~ below_bench_2 + lis_prem_pos + lis_prem_neg + lis_prem_pos_sq + lis_prem_neg_sq + lis_prem_pos_cu + lis_prem_neg_cu + lis_prem_pos_qu + lis_prem_neg_qu', data = data_06).fit(cov_type='cluster', cov_kwds={'groups': data_06['uniqueID']})
quad_2007 = smf.ols(formula = 'ln_share ~ below_bench_2 + lis_prem_pos + lis_prem_neg + lis_prem_pos_sq + lis_prem_neg_sq + lis_prem_pos_cu + lis_prem_neg_cu + lis_prem_pos_qu + lis_prem_neg_qu', data = data_07).fit(cov_type='cluster', cov_kwds={'groups': data_07['uniqueID']})
quad_2008 = smf.ols(formula = 'ln_share ~ below_bench_2 + lis_prem_pos + lis_prem_neg + lis_prem_pos_sq + lis_prem_neg_sq + lis_prem_pos_cu + lis_prem_neg_cu + lis_prem_pos_qu + lis_prem_neg_qu', data = data_08).fit(cov_type='cluster', cov_kwds={'groups': data_08['uniqueID']})
quad_2009 = smf.ols(formula = 'ln_share ~ below_bench_2 + lis_prem_pos + lis_prem_neg + lis_prem_pos_sq + lis_prem_neg_sq + lis_prem_pos_cu + lis_prem_neg_cu + lis_prem_pos_qu + lis_prem_neg_qu', data = data_09).fit(cov_type='cluster', cov_kwds={'groups': data_09['uniqueID']})
quad_2010 = smf.ols(formula = 'ln_share ~ below_bench_2 + lis_prem_pos + lis_prem_neg + lis_prem_pos_sq + lis_prem_neg_sq + lis_prem_pos_cu + lis_prem_neg_cu + lis_prem_pos_qu + lis_prem_neg_qu', data = data_10).fit(cov_type='cluster', cov_kwds={'groups': data_10['uniqueID']})

#putting results in table
data_year_quad = [quad_2006, quad_2007, quad_2008, quad_2009, quad_2010]
results_quad = []
for quad_year in data_year_quad:
    result_quad = {"Below benchmark, 2006" : quad_year.params.below_bench_2.round(3), "se_1" : quad_year.bse.below_bench_2.round(3),"Observations" : quad_year.nobs, "R^2" : quad_year.rsquared.round(3)}
    results_quad.append(result_quad)
results_df_quad = pd.DataFrame(results_quad)
results_df_quad.index = [2006, 2007, 2008, 2009, 2010]
results_df_quad['se_1'] = results_df_quad['se_1'].apply(lambda x: f'({x})')
table_3_b = results_df_quad.T
table_3_b.index = ['Below benchmark, 2006', ' ', 'Observations', 'R^2']
panel_b = pd.DataFrame(index=['Panel B. Polynomial, bandwidth $4'])
table_3_B = pd.concat([panel_b, table_3_b])

#combining tables
table_3 = pd.concat([table_3_A, table_3_B])
table_3.fillna('', inplace=True)