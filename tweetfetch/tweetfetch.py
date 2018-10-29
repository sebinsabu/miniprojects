# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 10:33:18 2018

@author: Sebin
"""
import tweepy
import csv
import pandas as pd
from textblob import TextBlob
####input your credentials here
consumer_key = 'VFBEwMpMjtlV8OIA0mfucV6kY'
consumer_secret = 'eukgnIEVhoXF2B7Z34UpDozbNoBPza97A8eimYQKX5gVij8WKc'
access_token = '1041578973338066944-kvBimbneKmEGrXZeUralzYQB3fY4a6'
access_token_secret = 'F5CnUDFqldUJL20n45wy9OI3OSg63dBIBcoVQA3baZKV2'
twitterhandle = 'ndtv'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)
#####United Airlines
# Open/Create a file to append data
#csvFile = open('hope.csv', 'a')
#Use csv Writer
#csvWriter = csv.writer(csvFile)
runner = 0
sentiment_score_summer = 0

for tweet in tweepy.Cursor(api.user_timeline, id=twitterhandle,count=90,
                           lang="en",
                           since="2014-05-26").items():
    print (tweet.created_at, tweet.text)
#    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
    statement = tweet.text
    sentiment = TextBlob(statement)
    sentiment_score = sentiment.sentiment.polarity
    print(sentiment_score)
    runner = runner + 1
    sentiment_score_summer = sentiment_score_summer+sentiment_score

print("No of Tweets Analyzed ::",runner,"Total Sum of Senti_Score :: ",sentiment_score_summer,"Average Sentimence::",sentiment_score_summer/runner)


#