#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API for the number of subscribers for a given subreddit.
    If the subreddit is invalid, returns 0.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "python:reddit.subscriber.counter:v1.0 \
        (by HousingBorn8812)"
        }

    response = requests.get(url, headers=headers, allow_redirects=False)
    try:
        return response.json().get('data').get('subscribers')
    except Exception:
        return 0
