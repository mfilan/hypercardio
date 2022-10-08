from flask import Flask, jsonify, request
import json
import os

app = Flask(__name__)


@app.route('/doctor', methods=['POST'])
def get_drugs():
    data = request.get_json()
    diseases = data["diseases"]
    exclude_list = data["excludeList"]

    mock_json = open(os.path.join("contracts", "doctor_module", "response_diseases.json"), "r")
    return json.load(mock_json)

@app.route('/patient', methods=['POST'])
def add_income():
    data = request.get_json()
    patient_drugs_list = data["patientDrugsList"]
    new_drug_name = data["newDrugName"]

    mock_json = open(os.path.join("contracts", "patient_module", "response_interactions.json"), "r")
    return json.load(mock_json)


if __name__ == '__main__':
    app.run(debug=True)
