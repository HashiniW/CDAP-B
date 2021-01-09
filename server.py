from flask import Flask, jsonify
from routes.lstm_price_route import lstm_price_blueprint
from routes.lstm_route import lstm_blueprint

from flask_cors import CORS, cross_origin

import csv

import json

server = Flask(__name__)
CORS(server)
server.config.from_object('config')

server.config['JSON_AS_ASCII'] = False
server.config['CORS_HEADERS'] = 'Content-Type'

server.register_blueprint(lstm_blueprint)
server.register_blueprint(lstm_price_blueprint)

#Set csv file path that program should have to read
tomato_csvFilePath  = 'tomato.csv'
potato_csvFilePath  = 'potato.csv'
onion_csvFilePath   = 'onion.csv'
cabbage_csvFilePath = 'cabbage.csv'
brinjal_csvFilePath = 'brinjal.csv'
csvFilePath         = 'train.csv'

#Set path and file name for json file that system should be created
tomato_jsonFilePath  = 'tomato.json'
potato_jsonFilePath  = 'potato.json'
onion_jsonFilePath   = 'onion.json'
cabbage_jsonFilePath = 'cabbage.json'
brinjal_jsonFilePath = 'brinjal.json'
jsonFilePath         = 'demand.json'

#Create service for read curret updated csv and create json file
@server.route('/tomatocsv')
def tomato_csv_json():
    #create object to store rows in csv file
    data={}
    #initialize the object index
    i = 0
    #start reading csv file
    with open(tomato_csvFilePath) as f:
        #Create file reader
        csvReader = csv.DictReader(f)
        #loop through the rows that read by file reader
        for rows in csvReader:
            id = i #set object id 0 to number of rows - 1 in csv file
            data[id] = rows #set current row as object
            i = i+1 #increase id by 1

    #open file reder for create JSON file with CSV data
    with open(tomato_jsonFilePath, "w") as jf:
        #Write CSV data to JSON
        jf.write(json.dumps(data, indent=4))

    return json.dumps('Done')

#Create service for read curret updated csv and create json file
@server.route('/potatocsv')
def potato_csv_json():
    #create object to store rows in csv file
    data={}
    #initialize the object index
    i = 0
    #start reading csv file
    with open(potato_csvFilePath) as f:
        #Create file reader
        csvReader = csv.DictReader(f)
        #loop through the rows that read by file reader
        for rows in csvReader:
            id = i #set object id 0 to number of rows - 1 in csv file
            data[id] = rows #set current row as object
            i = i+1 #increase id by 1

    #open file reder for create JSON file with CSV data
    with open(potato_jsonFilePath, "w") as jf:
        #Write CSV data to JSON
        jf.write(json.dumps(data, indent=4))

    return json.dumps('Done')

#Create service for read curret updated csv and create json file
@server.route('/onioncsv')
def onion_csv_json():
    #create object to store rows in csv file
    data={}
    #initialize the object index
    i = 0
    #start reading csv file
    with open(onion_csvFilePath) as f:
        #Create file reader
        csvReader = csv.DictReader(f)
        #loop through the rows that read by file reader
        for rows in csvReader:
            id = i #set object id 0 to number of rows - 1 in csv file
            data[id] = rows #set current row as object
            i = i+1 #increase id by 1

    #open file reder for create JSON file with CSV data
    with open(onion_jsonFilePath, "w") as jf:
        #Write CSV data to JSON
        jf.write(json.dumps(data, indent=4))

    return json.dumps('Done')

#Create service for read curret updated csv and create json file
@server.route('/cabbagecsv')
def cabbage_csv_json():
    #create object to store rows in csv file
    data={}
    #initialize the object index
    i = 0
    #start reading csv file
    with open(cabbage_csvFilePath) as f:
        #Create file reader
        csvReader = csv.DictReader(f)
        #loop through the rows that read by file reader
        for rows in csvReader:
            id = i #set object id 0 to number of rows - 1 in csv file
            data[id] = rows #set current row as object
            i = i+1 #increase id by 1

    #open file reder for create JSON file with CSV data
    with open(cabbage_jsonFilePath, "w") as jf:
        #Write CSV data to JSON
        jf.write(json.dumps(data, indent=4))

    return json.dumps('Done')

#Create service for read curret updated csv and create json file
@server.route('/brinjalcsv')
def brinjal_csv_json():
    #create object to store rows in csv file
    data={}
    #initialize the object index
    i = 0
    #start reading csv file
    with open(brinjal_csvFilePath) as f:
        #Create file reader
        csvReader = csv.DictReader(f)
        #loop through the rows that read by file reader
        for rows in csvReader:
            id = i #set object id 0 to number of rows - 1 in csv file
            data[id] = rows #set current row as object
            i = i+1 #increase id by 1

    #open file reder for create JSON file with CSV data
    with open(brinjal_jsonFilePath, "w") as jf:
        #Write CSV data to JSON
        jf.write(json.dumps(data, indent=4))

    return json.dumps('Done')

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


#Return Tomato Data
@server.route('/tomato')
def create_json_obj_tomato():
   resp =  create_json_tomato()
   return json.dumps(resp)

