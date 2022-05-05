from flask import Flask
import os

app = Flask(__name__)

conf_location='aerospike.conf'

@app.route('/conf')
def index():
    return open(conf_location,"r").read()

@app.route('/shutdown')
def shutdown():
    os._exit(0)
    return 'Ok'

app.run(host='0.0.0.0', port=81)