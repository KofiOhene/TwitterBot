import tweepy
import datetime
import time

# Twitter API credentials
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

# Authenticate with Twitter
client = tweepy.Client(
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token=access_token,
    access_token_secret=access_token_secret
)


# Function to schedule a tweet
def schedule_tweet(tweet_content, scheduled_time):
    while True:
        current_time = datetime.datetime.now()
        if current_time >= scheduled_time:
            client.create_tweet(text=tweet)
            break
        time.sleep(1)  # Check every minute


# Example: Schedule a tweet for a specific time
tweet = "Good morning world (sent from python automation script)!"
scheduled_time = datetime.datetime(2024, 1, 7, 8, 4, 00)  # YYYY, MM, DD, HH, MM, SS
schedule_tweet(tweet, scheduled_time)
