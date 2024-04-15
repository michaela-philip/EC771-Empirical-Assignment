import pandas as pd
import numpy as np
from tabulate import tabulate
import os
import sys

script_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(script_dir, '..'))

def create_table(df):
    df = df.T
    df.columns = df.iloc[0]
    df = df[1:]
    # output = tabulate(df, headers = 'keys', tablefmt = 'fancy_grid')

    return df 