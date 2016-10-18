# Used to interface with the twitter API
import tweepy
import csv
import re
from textblob import TextBlob

consumer_key = ""
consumer_secret = ""
access_key = ""
access_secret = ""

def get_all_tweets(screen_name):
    # This array consists of every single tweet(the last 3024) by Donald Trump
    all_tweets = []
    # New tweets array will be blank when the limit of the last 3024 tweets is achieved
    new_tweets = []

    # We authorize tweepy to ensure the calls are properly authenticated to the correct account.
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    client = tweepy.API(auth)
    new_tweets = client.user_timeline(screen_name=screen_name, count = 200)

    while len(new_tweets) > 0:
        for tweet in new_tweets:
            # Donald Trump Tweets from his Android phone.
            if tweet.source == 'Twitter for Android':
                all_tweets.append(tweet.text.encode("utf-8"))
                print(tweet.text)
                analysis = TextBlob(tweet.text)
                print(analysis.sentiment)


        print("Retrieved %s tweets so far" %(len(all_tweets)))
        # Saving the id of the oldest tweet received - 1
        max_id = new_tweets[-1].id - 1
        new_tweets = client.user_timeline(screen_name = screen_name, count=200, max_id=max_id)

    return all_tweets

# Using regex to clean up all the fluff in the tweet that includes links, hashtags, mentions, retweets, videos, newlines, whitespace, extrawhitespace and encoded white space.
def clean_tweet(tweet):
    tweet = re.sub("https?\:\/\/", "", tweet)   #links
    tweet = re.sub("#\S+", "", tweet)           #hashtags
    tweet = re.sub("\.?@", "", tweet)           #at mentions
    tweet = re.sub("RT.+", "", tweet)           #Retweets
    tweet = re.sub("Video\:", "", tweet)        #Videos
    tweet = re.sub("\n", "", tweet)             #new lines
    tweet = re.sub("^\.\s.", "", tweet)         #leading whitespace
    tweet = re.sub("\s+", " ", tweet)           #extra whitespace
    tweet = re.sub("&amp;", "and", tweet)       #encoded ampersands
    return tweet

def add_tweets_to_csv(tweets):
    with open('trumptweets.csv', 'wb') as f:
        writer = csv.writer(f)
        for tweet in tweets:
            tweet = clean_tweet(tweet)
            if tweet:
                writer.writerow([tweet])

# Need to understand this
if __name__ == "__main__":
    tweets = get_all_tweets("realdonaldtrump")
    add_tweets_to_csv(tweets)
