# Import KafkaProducer from Kafka library
from kafka import KafkaProducer
import time

# Define server with port
bootstrap_servers = ['localhost:9092']

# Define topic name where the message will publish
topicName = 'First_Topic'

# Initialize producer variable
producer = KafkaProducer(bootstrap_servers = bootstrap_servers)

# Publish text in defined topic

producer.send(topicName, b'Hello from kafka...1')
time.sleep(1)
producer.send(topicName, b'Hello from kafka...2')
time.sleep(1)
producer.send(topicName, b'Hello from kafka...3')
time.sleep(1)
producer.send(topicName, b'Hello from kafka...4')
time.sleep(1)
producer.send(topicName, b'Hello from kafka...5')
time.sleep(1)
producer.send(topicName, b'Hello from kafka...6')
time.sleep(1)
producer.send(topicName, b'Hello from kafka...7')
time.sleep(1)
producer.send(topicName, b'Hello from kafka...8')
time.sleep(1)
producer.send(topicName, b'Hello from kafka...9')
time.sleep(1)
producer.send(topicName, b'Hello from kafka...10')
time.sleep(1)


# Print message
print("Exiting producer...")


