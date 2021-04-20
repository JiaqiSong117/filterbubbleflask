import tweepy

from tweepy import OAuthHandler
import pickle
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd

# Secret Credentials
def combinedsearch(users):
    ACCESS_TOKEN = "500435442-ZsyX0WGAgAsiK3mPMwCLVZgXaM4mPeLpOZHh46Uc"
    ACCESS_TOKEN_SECRET = "tI6pbzVsXWzNmfUEC07by6ZpJc5d58vu0sKxovxuDQEoY"
    CONSUMER_KEY = "zazEfoGYmcJp8IZCQZYeleORe"
    CONSUMER_SECRET = "JtTfz6C4WaCNZkzmn02U4GkOoilCyiIVKFFknuLgWD51MeVySm"

    auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)

    tweets = []
    retweet = []
    likes = []
    # input from website

    user_input = 'DA'
    userx = users

    data = []
    for i in range(len(userx)):
        searched_tweets = [status for status in tweepy.Cursor(api.user_timeline, id=userx[i]).items(200)]
        tweets = []
        for i in searched_tweets:
            tweets.append(i.text)
        data.append(tweets)

    # LOAD MODEL
    loaded_vec = CountVectorizer(vocabulary=pickle.load(open("count_vector.pkl", "rb")))
    loaded_tfidf = pickle.load(open("tfidf.pkl", "rb"))
    loaded_model = pickle.load(open("v9_softmax.pkl", "rb"))

    news_category = []

    for i in range(len(data)):
        for j in range(len(data[i])):
            X_new_counts = loaded_vec.transform([data[i][j]])
            X_new_tfidf = loaded_tfidf.transform(X_new_counts)
            predicted = loaded_model.predict(X_new_tfidf)
            # print(predicted)
            news_category.append(predicted)

    from itertools import islice

    def chunk(it, size):
        it = iter(it)
        return iter(lambda: tuple(islice(it, size)), ())

    x = []
    for i in range(len(news_category)):
        x.append(news_category[i][0])

    cumulative_count = []
    set_x = list(set(x))

    for j in range(len(set_x)):
        cumulative_count.append(x.count(set_x[j]))

    N_c = list(chunk(x, 200))

    count_y = []

    for i in range(len(N_c)):
        count = []
        for j in range(len(set_x)):
            count.append(N_c[i].count(set_x[j]))
        count_y.append(count)

    import json

    data = {}
    df = pd.DataFrame()
    df['category'] = set_x
    # print(set_x)

    if user_input == 'CA':
        data = dict(zip(set_x, cumulative_count))
        json_data = json.dumps(data)
    else:
        for i in range(len(count_y)):
            df[users[i]] = count_y[i]
        json_data = df.to_json(orient='records')

        return json_data




