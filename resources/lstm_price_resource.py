from flask_restful import Resource
from predictions.lstm_price_model import LstmModel
from flask import request

class Predict(Resource):
    def post(self):
        data = request.get_json()
       # print(data['Date'])
        #print('lstm')
        prediction = LstmModel().post(data["centre"], data["date"], data["commodity"])
        return prediction
