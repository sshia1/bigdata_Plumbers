# Requests code snippet

import requests
import json

url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
    'x-rapidapi-host': "covid-193.p.rapidapi.com",
    'x-rapidapi-key': "b7b5f2745dmshabc69c1dcba13f2p191da7jsnd98306ea16c5",
    "format":"json"
    }

response = requests.request("GET", url, headers=headers)
jDict = response.json()

print(type(jDict))
