from flask import Flask

app = Flask(__name__)

conf_location='aerospike.conf'

@app.route('/conf')
def index():
    return open(conf_location,"r").read()

app.run(host='0.0.0.0', port=81)