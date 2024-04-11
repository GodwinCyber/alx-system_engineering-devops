#!/usr/bin/python3
"""
Prints the titles of the first 10 hot posts
"""
import requests


def top_ten(subreddit):
    """Fetches and prints titles of the top 10 hot posts from a subreddit.
    Args:
        subreddit: The name of the subreddit to search (string).
    Returns:
        None if the subreddit is not found or an error occurs.
    """
    params = {"limit": 10}
    headers = {
        "User-agent": "python:subreddit.subscriber.counter:v1.0 \
        (by /u/HousingBorn8812)"
        }
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    response = requests.get(url, headers=headers,
                            allow_redirects=False, params=params)
    if response.status_code == 200:
        data = response.json()
        posts = data["data"]["children"]
        if data["data"]["dist"] == 0:
            print(None)
        else:
            for post in posts:
                print(post["data"]["title"])
    else:
        print(None)
