import tweepy
from tweepy import OAuthHandler
import pandas as pd
def hash(hashtag):
        # Secret Credentials
        ACCESS_TOKEN = "500435442-ZsyX0WGAgAsiK3mPMwCLVZgXaM4mPeLpOZHh46Uc"
        ACCESS_TOKEN_SECRET = "tI6pbzVsXWzNmfUEC07by6ZpJc5d58vu0sKxovxuDQEoY"
        CONSUMER_KEY = "zazEfoGYmcJp8IZCQZYeleORe"
        CONSUMER_SECRET = "JtTfz6C4WaCNZkzmn02U4GkOoilCyiIVKFFknuLgWD51MeVySm"

        #
        auth=OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)
        api=tweepy.API(auth)

        ut= hashtag

        popular_tweets = api.search(q=ut, result_type='popular')

        # popular_tweets[1]

        l1=[]
        l2=[]
        l3=[]
        l5=[]
        l4=[]
        for j in range(5):
                l4.append(popular_tweets[j].user.profile_image_url)
                l3.append(popular_tweets[j].text)
                l1.append(popular_tweets[j].user.screen_name)
                l2.append(popular_tweets[j].retweet_count)
                l5.append(popular_tweets[j].user.name)

        #      l=[cat("\n"+popular_tweets[j].text,"\nBy--  "+popular_tweets[j].user.name,'RetweetCount:'+popular_tweets[j].ret]
        data=pd.DataFrame()

        data['Twitter_ID']=l1
        data['Tweet']=l3
        data['Twitter_Photo']=l4
        data['Retweet_Count']=l2
        data['Twitter_name']=l5
        d2 = data.to_json(orient='records',lines=True)
        print(d2)
        return d2

