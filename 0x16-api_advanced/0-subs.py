#!/usr/bin/python3

""" import necessary modules"""
import json
import requests


def number_of_subscribers(subreddit):
    """returns the numbers of total subscribers on a subreddit"""
    
    url = 'https://www.reddit.com/r/{}/about/.json'.format(subreddit)
    headers = {'User-Agent': 'MyAPI/0.0.1'}
    res = requests.get(url, allow_redirects=False, headers=headers)
    if (res.status_code == 200):
        resp = json.loads(res.text)
        subscriber_count = resp['data']['subscribers']
        return subscriber_count
    else:
        return 0
