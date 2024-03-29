import requests
import json
from PIL import Image

url = "https://www.reddit.com/r/memes/hot/.json"
r = requests.get(url).json()
print(requests.get(url,headers = {'User-agent': '1'}).json())