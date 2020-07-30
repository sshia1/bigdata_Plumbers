# Requests code snippet

import requests
import json

url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
    'x-rapidapi-host': "covid-193.p.rapidapi.com",
    'x-rapidapi-key': "",
    "format":"json"
    }

response = requests.request("GET", url, headers=headers)
jDict = response.json()

print(type(jDict))
