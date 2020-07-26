from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np

app = Flask(__name__)
pipeline = joblib.load("insurance_prediction.joblib")

#Use my own html to build homepage
@app.route('/')
def home():
  return render_template('template.html')

#Read input from browser and return the calculation to browser
@app.route('/predict',methods=['POST'])
def predict():
  #Read input from browser
  age = request.form["age"]
  sex = request.form["sex"]
  bmi = request.form["bmi"]
  children = request.form["children"]
  smoker = request.form["smoker"]
  region = request.form["region"]
  
  #Predict then return the calculation to browser
  X = np.array([age, sex, bmi, children, smoker, region])
  prediction = pipeline.predict(X)
  return render_template('template.html', prediction_text='Expense of insurance should be $ {}'.format(prediction))


if __name__ == "__main__":
  app.run(debug=True)
