import pandas as pd
import numpy as np

def get_stats(df):
    data = []

    for i in df['cohort_year'].unique():
        #calculate the values
        monthly_premium = np.mean(df[df['cohort_year'] == i]['premium']).round(0)
        monthly_premium_std = np.std(df[df['cohort_year'] == i]['premium']).round(0)
        deductible = np.mean(df[df['cohort_year'] == i]['deductible']).round(0)
        deductible_std = np.std(df[df['cohort_year'] == i]['deductible']).round(0)
        benefit = ((((df['benefit'] == 'E') & (df['cohort_year'] ==i)).sum()) / len(df[df['cohort_year'] == i])).round(2)
        existing_firm_US = round((len(df[(df['firm_cohort'] != i) & (df['cohort_year'] == i)]) / len(df[df['cohort_year'] == i])), 2)
        existing_firm_state = round((len(df[(df['firm_cohort_state'] != i) & (df['cohort_year'] == i)])) / (len(df[df['cohort_year'] == i])), 2)
        firms = df[df['cohort_year']==i]['orgParentCode'].nunique()
        plans = df[df['cohort_year']==i]['uniqueID'].nunique()

        #get rid of trailing zeros and do some formatting
        year = '{:.0f}'.format(i)
        monthly_premium = '${:.0f}'.format(monthly_premium)
        monthly_premium_std = '({:.0f})'.format(monthly_premium_std)
        deductible = '${:.0f}'.format(deductible)
        deductible_std = '({:.0f})'.format(deductible_std)
        plans = '{:,.0f}'.format(plans)

        #append the values 
        data.append({'year': year, 'premium': monthly_premium, 'premium_std': monthly_premium_std, 'deductible': deductible, 'ded_std': deductible_std, 'benefit': benefit, 'existing US firm' : existing_firm_US, 'existing state firm' : existing_firm_state, 'firms': firms, 'plans': plans})

    output = pd.DataFrame(data)
    return output