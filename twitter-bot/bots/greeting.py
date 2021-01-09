import tweepy
import logging
from config import create_api
import time
import datetime

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

greetingKeywords = ["hello", "hey there", "hey", "hi", "hai", "hei",
                    "yo", "aye", "ay",
                    "what's up", "whats up", "what up", "sup",
                     "holla", "hola", "holler",
                     "good morning", "good-morning", "goodmorning", "gm", "morning", "mornin",
                     "good evening", "good-evening", "goodevening", "evening", "evenin'", "evenin",
                     "good afternoon", "good-afternoon", "goodafternoon", "afternoon"
                      "good night", "goodnight", "good-night", "gnight", "night", "nite", "gn"]

#questions = [""]

def greetings(api, keywords, since_id):
    today_date = datetime.datetime.now().strftime("%A")
    logger.info("Retrieving mentions")
    new_since_id = since_id
    for tweet in tweepy.Cursor(api.mentions_timeline,
        since_id=since_id).items():
        new_since_id = max(tweet.id, new_since_id)
        if tweet.in_reply_to_status_id is not None:
            continue
        try:
            if any(keyword in tweet.text.lower() for keyword in keywords) and not tweet.favorited:
                logger.info(f"Saying hello to {tweet.user.name}")

                if not tweet.user.following:
                    tweet.user.follow()
                if not tweet.favorited:
                    try:
                        tweet.favorite()
                    except Exception as e:
                        logger.error("Error on fav", exc_info=True)
                api.update_status( "@" + tweet.user.screen_name + " Happy "+ today_date+ "!", in_reply_to_status_id=tweet.id)
            elif(tweet.favorited):
                logger.info(f"Tweet is duplicate, skipped.")
        except Exception:
            logger.info(f"Tweet is duplicate, skipped.")
    return new_since_id

def main():
    api = create_api()
    since_id = 1
    while True:
        since_id = greetings(api, greetingKeywords, since_id)
        logger.info("Waiting...")
        time.sleep(60)

if __name__ == "__main__":
    main()