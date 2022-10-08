from flask import Flask, jsonify, request
import json

app = Flask(__name__)


@app.route('/doctor', methods=['POST'])
def get_drugs():
    data = request.get_json()
    diseases = data["diseases"]
    exclude_list = data["excludeList"]

    return jsonify({
        "recommendedDrugs": [
            {
                "drugName": "drugName1",
                "substanceName": "substanceName1",
                "diseases": [
                    "diseasesName1",
                    "diseasesName2"
                ],
                "activeCompounds": [
                    "compounds1",
                    "compounds2"
                ]
            },
            {
                "drugName": "drugName2",
                "substanceName": "substanceName2",
                "diseases": [
                    "diseasesName1",
                    "diseasesName2"
                ],
                "activeCompounds": [
                    "compounds1",
                    "compounds2"
                ]
            }
        ],
        "otherRecommendations": [
            [
                {
                    "drugName": "drugName1",
                    "substanceName": "substanceName1",
                    "diseases": [
                        "diseasesName1",
                        "diseasesName2"
                    ],
                    "activeCompounds": [
                        "compounds1",
                        "compounds2"
                    ]
                },
                {
                    "drugName": "drugName2",
                    "substanceName": "substanceName2",
                    "diseases": [
                        "diseasesName1",
                        "diseasesName2"
                    ],
                    "activeCompounds": [
                        "compounds1",
                        "compounds2"
                    ]
                }
            ],
            [
                {
                    "drugName": "drugName1",
                    "substanceName": "substanceName1",
                    "diseases": [
                        "diseasesName1",
                        "diseasesName2"
                    ],
                    "activeCompounds": [
                        "compounds1",
                        "compounds2"
                    ]
                },
                {
                    "drugName": "drugName2",
                    "substanceName": "substanceName2",
                    "diseases": [
                        "diseasesName1",
                        "diseasesName2"
                    ],
                    "activeCompounds": [
                        "compounds1",
                        "compounds2"
                    ]
                }
            ]
        ]
    }
    )


@app.route('/patient', methods=['GET'])
def add_income():
    data = request.get_json()
    return jsonify("dupa")


if __name__ == '__main__':
    app.run(debug=True)
