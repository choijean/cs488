# this script splits a loop data csv and produces
# a new csv file of loop data for each different date

import pandas as pd

rawdata = pd.read_csv("freeway_loopdata_oneweek.csv",
                      parse_dates=['starttime'])

# clean loop data by removing null/0 speeds
data = rawdata[rawdata['speed'].notna()]
data = data[data['speed'] > 0]


data_category_range = data['starttime'].map(
    pd.Timestamp.date).unique().tolist()
print(type(data_category_range[0]))


for i, value in enumerate(data_category_range):
    data[data['starttime'].dt.strftime('%Y-%m-%d').str.contains(value.strftime('%Y-%m-%d'))].to_csv(
        str(value)+r'.csv', index=False, na_rep='N/A')
    print(f"done with {i}, {value}")
