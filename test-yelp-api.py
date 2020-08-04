import requests

url = "https://yelp-com.p.rapidapi.com/business/DAiqwrmv19Uv-I1bOoAJCQ"

headers = {
    'x-rapidapi-host': "yelp-com.p.rapidapi.com",
    'x-rapidapi-key': "b7b5f2745dmshabc69c1dcba13f2p191da7jsnd98306ea16c5"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)