#Filter out data from JSON and select data for tomato
def create_json_tomato():
    # Create empty list
    final_json = []

    #Read tomato.json file and assign values to variable
    with open('./tomato.json') as f:
        tomato = json.load(f)

    #modify and create JSON object for each record
    for i in range(len(tomato)):
        #read each object in JSON file
        json_obj = tomato[str(i)]
        #Filter data for tomato and select records for centre Pettah, Dambulla, Jaffna
        if json_obj["commodity_name"] == "Tomato" and (json_obj["centre_name"] == "DELHI" or json_obj["centre_name"] == "KOLKATA" or json_obj["centre_name"] == "MUMBAI"):
            json_obj["commodity_name"] = 'Tomato'

            #Modify centre names
            if json_obj["centre_name"] == "DELHI":
                json_obj["centre_name"] = "DELHI"
            elif json_obj["centre_name"] == "KOLKATA":
                json_obj["centre_namem"] = "KOLKATA"
            elif json_obj["centre_name"] == "MUMBAI":
                json_obj["centre_name"] = "MUMBAI"

            #Append modified record to final object
            final_json.append(json_obj)

    return final_json

#Return Potato Data
@server.route('/potato')
def create_json_obj_potato():
   resp =  create_json_potato()
   return json.dumps(resp)

#Filter out data from JSON and select data for potato
def create_json_potato():
    # Create empty list
    final_json = []

    #Read potato.json file and assign values to variable
    with open('./potato.json') as f:
        potato = json.load(f)

    #create JSON object for each record
    for i in range(len(potato)):
        json_obj = potato[str(i)]
        if json_obj["commodity_name"] == "Potato" and (json_obj["centre_name"] == "DELHI" or json_obj["centre_name"] == "KOLKATA" or json_obj["centre_name"] == "MUMBAI"):
            json_obj["commodity_name"] = 'Potato'

            #Modify centre names
            if json_obj["centre_name"] == "DELHI":
                json_obj["centre_name"] = "DELHI"
            elif json_obj["centre_name"] == "KOLKATA":
                json_obj["centre_namem"] = "KOLKATA"
            elif json_obj["centre_name"] == "MUMBAI":
                json_obj["centre_name"] = "MUMBAI"

            final_json.append(json_obj)

    return final_json

#Return Onion Data
@server.route('/onion')
def create_json_obj_onion():
   resp =  create_json_onion()
   return json.dumps(resp)

#Filter out data from JSON and select data for onion
def create_json_onion():
    # Create empty list
    final_json = []

    #Read onion.json file and assign values to variable
    with open('./onion.json') as f:
        onion = json.load(f)

    #create JSON object for each record
    for i in range(len(onion)):
        json_obj = onion[str(i)]
        if json_obj["commodity_name"] == "Onion" and (json_obj["centre_name"] == "DELHI" or json_obj["centre_name"] == "KOLKATA" or json_obj["centre_name"] == "MUMBAI"):
            json_obj["commodity_name"] = 'Onion'

            #Modify centre names
            if json_obj["centre_name"] == "DELHI":
                json_obj["centre_name"] = "DELHI"
            elif json_obj["centre_name"] == "KOLKATA":
                json_obj["centre_namem"] = "KOLKATA"
            elif json_obj["centre_name"] == "MUMBAI":
                json_obj["centre_name"] = "MUMBAI"

            final_json.append(json_obj)

    return final_json

#Return Cabbage Data
@server.route('/cabbage')
def create_json_obj_cabbage():
   resp =  create_json_cabbage()
   return json.dumps(resp)

#Filter out data from JSON and select data for cabbage
def create_json_cabbage():
    # Create empty list
    final_json = []

    #Read cabbage.json file and assign values to variable
    with open('./cabbage.json') as f:
        cabbage = json.load(f)

    #create JSON object for each record
    for i in range(len(cabbage)):
        json_obj = cabbage[str(i)]
        if json_obj["commodity_name"] == "Cabbage" and (json_obj["centre_name"] == "DELHI" or json_obj["centre_name"] == "KOLKATA" or json_obj["centre_name"] == "MUMBAI"):
            json_obj["commodity_name"] = 'Cabbage'

            #Modify centre names
            if json_obj["centre_name"] == "DELHI":
                json_obj["centre_name"] = "DELHI"
            elif json_obj["centre_name"] == "KOLKATA":
                json_obj["centre_namem"] = "KOLKATA"
            elif json_obj["centre_name"] == "MUMBAI":
                json_obj["centre_name"] = "MUMBAI"

            final_json.append(json_obj)

    return final_json

#Return Brinjal Data
@server.route('/brinjal')
def create_json_obj_brinjal():
   resp =  create_json_brinjal()
   return json.dumps(resp)

#Filter out data from JSON and select data for brinjal
def create_json_brinjal():
    # Create empty list
    final_json = []

    #Read brinjal.json file and assign values to variable
    with open('./brinjal.json') as f:
        brinjal = json.load(f)

    #create JSON object for each record
    for i in range(len(brinjal)):
        json_obj = brinjal[str(i)]
        if json_obj["commodity_name"] == "Brinjal" and (json_obj["centre_name"] == "DELHI" or json_obj["centre_name"] == "KOLKATA" or json_obj["centre_name"] == "MUMBAI"):
            json_obj["commodity_name"] = 'Brinjal'
            
            #Modify centre names
            if json_obj["centre_name"] == "DELHI":
                json_obj["centre_name"] = "DELHI"
            elif json_obj["centre_name"] == "KOLKATA":
                json_obj["centre_namem"] = "KOLKATA"
            elif json_obj["centre_name"] == "MUMBAI":
                json_obj["centre_name"] = "MUMBAI"

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

if __name__ == '__main__':
    server.run()
