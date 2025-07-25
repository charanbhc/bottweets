import os
import tweepy

# === Twitter API credentials from GitHub Secrets ===
api_key = os.getenv("API_KEY")
api_secret = os.getenv("API_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

# Authenticate with Twitter API
auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# === Tweet tracking setup ===
total_images = 1000
max_tweets = 5000
index_file = "current_index.txt"
images_folder = "random_images"  # Folder where all 1000 images are stored

# Ensure index file exists
if not os.path.exists(index_file):
    with open(index_file, "w") as f:
        f.write("0")

# Read current index
with open(index_file, "r") as f:
    index = int(f.read().strip())

# Stop after 5000 tweets
if index >= max_tweets:
    print("✅ 5000 tweets done. Exiting.")
    exit()

# Select image (loop after 1000)
image_number = (index % total_images) + 1
image_path = os.path.join(images_folder, f"image_{image_number}.png")

# === Tweet with image ===
status = "#SaveHHVMBuyers"
api.update_status_with_media(status=status, filename=image_path)

print(f"✅ Tweeted {index + 1}/{max_tweets} - {image_path}")

# Update index
with open(index_file, "w") as f:
    f.write(str(index + 1))
