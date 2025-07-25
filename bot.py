import os
import tweepy
import time
import random

# Use environment variables for safety
API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_SECRET = os.getenv("ACCESS_SECRET")

# Auth setup
auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

# Simple bot loop that tweets every 10 seconds
while True:
    tweet = f"Automated tweet: {random.randint(1000, 9999)}"
    api.update_status(tweet)
    print(f"Tweeted: {tweet}")
    time.sleep(10)
