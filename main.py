import tweepy
import tkinter
import os
from dotenv import load_dotenv
import requests
import json
from PIL import Image

load_dotenv()

consumer_key = os.getenv('consumer_key')
consumer_secret = os.getenv('consumer_secret')
access_token = os.getenv('access_token')
access_token_secret = os.getenv('access_token_secret')
bearer_token=os.getenv('bearer_token')

client = tweepy.Client(bearer_token=bearer_token,
                       consumer_key=consumer_key,
                       consumer_secret=consumer_secret,
                       access_token=access_token,
                       access_token_secret=access_token_secret,
                       wait_on_rate_limit=True)

posts = []
titles = []
medias = []

url = "https://www.reddit.com/r/memes/hot/.json"
r = requests.get(url, headers = {'User-agent': '1'}).json()

for i in r["data"]["children"]:
    if i["data"]["over_18"] == True:
        continue
    if i["data"]["is_video"] == True:
        continue
    post = i["data"]["permalink"]
    if post in posts:
        continue
    title = i["data"]["title"]
    imageLink = i["data"]["url"]
    filename = imageLink.split('/')[-1]
    r = requests.get(imageLink, allow_redirects=True)
    open(filename, 'wb').write(r.content)