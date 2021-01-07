#twitter-bot/bots/config.py
import tweepy
import logging
import os

#Environment variables
os.environ["CONSUMER_KEY"] = "2Afu2b2nX2urF5bGkI9Llh6m3"
os.environ["CONSUMER_SECRET"] = "CpjHP5dP84y7rNGEPuobA6RCzcCaFBFjBJZqhSGi5Jex51QBEV"
os.environ["ACCESS_TOKEN"] = "501130053-tdxTbNAvGzw8thzLqOFzLzhdFAJXSTowmAlq7NeJ"
os.environ["ACCESS_TOKEN_SECRET"] = "ecogAWzWL2MYNwTqQlPgXG1axMxtiKgYMXrYpj3zWK82V"

#Setting Logger
logger = logging.getLogger()

#Using environment variables to create the API
def create_api():
    consumer_key = os.getenv("CONSUMER_KEY")
    consumer_secret = os.getenv("CONSUMER_SECRET")
    access_token = os.getenv("ACCESS_TOKEN")
    access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True, 
        wait_on_rate_limit_notify=True)
    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
    logger.info("API created")
    return api