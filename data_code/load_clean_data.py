import pandas as pd
import numpy as np
import os
import sys

script_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(script_dir, '..'))

from helpers.read import read_data
from helpers.windows import get_windows

main = read_data('data/input/Data_main.dta')
subsidy = read_data('data/input/Data_subsidyinfo.dta')

main.to_csv('data/input/main.csv', index=False)
subsidy.to_csv('data/input/subsidy.csv', index=False)

#create cohort and age variables
main['cohort_year'] = main.groupby('uniqueID')['year'].transform('min') #the year the plan was first offered
main['plan_age'] = main['year'] - main['cohort_year']
main['firm_cohort'] = main.groupby('orgParentCode')['year'].transform('min') #the year the firm first offers a plan
main['firm_cohort_state'] = main.groupby(['orgParentCode', 'state'])['year'].transform('min') #the year that the firm first offers a plan in the state
main['e_ben'] = np.where(main['benefit'] == 'E', 1, 0) #indicator for enhanced benefit
main['firm_exists'] = np.where((main['firm_cohort'] < main['year']), 1, 0) #if the firm existed before the year observed
main['firm_exists_state'] = np.where((main['firm_cohort_state'] < main['year']), 1, 0) #if the firm existed in the state before the year observed
main['share'] = main.groupby(['state', 'year', 'uniqueID'])['enrollment'].transform('sum') / main.groupby(['state', 'year'])['enrollment'].transform('sum') #share of enrollment in state and year
main['ln_share'] = np.log(main['share'])
main.to_csv('data/output/main_plus.csv', index=False)

#restructure subsidy data
subsidy = subsidy.melt(id_vars='PDPregion', value_vars = ['s2006', 's2007', 's2008', 's2009', 's2010'], var_name='year', value_name='subsidy')
subsidy['year'] = subsidy['year'].str[1:].astype(int)
subsidy.to_csv('data/output/subsidy_plus.csv', index=False)

#merge main and subsidy data and calculate lis premium
full_data = pd.merge(main, subsidy, on = ['PDPregion', 'year'], how = 'outer')
full_data['lis_premium'] = full_data['premium'] - full_data['subsidy']

#new variables from Ericson's code
full_data['proposed_benchmark'] = np.where(full_data['lis_premium'] <= 0, 1, 0)
full_data['proposed_benchmark'] = np.where(full_data['benefit'] == 'E', np.nan, full_data['proposed_benchmark'])
full_data['lis_prem_neg'] = np.where(full_data['lis_premium'] <= 0, full_data['lis_premium'], 0)
full_data['lis_prem_pos'] = np.where(full_data['lis_premium'] >= 0, full_data['lis_premium'], 0)

#create RD windows and benchmark indicators
full_data = get_windows(full_data, 10, 2006, 1)
full_data = get_windows(full_data, 4, 2006, 2)
full_data = get_windows(full_data, 2.5, 2006, 3)
full_data = get_windows(full_data, 6, 2006, 4)

#create polynomials
full_data['lis_prem_neg_sq'] = full_data['lis_prem_neg'] ** 2
full_data['lis_prem_neg_cu'] = full_data['lis_prem_neg'] ** 3
full_data['lis_prem_neg_qu'] = full_data['lis_prem_neg'] ** 4
full_data['lis_prem_pos_sq'] = full_data['lis_prem_pos'] ** 2
full_data['lis_prem_pos_cu'] = full_data['lis_prem_pos'] ** 3
full_data['lis_prem_pos_qu'] = full_data['lis_prem_pos'] ** 4

full_data.to_csv('data/output/full_data.csv', index=False)