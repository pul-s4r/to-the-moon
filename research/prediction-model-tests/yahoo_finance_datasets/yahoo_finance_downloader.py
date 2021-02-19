import sys
import json
import requests
from datetime import date

def save_json(company_name, region):
    url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v3/get-historical-data"
    query_string = {"symbol": company_name, "region": region}
    headers = { 
        'x-rapidapi-key': "127f3b95afmsh16d861bcb826bcfp1f8dedjsn598493929766",
        'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
    }

    response = requests.request('GET', url, headers=headers, params=query_string)

    with open(f'./{company_name}_{date.today().strftime("%Y%m%d")}.txt', 'w') as outfile:
        json.dump(response.text, outfile)


save_json(sys.argv[1], sys.argv[2])
