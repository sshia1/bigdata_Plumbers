# Requests code snippet

import requests

url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
    'x-rapidapi-host': "covid-193.p.rapidapi.com",
    'x-rapidapi-key': ""
    }

response = requests.request("GET", url, headers=headers)

print(response.text)
