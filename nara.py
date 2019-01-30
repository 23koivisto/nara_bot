#!/usr/bin/python3
import tweepy
import requests
import json
from datetime import date, timedelta

page_size = 20
start_record = 1
ts = date.today() - timedelta(1)
'''
params queries based on search criteria documented at https://www.federalregister.gov/developers/api/v1
'''
params = {"per_page":"20",
          "order":"relevance",
          "conditions[publication_date][is]":ts,
          "conditions[agencies][]":"national-archives-and-records-administration",
          "conditions[term]":"\"records schedules\""}
headers = {"accept":"application/json"}
base_url = "http://www.federalregister.gov/api/v1/documents.json"

consumer_key = "enter your Twitter API consumer key"
consumer_secret = "enter your Twitter API consumer secret"
access_key = "enter your Twitter API access key"
access_secret = "enter your Twitter API access secret"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

r=requests.get(base_url, params=params, headers=headers)
print(r.url)
json = r.json()
if 'results' in json:
    record = json['results']
    for i in record:
        out = (i['publication_date'] + ': Doc. No. ' + i['document_number'] + ' -- \"' + i['title']) + '\" ' + (i['html_url'])
        print(out)
else:
    print('There are no new record schedule documents to share.')
