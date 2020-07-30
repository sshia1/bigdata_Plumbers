# Requests code snippet

import requests

url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
    'x-rapidapi-host': "covid-193.p.rapidapi.com",
    'x-rapidapi-key': "b7b5f2745dmshabc69c1dcba13f2p191da7jsnd98306ea16c5"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)
