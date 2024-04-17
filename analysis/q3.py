import pandas as pd
import os
import sys
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
import numpy as np

script_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(script_dir, '..'))

from data_code.load_clean_data import full_data as full_data
from helpers.bins import get_bins

### Redoing figure 3 with 10 bins ###
full_data = get_bins(full_data, 2006, 10, 10)
results = pd.DataFrame()

#local averages with bin size $1, bandwidth of $10, year 2006, no enhanced benefits
condition1 = ((full_data['rd_window_1'] == 1) & (full_data['year'] == 2006) & (full_data['e_ben']==0))
scatter_data = full_data[condition1]
bin_scatter = smf.ols(formula = 'ln_share ~ C(bin)', data = scatter_data).fit()
scatter_data['bin_scatter'] = bin_scatter.predict(scatter_data)

#local linear predition with bandwidth of $4, year 2006, no enhanced benefits
condition2 = ((full_data['rd_window_2'] == 1) & (full_data['year'] == 2006) & (full_data['e_ben']==0))
lin_data = full_data[condition2]
local_lin = smf.ols(formula = 'ln_share ~ below_bench_1 + lis_prem_pos + lis_prem_neg', data = lin_data).fit(cov_type='cluster', cov_kwds={'groups': lin_data['uniqueID']})
lin_data['local_lin'] = local_lin.predict(lin_data)
lin_data_sort = lin_data.sort_values(by='lis_premium')

#quartic polynomial prediction with bandwith of $10, year 2006, no enhanced benefits
condition3 = ((full_data['rd_window_1'] == 1) & (full_data['year'] == 2006) & (full_data['e_ben']==0))
poly_data = full_data[condition3]
quart_poly = smf.ols(formula = 'ln_share ~ below_bench_1 + lis_prem_pos + lis_prem_neg + lis_prem_pos_sq + lis_prem_neg_sq + lis_prem_pos_cu + lis_prem_neg_cu + lis_prem_pos_qu + lis_prem_neg_qu', data = poly_data).fit(cov_type='cluster', cov_kwds={'groups': poly_data['uniqueID']})
poly_data['quart_poly'] = quart_poly.predict(poly_data)
poly_data_sort = poly_data.sort_values(by='lis_premium')

#creating the graph 
plt.close()
ytitle = "Log Enrollment Share, 2006"
plt.scatter(scatter_data['bin'], scatter_data['bin_scatter'], label='Scatter')
plt.plot(lin_data_sort['lis_premium'], lin_data_sort['local_lin'], linestyle='dashed', color='gray', label='Local Linear')
plt.plot(poly_data_sort['lis_premium'], poly_data_sort['quart_poly'], linestyle='solid', color='black', label='Quartic Polynomial')
plt.xlabel("Monthly Premium - LIS Subsidy, 2006")
plt.ylabel(ytitle)
plt.title("Effect of Benchmark Status on Enrollment (10 Bins)")
plt.legend()
plt.savefig('data/output/Figure3a.png')
plt.show()


### Redoing figure 3 with 30 bins ###
full_data = get_bins(full_data, 2006, 30, 10)
results = pd.DataFrame()

#local averages with bin size $0.33, bandwidth of $10, year 2006, no enhanced benefits
condition1 = ((full_data['rd_window_1'] == 1) & (full_data['year'] == 2006) & (full_data['e_ben']==0))
scatter_data = full_data[condition1]
bin_scatter = smf.ols(formula = 'ln_share ~ C(bin)', data = scatter_data).fit()
scatter_data['bin_scatter'] = bin_scatter.predict(scatter_data)

#local linear predition with bandwidth of $4, year 2006, no enhanced benefits
condition2 = ((full_data['rd_window_2'] == 1) & (full_data['year'] == 2006) & (full_data['e_ben']==0))
lin_data = full_data[condition2]
local_lin = smf.ols(formula = 'ln_share ~ below_bench_1 + lis_prem_pos + lis_prem_neg', data = lin_data).fit(cov_type='cluster', cov_kwds={'groups': lin_data['uniqueID']})
lin_data['local_lin'] = local_lin.predict(lin_data)
lin_data_sort = lin_data.sort_values(by='lis_premium')

#quartic polynomial prediction with bandwith of $10, year 2006, no enhanced benefits
condition3 = ((full_data['rd_window_1'] == 1) & (full_data['year'] == 2006) & (full_data['e_ben']==0))
poly_data = full_data[condition3]
quart_poly = smf.ols(formula = 'ln_share ~ below_bench_1 + lis_prem_pos + lis_prem_neg + lis_prem_pos_sq + lis_prem_neg_sq + lis_prem_pos_cu + lis_prem_neg_cu + lis_prem_pos_qu + lis_prem_neg_qu', data = poly_data).fit(cov_type='cluster', cov_kwds={'groups': poly_data['uniqueID']})
poly_data['quart_poly'] = quart_poly.predict(poly_data)
poly_data_sort = poly_data.sort_values(by='lis_premium')

#creating the graph 
plt.close()
ytitle = "Log Enrollment Share, 2006"
plt.scatter(scatter_data['bin'], scatter_data['bin_scatter'], label='Scatter')
plt.plot(lin_data_sort['lis_premium'], lin_data_sort['local_lin'], linestyle='dashed', color='gray', label='Local Linear')
plt.plot(poly_data_sort['lis_premium'], poly_data_sort['quart_poly'], linestyle='solid', color='black', label='Quartic Polynomial')
plt.xlabel("Monthly Premium - LIS Subsidy, 2006")
plt.ylabel(ytitle)
plt.title("Effect of Benchmark Status on Enrollment (30 Bins)")
plt.legend()
plt.savefig('data/output/Figure3b.png')
plt.show()