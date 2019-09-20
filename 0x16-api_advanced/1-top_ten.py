#!/usr/bin/python3


def top_ten(subreddit):
    import requests
    url = 'https://www.reddit.com/r/{}/new.json?sort=new'.format(subreddit)

    headers = {
        'User-Agent': 'My User Agent 1.0'
    }

    reditt = requests.get(url, headers=headers)

    if reditt.status_code != 200:
        print(None)
        return

    try:
        json = reditt.json()
        x = json.get('data').get('children')
        for i in x:
            print(i.get('data').get('title'))
    except Exception:
        pass
