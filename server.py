from flask import Flask, jsonify, request
import json
import pandas as pd
import os


app = Flask(__name__)

drugs_interactions_df = pd.read_csv(os.path.join('data','final','drugs_interactions.csv'))
general_info_df = pd.read_csv(os.path.join('data','final','general_info.csv'))


@app.route('/doctor', methods=['POST'])
def get_drugs():
    data = request.get_json()
    diseases = data["diseases"]
    exclude_list = data["excludeList"]

    mock_json = open(os.path.join("contracts", "doctor_module", "response_diseases.json"), "r", encoding='utf-8')
    return json.load(mock_json)

@app.route('/patient', methods=['POST'])
def add_income():
    data = request.get_json()
    patient_drugs_list = data["patientDrugsList"]
    new_drug_name = data["newDrug"].lower()
    patient_drugs_list = [i.lower() for i in patient_drugs_list]

    new_drug_info = general_info_df[general_info_df.drug_name == new_drug_name]

    schema = {
      "drug": None,
      "substance": None,
      "description": None,
      "suggestedReplacement": [],
      "interactions": []
    }
    found_data =list (new_drug_info.loc[:,['drug_name','drug_raw_name','description']].drop_duplicates().to_dict(orient='index').values())
    if found_data != []:
        found_data = found_data[0]
        schema['drug'] = found_data['drug_name']
        schema['substance'] = found_data['drug_raw_name']
        schema['description'] =found_data['description'] if len(found_data['description']) < 100 else found_data['description'][:100]+ '... Read more'

        data = drugs_interactions_df[
            (drugs_interactions_df.drug_name.isin(patient_drugs_list))
            & (drugs_interactions_df.interacting_drug == found_data['drug_raw_name'])
        ]
        found_interacting_data = data.loc[:,['drug_name','interacting_drug','class','interacting_drug_treated_disease']].drop_duplicates()
        found_interacting_data = found_interacting_data.groupby('drug_name').apply(lambda x: x.sample(3)).reset_index(drop=True)
        for _, group in found_interacting_data.groupby('drug_name'):
            if group.shape[0] > 0:
                drug = group['drug_name'].values[0]
                substance = group['interacting_drug'].values[0]
                level = group['class'].values[0]
                diseases =  list(group['interacting_drug_treated_disease'].values)
                schema['interactions'].append({
                    'drug': drug,
                    'level': level,
                    'diseases': diseases
                })



    return schema
    # mock_json = open(os.path.join("contracts", "patient_module", "response_interactions.json"), "r", encoding='utf-8')
    # return json.load(mock_json)


if __name__ == '__main__':
    app.run(debug=True)

    # "Benadryl",
    # "Bunavail",
    # "Diflucan"