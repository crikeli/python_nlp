import tweepy
from textblob import TextBlob

consumer_key = "qc3xNBhXKoeuaNyOdr1FDWwzZ"
consumer_secret = "HW6z7h9DYFFJZmZTrQfcGkMONa5k5X1HYmE2Qv0JuOgCIBXRBg"
access_key = "4900371912-CPNC1CIg0uDKylFEPClYJqw7fKLqoyfZ2MczCjl"
access_secret = "7n8dkQi3NBtJFm4bEgo5sftaNFv5IRkts1R7gpjV2UbOT"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)

api = tweepy.API(auth)

public_tweets = api.search('melania')

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
