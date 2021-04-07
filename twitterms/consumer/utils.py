from decouple import config

# Read from .env file.
TWITTER_API_KEY = config('TWITTER_API_KEY')
TWITTER_API_SECRET = config('TWITTER_API_SECRET')


# Twitter API endpoint URL
TWITTER_API_ENDPOINT = 'https://api.twitter.com/2/'

# Twitter API tweets resource
TWITTER_API_TWEET = 'tweets/'