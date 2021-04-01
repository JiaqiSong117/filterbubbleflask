import json
import pandas as pd
from sklearn.model_selection import train_test_split
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier

tweets = []
for line in open('News_Category_Dataset_v2.json', 'r'):
    tweets.append(json.loads(line))

model_dataset=pd.DataFrame()
model_dataset['News']='Not_Available'
model_dataset['Category']='Not_Available'
news=[]
category=[]
for i in range(len(tweets)):
    a=tweets[i]
    category.append(a['category'])
    news.append(a['headline'])
model_dataset['News']=news
model_dataset['Category']=category



#GET VECTOR COUNT
count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(model_dataset.News)

#SAVE WORD VECTOR
pickle.dump(count_vect.vocabulary_, open("../count_vector2.pkl", "wb"))

from sklearn.feature_extraction.text import TfidfTransformer

#TRANSFORM WORD VECTOR TO TF IDF
tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)

#SAVE TF-IDF
pickle.dump(tfidf_transformer, open("../tfidf2.pkl", "wb"))


# Multinomial Neural Network



clf_neural = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(15,), random_state=1)

X_train, X_test, y_train, y_test = train_test_split(X_train_tfidf, model_dataset.Category, test_size=0.25, random_state=42)

clf_neural.fit(X_train, y_train)
#SAVE MODEL
pickle.dump(clf_neural, open("../softmax.pkl", "wb"))
################################
print('done')
import pickle
from sklearn.feature_extraction.text import CountVectorizer

