import os
import pandas as pd
import pickle
from flask import Blueprint, request, render_template
app_mini = Blueprint("predict",__name__)




def get_cleaned_data(form_data):
    gestation =float(form_data['gestation'])
    parity =float(form_data['parity'])
    age =float(form_data['age'])
    height =float(form_data['height'])
    weight =float(form_data['weight'])
    smoking =float(form_data['smoke'])

    return {
        'gestation': gestation,
        'parity': parity,
        'age': age,
        'height': height,
        'weight': weight,
        'smoke': smoking
    }




@app_mini.route('/')
def home():
    return render_template('index.html')


@app_mini.route('/predict', methods=['POST'])
def get_prediction ():
    baby_data=request.get_json()
    print(baby_data)
    # convert innto the dataframe
    # cleaned_data=get_cleaned_data(baby_data)
    df=pd.DataFrame(baby_data)
     # select the required columns
    df=df[['gestation','parity','age','height','weight','smoke']]
    # load a machine learning model
    path=os.path.join(os.path.dirname(__file__),'model/lr.pkl')
    with open(path, 'rb') as obj:
        model=pickle.load(obj)

    # make a prediction
    prediction=model.predict(df)
    prediction=round(float(prediction[0]),2 )
    responce= prediction
    return str(responce)
