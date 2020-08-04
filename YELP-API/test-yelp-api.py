#
# test Python script to read Yelp data
#

import http.client

conn = http.client.HTTPSConnection("yelp-com.p.rapidapi.com")

headers = {
    'x-rapidapi-host': "yelp-com.p.rapidapi.com",
    'x-rapidapi-key': "b7b5f2745dmshabc69c1dcba13f2p191da7jsnd98306ea16c5"
    }

conn.request("GET", "/business/DAiqwrmv19Uv-I1bOoAJCQ", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
