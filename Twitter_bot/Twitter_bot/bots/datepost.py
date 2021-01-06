import tweepy
import logging
from config import create_api
import time
from datetime import datetime, timedelta

logging.basiscConfig(_levelToName=logging.INFO)
logger = logging.getLogger()

todayDate = datetime.now().replace(minute=0,second=0,microsecond=0)
today8Am = todayDate.replace(hour=8)

def tweet_daily(api, last_tweeted, text):
    if last_tweeted < today8Am:
        api.update_status("The date is: " + todayDate().strftime('%m/%d/%Y'))
        logger.info(f"Tweeted {text} at {datetime.now().strftime('%m/%d/%Y at %H:%M:$S')}")
        return datetime.now()
    else:
        return last_tweeted

def main():
    api = tweet_daily()
    last_tweeted = datetime.now()
    while True:
        last_tweeted = tweet_daily(api, last_tweeted, text)
        logger.info("Waiting...")
        time.sleep(60)

    

if __name__ == "__main__":
    main()