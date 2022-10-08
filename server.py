from flask import Flask, jsonify, request
import json

app = Flask(__name__)
f = open('diseases.json')
db = json.load(f)

@app.route('/doctor', methods=['GET'])
def get_drugs():
    data = request.get_json()
    diseases = data["diseases"]

    if "excludeList" in data

    return jsonify()


    {
  "diseases": [
    "diseasesName",
    "diseasesName"
  ],
  "excludeList": [
    "excludeSubstances1",
    "excludeSubstances2"
  ]
}


@app.route('/patient', methods=['GET'])
def add_income():
    data = request.get_json()
    return jsonify("dupa")