from flask import Flask
from flask import json

import logging

app = Flask(__name__)

@app.route('/status')
def status():
    response = app.response_class(
            response=json.dumps({"result":"OK - healthy"}),
            status=200,
            mimetype='application/json'
    )

    log('status')

    return response

@app.route('/metrics')
def metrics():
    response = app.response_class(
            response=json.dumps({"status":"success","code":0,"data":{"UserCount":140,"UserCountActive":23}}),
            status=200,
            mimetype='application/json'
    )

    log('metrics')

    return response

@app.route("/")
def hello():
    return "Hello World!"

def log(endpoint_name):
    logging.basicConfig(filename='app.log', format='%(asctime)s, %(message)s', level=logging.DEBUG)
    logging.debug(endpoint_name + ' endpoint was reached')

if __name__ == "__main__":
    app.run(host='0.0.0.0')