# from werkzeug.security import generate_password_hash, check_password_hash
# from flask import request, jsonify
# # from flask import json
import pandas as pd
# import numpy as np
# from sklearn import model_selection
# from sklearn.linear_model import LogisticRegression
# from sklearn.decomposition import PCA
# from sklearn.preprocessing import scale
import pickle
import keras
# import json

# from predictions.preprocess_model import PreprocessModel
from flask import jsonify


class LstmModel:

    def get_prediction(self, item, date):
        data = pd.read_csv('90_day_prediction.csv')

        # result = data.loc[(data['item'] == int(item)) & (data['date'] == date), 'pred_avg_sale'].values
        result = {
            'pred_avg_sale': data.loc[(data['item'] == int(item)) & (data['date'] == date), 'pred_avg_sale'].values[0]}
        return jsonify(result)
