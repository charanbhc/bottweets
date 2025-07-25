import os
import tweepy
from sentences import sentences

# Auth keys from GitHub Secrets
api_key = os.getenv("API_KEY")
api_secret = os.getenv("API_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

# Authenticate with Twitter
auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# Track progress
index_file = "tweet_index.txt"

# Read index
if os.path.exists(index_file):
    with open(index_file, "r") as f:
        index = int(f.read().strip())
else:
    index = 0

# Stop after 5000
if index >= 5000:
    print("✅ Done with 5000 tweets.")
    exit()

# Compose tweet
text = f"#SaveHHVMBuyers {sentences[index]}"
api.update_status(text)

# Save next index
with open(index_file, "w") as f:
    f.write(str(index + 1))

print(f"Tweeted: {text}")
