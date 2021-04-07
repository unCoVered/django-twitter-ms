from .. import utils

def get_tweet(requests, tweet_id):
    return requests.get(utils.TWITTER_API_ENDPOINT + utils.TWITTER_API_TWEET + tweet_id)

def get_user_timeline(requests, user_id):
    return None
