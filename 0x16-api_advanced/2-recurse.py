#!/usr/bin/python3
"""Function to query a list of all hot posts on a given Reddit subreddit."""
import requests

def recurse(subreddit, hot_list=[], after=None):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'linux:0x16.api.advanced:v1.0.0'}
    params = {'limit': 100, 'after': after}
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        children = data['data']['children']
        for child in children:
            title = child['data']['title']
            hot_list.append(title)

        after = data['data']['after']
        if after:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    else:
        return None
