from flask import Flask, render_template, request, jsonify, make_response, after_this_request, Response
import pandas as pd
import pickle
import datetime
import json
from flask_cors import CORS, cross_origin


model = pickle.load(open('demo.pkl', 'rb'))

app = Flask(__name__)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/predict',methods=['POST'])
@cross_origin()
def predict():
#    print(request.form)
    year = datetime.date.today().year

    # print(request.data)
    data = json.dumps(request.data.decode('utf-8'))
    print(data)
    crop = int(data[-3])

    # crop = int(request.form.get('crop'))
#    population = request.form.get('population')
#    demand = request.form.get('demand')

    data = pd.read_csv('Crops  - Merged Data.csv')
    print(data[data["crop (paddy-0, wheat-1, jowar-2, bajra-3, arhar-4, onion-5)"]==crop])

    demand_per_person = data[data["crop (paddy-0, wheat-1, jowar-2, bajra-3, arhar-4, onion-5)"]==crop]['demand per person(kg)']


    print(demand_per_person)
    demand_per_person = demand_per_person[crop*5]
    print(demand_per_person)

    population = model.predict([[year]])[0]

    demand = ((population*demand_per_person)/1000).round(4)
#    print(po)



    response = jsonify({"total_demand": demand})
    # response.headers.add("Access-Control-Allow-Origin", 'http://localhost:3000')
    return response
