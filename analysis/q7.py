import pandas as pd
import os
import sys
import numpy as np
import statsmodels.formula.api as smf
from rdrobust import rdrobust,rdbwselect,rdplot

script_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(script_dir, '..'))

from data_code.load_clean_data import full_data as full_data

years = [2006, 2007, 2008, 2009, 2010]

rd_lin = {}
rd_poly = {}

for i in years:
    data = full_data[full_data['year'] == i]
    x = data['lis_premium_06']
    y = data['ln_share'] 
    rd_lin[i] = rdrobust(y, x, bwselect = 'cerrd')
    rd_poly[i] = rdrobust(y, x, bwselect='cerrd', p = 2)

rd_lin_2006 = rd_lin[2006]

#putting results in table
results = []
for year in years:
    result = {"LIS Premium, 2006" : rd_lin[year].coef.values[0][0].round(3), "se_1" : rd_lin[year].se.values[0][0].round(3), "Bandwidth" : rd_lin[year].bws.values[0,0].round(2)}
    results.append(result)
results_df = pd.DataFrame(results)
results_df.index = [2006, 2007, 2008, 2009, 2010]
results_df['se_1'] = results_df['se_1'].apply(lambda x: f'({x})')
table_4_a = results_df.T
table_4_a.index = ['LIS Premium, 2006', ' ', 'Bandwidth']
panel_a = pd.DataFrame(index=['Panel A. Local linear, CE-optimal Bandwidths'])
table_4_A = pd.concat([panel_a, table_4_a])

#putting results in table
results_quad = []
for year in years:
    result_quad = {"LIS Premium, 2006" : rd_poly[year].coef.values[0][0].round(3), "se_1" : rd_poly[year].se.values[0][0].round(3), "Bandwidth" : rd_poly[year].bws.values[0,0].round(2)}
    results_quad.append(result_quad)
results_df_quad = pd.DataFrame(results_quad)
results_df_quad.index = [2006, 2007, 2008, 2009, 2010]
results_df_quad['se_1'] = results_df_quad['se_1'].apply(lambda x: f'({x})')
table_4_b = results_df_quad.T
table_4_b.index = ['LIS Premium, 2006', ' ', 'Bandwidth']
panel_b = pd.DataFrame(index=['Panel B. Polynomial, CE-optimal Bandwidths'])
table_4_B = pd.concat([panel_b, table_4_b])

#combining tables
table_4 = pd.concat([table_4_A, table_4_B])
table_4.fillna('', inplace=True)