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
  
  CONSUMER_KEY        = "wJsFsQw84oZPOYFBhm79tqxpn"
  CONSUMER_SECRET     = "WBBswNrbiknyJHT3k3wbNiBQ0p1NIidUZ0pnQAHlZ9SI6lSd63"
  ACCESS_TOKEN        = "1281254230268002306-wKACT10xkkpfz6tzBLviR2C2IZOM1V"
  ACCESS_TOKEN_SECRET = "SboVyteQ7NiKw4JYWnhbdb3LdSKSaml21dxkgDCadUOr7"
  
  auth = OAuthHandler(twitter_credentials.CONSUMER_KEY,twitter_credentials.CONSUMER_SECRET)
  auth.set access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)
  
  stream = Stream(auth, listener)
  
  stream.filter(track=['COVID-19'])
  
  
  
