#
# this is a PySpark Python program which is designed to interface
# with Kafka producer running from another console
# independently
#
# data is received from Kafka producer which uses PySpark session as 
# a bridge to connect to Hive and write to it.
#
# Data is sent one record at a time which is appended to the database table.
#
# Lacks logic to handle to continually go to new Hive tables to avoid
# duplicate keys.
#
# POC only.
#
                                                                             

from pyspark.streaming.kafka	import KafkaUtils
from pyspark.streaming		import StreamingContext
from pyspark			import SparkContext
from pyspark.sql		import SparkSession
from pyspark			import sql
from pyspark.sql		import SQLContext
import				json
from pyspark.sql.types		import ArrayType, StructField, StructType, StringType, IntegerType
from pyspark.sql		import Row
import				pyspark.sql.types	as	st
from collections 		import	namedtuple



sc = SparkContext(appName="PythonStreamingKafkaSparkHive")



ssc = StreamingContext(sc, 1) # old style Spark code instead of SparkSession



kvs = KafkaUtils.createStream(ssc, 'localhost:2181', 'spark-streaming-consumer', {'kafkaRapidAPISpark':1})



result1 = kvs.map(lambda x: x[1]) # get rid of junk at x[0] due to kafka



result2=result1.map(lambda rec: json.loads(rec.decode('utf-8'))) # deserialize or go from byte stream to list of dictionaries



#def convert2tuple(rec): # lambda function to convert to namedtuple for schema
#	final_list=[]
#	for entry in rec:
#		namedTupleObj=dataTuple(**entry)
#		final_list.append(namedTupleObj)
#	return(final_list)


def diag(rec):
	dataTuple=namedtuple('schema', ['country','continent','population','cases','deaths','tests'])
	return(dataTuple(rec['country'], rec['continent'], rec['population'], rec['cases'], rec['deaths'], rec['tests']))


result3=result2.map(lambda rec: diag(rec))

          
                                                                                           
ss = SparkSession.builder.appName("covid2hive").config("spark.sql.warehouse.dir", "/user/hive/warehouse/").config("hive.metastore.uris", "thrift://localhost:9083").enableHiveSupport().getOrCreate()   



def handle_rdd(rdd):                                                                                                    
	if not rdd.isEmpty():                                                                                               
		global ss
		
		# do tuple format conversion much earlier, outside this routine using lambda function
		
		df=ss.createDataFrame(rdd)
		 
		# print("AFTER CREATE-DATA-FRAME!!!!!!!!!!!!!!!!!!!!!!!!!")   
		                                
		print(">>>>BEFORE HIVE TABLE SAVE ************************************************************")
		df.show()                                                                              
		print("******************************************************************************<<<<<<<<<")    
		
		                     
		df.write.saveAsTable(name='default.covid19', format='hive', mode='append')                  

                                                           
                                                                             
ss.sparkContext.setLogLevel('WARN') 
                                

                                
result3.foreachRDD(handle_rdd) 



ssc.start()
ssc.awaitTermination()                                                                     



