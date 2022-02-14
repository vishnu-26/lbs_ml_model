from flask import Flask, render_template, request
import pandas as pd
import pickle
import datetime

model = pickle.load(open('demo.pkl', 'rb'))

app = Flask(__name__)

@app.route('/predict',methods=['POST'])
def predict():
#    print(request.form)
    year = datetime.date.today().year
    crop = int(request.form.get('crop'))
#    population = request.form.get('population')
#    demand = request.form.get('demand')

    data = pd.read_csv('Crops  - Merged Data.csv')
    print(data[data["crop (paddy-0, wheat-1, jowar-2, bajra-3, arhar-4, onion-5)"]==crop])

    demand_per_person = data[data["crop (paddy-0, wheat-1, jowar-2, bajra-3, arhar-4, onion-5)"]==crop]['demand per person(kg)']


    print(demand_per_person)
    demand_per_person = demand_per_person[crop*5]
    print(demand_per_person)

    population = model.predict([[year]])[0]
    
    total_demand = ((population*demand_per_person)/1000).round(4)
#    print(po)
    response = {"total_demand": total_demand}
    return response
