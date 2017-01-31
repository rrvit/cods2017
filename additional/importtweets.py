'''
This file is used to import tweets from Twitter. Keys and access tokens are already added to this code which will expire in some days.
Therefore generate new keys to run this code without any errors
Importing tweets will require a network connetion and the import will take approximately 1 second per tweet
Uses additional library named Tweepy that needs to be installed seperately along with Python
'''

import tweepy
from tweepy import OAuthHandler
import csv
from pprint import pprint

#Authenticating and connecting to Twitter
consumer_key = 'wwkk8nYdOaYpjV1y0TFkI4BBh'
consumer_secret = 'FyiN1mh3fty8OkTlQ8GlPQL0oaBeskIVcqjplZ76EodFluYoKO'
access_token = '765032930498400256-4JaSqoXWn7QmS52oe3R0tktNdSjDGRs'
access_secret = 'UtSk5RzUETSxMo2XLARwwWUtzFXWfLDCLdFsKkbvCwrTD'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)


count=1                     
alist=[]                    #List to save tweets
with open('Datasheet.csv', 'rb') as f:
    reader = csv.reader(f)
    with open('tweets_all.csv', 'wb') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        for row in reader:
            print count
            p=''
            tweetid=row[0]
            #if count>100000:           #Number of tweets to be imported
                #break
            if count>0:
                api = tweepy.API(auth)
                try:
                    tweet = api.get_status(tweetid)
                    p=tweet.text.encode('utf-8')
                    print count
                    print tweetid
                    print p
                    rowform=[]
                    rowform.append(tweetid)
                    rowform.append(p)
                    wr.writerow(rowform)
                
                except tweepy.TweepError,e:
                    p='Error'
                    print e
            count=count+1

