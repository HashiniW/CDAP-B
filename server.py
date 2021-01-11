from flask import Flask, jsonify, request, json
from routes.lstm_price_route import lstm_price_blueprint
from routes.lstm_route import lstm_blueprint
from bson.json_util import dumps
from bson.objectid import ObjectId
from flask_cors import CORS, cross_origin

import csv
import json
import pymongo

server = Flask(__name__)

#Enable cross origin resource sharing
CORS(server)
server.config.from_object('config')

server.config['JSON_AS_ASCII'] = False
server.config['CORS_HEADERS'] = 'Content-Type'

server.register_blueprint(lstm_blueprint)
server.register_blueprint(lstm_price_blueprint)

#Setup mongodb client to application
#Database available at MongoDB Atlas
myclient = pymongo.MongoClient("mongodb+srv://prasangika:prasangika1234@cluster0.n7wlp.mongodb.net/farmer_ranking?ssl=true&ssl_cert_reqs=CERT_NONE")
mydb = myclient["farmer_ranking"]



#Set csv file path that program should have to read
csvFilePath         = 'train.csv'

#Set path and file name for json file that system should be created
jsonFilePath         = 'demand.json'

#Create service for read curret updated csv and create json file
@server.route('/csv')
def csv_json():
    #create object to store rows in csv file
    data={}
    #initialize the object index
    i = 0
    #start reading csv file
    with open(csvFilePath) as f:
        #Create file reader
        csvReader = csv.DictReader(f)
        #loop through the rows that read by file reader
        for rows in csvReader:
            id = i #set object id 0 to number of rows - 1 in csv file
            data[id] = rows #set currebt row as object
            i = i+1 #increase id by 1

    #open file reder for create JSON file with CSV data
    with open(jsonFilePath, "w") as jf:
        #Write CSV data to JSON
        jf.write(json.dumps(data, indent=4))

    return json.dumps('finisshed')

#Return Store 1 Data
@server.route('/data')
def create_json_obj():
   resp =  create_json_data()
   return json.dumps(resp)

#Filter out data from JOSN and select data for store 1
def create_json_data():
    # Create empty list
    final_json = []

    #Read demand.json file and assign values to variable
    with open('./data.json') as f:
        data = json.load(f)

    #modify and create JSON object for each record
    for i in range(len(data)):
        #read each object in JSON file
        json_obj = data[str(i)]
        #Filter data for store 1 and select records for item 1,2,3
        if json_obj["centre_name"] == "DELHI" and (json_obj["commodity_name"] == "Tomato"):
            json_obj["centre_name"] = 'DELHI'

        #Append modified record to final object
        final_json.append(json_obj)

    return final_json

#Return Store 1 Data
@server.route('/store1')
def create_json_obj_store1():
   resp =  create_json_store1()
   return json.dumps(resp)

#Filter out data from JOSN and select data for store 1
def create_json_store1():
    # Create empty list
    final_json = []

    #Read demand.json file and assign values to variable
    with open('./demand.json') as f:
        demand = json.load(f)

    #modify and create JSON object for each record
    for i in range(len(demand)):
        #read each object in JSON file
        json_obj = demand[str(i)]
        #Filter data for store 1 and select records for item 1,2,3
        if json_obj["store"] == "1" and (json_obj["item"] == "1" or json_obj["item"] == "2" or json_obj["item"] == "3"):
            #Modify store 1 name
            json_obj["store"] = 'Wattala'

            #Modify item names
            if json_obj["item"] == "1":
                json_obj["item"] = "Potato"
            elif json_obj["item"] == "2":
                json_obj["item"] = "Tomato"
            elif json_obj["item"] == "3":
                json_obj["item"] = "Carrot"

            #Append modified record to final object
            final_json.append(json_obj)

    return final_json

#Return Store 2 Data
@server.route('/store2')
def create_json_obj_store2():
   resp =  create_json_store2()
   return json.dumps(resp)

