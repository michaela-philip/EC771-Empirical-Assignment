import pandas as pd

from helpers.read import read_data

main = read_data('data/input/Data_main.dta')
subsidy = read_data('data/input/Data_subsidyinfo.dta')

main.to_csv('data/input/main.csv', index=False)
subsidy.to_csv('data/input/subsidy.csv', index=False)

main['cohort_year'] = main.groupby('uniqueID')['year'].transform('min')
main['plan_age'] = main['year'] - main['cohort_year']
main['firm_cohort'] = main.groupby('orgParentCode')['year'].transform('min')
main['firm_cohort_state'] = main.groupby(['orgParentCode', 'state'])['year'].transform('min')

main.to_csv('data/output/main_plus.csv', index=False)