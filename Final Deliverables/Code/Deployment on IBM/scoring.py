import numpy as np  
from flask import Flask, render_template, request, url_for, redirect 
import requests
from tensorflow.keras.models import load_model  

API_KEY = "DbnVb60NWCN5h5qNhluA4fBGkhD6DPJrwonUoPuAarfJ"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

app = Flask(__name__)  
model = load_model('crude_oil_price_prediction.h5')  

@app.route('/', methods=['GET', 'POST'])
def home():
    error = None
    if request.method == 'POST':
        if request.form['username'] != "admin" or request.form['password'] != "admin":
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('mains'))
    return render_template('login.html', error=error)


@app.route('/mains', methods=['GET', 'POST'])
def mains():
    return render_template('index.html')

@app.route('/stats', methods=['GET', 'POST'])
def stats():
    return render_template('stats.html')



@app.route('/about')
def home1():
    return render_template("index.html")  

@app.route('/predict')
def home2():
    return render_template("web.html")  

@app.route('/contact')
def contact():
    return render_template("contact.html") 


@app.route('/login', methods=['POST'])  
def login():
    a = request.form['year1']
    b = request.form['year2']
    c = request.form['year3']
    d = request.form['year4']
    e = request.form['year5']
    f = request.form['year6']
    g = request.form['year7']
    h = request.form['year8']
    i = request.form['year9']
    j = request.form['year10']  
    x_input = [[float(a), float(b), float(c), float(d), float(e), float(f), float(g), float(h), float(i), float(j)]]
    print(x_input)
    payload_scoring = {"input_data": [{"field": [["year1","year2","year3","year4","year5","year6","year7","year8","year9","year10"]], "values": x_input}]}
    response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/bf470391-47f6-4850-a9ee-324df4a39f3e/predictions?version=2022-11-15', json=payload_scoring,headers={'Authorization': 'Bearer ' + mltoken})
    print("Scoring response")
    predictions=response_scoring.json()
    print(response_scoring.json())
    return render_template("web.html", showcase='The Predicted crude oil price is : Rs. '+str(predictions['predictions'][0]['values'][0][0]))


if __name__ == '__main__':
    app.run(debug=False)