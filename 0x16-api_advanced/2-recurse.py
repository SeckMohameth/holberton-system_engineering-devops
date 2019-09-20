#!/usr/bin/python3
import requests

def recurse(subreddit, hot_list=[], after=''):
    url = 'https://www.reddit.com/r/{}/hot.json?after={}'.format(
        subreddit, after)

    headers = {'user-agent': 'nick'}

    reditt = requests.get(url, headers=headers)

    if reditt.status_code != 200:
        return

    json = reditt.json()
    x = json.get('data').get('children')
    for i in x:
        hot_list.append(i.get('data').get('title'))


    after = json.get('data').get('after')
    if after is None:
        return hot_list
    else:
        return recurse(subreddit, hot_list, after)
