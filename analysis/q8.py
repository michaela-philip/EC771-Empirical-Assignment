import pandas as pd
import os
import sys
import numpy as np
import statsmodels.formula.api as smf
from linearmodels.iv import IV2SLS

script_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(script_dir, '..'))

from data_code.load_clean_data import full_data as full_data

#value of premium (without subsidy) in 2006
data_2006 = full_data[full_data['year'] == 2006]
premium_2006 = data_2006[['uniqueID', 'premium']].drop_duplicates()
premium_2006.rename(columns={'premium': 'premium_06'}, inplace=True)
full_data = pd.merge(full_data, premium_2006, on='uniqueID', how='left')

#premium (without subsidy) in 2007
data_2007 = full_data[full_data['year'] == 2007]
premium_2007 = data_2007[['uniqueID', 'premium']].drop_duplicates()
premium_2007.rename(columns={'premium': 'premium_07'}, inplace=True)
full_data = pd.merge(full_data, premium_2007, on='uniqueID', how='left')

full_data['premium_diff'] = full_data['premium_07'] - full_data['premium_06']

full_data = full_data.rename(columns={'ln_share': 'lnshare', 'lis_premium_06' : 'lispremium06'})

#run 2sls
endog = full_data['lnshare'] 
dependent = full_data['premium_diff']
instruments = full_data['lispremium06']
iv = IV2SLS(dependent, None, endog, instruments).fit()