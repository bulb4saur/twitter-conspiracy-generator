import os
import re

import tweepy
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv(".env")

# Get Twitter API keys and tokens from environment variables
API_KEY = os.getenv("TWITTER_API_KEY")
API_SECRET_KEY = os.getenv("TWITTER_API_KEY_SECRET")
ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

# Setup our client
client = tweepy.Client(
    consumer_key=API_KEY,
    consumer_secret=API_SECRET_KEY,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET,
)


def split_text_into_chunks(text, chunk_size=250):
    """Split text into chunks of specified size, ensuring sentences are not split."""

    # Split text into sentences
    sentences = re.split(r"(?<=[.!?]) +", text)
    chunks = []
    chunk = ""

    for sentence in sentences:
        if len(chunk) + len(sentence) + 1 <= chunk_size:
            if chunk:
                chunk += " " + sentence
            else:
                chunk = sentence
        else:
            chunks.append(chunk)
            chunk = sentence

    if chunk:
        chunks.append(chunk)

    return chunks


def post_conspiracy_theory(theory_text):
    try:
        chunks = split_text_into_chunks(theory_text)

        # Post the first chunk as the initial tweet
        response = client.create_tweet(text=chunks[0])
        print("First tweet posted successfully!", response)

        # Post the remaining chunks as replies to the first tweet
        tweet_id = response.data["id"]
        for chunk in chunks[1:]:
            response = client.create_tweet(
                text=chunk,
                in_reply_to_tweet_id=tweet_id,
            )
            tweet_id = response.data["id"]
            print("Reply tweet posted successfully!", response)

    except tweepy.TweepyException as e:
        print(f"Error: {e}")
