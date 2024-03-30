import tweepy
import tkinter
import os
from dotenv import load_dotenv
import requests
from PIL import Image
import time
import shutil

if not os.path.exists(".env"):
    print(".env fils does not exist. Create it with your twitter credentials.")
    exit()

load_dotenv()

consumer_key = os.getenv('consumer_key')
consumer_secret = os.getenv('consumer_secret')
access_token = os.getenv('access_token')
access_token_secret = os.getenv('access_token_secret')
bearer_token=os.getenv('bearer_token')
posts = []
titles = []
medias = []
file_limit = 5242880

if not os.path.exists("past_tweets.txt"):
    open("past_tweets.txt",'w')
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
    title = i["data"]["title"]
    file = open("past_tweets.txt")
    l = file.readlines()
    if title+"\n" in l:
        file.close()
        continue
    file.close()
    imageLink = i["data"]["url"]
    filename = "Images/"
    filename+=(imageLink.split('/')[-1])
    r = requests.get(imageLink, allow_redirects=True)
    try:
        open(filename, 'wb').write(r.content)
        if os.path.getsize(filename=filename) > file_limit:
            os.remove(filename)
            continue
        posts.append(post)
        titles.append(title)
        medias.append(filename)
    except Exception as error:
        print("ERROR")
        print(error)
        exit()
    j+=1

print("Got all the memes")

def getAPI(consumer_key, consumer_secret, access_token, access_token_secret) -> tweepy.API:
    auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret)
    auth.set_access_token(
        access_token,
        access_token_secret,
    )
    return tweepy.API(auth)

def getClient(consumer_key, consumer_secret, access_token, access_token_secret) -> tweepy.Client:
    client = tweepy.Client(
        consumer_key=consumer_key,
        consumer_secret=consumer_secret,
        access_token=access_token,
        access_token_secret=access_token_secret,
    )

    return client

try:
    api = getAPI(consumer_key, consumer_secret, access_token, access_token_secret)
    client = getClient(consumer_key, consumer_secret, access_token, access_token_secret)
    userName = ""
    print("Logged in to {}".format(api.verify_credentials().name))
    userName = api.verify_credentials().screen_name
except Exception as error:
    print("AUTH ERROR")
    print(error)
    exit()

for i in range(len(posts)):
    try:
        media_path = medias[i]
        media = api.media_upload(filename=media_path,chunked=True)
        media_id = media.media_id
        client.create_tweet(text=titles[i],media_ids=[media_id])
        print("{}. Tweeted successfully".format(i+1))
        with open('past_tweets.txt','a') as file:
            file.write("{}\n".format(titles[i]))
        time.sleep(8640)
    except Exception as error:
        print("ERROR TWEETING")
        print(error)
        exit()