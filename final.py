# Final Project

import pandas as pd
import geopandas as gpd

# Load in data
geo_data = gpd.read_file('United States Counties.csv')
food_access = pd.read_excel('access2015.xls', sheet_name='ACCESS')
stores = pd.read_excel('access2015.xls', sheet_name='STORES')
restaurants = pd.read_excel('access2015.xls', sheet_name='RESTAURANTS')

pop_by_county = pd.read_excel('access2015.xls',
                              sheet_name='Supplemental Data - County')
part_by_state = pd.read_excel('access2015.xls',
                              sheet_name='Supplemental Data - State')
exp_per_cap = pd.read_csv('health_exp_per_capita.csv')

# Select rows of interest in food access dataframe
food_access = food_access[['FIPS', 'State', 'County','PCT_LACCESS_POP10',
                           'PCT_LACCESS_LOWI10', 'PCT_LACCESS_CHILD10', 
                           'PCT_LACCESS_SENIORS10', 'PCT_LACCESS_HHNV10']]

# Select rows of interest in stores dataframe
stores = stores[['PCH_GROC_07_12', 'PCH_GROCPTH_07_12', 'PCH_SUPERC_07_12',
                 'SUPERCPTH07', 'SUPERCPTH12', 'PCH_SUPERCPTH_07_12', 
                 'PCH_CONVS_07_12', 'CONVSPTH07', 'CONVSPTH12',
                 'PCH_CONVSPTH_07_12', 'PCH_SPECS_07_12', 'SPECSPTH07',
                 'SPECSPTH12', 'PCH_SPECSPTH_07_12', 'PCH_SNAPS_08_12',
                 'SNAPSPTH08', 'SNAPSPTH12', 'PCH_SNAPSPTH_08_12']]

# Select rows of interest in restaurants dataframe
restaurants = restaurants[['PCH_FFR_07_12', 'FFRPTH07', 'FFRPTH12',
                           'PCH_FFRPTH_07_12', 'PC_FFRSALES02',
                           'PC_FFRSALES07', 'PC_FSRSALES02', 'PC_FSRSALES07']]


# Select rows of interest in participation dataframe

# Select rows of interest for the health expenditure data
exp_per_cap = exp_per_cap[['Item', 'Group', 'Region_Name', 'State_Name',
                           'Y2010', 'Y2011', 'Y2012', 'Y2013', 'Y2014',
                           'Average_Annual_Percent_Growth']]
exp_per_cap = exp_per_cap.rename(index=str,
                                 columns={'Item': 'type_care',
                                          'Y2010': 'H_EXP2010',
                                          'Y2011': 'H_EXP2011',
                                          'Y2012': 'H_EXP2012',
                                          'Y2013': 'H_EXP2013',
                                          'Y2014': 'H_EXP2014'})

# Join data frames with geometry information
