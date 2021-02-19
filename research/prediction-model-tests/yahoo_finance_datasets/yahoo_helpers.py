import sys
import json
import pandas as pd


def json_to_dataframe(filename):
    # need to put docstring
    # need to put extensive error checking
    # with open(filename, 'r') as infile:
    #     json_string = infile.read()
    
    # json_data = json.loads(json_string)
    # return pd.DataFrame.from_dict(json_data, orient='index')
    with open(filename, 'r') as infile:
        data = json.load(infile)
        return pd.json_normalize(data['prices'])

dataframe = json_to_dataframe(sys.argv[1])
print(dataframe.info)
