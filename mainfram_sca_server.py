from flask import Flask,request,jsonify
from pymongo import MongoClient
import json
from pprint import pprint
client = MongoClient()
db = client['test-database']

app = Flask(__name__)

# print(db.list_collection_names())

def cleanup_method(mongo_query_result):
    del mongo_query_result['_id']
    return mongo_query_result



@app.route('/api/v1/masterInventory',methods = ['GET'])
def masterInventory():
    ite = db.config.XYZ_COMPANY_METADATA.find({'type': 'Master-Inventory'})[0]
    ##print(json.dumps(ite))
    return jsonify(cleanup_method(ite))

@app.route('/api/v1/crossReference',methods = ['GET'])
def crossReference():
    ite = db.config.XYZ_COMPANY_METADATA.find({'type': 'Cross-Ref'})[0]
    #del ite['_id']
    #print(json.dumps(ite))
    return jsonify(cleanup_method(ite))

@app.route('/api/v1/CRUD',methods = ['GET'])
def CRUD():
    ite = db.config.XYZ_COMPANY_METADATA.find({'type': 'Crud'})[0]
    #print(json.dumps(ite))
    return jsonify(cleanup_method(ite))

@app.route('/api/v1/orphanReport',methods = ['GET'])
def orphanReport():
    ite = db.config.XYZ_COMPANY_METADATA.find({'type': 'Orphan-Report'})[0]
    #print(json.dumps(ite))
    return jsonify(cleanup_method(ite))

@app.route('/api/v1/missingComponents',methods = ['GET'])
def missingComponents():
    ite = db.config.XYZ_COMPANY_METADATA.find({'type': 'Missing-Components'})[0]
    #print(json.dumps(ite))
    return jsonify(cleanup_method(ite))

if __name__ == '__main__':
   app.run(debug = True,host= '0.0.0.0')