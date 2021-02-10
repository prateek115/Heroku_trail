from flask import Flask, request, jsonify, render_template
import pandas as pd
import joblib

app = Flask(__name__)
model = joblib.load('model.pkl')

@app.route('/')
def home():
    return render_template('webpage.html')

@app.route('/predict', methods=['POST'])
def predict():
    age = int(request.form['Age'])
    gender = request.form['Gender']
    gender = gender.lower()
    bmi = float(request.form['BMI'])
    children = int(request.form['Children'])
    smoker = request.form['Smoker']
    smoker = smoker.lower()
    region = request.form['Region']
    region = region.lower()
    
    inputs = pd.DataFrame({'age':age, 'sex': gender, 'bmi': bmi, 'children': children, 'smoker': smoker, 'region': region}, index=[0])
    prediction = model.predict(inputs)
    output = round(prediction[0], 2)
    return render_template('webpage.html', prediction_text = "Predicted Insurance Cost is $ {}".format(output))

if __name__=="__main__":
    app.run(debug=True)