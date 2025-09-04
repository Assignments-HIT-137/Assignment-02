import pandas as pd
import numpy as np
import glob
import os

# Step 0: Loading ALL CSV files

all_files = glob.glob(os.path.join("temperatures", "*.csv"))
dfs = []

for file in all_files:
    df = pd.read_csv(file)
    
    # Keeping relevant columns
    df = df[['STATION_NAME', 'STN_ID', 'LAT', 'LON',
             'January','February','March','April','May','June',
             'July','August','September','October','November','December']]
    
    # Reshaping : wide → long format
    df_long = df.melt(
        id_vars=['STATION_NAME','STN_ID','LAT','LON'],
        value_vars=['January','February','March','April','May','June',
                    'July','August','September','October','November','December'],
        var_name='month', value_name='temperature'
    )
    
    # Dropping missing values
    df_long = df_long.dropna(subset=['temperature'])
    
    dfs.append(df_long)

# Combining all years
data = pd.concat(dfs, ignore_index=True)

# Step 1: Mapping months to numbers

month_map = {
    'January':1, 'February':2, 'March':3, 'April':4, 'May':5, 'June':6,
    'July':7, 'August':8, 'September':9, 'October':10, 'November':11, 'December':12
}
data['month_num'] = data['month'].map(month_map)

# Step 2: Defining Australian seasons

def get_season(month):
    if month in [12, 1, 2]:
        return "Summer"
    elif month in [3, 4, 5]:
        return "Autumn"
    elif month in [6, 7, 8]:
        return "Winter"
    else:
        return "Spring"

data['season'] = data['month_num'].apply(get_season)
