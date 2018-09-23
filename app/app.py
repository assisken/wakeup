import os
import subprocess as sp

from flask import Flask, request, Response
from flask_ini import FlaskIni

BASE = os.path.dirname(os.path.abspath(__name__))
app = Flask(__name__)
with app.app_context():
    app.iniconfig = FlaskIni()
    app.iniconfig.read(f'{BASE}/config.ini')


@app.route('/wakeup', methods=['GET'])
def hello_world():
    mac = request.args.get('mac', None)
    host = request.args.get('host', None)
    if not mac or not host:
        return Response('Missing required arguments.', status=403)

    sp.run(f'{BASE}/scripts/wakeup.sh {mac} {host}', shell=True)
    return Response('Success')
