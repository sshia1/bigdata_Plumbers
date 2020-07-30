# this is a PySpark Python program which is designed to interface
# with Kafka producer running from another console
# independently
#
                                                                             

from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils

# choose a name for the app
sc = SparkContext(appName="PythonStreamingKafkaSpark")

# streaming window of 1 second
ssc = StreamingContext(sc, 1)


kvs = KafkaUtils.createStream(ssc, 'localhost:2181', 'spark-streaming-consumer', {'kafkaRapidAPISpark':1})


# print your stream
print("STREAM>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
kvs.pprint()


#parsed = kvs.map(lambda v: json.loads(v[1]))

#parsed = kvs.value;
#print(parsed)

#values = kvs.map(lambda entry: entry[1])
#print(values)
#values = kvs.map(lambda (k, v): json.loads(v))
#values=kvs.pprint()
#print("STREAM>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
#print(values)
print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")

ssc.start()
ssc.awaitTermination()                                                                     
 

