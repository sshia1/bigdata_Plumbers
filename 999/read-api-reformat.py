# Requests code snippet

import requests
import json


url		= "https://covid-193.p.rapidapi.com/statistics"
headers	= {
	'x-rapidapi-host': "covid-193.p.rapidapi.com",
	'x-rapidapi-key': "",
	"format":"json"
}


def reformat_json(newDict):
	list_dict = {}
	for entry in newDict["response"]:
		country	=entry["country"]
		if not(country in ["get","parameters","results","errors","response"]):
			if country is None:
				country="None"
			continent	=entry["continent"]
			if continent is None:
				continent="None"
			population	=entry["population"]
			if population is None:
				population=0
			cases		=entry["cases"]
			if cases is None:
				cases = {}	
			deaths		=entry["deaths"]
			if deaths is None:
				deaths = {}
			tests		=entry["tests"]
			if tests is None:
				tests={}	
			day		=entry["day"]
			time		=entry["time"]
			cases_total=0
			if "total" in cases:
				cases_total 	=cases["total"]
			deaths_total=0
			if "total" in deaths:
				deaths_total	=deaths["total"]
			tests_total=0
			if "total" in tests:
				tests_total	=tests["total"]
			if cases_total is None:
				cases_total = 0
			if deaths_total is None:
				deaths_total = 0
			if tests_total is None:
				tests_total = 0	
			list_dict[country]={"continent":continent,"population":population,"cases":cases_total,"deaths":deaths_total,"tests":tests_total}
	return(list_dict)
	
	
def dump_json(dict):
	#country	= "COUNTRY"
	#continent	= "CONTINENT"
	#population	= "POPULATION"
	#cases_total	= "TOTAL CASES"
	#deaths_total	= "TOTAL DEATHS"
	#tests_total	= "TOTAL TESTS"
	print('"COUNTRY: {"CONTINENT", "POPULATION", "TOTAL CASES", "TOTAL DEATHS", "TOTAL TESTS"}')
	for k,v in dict.items():
		#print(k)
		if not(k in ["get","parameters","results","errors","response"]):
			print("{}: {}".format(k,v))
	return("")

# *************** MAIN *********************
response	= requests.request("GET", url, headers=headers)
jDict		= response.json()
new_dict	= reformat_json(jDict)
dump_json(new_dict)
# ************** END MAIN ******************



