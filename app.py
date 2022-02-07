from flask import Flask, render_template, request
import pickle

model = pickle.load(open('crops_demand.pkl', 'rb'))

app = Flask(__name__)

@app.route('/predict',methods=['POST'])
def predict():
#    print(request.form)
    year = request.form.get('year')
    crop = request.form.get('crop')
    population = request.form.get('population')
    demand = request.form.get('demand')

    result = model.predict([[year, crop, population, demand]])[0]
    response = {"result": result}
    return response
