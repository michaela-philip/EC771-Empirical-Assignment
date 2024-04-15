import pandas as pd
import os
import sys

script_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(script_dir, '..'))

from data_code.load_clean_data import main, subsidy

full_data = pd.merge(main, subsidy, on = ['PDPregion', 'year'], how = 'outer')

full_data['lis_premium'] = full_data['premium'] - full_data['subsidy']