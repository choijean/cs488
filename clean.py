# this script performs two functions:
#  1. cleans the loop data by removing all empty speeds
#  2. merges the csv files into a single json file

import pandas as pd
import json


# read csv documents
stationsdf = pd.read_csv("freeway_stations.csv")
detectorsdf = pd.read_csv("freeway_detectors.csv")
highwaysdf = pd.read_csv("highways.csv")
loopdf = pd.read_csv("freeway_loopdata_onehour.csv", parse_dates=['starttime'])

# clean loop data by removing empty speeds
cleanloopdf = loopdf[loopdf['speed'].notna()]


# keeping only relevant columns for detectors
cols = ['detectorid', 'detectorclass', 'lanenumber', 'stationid']
new_detectorsdf = detectorsdf[cols]


# station and highway dataframe
stationsAndHighways = stationsdf.merge(highwaysdf, on="highwayid", how="left")

# merge data into detectors
d = (
    new_detectorsdf.merge(
        cleanloopdf
        .groupby("detectorid")
        .apply(lambda g: g.to_dict(orient="records"))
        .reset_index(name="loopdata"),
        how="left", on="detectorid")
)

# merge detectors into stations
data = (
    stationsAndHighways.merge(
        d
        .groupby("stationid")
        .apply(lambda g: g.to_dict(orient="records"))
        .reset_index(name="detectors"),
        how="left", on="stationid")
)

# write to json
data.to_json(r'clean_onehour.json', orient='records',
             indent=4, date_format="iso")
