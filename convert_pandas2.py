import pandas as pd
import json

stationsdf = pd.read_csv("freeway_stations.csv")
detectorsdf = pd.read_csv("freeway_detectors.csv")
highwaysdf = pd.read_csv("highways.csv")
loopdf = pd.read_csv("freeway_loopdata_onehour.csv")

# keeping only relevant columns for detectors
cols = ['detectorid', 'detectorclass', 'lanenumber', 'stationid']
new_detectorsdf = detectorsdf[cols]

# station and highway dataframe
stationsAndHighways = stationsdf.merge(highwaysdf, on="highwayid", how="left")

# merge data into detectors
d = new_detectorsdf.merge(
        loopdf
        .groupby("detectorid")
        .apply(lambda g: g.to_dict(orient="records"))
        .reset_index(name="loopdata"),
        how="left", on="detectorid")
# print(d)

# merge detectors into stations
data = stationsAndHighways.merge(
        d
        .groupby("stationid")
        .apply(lambda g: g.to_dict(orient="records"))
        .reset_index(name="detectors"),
        how="left", on="stationid").to_json(orient="records")
# print(data)

# write to json
with open("test_pandas2.json", "w") as jsonFile:
    jsonFile.write(json.dumps(json.loads(data), indent=4))
