#!/usr/bin/env python3
from flask import Flask, render_template, request, jsonify
import json
import math
import random
import json
import requests
import os
app = Flask(__name__)


@app.route('/')
@app.route('/index.htm')
def index():
    return render_template('index.htm')
def doRender(tname, values={}):
	if not os.path.isfile( os.path.join(os.getcwd(), 'templates/'+tname) ): #No such file
		return render_template('index.htm')
	return render_template(tname, **values) 

@app.route('/addnumber')
def add():
    minhistory = 100
    shots = 1000000
    global m
    global n
    m=0
    n=0
    y=request.args.get('y', 0, type=int)
    z= request.args.get('z', 0, type=int)
    t=request.args.get('t', 0, type=int)
    minhistory=y
    shots=z
    sig=t
    api_url="https://uv81at1uxk.execute-api.us-east-1.amazonaws.com/prod/project"
    todo={"y":y, "z":z, "t":t}
    headers={"Content-Type":"application/json"}
    resp=requests.post(api_url, data=json.dumps(todo), headers=headers)
    json_string=resp.json()
    print(json_string)
    return jsonify(result=json_string)

@app.errorhandler(500)
# A small bit of error handling
def server_error(e):
    logging.exception('ERROR!')
    return """
    An  error occurred: <pre>{}</pre>
    """.format(e), 500


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080, debug=True)
