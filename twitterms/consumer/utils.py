from decouple import config

# Read from .env file.
TWITTER_BEARER_TOKEN = config('TWITTER_BEARER_TOKEN')

# Twitter API endpoint URL
TWITTER_API_ENDPOINT = 'https://api.twitter.com/2/'

# Twitter API resourceS
TWITTER_API_TWEETS = 'tweets/'
TWITTER_API_USERS = 'users/'

# Methods
def create_headers():
    headers = {"Authorization": "Bearer {}".format(TWITTER_BEARER_TOKEN)}
    return headers

def create_tweets_url():
    return TWITTER_API_ENDPOINT + TWITTER_API_TWEETS

def create_users_url():
    return TWITTER_API_ENDPOINT + TWITTER_API_USERS

