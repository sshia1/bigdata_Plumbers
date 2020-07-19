from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy ipmort Stream


class StdOutListener(StreamListener):
  def on data(self,data):
    print(data)
    return True
    
  def on_error(self,status):
    print(status)
    
if __name__=="__main__":
  listener = StdOutListener()
  
  
  
  auth = OAuthHandler(twitter_credentials.CONSUMER_KEY,twitter_credentials.CONSUMER_SECRET)
  auth.set access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)
  
  stream = Stream(auth, listener)
  
  stream.filter(track=['COVID-19'])
  
  
  
