# this is a PySpark Python program which is designed to interface
# with Kafka producer running from another console
# independently
#

#import sys
#import time
#from kafka                   import KafkaConsumer
#from pyspark.streaming.kafka import KafkaUtils
#from pyspark.streaming       import StreamingContext
#from pyspark                 import SparkContext                                                                                        
#from pyspark.sql             import SparkSession                                                                                    

from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils

# choose a name for the app
sc = SparkContext(appName="PythonStreamingKafkaSpark")

# streaming window of 1 second
ssc = StreamingContext(sc, 1)

# creating the strean:
# Documentation: http://spark.apache.org/docs/2.1.0/api/python/pyspark.streaming.html#pyspark.streaming.kafka.KafkaUtils
#   - StreamingContext
#   - Zookeeper quorum (hostname:port)
#   - The group id for this consumer
#   - {topic_name -> numPartitions} 

kvs = KafkaUtils.createStream(ssc, 'localhost:2181', 'spark-streaming-consumer', {'kafkaRapidAPISpark':1})

# print your stream
print("STREAM>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
kvs.pprint()
print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")

ssc.start()
ssc.awaitTermination()                                                                     
                         
                         
                         
                                                                                                
#ss.sparkContext.setLogLevel('WARN')                                                                                     
#ks = KafkaUtils.createDirectStream(ssc, ['tweets'], {'metadata.broker.list': 'localhost:9099'})                       
#lines = ks.map(lambda x: x[1])                                                                                          
#transform = lines.map(lambda tweet: (tweet, int(len(tweet.split())), int(len(tweet))))                                  
#transform.foreachRDD(handle_rdd)                                                                                        
#ssc.start()                                                                                                             
#ssc.awaitTermination()
#
#
#
#sc = SparkContext(appName="KafkaConsumer")
#str_c = StreamingContext(sc, 5)
#
#
#
#
#bootstrap_servers = ['localhost:9092'] # Define server with port
#topicName         = 'First_Topic'      # Define topic name from where the message will recieve
#consumer          = KafkaConsumer (topicName, group_id ='group1',bootstrap_servers = bootstrap_servers) # Initialize consumer variable
#
# Read and print message from consumer
#for msg in consumer:
#	print("Topic Name=%s,Message=%s"%(msg.topic,msg.value))
#	time.sleep(1)
#
# Terminate the script
#print("Exiting consumer...")
#sys.exit()



