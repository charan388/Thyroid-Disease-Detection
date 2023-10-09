import os
import pandas as pd
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from flask_cors import cross_origin
from prediction.predict import prediction
application = Flask(__name__)

application.config["csv_file"] = "C:/Users/charan/Desktop/Prediction_Output_File/"
application.config["sample_file"] = "Prediction_SampleFile/"


@application.route('/')
@cross_origin()
def home():
    return render_template('index.html')


@application.route('/return_sample_file/')
@cross_origin()
def return_sample_file():
    sample_file = os.listdir("../Prediction_SampleFile/")[0]
    return send_from_directory(application.config["sample_file"], sample_file)


@application.route('/return_file/')
@cross_origin()
def return_file():
    final_file = os.listdir("C:/Users/charan/Desktop/Prediction_Output_File/")[0]
    return send_from_directory(application.config["csv_file"], final_file)


@application.route('/result')
@cross_origin()
def result():
    return render_template('result.html')


@application.route('/predict', methods=['POST'])
@cross_origin()
def predict():
    if request.method == 'POST':
        if 'csvfile' not in request.files:
            return render_template("invalid.html")

        file = request.files['csvfile']

        df = pd.read_csv(file, index_col=[0])

        path = 'Prediction_InputFileFromUser/'

        # if os.path.isfile('Prediction_InputFileFromUser/InputFile.csv'):
        # os.remove('Prediction_InputFileFromUser/InputFile.csv')

        df.to_csv('Prediction_InputFileFromUser/InputFile.csv')

        pred = prediction()  # object initialization

        pred.predictionFromModel()

    return redirect(url_for('result'))


if __name__ == '__main__':
    application.run(debug=True)

