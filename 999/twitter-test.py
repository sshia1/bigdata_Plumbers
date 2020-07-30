import tweepy

CONSUMER_KEY        = "wJsFsQw84oZPOYFBhm79tqxpn"
CONSUMER_SECRET     = "WBBswNrbiknyJHT3k3wbNiBQ0p1NIidUZ0pnQAHlZ9SI6lSd63"
ACCESS_TOKEN        = "1281254230268002306-wKACT10xkkpfz6tzBLviR2C2IZOM1V"
ACCESS_TOKEN_SECRET = "SboVyteQ7NiKw4JYWnhbdb3LdSKSaml21dxkgDCadUOr7"

auth   = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api    = tweepy.API(auth)

status = "Testing!"
api.update_status(status=status)
