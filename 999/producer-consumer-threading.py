from kafka import KafkaConsumer
from kafka import KafkaProducer
import threading
import sys
import time
import json

  
def print_x(x, n): 
	for i in range(n):
		print(x)
		
		
def producer():
	print("Entered producer...")
	bootstrap_servers = ['localhost:9092']
	topicName = 'First_Topic'
	producer = KafkaProducer(bootstrap_servers = bootstrap_servers)
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
	print("Exiting producer...")


def consumer():
	print("Entered consumer...")
	bootstrap_servers = ['localhost:9092']
	topicName = 'First_Topic'
	consumer = KafkaConsumer (topicName, group_id ='group1',bootstrap_servers = bootstrap_servers)
	for msg in consumer:
		print("Topic Name=%s,Message=%s"%(msg.topic,msg.value))
		time.sleep(1)
	print("Exiting consumer...")

  
if __name__ == "__main__": 
	# create threads
	#t1 = threading.Thread(target=print_x, args=(1, 5,)) 
	#t2 = threading.Thread(target=print_x, args=(2, 10,)) 
	
	t1 = threading.Thread(target=producer) 
	t2 = threading.Thread(target=consumer) 
	
	# start thread 1 
	t1.start() 
	# start thread 2 
	t2.start() 
	
	# wait until thread 1 is completely executed 
	t1.join() 
	# wait until thread 2 is completely executed 
	t2.join() 
	# both threads completely executed 
	
	print("Done!") 
