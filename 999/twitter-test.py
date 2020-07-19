import tweepy


auth   = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api    = tweepy.API(auth)

status = "Testing!"
api.update_status(status=status)
