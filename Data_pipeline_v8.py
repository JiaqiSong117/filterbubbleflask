#!/usr/bin/env python
# coding: utf-8

# !pip install geocoder
import tweepy

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

import matplotlib.pyplot as plt
import pandas as pd

def trending():
    # Secret Credentials
    ACCESS_TOKEN = "500435442-ZsyX0WGAgAsiK3mPMwCLVZgXaM4mPeLpOZHh46Uc"
    ACCESS_TOKEN_SECRET = "tI6pbzVsXWzNmfUEC07by6ZpJc5d58vu0sKxovxuDQEoY"
    CONSUMER_KEY = "zazEfoGYmcJp8IZCQZYeleORe"
    CONSUMER_SECRET = "JtTfz6C4WaCNZkzmn02U4GkOoilCyiIVKFFknuLgWD51MeVySm"

    # In[3]:
    auth=OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)
    api=tweepy.API(auth)

    # In[4]:
    tweets=[]
    retweet=[]
    likes=[]

    #LOAD MODEL
    loaded_vec = CountVectorizer(vocabulary=pickle.load(open("count_vector.pkl", "rb")))
    loaded_tfidf = pickle.load(open("tfidf.pkl","rb"))
    loaded_model = pickle.load(open("NEW_softmax.pkl","rb"))

    import sys
    import geocoder
    # Available Locations
    places = api.geo_search(query="AUSTRALIA", granularity="country")
    place_id = places[0].id

    available_loc = api.trends_available()
        # Trends for Specific Country
        # location as argument variable
    lat=-37.8136
    lng=144.9631
    closest_loc = api.trends_closest(lat, lng)
    trends = api.trends_place(closest_loc[0]['woeid'])

    trends2=trends[0]['trends'][:10]
    d={}
    # for i in range(len(trends2)):
    #     print('####################################')
    #     string="#"+str(trends2[i]['name'])
    #     print(string)
    #
    #     popular_tweets=[]
    #     popular_tweets = api.search(q=trends2[i]['name'], result_type='popular')
    #     # for j in range(len(popular_tweets)):
    #     #     print("\n"+popular_tweets[j].text)
    #     #     print("\nBy--  "+popular_tweets[j].user.name)
    # #        l=[cat("\n"+popular_tweets[j].text,"\nBy--  "+popular_tweets[j].user.name,'RetweetCount:'+popular_tweets[j].ret]
    #
    #     print('----------------------------------------------------')

    n=[]
    tv=[]
    for i in range(len(trends2)):
        n.append(str(trends2[i]['name']))
        tv.append(i+1)
    trending_data=dict(zip(n,tv))
    bar1=[n,tv]

    import json
    trending_data=dict(zip(n,tv))
    json_trending_data = json.dumps(trending_data)
    print(json_trending_data)
    return json_trending_data