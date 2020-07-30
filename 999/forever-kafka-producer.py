# this program is designed to be run from console after ZooKeeper &
# Kafka are already launched
#
from kafka import KafkaProducer
import time
import json
import requests


bootstrap_servers	= ['localhost:9092']                                   
topicName		= 'kafkaRapidAPISpark' #'First_Topic'                                        
#producer		= KafkaProducer(bootstrap_servers = bootstrap_servers) 
#pObj			= KafkaProducer(bootstrap_servers=bootstrap_servers,
#				value_serializer=lambda v: json.dumps(v).encode('utf-8'))

pObj			= KafkaProducer(bootstrap_servers=bootstrap_servers, value_serializer=lambda v: json.dumps(v).encode('utf-8'))

#pObj			= KafkaProducer(bootstrap_servers=bootstrap_servers)

url			= "https://covid-193.p.rapidapi.com/statistics"

headers		= {
    'x-rapidapi-host': "covid-193.p.rapidapi.com",
    'x-rapidapi-key': "b7b5f2745dmshabc69c1dcba13f2p191da7jsnd98306ea16c5"
}

# Publish text in defined topic

#pObj = KafkaProducer(bootstrap_servers='localhost:9092',
#                                 value_serializer=lambda v: json.dumps(v).encode('utf-8'))

print("Before producer while loop!...")
i=1
while True:
	#pObj.send(topicName, {"dataObjectID": "test1"})
	#pObj.send(topicName, {"dataObjectID": "test2"})
	response = requests.request("GET", url, headers=headers) # Get RapidAPI COVID-10 statistics
	jDict    = response.json()                               # convert to json 
	print("Sent:>>>>>>>>>>>>")
	print(jDict)
	print("<<<<<<<<<<<<<<<<<")
	pObj.send(topicName, jDict)
	time.sleep(1)
	i += 1
	if (i>=1000):
		break

#print("Before producer while loop!...")
#i=1
#while(True):
#	response = requests.request("GET", url, headers=headers)
#	
#	#producer.send(topicName, b'HELLO FROM KAFKA to SPARK!.........')
#	
#	time.sleep(1)
#	i += 1
#	if (i>=1000):
#		break


print("Exited producer while loop!...")

# Print message
print("Exiting producer...")


