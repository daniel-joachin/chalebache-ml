from flask import Flask
from flask import request
from flask import jsonify
import model
import requests
import os


def create_app():
    app = Flask(__name__)
    return app

app = create_app()

@app.route('/api/pothole/', methods=['POST'])
def verify_pothole():
    data = request.get_json()
    windows = model.createWindows(data) 
    locations = model.potholeOrNotPothole(windows)
    response = {'locations': locations}
    api_crud = os.getenv('API_CRUD')
    r_api_crud =requests.post(api_crud, data=response)
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True)
