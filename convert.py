import csv
import json


data = []
with open("freeway_stations.csv") as csvFile:
    csvReader = csv.DictReader(csvFile)

    # convert string to numbers before appending data
    for csvRow in csvReader:
        csvRow["stationid"] = int(csvRow["stationid"])
        csvRow["highwayid"] = int(csvRow["highwayid"])
        csvRow["milepost"] = float(csvRow["milepost"])
        csvRow["upstream"] = int(csvRow["upstream"])
        csvRow["downstream"] = int(csvRow["downstream"])
        csvRow["stationclass"] = int(csvRow["stationclass"])
        csvRow["numberlanes"] = int(csvRow["numberlanes"])
        csvRow["length"] = float(csvRow["length"])
        data.append(csvRow)

# write data to a json file
with open("test.json", "w") as jsonFile:
    jsonFile.write(json.dumps(data, indent=4))


