# CS-488P

Forest Pearson, Haley Siebert, Jean Choi

11/24/2020

## Queries

Since queries 1,2, and 5 can be exported to python they are included as such. Query 6 however can be found below.

>db.testtest.update({locationtext: "Foster NB"},{$set: {milepost: '22.6'}}

## Scripts

### `clean.py`

The purpose of this script is to:

1. parse a single CSV file
2. remove any empty or 0 speed data
3. produce a new CSV file containing the cleaned data

Example File Input/Output:

- Input file: freeway_loopdata.csv
- Output file: freeway_loopdata_clean.csv

### `cleanconvert.py`

The purpose of this script is to:

1. parse the loopdata, station, highway and detector CSV files
2. remove any empty or 0 speed data
3. merge the tables into a nested JSON format
4. produce a JSON file containing the cleaned, reformatted data

Example File Input/Output:

- Input files:
  - freeway_loopdata_oneweek.csv
  - freeway_stations.csv
  - freeway_detectors.csv
  - highways.csv
- Output file: loopdata_oneweek.json

### `split.py`

The purpose of this script is to:

1. parse the loopdata CSV file
2. remove any empty or 0 speed data
3. organize/create a new table for each date of data
4. produce a CSV file for each date of data

Example File Input/Output:

- Input files: freeway_loopdata_oneweek.csv
- Output files:
  - 2020-09-18.csv
  - 2020-09-19.csv
  - 2020-09-20.csv
  - etc.

### `splitconvert.py`

The purpose of this script is to:

1. parse the loopdata, station, highway and detector CSV files
2. remove any empty or 0 speed data
3. organize/create a new table for each date of data
4. convert each table into a json file

- Input files:
  - freeway_loopdata_oneweek.csv
  - freeway_stations.csv
  - freeway_detectors.csv
  - highways.csv
- Output files:
  - 2020-09-18.json
  - 2020-09-19.json
  - 2020-09-20.json
  - etc.
