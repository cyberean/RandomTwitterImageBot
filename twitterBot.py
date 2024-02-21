import tweepy
import os
import random
import io
import schedule
import time
from configs import client,api
from datetime import datetime, timedelta

api_key = "INPUT_HERE"
api_secret = "INPUT_HERE"
bearer_token = "INPUT_HERE"
access_token = "INPUT_HERE"
access_token_secret = "INPUT_HERE"

client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)
auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# Chooses a random image from your folder path
def tweet_action():
    folder_path = "YOUR_FOLDER_PATH_HERE"
    contents = os.listdir(folder_path)
    image_files = [
        file
        for file in contents
        if file.lower().endswith((".jpg", ".jpeg", ".png", ".gif"))
    ]
    random_image = random.choice(image_files)
    image_path = os.path.join(folder_path, random_image)

    with open(image_path, "rb") as file:
        image_content = file.read()
    image_io = io.BytesIO(image_content)
    media = api.media_upload(filename=random_image, file=image_io)
    client.create_tweet(text="#OnePiece", media_ids=[media.media_id])
# You don't need to have text of course, I created a One Piece themed twitter bot and used the One Piece hashtag for more visibility

# Change the value to however long you want it, I set it to 15 seconds to see if it worked.
schedule.every(15).seconds.do(tweet_action)

while True:
    schedule.run_pending()
    time.sleep(1)
