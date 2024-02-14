#!/usr/bin/python3
"""Module to get reddit top 10 subscribers"""
import requests


def recurse(subreddit, hot_list=[], count=0, after=None):
    """Queries the Reddit API and returns the top ten
    number of subscribers for a given subreddit"""

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    header = {"User-Agent": "Anything_1.0"}
    params = {"count": count, "after": after}
    data = requests.get(url, headers=header,
                        params=params, allow_redirects=False)

    if data.status_code >= 400:
        return None

    hot_list = hot_list + [(child.get("data").get("title"))
                           for child in data.json().get("data")
                           .get("children")]

    info = data.json()
    if not info.get("data").get("after"):
        return hot_list

    return recurse(subreddit, hot_list, info.get("data").get("count"),
                   info.get("data").get("after"))
