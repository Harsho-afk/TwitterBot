# TwitterBot

A Twitter bot written in Python that automates posting content on Twitter by fetching memes from Reddit. This project demonstrates how to authenticate with Twitter's API using Tweepy, retrieve content from Reddit, and post tweets with media attachments.

## Features

- **Twitter API Integration:** Authenticates with Twitter using API keys and tokens.
- **Reddit Meme Fetching:** Pulls the latest memes from the r/memes subreddit.
- **Media Upload:** Downloads meme images and uploads them as media with tweets.
- **Duplicate Prevention:** Checks a local log (`past_tweets.txt`) to avoid tweeting the same meme title more than once.
- **Scheduling:** Pauses between tweets to avoid spamming (configurable by modifying the sleep interval).

## Requirements

- **Python 3.6+**
- **Twitter Developer Account:** You must have valid Twitter API credentials.

## Setup

1. **Clone the repository:**
   
   ```
   git clone https://github.com/Harsho-afk/TwitterBot.git
   cd TwitterBot
   ```
2. **Configure Environment Variables:**
   
    Create a .env file in the root directory by copying the provided .env.template file:
    ```
    cp .env.template .env
    ```
    Open the .env file and set your Twitter API credentials.
3. **Install Dependencies:**
   
    Install the required Python packages using pip:
    ```
    pip install -r requirements.txt
    ```

## How It Works

- **Authentication:** The bot loads API credentials from the .env file and authenticates with Twitter using Tweepy.
- **Fetching Memes:** It retrieves the hot posts from the r/memes subreddit (excluding NSFW posts and videos) and downloads meme images.
- **Duplicate Check:** Before posting, it checks the past_tweets.txt file to avoid reposting previously tweeted memes.
- **Tweeting:** The bot uploads the image to Twitter and posts a tweet with the meme title and attached media.
- **Rate Limiting:** A sleep interval is implemented between tweets to space out the posts.

## Usage

Run the bot with:
```
python main.py
```
The bot will log into Twitter, fetch memes from Reddit, and post tweets automatically. Monitor the console output for status messages.
