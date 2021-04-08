from . import user_consumer
import requests

from django.test import SimpleTestCase

class TestConsumeUser(SimpleTestCase):
    def test_when_tweet_exists_return_tweet(self):
        user_id = '2244994945'
        response = user_consumer.get_user(requests, user_id)

        print(response)

        assert response['data'] is not None
        assert response['data']['id'] == '2244994945'


    def test_when_tweet_exists_return_error(self):
        user_id = '0'
        response = user_consumer.get_user(requests, user_id)

        print(response)

        assert response['errors'] is not None
        assert response['errors'][0]['title'] == 'Not Found Error'