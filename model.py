# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
from nltk.stem import WordNetLemmatizer
nltk.download('wordnet')
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC, LinearSVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB,MultinomialNB,BernoulliNB
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report



news_train = pd.read_csv('BBC News Train.csv')
news_test = pd.read_csv('BBC News Test.csv')
# Assigning numeric value
news_train['Category_num'] = news_train['Category'].factorize()[0]
# Getting Categories and their assigned number
news_train[['Category','Category_num']].drop_duplicates()

# Removing non alphabets, stopwords
lemma = WordNetLemmatizer()
corpus = []
for i in range(0, len(news_test)):
    Text = re.sub('[^a-zA-Z]', ' ', news_test['Text'][i])
    Text = Text.lower()
    Text = Text.split()

    Text = [lemma.lemmatize(word) for word in Text if not word in stopwords.words('english')]
    news_test['Text'][i] = ' '.join(Text)


# Converting to vectors
Tfidf = TfidfVectorizer(max_features = 5000)
X = Tfidf.fit_transform(news_train['Text']).toarray()
y = news_train['Category_num']
test_data = Tfidf.fit(news_test['Text'])
pickle.dump(Tfidf,open("transform.pkl","wb"))


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 0, shuffle = True)

# MultinomialNaiveBayes
mNB = MultinomialNB()
model = mNB.fit(X_train, y_train)
predict_mNB = mNB.predict(X_test)

accuracy_score(y_test,predict_mNB)
print(classification_report(y_test,predict_mNB))

pickle.dump(mNB,open("ArticleSortingModel1.pkl","wb"))

