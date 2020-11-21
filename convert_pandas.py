import pandas as pd
import json

stationsdf = pd.read_csv("freeway_stations.csv")
detectorsdf = pd.read_csv("freeway_detectors.csv")
highwaysdf = pd.read_csv("highways.csv")
loopdf = pd.read_csv("smallloop.csv")

# keeping only relevant columns for detectors
cols = ['detectorid', 'detectorclass', 'lanenumber', 'stationid']
new_detectorsdf = detectorsdf[cols]

# station and highway dataframe
stationsAndHighways = stationsdf.merge(highwaysdf, on="highwayid", how="left")

# merge detectors into stations
data = (
    stationsAndHighways.merge(
        new_detectorsdf
        .groupby("stationid")
        .apply(lambda g: g.to_dict(orient="records"))
        .reset_index(name="detectors"),
        how="left", on="stationid")
    .to_json(orient="records")
)
# print(data)

# write to json
with open("test_pandas.json", "w") as jsonFile:
    jsonFile.write(json.dumps(json.loads(data), indent=4))
