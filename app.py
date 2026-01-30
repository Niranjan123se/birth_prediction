from flask import Flask, jsonify, render_template, request
import pandas as pd
import pickle

app = Flask(__name__)


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



@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def get_prediction ():
    baby_data=request.form
    # convert innto the dataframe
    cleaned_data=get_cleaned_data(baby_data)
    df=pd.DataFrame(cleaned_data, index=[0])

    # load a machine learning model
    with open('model/lr.pkl', 'rb') as obj:
        model=pickle.load(obj)

    # make a prediction
    prediction=model.predict(df)
    prediction=round(float(prediction[0]),2 )
    responce= prediction
    return render_template('index.html',responce=responce)



if __name__ == '__main__':
    app.run(debug=True)