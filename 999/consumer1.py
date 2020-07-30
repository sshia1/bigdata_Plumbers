# Import KafkaConsumer from Kafka library
from kafka import KafkaConsumer
import sys
import time

# Define server with port
bootstrap_servers = ['localhost:9092']

# Define topic name from where the message will recieve
topicName = 'First_Topic'

# Initialize consumer variable
consumer = KafkaConsumer (topicName, group_id ='group1',bootstrap_servers = bootstrap_servers)

# Read and print message from consumer
for msg in consumer:
	print("Topic Name=%s,Message=%s"%(msg.topic,msg.value))
	time.sleep(1)

# Terminate the script
print("Exiting consumer...")
sys.exit()
