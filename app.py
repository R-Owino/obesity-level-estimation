import os
from unittest import result
import numpy as np 
from flask import Flask, request, render_template
import pickle

# creating an instance of the class
app = Flask(__name__, template_folder='Templates')
model = pickle.load(open('modelkmeans.pkl', 'rb'))

# telling flask what url should trigger the function home()
@app.route('/')
@app.route('/index')
def home():
    return render_template('index.html')

# prediction function
def valPredictor(to_predict_list):
    to_predict = np.array(to_predict_list).reshape(1,16)
    # loading the model
    loaded_model = pickle.load(open('modelkmeans.pkl', 'rb'))
    # predict values using loaded model
    result = loaded_model.predict(to_predict)
    return result[0]


@app.route('/result',methods=['POST'])
def result():
    if request.method == 'POST':
        to_predict_list = request.form.values()
        to_predict_list = list(map(float, to_predict_list))
        result = valPredictor(to_predict_list)

        if float(result) == 0:
            prediction = 'You have a normal weight level but could easily relapse to insuffient weight level'
        elif float(result) == 1:
            prediction = 'You have obesity type II weight level but are at a high risk of obesity type III'
        elif float(result) == 2:
            prediction = 'You are at overweight level I but are at a high risk of being overweight level II'
          
        elif float(result) == 3:
            prediction = 'You have obesity type I weight level'
        elif float(result) == 4:
            prediction = 'You are at overweight level I'
        


        return render_template('result.html', prediction=prediction)
        
# starting the flask server
if __name__ == "__main__":
    app.run(debug=True)    
        




