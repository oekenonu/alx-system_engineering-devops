#!/usr/bin/python3
"""Module to get reddit subscribers count"""
import requests


def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers
    for a given subreddit"""

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    header = {"User-Agent": "Anything_1.0"}
    data = requests.get(url, headers=header, allow_redirects=False)

    if data.status_code >= 300:
        return 0

    return data.json().get("data").get("subscribers")
