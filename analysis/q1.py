import numpy as np
import pandas as pd
from tabulate import tabulate
import os
import sys

script_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(script_dir, '..'))

from data_code.load_data import main as main
from data_code.load_data import subsidy as subsidy

from helpers.descriptive_statistics import get_stats

descriptive_stats = get_stats(main)

table_1 = descriptive_stats.T

index = ['Mean monthly premium', '  ', 'Mean deductible', '  ', 'Fraction enhanced benefit', 'Fraction of US firms', 'Fraction of state firms', 'Number of unique firms', 'Number of plans']
table_1.index = index