# this script splits a loop data csv and produces
# a new json file of stations organized filled with data
# for a specific date

import pandas as pd
import json
from datetime import datetime, timedelta

# read csv documents
stationsdf = pd.read_csv("freeway_stations.csv")
detectorsdf = pd.read_csv("freeway_detectors.csv")
highwaysdf = pd.read_csv("highways.csv")
rawdata = pd.read_csv("freeway_loopdata_oneweek.csv",
                      parse_dates=['starttime'])

# convert time to not UTC format
rawdata['starttime'] = rawdata['starttime'].dt.tz_convert(
    None) - timedelta(hours=7)


# clean loop data by removing null/0 speeds
data = rawdata[rawdata['speed'] > 0].dropna()

# keeping only relevant columns for detectors
new_detectorsdf = detectorsdf[['detectorid',
                               'detectorclass', 'lanenumber', 'stationid']]

# categorize on loop data date
data_category_range = data['starttime'].map(
    pd.Timestamp.date).unique().tolist()

# station and highway dataframe
stationsAndHighways = stationsdf.merge(highwaysdf, on="highwayid", how="left")


for i, value in enumerate(data_category_range):
    df = data[data['starttime'].dt.strftime(
        '%Y-%m-%dT%H:%M%:%SZ').str.startswith(value.strftime('%Y-%m-%d'))]
    # print(df)

    # merge data into detectors
    d = (
        new_detectorsdf.merge(
            df
            .groupby("detectorid")
            .apply(lambda g: g.to_dict(orient="records"))
            .reset_index(name="loopdata"),
            how="left", on="detectorid")
    )
    # print(d)

    # merge detectors into stations
    d2 = (
        stationsAndHighways.merge(
            d
            .groupby("stationid")
            .apply(lambda g: g.to_dict(orient="records"))
            .reset_index(name="detectors"),
            how="left", on="stationid")
    )
    # print(data)

    # # write to json
    d2.to_json(str(value)+r'.json', orient='records',
               indent=4, date_format="iso")

    print(f"done with {i}, {value}")
