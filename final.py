# Final Project

import pandas as pd

# Load in data
pop_by_county = pd.read_excel('access2015.xls',
                              sheet_name='Supplemental Data - County')
part_by_state = pd.read_excel('access2015.xls',
                              sheet_name='Supplemental Data - State')
obes_prev = pd.read_excel('obs.xlsx')
exp_per_cap = pd.read_csv('health_exp_per_capita.csv')

# Select rows of interst for the obesity prevalence data
obes_prev.drop(['number04', 'percent04', 'lower confidence limit04',
                'upper confidence limit04', 'age-adjusted percent04',
                'age-adjusted lower confidence limit04',
                'age-adjusted upper confidence limit04', 'number05',
                'percent05', 'lower confidence limit05',
                'upper confidence limit05', 'age-adjusted percent05',
                'age-adjusted lower confidence limit05',
                'age-adjusted upper confidence limit05', 'number06',
                'percent06', 'lower confidence limit06',
                'upper confidence limit06', 'age-adjusted percent06',
                'age-adjusted lower confidence limit06', 
                'age-adjusted upper confidence limit06', 'number07',
                'percent07', 'lower confidence limit07',
                'upper confidence limit07', 'age-adjusted percent07',
                'age-adjusted lower confidence limit07',
                'age-adjusted upper confidence limit07', 'number08',
                'percent08', 'lower confidence limit08',
                'upper confidence limit08', 'age-adjusted percent08',
                'age-adjusted lower confidence limit08',
                'age-adjusted upper confidence limit08', 'number09',
                'percent09', 'lower confidence limit09',
                'upper confidence limit09', 'age-adjusted percent09',
                'age-adjusted lower confidence limit09', 
                'age-adjusted upper confidence limit09'], axis=1, inplace=True)

# Select rows of interest for the health expenditure data
exp_per_cap = exp_per_cap[['Item', 'Group', 'Region_Name', 'State_Name',
                           'Y2010', 'Y2011', 'Y2012', 'Y2013', 'Y2014',
                           'Average_Annual_Percent_Growth']]
exp_per_cap = exp_per_cap.rename(index=str,
                   columns={'Item': 'type_care', 'Y2010': 'H_EXP2010', 
                            'Y2011': 'H_EXP2011', 'Y2012': 'H_EXP2012',
                            'Y2013': 'H_EXP2013', 'Y2013': 'H_EXP2014'})
