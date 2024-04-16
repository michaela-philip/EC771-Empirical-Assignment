import pandas as pd
import numpy as np
import os
import sys

script_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(script_dir, '..'))

def get_windows(df, window_size, year, window_number):
    df['rd_window_'+str(window_number)] = np.where(((df['lis_premium'] >= -window_size) & (df['lis_premium'] <= window_size) & (df['year'] == year)), 1, 0)
    df['below_bench_'+str(window_number)] = np.where(((df['lis_premium'] <= 0) & (df['rd_window_1'] == 1)), 1, 0)

    return df