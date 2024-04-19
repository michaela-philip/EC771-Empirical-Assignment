import pandas as pd
import os
import sys
import numpy as np
import statsmodels.formula.api as smf
from linearmodels.iv import IV2SLS

script_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(script_dir, '..'))

from data_code.load_clean_data import full_data as full_data

# data.2007 <- final.data %>%
#   filter(year==2007) %>%
#   select(orgParentCode, planName, state, contractId, uniqueID,
#          premium_2007=premium)

# reg.data <- data.2006 %>%
#   left_join(data.2007, by=c("orgParentCode","planName","state",
#                             "contractId","uniqueID")) %>%
#   mutate(premium_diff=premium_2007-premium_2006)

# mean.share <- round(as.numeric(reg.data %>% summarize(mean_share=mean(share, na.rm=TRUE))), 3)
# inertia <- feols(premium_diff~1 | ln_share~LISPremium_2006, data=reg.data)


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

#run 2sls
endog = full_data['ln_share'] 
dependent = full_data['premium_diff']
instruments = full_data['lis_premium_06']
iv = IV2SLS(dependent, None, endog, instruments).fit()
