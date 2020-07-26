# -*- coding: utf-8 -*-
"""insurance.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1g-jkHKj7J2QV6r2d5b64HdikeY0gR4LP

**Packages**
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
import joblib

"""**Load Data**"""

#Read csv file from my Github repository
url = 'https://raw.githubusercontent.com/RuiminZeng/ML-for-A-Final-Project/master/insurance%20data.csv'
insurance_data = pd.read_csv(url, error_bad_lines=False)
insurance_data.head(10)

"""**Split Data**"""

#Y is my target
Y = insurance_data.expenses

#X are the features for prediction
features = ['age', 'sex', 'bmi', 'children', 'smoker', 'region']
X = insurance_data[features]

#Split into two parts, one is training data set, another is validataion data set
#train_x and train_y are for training the model
#Validation_x is for calculating
#Use validation_x to get prediction
#Vaidation_y is actual y which is used to compare with our prediction
train_X, validation_X, train_y, validation_y = train_test_split(X, Y, random_state=0)

"""**Define Processing Steps**"""

#Sperate two types of columns
numerical_cols = ['age', 'bmi', 'children']
categorical_cols = ['sex', 'smoker', 'region']

#Copy data to avoid disturbing data in original file
#Make changes in these copied data
processed_train_x = train_X.copy()
processed_validation_x = validation_X.copy()

#Define two types of imputers
numerical_imputer = SimpleImputer()
categorical_imputer = Pipeline(steps=[('imputer', SimpleImputer(strategy='most_frequent')), ('onehot', OneHotEncoder(handle_unknown='ignore'))])

#Bundle imputers together into preprocessor
preprocessor = ColumnTransformer(transformers=[('numerical', numerical_imputer, numerical_cols), ('categorical', categorical_imputer, categorical_cols)])

"""**Define Model**"""

my_model = RandomForestRegressor(random_state=0)

"""**Bundle Preprocessor and Model by Using Pipeline**"""

#Step 1: preprocessing
#Step 2: modeling
my_pipeline = Pipeline(steps=[('preprocessor', preprocessor), ('model', my_model)])

"""**Use Pipeline to Fit and Predict**"""

#Apply all transformations in preprocessing step then fit the model
my_pipeline.fit(processed_train_x, train_y)

#Apply all transformation in preprocessing step then predict
prediction = my_pipeline.predict(processed_validation_x)

#Compare actual y and prediction
score = mean_absolute_error(validation_y, prediction)
print('Mean absolute error is:', score)

"""**Pickle out Model**"""

joblib.dump(my_pipeline, 'insurance_prediction.joblib')
