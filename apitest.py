#!/usr/bin/env python3
from requests_oauthlib import OAuth1Session
import json
import datetime, time, sys

with open('./secret.json') as f:
    keys = json.load(f)

sess = OAuth1Session(keys['consumer_key'], keys['consumer_secret'], \
                     keys['access_token'], keys['access_token_secret'])
url = 'https://api.twitter.com/1.1/followers/list.json'
res = sess.get(url, params={'screen_name':'machine105', 'count':20, 'skip_status':1, 'include_user_entities':'false'})

with open('apitest.json', 'w') as f:
    f.write(res.text)

res_text = json.loads(res.text)
for tweet in res_text['statuses']:
    print(tweet['id'])
    print(tweet['text'])

