from waitress import serve
from flaskserver import app

port=3022

serve(app,host='0.0.0.0',port=port)