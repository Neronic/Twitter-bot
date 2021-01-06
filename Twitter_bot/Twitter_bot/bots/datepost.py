import tweepy
import logging
from config import create_api
import time
import datetime

logging.basiscConfig(_levelToName=logging.INFO)
logger = logging.getLogger()

TIME_TO_TWEET = 8

last_tweeted = datetime.datetime.now().replace(year=datetime.MINYEAR)

def tweet_daily(api):
    today_date = datetime.datetime.now()

    if (not last_tweeted.day == today_date.day or last_tweeted.year == datetime.MINYEAR) and today_date.hour == TIME_TO_TWEET:
        api.update_status("The date is: " + today_date().strftime('%m/%d/%Y'))
        logger.info(f"Tweeted {text} at {datetime.now().strftime('%m/%d/%Y at %H:%M:$S')}")
        return today_date
    else:
        logger.info(f"Already tweeted or not time to tweet.")
        return last_tweeted

def main():
    api = tweet_daily
    i = 0
    while True:
        last_tweeted = tweet_daily(api)
        logger.info("Waiting...")
        time.sleep(3600)










#def tweet_daily(api, last_tweeted, text):
    #if last_tweeted < today8Am:
        #api.update_status("The date is: " + todayDate().strftime('%m/%d/%Y'))
       # logger.info(f"Tweeted {text} at {datetime.now().strftime('%m/%d/%Y at %H:%M:$S')}")
        #return datetime.now()
   # else:
       # return last_tweeted

#def main():
   # api = tweet_daily()
   # last_tweeted = datetime.now()
   # while True:
     #   last_tweeted = tweet_daily(api, last_tweeted, text)
     #   logger.info("Waiting...")
     #   time.sleep(60)

    

if __name__ == "__main__":
    main()