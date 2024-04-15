import pandas as pd
import numpy as np

def get_stats(df):

    data = []

    year = df['cohort_year']
    df = df[df['plan_age'] == 0]
    premium = df.groupby('cohort_year')['premium'].agg(['mean']).round(0)
    premium_std = df.groupby('cohort_year')['premium'].agg(['std']).round(0)
    deductible = df.groupby('cohort_year')['deductible'].agg(['mean']).round(0)
    deductible_std = df.groupby('cohort_year')['deductible'].agg(['std']).round(0)
    enhanced_benefit = df.groupby('cohort_year')['e_ben'].mean().round(2)
    firms = df.groupby('cohort_year')['orgParentCode'].nunique()
    plans = df.groupby('cohort_year')['uniqueID'].nunique()
    existing_firm_US = df.groupby('cohort_year')['firm_exists'].mean().round(2)
    existing_firm_state = df.groupby('cohort_year')['firm_exists_state'].mean().round(2)
    
    #get rid of trailing zeros and do some formatting
    premium = premium.map('${:.0f}'.format)
    premium_std = premium_std.map('({:.0f})'.format)
    deductible = deductible.map('${:.0f}'.format)
    deductible_std = deductible_std.map('({:.0f})'.format)
    plans = plans.map('{:,.0f}'.format)

    cohort_year = [2006, 2007, 2008, 2009, 2010]

    premium.index = cohort_year
    premium_std.index = cohort_year
    deductible.index = cohort_year
    deductible_std.index = cohort_year
    enhanced_benefit.index = cohort_year
    firms.index = cohort_year
    plans.index = cohort_year
    existing_firm_US.index = cohort_year
    existing_firm_state.index = cohort_year

    output = pd.concat([premium, premium_std, deductible, deductible_std, enhanced_benefit, existing_firm_US, existing_firm_state, firms, plans], axis = 1)
    return output
