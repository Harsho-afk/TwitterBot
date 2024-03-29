import tweepy
import tkinter
import os
from dotenv import load_dotenv
import requests
from PIL import Image
import time
import shutil

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

if os.path.exists("Images"):
    shutil.rmtree("Images")
os.makedirs("Images")

url = "https://www.reddit.com/r/memes/hot/.json"
r = requests.get(url, headers = {'User-agent': '1'}).json()

try:
    print('Message = {} and Error = {}'.format(r['message'],r['error']))
except:
    pass

limit = 10
j = 0
for i in r["data"]["children"]:
    if j >= limit:
        break
    if i["data"]["over_18"] == True:
        continue
    if i["data"]["is_video"] == True:
        continue
    post = i["data"]["permalink"]
    if post in posts:
        continue
    posts.append(post)
    title = i["data"]["title"]
    titles.append(title)
    imageLink = i["data"]["url"]
    filename = "Images/"
    filename+=(imageLink.split('/')[-1])
    r = requests.get(imageLink, allow_redirects=True)
    try:
        open(filename, 'wb').write(r.content)
        medias.append(filename)
    except:
        print("ERROR")
        exit()
    j+=1
    
DIR = 'Images'
while(len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])!=10):
    time.sleep(1)

