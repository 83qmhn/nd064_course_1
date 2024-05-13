from flask import Flask
from flask import json
from flask.logging import create_logger

app = Flask(__name__)

logger = create_logger(app)

@app.route('/status')
def status():
    response = app.response_class(
        response=json.dumps({"result":"OK - healthy"}),
        status=200,
        mimetype='application/json'
    )

    logger.info('Status request successful')
    logger.debug('DEBUG message')
    return response

@app.route('/metrics')
def metrics():
    response = app.response_class(
        response=json.dumps({"status":"success","code":0,"data":{"UserCount":140,"UserCountActive":23}}),
        status=200,
        mimetype='application/json'
    )
    logger.info('Metrics request successful')
    return response

@app.route("/")
def hello():
    logger.info('Main request successful')
    return "Hello World!"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
