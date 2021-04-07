from . import tweet_consumer
import requests

from django.test import SimpleTestCase

class TestConsumeTweet(SimpleTestCase):
    def test_when_tweet_exists_return_tweet(self):
        tweet_id = '1374723260168953856'
        response = tweet_consumer.get_tweet(requests, tweet_id)

        print(response)

        assert response['data'] is not None
        assert response['data']['id'] == '1374723260168953856'


    def test_when_tweet_exists_return_error(self):
        tweet_id = '0'
        response = tweet_consumer.get_tweet(requests, tweet_id)

        print(response)

        assert response['errors'] is not None
        assert response['errors'][0]['title'] == 'Not Found Error'


class TestConsumeUserTweets(SimpleTestCase):
    def test_when_user_exists_return_timeline(self):
        user_id = '2244994945'
        response = tweet_consumer.get_user_timeline(requests, user_id)

        print(response)

        assert response['data'] is not None
        assert response['data'][0]['id'] is not None

    def test_when_user_exists_return_error(self):
        user_id = '0'
        response = tweet_consumer.get_user_timeline(requests, user_id)

        print(response)

        assert response['errors'] is not None
        assert response['errors'][0]['title'] == 'Not Found Error'