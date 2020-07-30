# Import KafkaConsumer from Kafka library
from kafka import KafkaConsumer

# Import sys module
import sys

# Import json module to serialize data
import json

# Initialize consumer variable and set property for JSON decode
consumer = KafkaConsumer ('JSONtopic',bootstrap_servers = ['localhost:9092'],value_deserializer=lambda m: json.loads(m.decode('utf-8')))

# Read data from kafka
for message in consumer:
	print("Consumer records:\n")
	print(message)
print("\nReading from JSON data\n")
print("Name:",message[6]['name'])
print("Email:",message[6]['email'])
# Terminate the script
sys.exit()
