# import the module 
#import tweepy 

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
  
# assign the values accordingly 


  
# authorization of consumer key and consumer secret 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
  
# set access to user's access key and access secret  
auth.set_access_token(access_token, access_token_secret) 
  
# calling the api  
api = tweepy.API(auth) 
  
# the text to be tweeted 
status = "This is a tweet."
  
# posting the tweet 
api.update_status(status) 

