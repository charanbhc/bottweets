import os
import tweepy

# Twitter credentials (use environment variables for security)
api_key = os.getenv("API_KEY")
api_secret = os.getenv("API_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

# Authenticate with Twitter
auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# === TWEET TRACKING LOGIC ===

# Total images and tweet cap
total_images = 1000
max_tweets = 5000

# Read index
with open("current_index.txt", "r") as f:
    index = int(f.read().strip())

# Stop after 5000 tweets
if index >= max_tweets:
    print("✅ 5000 tweets done. Exiting.")
    exit()

# Pick image to tweet
image_number = (index % total_images) + 1
image_path = f"images/image_{image_number}.png"  # Adjust if images in 'images/' folder

# Tweet with image
status = "#SaveHHVMBuyers"
api.update_status_with_media(status=status, filename=image_path)

print(f"Tweeted {index+1}/5000 - {image_path}")

# Increment index
with open("current_index.txt", "w") as f:
    f.write(str(index + 1))
