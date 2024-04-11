#!/usr/bin/python3
"""
Prints number_of_subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers for a given subreddit"""
    headers = {
        'User-Agent': 'python:subreddit.subscriber.counter:v1.0 \
        (by /u/HousingBorn8812)'
        }
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    res = requests.get(url, headers=headers, allow_redirects=False)
    if res.status_code == 200:
        data = res.json()
        return data['data']['subscribers']
    return
