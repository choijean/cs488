import pandas as pd
import json


# read csv documents
loopdf = pd.read_csv("freeway_loopdata_oneweek.csv", parse_dates=['starttime'])

# clean loop data by removing null/0 speeds
cleanloopdf = loopdf[loopdf['speed'] > 0].dropna()

cleanloopdf.to_csv(
    r'freeway_loopdata_oneweek_clean.csv', index=False, na_rep='N/A')
