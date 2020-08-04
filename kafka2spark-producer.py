#
# this program is designed to be run from console after ZooKeeper &
# Kafka are already launched
#
from kafka import KafkaProducer
import time
import json
import requests


bootstrap_servers	= ['localhost:9092']                                   
topicName		= 'kafkaRapidAPISpark' #'First_Topic'                                        
pObj			= KafkaProducer(bootstrap_servers=bootstrap_servers, value_serializer=lambda v: json.dumps(v).encode('utf-8'))
url			= "https://covid-193.p.rapidapi.com/statistics"
headers		= {
				'x-rapidapi-host': "covid-193.p.rapidapi.com",
				'x-rapidapi-key': "b7b5f2745dmshabc69c1dcba13f2p191da7jsnd98306ea16c5"
}


def reformat_json(newDict):
	list_dict = {}
	l=[]
	i=0
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
			c = country	
			c = "{" + '"' + "COUNTRY" + '"' + ":" + '"' + country + '"' + "}"
			#list_dict[c]
			l.append({"country":country,"continent":continent,"population":population,"cases":cases_total,"deaths":deaths_total,"tests":tests_total})
			#d= {"country":country,"continent":continent,"population":population,"cases":cases_total,"deaths":deaths_total,"tests":tests_total}
			#l.append({"entry":d})
			
			i += 1
			#if (i >= 2):
			#	break
	#return(list_dict)
	return(l)
	#return({"data":l})


def dump_json(dict):
	country	= "COUNTRY"
	continent	= "CONTINENT"
	population	= "POPULATION"
	cases_total	= "TOTAL CASES"
	deaths_total	= "TOTAL DEATHS"
	tests_total	= "TOTAL TESTS"
	print(format(country," <25"),format(continent,"<20"),format(population,"<15"),format(cases_total,"<15"),format(deaths_total,"<15"),format(tests_total,"<15"))
	for k,v in dict.items():
		print("{}: {}".format(k,v))
	return("")


print("Before producer while loop!...")
i=1
while True:
	response = requests.request("GET", url, headers=headers) # Get RapidAPI COVID-10 statistics
	jDict    = response.json()                               # convert to json 
	#jDict=response.text
	
	#print("Sent:>>>>>>>>>>>>")
	
	#print(jDict)
	new_dict = reformat_json(jDict)
	#new_dict = jDict
	#dump_json(new_dict)
	
	#print(new_dict)
	
	#print("<<<<<<<<<<<<<<<<<")
	
	
	for entry in new_dict:
		#pObj.send(topicName, new_dict)
		pObj.send(topicName, entry)
		print("SENT: " + str(entry) + " >>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
		time.sleep(5)
	
	
	i += 1
	if (i>=1000):
		break

print("Exited producer while loop!...")
print("Exiting producer...")














