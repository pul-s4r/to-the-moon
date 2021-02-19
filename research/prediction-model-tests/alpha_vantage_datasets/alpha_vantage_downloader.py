import sys
import json
from datetime import date
from alpha_vantage.timeseries import TimeSeries


api_key = '1PRBO66RYM7SV7B9'
history_points = 30


def save_json(company_name):
    ts = TimeSeries(key=api_key)
    data = ts.get_daily_adjusted(company_name, outputsize='full')
    
    with open(f'./{company_name}_{date.today().strftime("%Y%m%d")}.json', 'w') as outfile:
        json.dump(data, outfile)


save_json(sys.argv[1])
