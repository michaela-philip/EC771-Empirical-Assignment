import pandas as pd
import os
import sys
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
import numpy as np
from rdrobust import rdrobust,rdbwselect,rdplot

script_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(script_dir, '..'))

from data_code.load_clean_data import full_data as full_data

#binned scatterplot using rdplot with optimal bin size
condition1 = ((full_data['rd_window_1'] == 1) & (full_data['year'] == 2006) & (full_data['e_ben']==0))
scatter_data = full_data[condition1]
bin_scatter = rdplot(y=scatter_data['ln_share'], x=scatter_data['lis_premium'], binselect='es', ci=95)
x = bin_scatter.vars_bins.rdplot_mean_x
y= bin_scatter.vars_bins.rdplot_mean_y
n_bins = len(x)

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
plt.scatter(x, y, label='Scatter')
plt.plot(lin_data_sort['lis_premium'], lin_data_sort['local_lin'], linestyle='dashed', color='gray', label='Local Linear')
plt.plot(poly_data_sort['lis_premium'], poly_data_sort['quart_poly'], linestyle='solid', color='black', label='Quartic Polynomial')
plt.xlabel("Monthly Premium - LIS Subsidy, 2006")
plt.ylabel(ytitle)
plt.title("Effect of Benchmark Status on Enrollment (11 Bins)")
plt.legend()
plt.savefig('data/output/Figure3d.png')
plt.show()
print("The optimal number of bins is " + str(n_bins) + ".")