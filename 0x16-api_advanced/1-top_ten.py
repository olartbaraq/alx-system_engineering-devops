#!/usr/bin/python3

""" import necessary modules"""
import json
import requests


def top_ten(subreddit):
    """list top 10 hot posts"""

    url = 'https://www.reddit.com/r/' + subreddit + '/hot.json?limit=10'
    headers = {'User-Agent': 'MyAPI/0.0.1'}
    res = requests.get(url, allow_redirects=False, headers=headers)

    if (res.status_code == 200):
        res_json = res.json()
        for post in res_json['data']['children']:
            print(post['data']['title'])
    else:
        print(None)
