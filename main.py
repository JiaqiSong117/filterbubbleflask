# import libraries
import tweepy
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import plotly.graph_objects as go
import json


import pandas as pd

# Secret Credentials
def tasks(username):
    ACCESS_TOKEN = "500435442-ZsyX0WGAgAsiK3mPMwCLVZgXaM4mPeLpOZHh46Uc"
    ACCESS_TOKEN_SECRET = "tI6pbzVsXWzNmfUEC07by6ZpJc5d58vu0sKxovxuDQEoY"
    CONSUMER_KEY = "zazEfoGYmcJp8IZCQZYeleORe"
    CONSUMER_SECRET = "JtTfz6C4WaCNZkzmn02U4GkOoilCyiIVKFFknuLgWD51MeVySm"

    auth=OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)
    api=tweepy.API(auth)

    tweets=[]
    retweet=[]
    likes=[]

    userx=username
    print(username)
    searched_tweets = [status for status in tweepy.Cursor(api.user_timeline, id=userx).items(200)]
    tweets = []
    for i in searched_tweets:
        tweets.append(i.text)

    new_docs=tweets

    #LOAD MODEL
    loaded_vec = CountVectorizer(vocabulary=pickle.load(open("count_vector.pkl", "rb")))
    loaded_tfidf = pickle.load(open("tfidf.pkl","rb"))
    loaded_model = pickle.load(open("New_softmax.pkl","rb"))

    news_category=[]

    for i in range(len(new_docs)):
        X_new_counts = loaded_vec.transform([new_docs[i]])
        X_new_tfidf = loaded_tfidf.transform(X_new_counts)
        predicted = loaded_model.predict(X_new_tfidf)
        news_category.append(predicted)

    x=[]
    for i in range(len(news_category)):
        x.append(news_category[i][0])

    set_x=list(set(x))
    set_x_count=[]

    for j in range(len(set_x)):
        set_x_count.append(x.count(set_x[j]))

    Tweet_Uni=dict(zip(set_x,set_x_count))

    count1=list(Tweet_Uni.values())
    size1=[]
    for i in count1:
        size1.append(i*2)

    colours=[]
    c=120
    for i in range(len(count1)):
        c=c+2
        colours.append(c)

    #Convert to json
    data = {}
    data=dict(zip(set_x,set_x_count))
    json_data = json.dumps(data)
    print(json_data)
    return json_data

# graph
# fig = go.Figure(data=[go.Scatter(
#     x=set_x,
#     y=set_x_count,
#     mode='markers',
#     marker=dict(
#         color=colours,
#         size=size1,
#         showscale=True
#         )
# )])
# fig.show()
