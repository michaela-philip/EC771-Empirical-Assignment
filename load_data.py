import pandas as pd

from helpers.read import read_data

main = read_data('data/input/Data_main.dta')
subsidy = read_data('data/input/Data_subsidyinfo.dta')

print(main.head())
print(subsidy.head())