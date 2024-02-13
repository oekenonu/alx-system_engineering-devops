#!/usr/bin/python3
"""Module to get reddit top 10 subscribers"""
import requests


def top_ten(subreddit):
    """Queries the Reddit API and returns the top ten
    number of subscribers for a given subreddit"""

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    header = {"User-Agent": "Anything_1.0"}
    data = requests.get(url, headers=header, allow_redirects=False)

    if data.status_code >= 300:
        print ('None')
    else:
        [print(child.get("data").get("title"))
         for child in data.json().get("data").get("children")]
