# John S, July 22, 2020
#
# FILE: "covid-19-kafka-producer.py"
# DESCRIPTION:
#   Uses covid-193 api from rapidapi.com to get periodic global COVID-19 statistics.
#
#   covid-193 api interface updates the data every 15 minutes.
#
#   rapidapi interface is invoked within the producer thread of kafka framework.
#
#   There is no Kafka consumer thread in this version since it expects Spark pySpark
#   consumer that is invoked separately in a separate program.
#

from kafka import KafkaProducer
from kafka import KafkaConsumer

import threading
import logging
import time
import json
import requests


topicName = 'corona-topic'
url       = "https://covid-193.p.rapidapi.com/statistics"

headers   = {
    'x-rapidapi-host': "covid-193.p.rapidapi.com",
    'x-rapidapi-key': "b7b5f2745dmshabc69c1dcba13f2p191da7jsnd98306ea16c5",
    "format":"json"
    }


class producer(threading.Thread):
    daemon = True
    def run(self):
        pObj = KafkaProducer(bootstrap_servers='localhost:9092',
                                 value_serializer=lambda v: json.dumps(v).encode('utf-8'))
        while True:
            #pObj.send(topicName, {"dataObjectID": "test1"})
            #pObj.send(topicName, {"dataObjectID": "test2"})
            response = requests.request("GET", url, headers=headers)
            jDict    = response.json()
            
            print("SENDING>>>")
            print(jDict)
            print("<<<")
            
            pObj.send(topicName, jDict)
            time.sleep(1)
 
            
class consumer(threading.Thread):
    daemon = True
    def run(self):
        cObj = KafkaConsumer(bootstrap_servers='localhost:9092',
                                 auto_offset_reset='earliest',
                                 value_deserializer=lambda m: json.loads(m.decode('utf-8')))
        cObj.subscribe([topicName])
        for message in cObj:
            print(">>>>>>>>>>>>>>>>>>>>> RAPIDAPI: COVID-19 DATA <<<<<<<<<<<<<<<<<<<<<") 
            print(message.value)
            print(">>>>>>>>>>>>>>>>>>>>>--------- END----------- <<<<<<<<<<<<<<<<<<<<<") 
            print("\n")

            
            
def main():
    producer().start()
#   consumer().start()
    time.sleep(10)
    
    
if __name__ == "__main__":
    logging.basicConfig(
        format='%(asctime)s.%(msecs)s:%(name)s:%(thread)d:' +
               '%(levelname)s:%(process)d:%(message)s',
        level=logging.INFO
    )
    main()
    
    
    
    
    
    
