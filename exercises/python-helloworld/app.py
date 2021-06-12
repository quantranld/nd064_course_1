from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/status")
def status():
    return '{"user": "admin", "result": "OK - healthy"}'
    
@app.route("/metrics")
def metrics():
    return '{"user": "admin", "data": {"UserCount": 140, "UserCountActive": 23} }'

# This tells your operating system to listen on all public IPs.
if __name__ == "__main__":
    app.run(host='0.0.0.0')
