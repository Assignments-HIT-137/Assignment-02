import pandas as pd
import numpy as np
import glob
import os
def calculate_seasonal_avg(data):
    season_avg = data.groupby('season')['temperature'].mean().round(1)

    with open("average_temp.txt", "w") as f:
         for season, avg in season_avg.items():
            f.write(f"{season}: {avg}°C\n")

def calculate_temperatureRange(data):
    station_range = data.groupby('STATION_NAME')['temperature'].agg(['min','max'])
    station_range['range'] = station_range['max'] - station_range['min']

    max_range = station_range['range'].max()
    largest_range_stations = station_range[station_range['range'] == max_range]

    with open("largest_temp_range_station.txt", "w") as f:
        for station, row in largest_range_stations.iterrows():
            f.write(f"{station}: Range {row['range']:.1f}°C (Max: {row['max']:.1f}°C, Min: {row['min']:.1f}°C)\n")    

def calculate_temperatureStability(data):

    station_std = data.groupby('STATION_NAME')['temperature'].std()

    min_std = station_std.min()
    max_std = station_std.max()

    most_stable = station_std[station_std == min_std]
    most_variable = station_std[station_std == max_std]

    with open("temperature_stability_stations.txt", "w") as f:
        for station, std in most_stable.items():
            f.write(f"Most Stable: {station}: StdDev {std:.1f}°C\n")
        for station, std in most_variable.items():
            f.write(f"Most Variable: {station}: StdDev {std:.1f}°C\n")    
# Step 1: Loading ALL CSV files
def main():
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

    # Step 2: Mapping months to numbers

    month_map = {
        'January':1, 'February':2, 'March':3, 'April':4, 'May':5, 'June':6,
        'July':7, 'August':8, 'September':9, 'October':10, 'November':11, 'December':12
    }
    data['month_num'] = data['month'].map(month_map)

    # Step 3: Defining Australian seasons

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
    # Step 4: Seasonal Average across ALL stations & years 
    calculate_seasonal_avg(data)
    # Step 5: Temperature Range per Station
    calculate_temperatureRange(data)
    # Step 6: Temperature Stability (StdDev)    
    calculate_temperatureStability(data)
    print("Analysis completed. Results saved to text files.")

if __name__=="__main__":
    main()

