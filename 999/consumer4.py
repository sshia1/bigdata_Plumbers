# Import KafkaConsumer from Kafka library
from kafka import KafkaConsumer
from kafka import kafkaProducer
import sys
import time
import json
import pickle
import requests
import threading
import logging

# Define server with port
bootstrap_servers = ['localhost:9092']

# Define topic name from where the message will recieve
topicName = 'First_Topic'

# Initialize consumer variable
#consumer = KafkaConsumer (topicName, group_id ='group1',bootstrap_servers = bootstrap_servers)
# consumer = KafkaConsumer(topicName,bootstrap_servers=bootstrap_servers, value_deserializer=lambda m: pickle.load(m))
#consumer = KafkaConsumer(topicName, bootstrap_servers=bootstrap_servers,value_deserializer=lambda m: json.loads(m.decode('utf-8')))

consumer = KafkaConsumer(bootstrap_servers=bootstrap_servers, auto_offset_reset='earliest', value_deserializer=lambda m: json.loads(m.decode('utf-8')))
consumer.subscribe(topicName)

#consumer = KafkaConsumer (topicName,bootstrap_servers = ['localhost:9092'],value_deserializer=lambda m: json.loads(m.decode('utf-8')))

#consumer = KafkaConsumer(bootstrap_servers='victoria.com:6667',
#                                 auto_offset_reset='earliest',
#                                 value_deserializer=lambda m: json.loads(m.decode('utf-8')))
#        consumer.subscribe(['my-topic'])

# Read and print message from consumer
print("before consumer for loop!")
for message in consumer:
	# print("Topic Name=%s,Message=%s"%(message.topic,message.value))
	#print("Consumer records:\n")
	print(message)
	#print("\nReading from JSON data\n")
	#print("Name:",message[6]['name'])
	#print("Email:",message[6]['email'])
	#time.sleep(1)

# Terminate the script
print("Exiting consumer...")
sys.exit()
