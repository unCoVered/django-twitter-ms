from . import tweet_consumer
import requests

from django.test import SimpleTestCase

class TestConsumeTweet(SimpleTestCase):
    def test_when_tweet_exists_return_tweet(self):
        tweet_id = '1374723260168953856'
        tweet = tweet_consumer.get_tweet(requests, tweet_id)

        print(tweet)

        assert tweet is not None


    def test_when_tweet_exists_return_error(self):
        None


class TestConsumeUserTweets(SimpleTestCase):
    def test_when_user_exists_return_timeline(self):
        return None