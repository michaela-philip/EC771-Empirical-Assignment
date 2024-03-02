import numpy as np
import pandas as pd
from tabulate import tabulate

from load_data import main as main
from load_data import subsidy as subsidy

from helpers.descriptive_statistics import get_stats
from helpers.tables import create_table

descriptive_stats = get_stats(main)
descriptive_stats.sort_values(by='year', inplace=True)
table_1 = create_table(descriptive_stats)

index = ['Mean monthly premium', '  ', 'Mean deductible', '  ', 'Fraction enhanced benefit', 'Fraction of US firms', 'Fraction of state firms', 'Number of unique firms', 'Number of plans']

table_1.index = index

print(table_1)