

import os
import tweepy
from secretdressup import *
from time import gmtime, strftime


# ====== Individual bot configuration ==========================
bot_username = 'dressuptweet'
logfile_name = bot_username + ".log"

# ==============================================================





def create_tweet():
    """Create the text of the tweet you want to send."""
    # Replace this with your code!
    text = "look out for my latest fashion trend, you can't afford to miss it"
    return text

def tweet(text):
    """Send out the text as a tweet."""
    # Twitter authentication
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    api = tweepy.API(auth)

    # Send the tweet and log success or failure
    try:
        api.update_status(text)
    except tweepy.error.TweepError as e:
        log(e.message)
    else:
        log("Tweeted: " + text)



def log(message):
    """Log message to logfile."""
    path = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    with open(os.path.join(path, logfile_name), 'a+') as f:
        t = strftime("%d %b %Y %H:%M:%S", gmtime())
        f.write("\n" + t + " " + message)


if __name__ == "__main__":
    tweet_text = create_tweet()
    tweet(tweet_text)