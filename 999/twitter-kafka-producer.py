#
# twitter to kafka producer test script
#


from   kafka    import KafkaProducer
from   datetime import datetime
import tweepy
import sys
import re


TWEET_TOPICS = ['COVID-19']
KAFKA_BROKER = 'localhost:9092'
KAFKA_TOPIC = 'tweets'


class Streamer(tweepy.StreamListener):
	def on_error(self, status_code):
		if status_code == 402:
			return False
	
	
	def on_status(self, status):
		tweet	= status.text
		tweet	= re.sub(r'RT\s@\w*:\s', '', tweet)
		tweet	= re.sub(r'https?.*', '', tweet)
		global producer
		producer.send(KAFKA_TOPIC, bytes(tweet, encoding='utf-8'))
		print("TWEET>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
		print(tweet)
		print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
		d	= datetime.now()
		#print(f'[{d.hour}:{d.minute}.{d.second}] sending tweet')
		print("...sent tweet!")



# put your API keys here


auth		= tweepy.OAuthHandler(consumer_key, consumer_secret_key)
auth.set_access_token(access_token, access_token_secret)
api		= tweepy.API(auth)
streamer	= Streamer()
stream		= tweepy.Stream(auth=api.auth, listener=streamer)


try:
	producer = KafkaProducer(bootstrap_servers=KAFKA_BROKER)
except Exception as e:
	#print(f'Error Connecting to Kafka --> {e}')
	print("Error connecting to Kafka!")
	sys.exit(0)
	sys.exit(1)


stream.filter(track=TWEET_TOPICS)



