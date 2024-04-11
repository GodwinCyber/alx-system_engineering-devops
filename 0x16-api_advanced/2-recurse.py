#!/usr/bin/python3
"""
Prints the titles of all hot articles
"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """Fetches and returns titles of all hot posts from a subreddit recursively
    using pagination
    Args:
        subreddit: The name of the subreddit to search (string).
        hot_list: An empty list to accumulate titles (list, optional).
        after: The value of the 'after' parameter for pagination
        (string, optional).
    Returns:
        A list containing titles of all hot posts or None if the
        subreddit is not found.
    """
    params = {"after": after}
    headers = {
        "User-agent": "python:subreddit.hot_article_fetcher.v1.0 \
        (by /u/HousingBorn8812)"
        }
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    response = requests.get(url, headers=headers, allow_redirects=False,
                            params=params)
    if response.status_code == 200:
        data = response.json()
        posts = data["data"]["children"]
        after = data["data"]["after"]
        if after is None:
            return hot_list
        else:
            hot_list.append(posts[0]["data"]["title"])
            return recurse(subreddit, hot_list, after)
    else:
        return None
