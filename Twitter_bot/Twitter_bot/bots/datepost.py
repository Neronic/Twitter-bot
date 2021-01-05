import tweepy
import logging
from config import create_api
import time
from datetime import datetime, timedelta

logging.basiscConfig(_levelToName=logging.INFO)
logger = logging.getLogger()

def tweet_daily(api, last_tweeted, text):
    if last_tweeted < datetime.now()-timedelta(hours=24):
        api.update_status("The date is: ")
        logger.info(f"Tweeted {text} at {datetime.now().strftime('%m/%d/%Y at %H:%M:$S')}")
        return datetime.now()
    else:
        return last_tweeted