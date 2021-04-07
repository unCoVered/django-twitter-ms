from . import tweet_consumer
import requests

from django.test import SimpleTestCase

class TestConsumeTweet(SimpleTestCase):
    def test_when_tweet_exists_return_tweet(self):
        tweet_id = '0'
        tweet = tweet_consumer.get_tweet(requests, tweet_id).json()

        print(tweet)

        assert tweet is not None