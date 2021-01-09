import pandas as pd
import pickle
import keras

from flask import jsonify

import csv
import json

class LstmModel:

    def post(self, centre_name, date, commodity_name):

        print(commodity_name)
        
        if commodity_name.capitalize() == 'Tomato':
            return self.get_tomato_prediction(centre_name, date)

        elif commodity_name.capitalize() == 'Potato': 
            return self.get_potato_prediction(centre_name, date)

        elif commodity_name.capitalize() == 'Onion': 
            return self.get_onion_prediction(centre_name, date)

        elif commodity_name.capitalize() == 'Cabbage': 
            return self.get_cabbage_prediction(centre_name, date)
            
        else:
            return self.get_brinjal_prediction(centre_name, date)
   
    def get_tomato_prediction(self, centre_name, date):
        Data = pd.read_csv('lstm_price_prediction_tomato.csv')
        result = {
            'predicted_retail_price': Data.loc[(Data['centre_name'] == centre_name) & (Data['date'] == date), 'predicted_retail_price'].values[0]}
        return jsonify(result)

    def get_today_tomato_prediction(self, centre_name, date):
        Data = pd.read_csv('lstm_price_prediction_tomato.csv')
        result = {
            'predicted_retail_price': Data.loc[(Data['centre_name'] == centre_name) & (Data['date'] == date), 'predicted_retail_price'].values[0]}
        return jsonify(result)

    def get_potato_prediction(self, centre_name, date):
        Data = pd.read_csv('lstm_price_prediction_potato.csv')
        result = {
            'predicted_retail_price': Data.loc[(Data['centre_name'] == centre_name) & (Data['date'] == date), 'predicted_retail_price'].values[0]}
        return jsonify(result)

    def get_today_potato_prediction(self, centre_name, date):
        Data = pd.read_csv('lstm_price_prediction_tomato.csv')
        result = {
            'predicted_retail_price': Data.loc[(Data['centre_name'] == centre_name) & (Data['date'] == date), 'predicted_retail_price'].values[0]}
        return jsonify(result)

    def get_onion_prediction(self, centre_name, date):
        Data = pd.read_csv('lstm_price_prediction_onion.csv')
        result = {
            'predicted_retail_price': Data.loc[(Data['centre_name'] == centre_name) & (Data['date'] == date), 'predicted_retail_price'].values[0]}
        return jsonify(result)

    def get_today_onion_prediction(self, centre_name, date):
        Data = pd.read_csv('lstm_price_prediction_tomato.csv')
        result = {
            'predicted_retail_price': Data.loc[(Data['centre_name'] == centre_name) & (Data['date'] == date), 'predicted_retail_price'].values[0]}
        return jsonify(result)

    def get_cabbage_prediction(self, centre_name, date):
        Data = pd.read_csv('lstm_price_prediction_cabbage.csv')
        result = {
            'predicted_retail_price': Data.loc[(Data['centre_name'] == centre_name) & (Data['date'] == date), 'predicted_retail_price'].values[0]}
        return jsonify(result)

    def get_today_cabbage_prediction(self, centre_name, date):
        Data = pd.read_csv('lstm_price_prediction_tomato.csv')
        result = {
            'predicted_retail_price': Data.loc[(Data['centre_name'] == centre_name) & (Data['date'] == date), 'predicted_retail_price'].values[0]}
        return jsonify(result)

    def get_brinjal_prediction(self, centre_name, date):
        Data = pd.read_csv('lstm_price_prediction_brinjal.csv')
        result = {
            'predicted_retail_price': Data.loc[(Data['centre_name'] == centre_name) & (Data['date'] == date), 'predicted_retail_price'].values[0]}
        return jsonify(result)

    def get_today_brinjal_prediction(self, centre_name, date):
        Data = pd.read_csv('lstm_price_prediction_tomato.csv')
        result = {
            'predicted_retail_price': Data.loc[(Data['centre_name'] == centre_name) & (Data['date'] == date), 'predicted_retail_price'].values[0]}
        return jsonify(result)