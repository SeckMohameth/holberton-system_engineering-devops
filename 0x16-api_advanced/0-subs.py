#!/usr/bin/python3


def number_of_subscribers(subreddit):
    import requests
    url = 'https://www.reddit.com/r/{}/new.json?sort=new'.format(subreddit)

    headers = {
        'User-Agent': 'My User Agent 1.0'
    }
    try:
        reditt = requests.get(url, headers=headers)
        json = reditt.json()
        return json.get('data').get('children')[0].get('data').get(
            'subreddit_subscribers')
    except Exception:
        pass
    return 0
