# -*- coding: utf-8 -*-
"""Spam_message_classification.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Svrov4OiWk1k-MoCFezk5fjtU6KIV30M

# Spam message classification 
  Random forest and support vector classifier are built to classify mail as ham or spam.
"""

# import basic libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# read the file
data=pd.read_csv('spam_data.tsv',sep='\t')

data.head()

data.info()

# check for missing values
data.isnull().sum()

data.shape

# count of labels
data['label'].value_counts()

data['label'].value_counts()/len((data))

"""Dataset is imbalanced"""

# lets make data balanced
ham=data[data['label']=='ham']
spam=data[data['label']=='spam']

ham.shape,spam.shape

ham=ham.sample(spam.shape[0])

#now data is balanced
ham.shape,spam.shape

# lets append ham and spam
data=ham.append(spam,ignore_index=True)

data.shape

# data labels are balanced
data['label'].value_counts()

plt.hist(data[data['label']=='ham']['length'],bins=100)
plt.hist(data[data['label']=='spam']['length'],bins=100)
plt.show()

plt.hist(data[data['label']=='ham']['punct'],bins=100)
plt.hist(data[data['label']=='spam']['punct'],bins=100)
plt.show()

"""Split data into x and y"""

x=data['message']
y=data['label']

#split data for train and test
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test =  train_test_split(x, y, test_size = 0.3, random_state =0, shuffle = True)

"""# Random forest"""

# import Tfidfvectorizer and random forest model
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline

model=Pipeline([('tfidf',TfidfVectorizer()),('model',RandomForestClassifier(n_estimators=20))])

model.fit(X_train,y_train)

y_pred=model.predict(X_test)

# evaluate the model using classification_report,confusion_matrix and accuracy_score
from sklearn.metrics import classification_report,accuracy_score,confusion_matrix
accuracy_score(y_test,y_pred)

confusion_matrix(y_test,y_pred)

print(classification_report(y_test,y_pred))

"""# Support vector machine"""

from sklearn.svm import SVC

model=Pipeline([('tfidf',TfidfVectorizer()),('model',SVC())])

model.fit(X_train,y_train)

y_pred=model.predict(X_test)

accuracy_score(y_test,y_pred)

confusion_matrix(y_test,y_pred)

print(classification_report(y_test,y_pred))

# lets check for our own data
A = ['Hello, welcome to  natural Language Processing tutorial']
B = ['hey! hope you are doing great ,how is your preparation?']
C = ['Congratulations, You won a lottery ticket worth $100 Million ! To claim call on 589557']

list=[A,B,C]
for x in list:
  print(model.predict(x))