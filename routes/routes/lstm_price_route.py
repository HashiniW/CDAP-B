from flask import Flask
from flask import Blueprint
from flask_restful import Api
from resources.lstm_price_resource import Predict
from flask_cors import CORS, cross_origin

lstm_price_blueprint = Blueprint('lstmPrice', __name__)
CORS(lstm_price_blueprint)

lstm_blueprint_api = Api(lstm_price_blueprint)

lstm_blueprint_api.add_resource(Predict, '/vegetable', methods=['POST'])