import pandas as pd
import os
import sys

script_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(script_dir, '..'))

def read_data(filepath):
    output = pd.read_stata(filepath)
    return output
