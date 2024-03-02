import pandas as pd
import numpy as np
from tabulate import tabulate

def create_table(df):
    df = df.T
    df.columns = df.iloc[0]
    df = df[1:]
    # output = tabulate(df, headers = 'keys', tablefmt = 'fancy_grid')

    return df 