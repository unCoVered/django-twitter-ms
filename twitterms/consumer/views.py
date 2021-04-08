from django.shortcuts import render, get_object_or_404
from .tweets import tweet_consumer
from .users import user_consumer


def tweet(request, tweet_id):
    response = tweet_consumer.get_tweet(tweet_id)

    return render(request, response.json())


def user_timeline(request, user_id):
    response = tweet_consumer.get_user_timeline(user_id)

    return render(request, response.json())


def user(request, user_id):
    response = user_consumer.get_user(user_id)

    return render(request, response.json())