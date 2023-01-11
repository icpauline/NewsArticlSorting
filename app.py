# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 00:51:16 2023

@author: Pauline
"""

from flask import Flask,render_template,url_for,request
#import pandas as pd 
import pickle


# load the model from disk
filename = 'ArticleSortingModel1.pkl'
clf = pickle.load(open(filename, 'rb'))
cv=pickle.load(open('transform.pkl','rb'))
app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/predict',methods=['GET','POST'])
def predict():
    if request.method == 'POST':
        message = request.form['message']
        data = [message]
        vect = cv.transform(data).toarray()
        my_prediction = clf.predict(vect)
        
        if my_prediction ==0:
            pred='Business'
        elif my_prediction == 1:
            pred='Technology'
        elif my_prediction==2:
            pred='Politics'
        elif my_prediction ==3:
            pred='Sport'
        elif my_prediction ==4:
            pred='Entertainment'
            
    return render_template('result.html',prediction = pred)



if __name__ == '__main__':
	app.run(host = '0.0.0.0' , port = 8080)