#Filter out data from JOSN and select data for store 2
def create_json_store2():
    # Create empty list
    final_json = []

    #Read demand.json file and assign values to variable
    with open('./demand.json') as f:
        demand = json.load(f)

    #create JSON object for each record
    for i in range(len(demand)):
        json_obj = demand[str(i)]
        if json_obj["store"] == "2" and (json_obj["item"] == "1" or json_obj["item"] == "2" or json_obj["item"] == "3"):
            json_obj["store"] = 'Nuwara Eliya'

            if json_obj["item"] == "1":
                json_obj["item"] = "Potato"
            elif json_obj["item"] == "2":
                json_obj["item"] = "Tomato"
            elif json_obj["item"] == "3":
                json_obj["item"] = "Carrot"

            final_json.append(json_obj)

    return final_json

#Return Store 3 Data
@server.route('/store3')
def create_json_obj_store3():
   resp =  create_json_store3()
   return json.dumps(resp)

#Filter out data from JOSN and select data for store 3
def create_json_store3():
    # Create empty list
    final_json = []

    #Read demand.json file and assign values to variable
    with open('./demand.json') as f:
        demand = json.load(f)

    #create JSON object for each record
    for i in range(len(demand)):
        json_obj = demand[str(i)]
        if json_obj["store"] == "3" and (json_obj["item"] == "1" or json_obj["item"] == "2" or json_obj["item"] == "3"):
            json_obj["store"] = 'Jaffna'

            if json_obj["item"] == "1":
                json_obj["item"] = "Potato"
            elif json_obj["item"] == "2":
                json_obj["item"] = "Tomato"
            elif json_obj["item"] == "3":
                json_obj["item"] = "Carrot"

            final_json.append(json_obj)

    return final_json

#Error Handler
@server.errorhandler(404)
def not_found(error=None):
    #Create error message as JSON
    message = {
        'status': 404,
        'message': 'Not Found' + request.url
    }

    resp = jsonify(message)

    resp.status_code = 404 #Http Service Not found

    return resp

#Retrieve processed data from database
@server.route('/')
def send_data():
    # set database name
    collectionName = mydb['farmer_rankings_collection']
    # Find all records in considering collection and sorting records in descending order
    result = collectionName.find().sort('score', -1)
    # Create results as JSON
    resp = dumps(result)
    return resp


#Retrieve farmers' personal data from database
@server.route('/farmers')
def send_farmers():
    # set database name
    collectionName = mydb['farmers']
    #Find all farmers' personal data from farmers collection
    result = collectionName.find()
    # Create results as JSON
    resp = dumps(result)
    return resp


# create database for processed data
@server.route('/createRanking',  methods=['POST'])
def create_interview():
    #create request
    _json = request.json
    #get data
    _data = _json["data"]

    #set collection name
    collectionName = mydb["farmer_rankings_collection"]

    #check _data has expected values and http method is POST
    if _data and request.method == "POST":
        #Loop whole data set until last record
        for data in _data:
            #insert data set into database
            collectionName.insert_one(data)
        #success response
        resp = jsonify("Data Added Successfully")
        resp.status_code = 200
        return resp
    else:
        return not_found()


#Update candidate ranking score in database
@server.route('/updateScore/<id>/<score>', methods=['PUT'])
def update_candidate(id, score):
    # set collection name
    collectionName = mydb['farmer_rankings_collection']
    #update record if farmer index is matched with id
    collectionName.update_one({"index": id}, {"$set": {"score": float(score + ".0")}})
    #success response
    resp = jsonify("Details updated successfully")
    resp.status_code = 200
    return resp


#Create data object from processed data
def create_json():
    # Create empty list
    final_json = []

    #Read demand.json file and assign values to variable
    with open('./vegetabledemand.json') as f:
        demand = json.load(f)
    # Read score.json file and assign values to variable
    with open('./score.json') as f:
        score = json.load(f)
    # Read supply.json file and assign values to variable
    with open('./supply.json') as f:
        supply = json.load(f)

    #create JSON object for each record
    for i in range(len(demand)):
        json_obj = {
            'index': "Farmer_" + str(i + 1),
            'score': score[str(i)] * 10,
            'demand': str(demand[str(i)]) + " KG" ,
            'supply': supply[str(i)]
        }
        #Add JSON object to previously created list
        final_json.append(json_obj)

    return final_json

#Run main method
if __name__ == '__main__':
    server.run(debug=True)
