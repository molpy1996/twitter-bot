import tweepy
import logging
from dotenv import load_dotenv
import os

load_dotenv()

logger = logging.getLogger()

# uses .txt file that store the 4 keys and read it.
# api_keys = open("D:\\Loisirs\\python\\twitter-bot\\src\\api_keys.txt", "r")
# #put each line of the .txt file in the corresponding variable
# CONSUMER_KEY=api_keys.readline().rstrip()
# CONSUMER_SECRET=api_keys.readline().rstrip()
# ACCESS_TOKEN=api_keys.readline().rstrip()
# ACCESS_TOKEN_SECRET=api_keys.readline().rstrip()
#
# api_keys.close()

def createAPI():
    consumer_key = os.getenv("CONSUMER_KEY")
    consumer_secret = os.getenv("CONSUMER_SECRET")
    access_token = os.getenv("ACCESS_TOKEN")
    access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

    # Authenticate to Twitter
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    # Create API object
    api = tweepy.API(auth)

    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
    logger.info("API created")
    return api
