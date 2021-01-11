import pandas as pd
import pickle
import keras

import sys

from flask_cors import CORS, cross_origin
from flask import jsonify

class LstmModel:

    @cross_origin()
    def get_price_prediction(self, centre_name, date, commodity_name):
        
        if commodity_name.capitalize() == 'Tomato':
            return self.read_in_json('lstm_price_prediction_tomato.csv', centre_name, date)

        elif commodity_name.capitalize() == 'Potato':
            return self.read_in_json('lstm_price_prediction_potato.csv', centre_name, date)

        elif commodity_name.capitalize() == 'Onion':
            return self.read_in_json('lstm_price_prediction_onion.csv', centre_name, date)

        elif commodity_name.capitalize() == 'Cabbage':
            return self.read_in_json('lstm_price_prediction_cabbage.csv', centre_name, date)

        else:
            return self.get_brinjal_prediction(centre_name, date)

    def read_in_json(self, file_name, centre_name, date):
        
        data_frame = pd.read_csv(file_name)

        # filters
        filter_centre = data_frame.centre_name == centre_name.upper()
        filter_date = data_frame.date == date
        filter_all = filter_centre & filter_date

        # required comma separated column names
        required_columns = 'predicted_retail_price'

        result_data = data_frame.loc[filter_all, required_columns]
        result_single = -1

        if not result_data.empty:
            result_single = result_data.values[0]

        result = {'predicted_retail_price': result_single }
        return jsonify(result)        