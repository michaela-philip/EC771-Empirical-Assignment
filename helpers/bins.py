import pandas as pd
import numpy as np
import os
import sys

script_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(script_dir, '..'))

#function to create bins as in Ericson (2014)
def get_bins(df, year, n_bins, h):
    step = h / n_bins
    df['bin_temp'] = np.nan

    for x in range(1, n_bins+1):
        df['bin_temp'] = np.where(((df['lis_premium'] >= - step * x) & (df['lis_premium'] < (-step * (x - 1))) & (df['year'] == year)), ( -step * x), df['bin_temp'])

    for x in range(1, n_bins+1):
        df['bin_temp'] = np.where(((df['lis_premium'] >= step * x) & (df['lis_premium'] < (step * (x + 1))) & (df['year'] == year)), (step * x), df['bin_temp'])

    df['bin'] = df.groupby('uniqueID')['bin_temp'].transform('max')

    return df