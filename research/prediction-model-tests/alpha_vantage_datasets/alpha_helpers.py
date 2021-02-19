import sys
import json
import pandas as pd


def json_to_dataframe(filename):
    with open(filename, 'r') as infile:
        data = json.load(infile)
        return pd.json_normalize(data)


dataframe = json_to_dataframe(sys.argv[1])
print(dataframe.info)
