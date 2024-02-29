import pandas as pd

def read_data(filepath):
    output = pd.read_stata(filepath)
    return output
