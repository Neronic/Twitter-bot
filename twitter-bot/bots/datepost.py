import tweepy
import logging
from config import create_api
import time
import datetime

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

TIME_TO_TWEET = 9

last_tweeted = datetime.datetime.now().replace(year=datetime.MINYEAR)
wednesday_tweet = "It's Wednesday my dudes"

def tweet_daily(api):
    today_date = datetime.datetime.now()

    if (not last_tweeted.day == today_date.day or last_tweeted.year == datetime.MINYEAR) and today_date.hour == TIME_TO_TWEET:
        if (today_date.weekday() == 2):
            api.update_status("The date is: " + today_date.strftime('%A, %B the %d, %Y') + "\nIt's Wednesday my dudes")
            logger.info(f"Tweeted at {datetime.datetime.now().strftime('%m/%d/%Y at %H:%M:%S')}")
        else:
            api.update_status("The date is: " + today_date.strftime('%A, %B the %d, %Y'))
            logger.info(f"Tweeted at {datetime.datetime.now().strftime('%m/%d/%Y at %H:%M:%S')}")

        return today_date
    else:
        logger.info(f"Already tweeted or not time to tweet.")
        return last_tweeted

def main():
    api = create_api()
    while True:
        last_tweeted = tweet_daily(api)
        logger.info("Waiting...")
        time.sleep(3600)

if __name__ == "__main__":
    main()



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

    

