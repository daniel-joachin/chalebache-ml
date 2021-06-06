from flask import Flask
from flask import request
from flask import jsonify
import model
import requests

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
    r_apiJoachin =requests.post("http://localhost:3030/api/potholes/", data=response)
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True)
