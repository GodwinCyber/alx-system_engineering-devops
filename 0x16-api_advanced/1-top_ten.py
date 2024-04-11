#!/usr/bin/python3
"""Function to print hot posts on a given Reddit subreddit."""
import requests


def top_ten(subreddit):
    """Fetches and prints titles of the top 10 hot posts from a subreddit.
    Args:
        subreddit: The name of the subreddit to search (string).
    Returns:
        None if the subreddit is not found or an error occurs.
     """
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "python:subreddit.subscriber.counter:v1.0 \
        (by /u/HousingBorn8812)"
    }
    params = {
        "limit": 10
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        print("None")
        return
    results = response.json().get("data")
    [print(c.get("data").get("title")) for c in results.get("children")]
