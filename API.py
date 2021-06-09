from flask import Flask
from flask import request
from flask import jsonify
import model
import requests
import os

modelo=None

def create_app():
    app = Flask(__name__)
    #Trainning model
    global modelo
    modelo=model.modelTraining()
    return app
app = create_app()

@app.route('/api/pothole/', methods=['POST'])
def verify_pothole():
    data = request.get_json()
    windows = model.createWindows([data]) 
    locations = model.potholeOrNotPothole(modelo,windows)
    response = {'locations': locations}
    #api_crud = os.getenv('API_CRUD')
    api_crud = "http://129.146.169.60:1441"
    r_api_crud =requests.post(api_crud+"/api/potholes/", json=response)
    return jsonify(response), 200

@app.route('/', methods=['GET'])
def testing():
    return jsonify({'message':'connected'}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
