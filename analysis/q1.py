import numpy as np
import pandas as pd
from tabulate import tabulate
import os
import sys
import matplotlib.pyplot as plt

script_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(script_dir, '..'))

from data_code.load_clean_data import main as main
from data_code.load_clean_data import subsidy as subsidy

from helpers.descriptive_statistics import get_stats

descriptive_stats = get_stats(main)

table_1 = descriptive_stats.T

index = ['Mean monthly premium', '  ', 'Mean deductible', '  ', 'Fraction enhanced benefit', 'Fraction of US firms', 'Fraction of state firms', 'Number of unique firms', 'Number of plans']
table_1.index = index

# table_1 = tabulate(table_1, tablefmt='pipe', headers='keys')

# print(table_1)

fig, ax = plt.subplots(1, 1, figsize = (5,3))
table_1 = plt.table(cellText=table_1.values, colLabels=table_1.columns, rowLabels = table_1.index, cellLoc = 'center',loc = 'center')
ax.axis('off')
plt.suptitle('Table 1')
plt.savefig('data/output/table_1.png', dpi = 300, bbox_inches='tight')
plt.show()

# fig, ax = plt.subplots(1, 1, figsize = (5,3))
# table2 = plt.table(cellText = hbpr_agg_summary.values, colLabels = columns, rowLabels = rows, cellLoc = 'center',loc = 'center', colWidths= [0.15, 0.15, 0.15, 0.15])
# # table2.scale(1.2, 1.3)
# ax.axis('off')
# # plt.suptitle('Funding over Program History')
# plt.savefig('data/output/hbpr_agg_summary.png', dpi = 300, bbox_inches='tight')
# plt.show()