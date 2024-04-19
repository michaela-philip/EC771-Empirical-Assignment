import pandas as pd
import os
import sys
import numpy as np
from rddensity import rddensity, rdplotdensity
import matplotlib.pyplot as plt

script_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(script_dir, '..'))

from data_code.load_clean_data import full_data as full_data

rd_test = rddensity(full_data['lis_premium'])

rd_test_pval = rd_test.p
rd_test_diff = rd_test.hat

print("The p-value for the manipulation test is " + str(rd_test_pval))
print("The difference in estimated density at the cutoff is " + str((rd_test_diff.right - rd_test_diff.left).round(4)))

density_plot = rdplotdensity(rd_test, full_data['lis_premium'], xlabel = 'Monthly Premium - LIS Subsidy', title = 'Manipulation Test')
# print(density_plot)