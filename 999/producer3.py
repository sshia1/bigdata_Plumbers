# Import KafkaProducer from Kafka library
from kafka import KafkaConsumer
from kafka import KafkaProducer
import time
import json
import pickle
import requests
import threading
import logging

# Define server with port
bootstrap_servers = ['localhost:9092']

# Define topic name where the message will publish
topicName = 'First_Topic'

# Initialize producer variable
# producer = KafkaProducer(bootstrap_servers = bootstrap_servers)
# producer = KafkaProducer(bootstrap_servers = bootstrap_servers, value_serializer=lambda v: pickle.dumps(v))
producer = KafkaProducer(bootstrap_servers = bootstrap_servers, value_serializer=lambda v: json.dumps(v).encode('utf-8'))
# producer = KafkaProducer(bootstrap_servers =['localhost:9092'],value_serializer=lambda v: json.dumps(v).encode('utf-8'))

# Publish text in defined topic


#producer.send(topicName, 'Hello from kafka...2')
#producer.send(topicName, {'name': 'fahmida','email':'fahmida@gmail.com'})
#time.sleep(1)

print("before producer while loop!")

while True:
            producer.send(topicName, {"dataObjectID": "test1"})
            producer.send(topicName, {"dataObjectID": "test2"})
            time.sleep(1)


# Print message
print("Exiting producer...")


