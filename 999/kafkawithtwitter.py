from tweepy.streaming import StreamListener
from tweepy           import OAuthHandler
from tweepy           import Stream
from kafka            import SimpleProducer, KafkaClient

keyword = "COVID"
portno  = "9092"

access_token        = ""
access_token_secret = "" 
consumer_key        = "" 
consumer_secret     = ""

class StdOutListener(StreamListener):
    def on_data(self, data):
        producer.send_messages(keyword, data.encode('utf-8'))
        print (data)
        return True
    def on_error(self, status):
        print (status)

kafka    = KafkaClient("localhost:"+portno)
producer = SimpleProducer(kafka)
l        = StdOutListener()


auth     = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)


stream   = Stream(auth, l)



stream.filter(track=keyword)
