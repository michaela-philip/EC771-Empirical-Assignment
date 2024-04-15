import pandas as pd
import numpy as np
import os
import sys

script_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(script_dir, '..'))

from helpers.read import read_data

main = read_data('data/input/Data_main.dta')
subsidy = read_data('data/input/Data_subsidyinfo.dta')

main.to_csv('data/input/main.csv', index=False)
subsidy.to_csv('data/input/subsidy.csv', index=False)

main['cohort_year'] = main.groupby('uniqueID')['year'].transform('min') #the year the plan was first offered
main['plan_age'] = main['year'] - main['cohort_year']
main['firm_cohort'] = main.groupby('orgParentCode')['year'].transform('min') #the year the firm first offers a plan
main['firm_cohort_state'] = main.groupby(['orgParentCode', 'state'])['year'].transform('min') #the year that the firm first offers a plan in the state
main['e_ben'] = np.where(main['benefit'] == 'E', 1, 0)
main['firm_exists'] = np.where((main['firm_cohort'] < main['year']), 1, 0) #if the firm existed before the year observed
main['firm_exists_state'] = np.where((main['firm_cohort_state'] < main['year']), 1, 0) #if the firm existed in the state before the year observed

main.to_csv('data/output/main_plus.csv', index=False)