from flask import Flask
import os

app = Flask(__name__)

conf_location='/etc/aerospike/aerospike.conf'

@app.route('/conf')
def index():
    return open(conf_location,"r").read()

@app.route('/shutdown')
def shutdown():
    os._exit(0)
    return 'Ok'
