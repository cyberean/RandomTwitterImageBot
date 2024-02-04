import tweepy
import os
import random
import io
import schedule
import time
from configs import client,api
from datetime import datetime, timedelta

api_key = "3646rx2Lquwl38thRP8GtYAJi"
api_secret = "SUnDjChTNiQCaRW2gqdiht5qyZErB9sUi1O3msGoRBxpdLW4YC"
bearer_token = "AAAAAAAAAAAAAAAAAAAAAKXYsAEAAAAAvbb5KtudGnK79MPJEoQs9P7vf7Y%3DVWRJhLUNBBddJ2OU5yy3bhXFLviOQYA4OTLecU87bxNWr5J5tD"
access_token = "1753627689389330432-Gucbeu78AzluplU0RA5MQEvaLo0RhP"
access_token_secret = "H8PB049lhogVadWVsBSGl9D1IcDbL9zS3GfkhGEBiFf8C"

client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)
auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)
def tweet_action():
    folder_path = "C:\\Users\\abdul\\OneDrive\\Desktop\\onepiece"
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


schedule.every(15).seconds.do(tweet_action)

while True:
    schedule.run_pending()
    time.sleep(1)