from flask import Flask
from flask import render_template
from pymongo import MongoClient
import json
from bson import json_util
from bson.json_util import dumps
from random import randint

	
#import matplotlib.pyplot as plt  
#from sklearn.cluster import KMeans
#import sklearn.metrics as sm
#from sklearn.decomposition import PCA

#import pandas as pd 
#import numpy as np

app = Flask(__name__)

MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017
DBS_NAME = 'chinair'
COLLECTION_NAME = 'march'
FIELDS = { '_id': False}

 

@app.route("/")
def index(): 
	return render_template("map.html")

@app.route("/map.html")
def map(): 
	return render_template("map.html")

@app.route("/correlation.html")
def correlation(): 
	return render_template("correlation.html")

	

@app.route("/d3-min.js")
def d3min():
	print("heedddddddddddddddddddddddddddddd")
	return render_template("d3-min.js")

@app.route("/parallel.csv")
def parallelcsv():
	print("heedddddddddddddddddddddddddddddd")
	return render_template("parallel.csv")



@app.route("/chinair.json")
def chinair():
	connection = MongoClient(MONGODB_HOST, MONGODB_PORT)
	collection = connection[DBS_NAME][COLLECTION_NAME]
	data_chinair = collection.find(projection=FIELDS)
	json_chinair = []
	for d in data_chinair:
		json_chinair.append(d) 
	json_chinair = json.dumps(json_chinair, default=json_util.default)  
	connection.close() 
	return json_chinair

@app.route("/station_locations.json")
def stationLocs():
	connection = MongoClient(MONGODB_HOST, MONGODB_PORT)
	collection = connection[DBS_NAME]["locations"]
	data_chinair = collection.find(projection=FIELDS)
	json_locations = []
	for d in data_chinair:
		json_locations.append(d) 
	json_locations = json.dumps(json_locations, default=json_util.default)  
	connection.close() 
	return json_locations

if __name__ == "__main__":
	app.run(host='0.0.0.0',port=5000,debug=True)

