#!/usr/bin/python3
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
        "User-Agent": "python:subreddit.subscriber.counter:v1.0 \
        (by /u/HousingBorn8812)"
        }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        posts = data.get("data", {}).get("children", [])
        if not posts:
            print(None)
        for post in posts:
            print(post.get("data", {}).get("title"))
    else:
        print(None)
