
from db import *
from datetime import *
import time
import sys
import mysql.connector
import json
import requests
# First we set our credentials

from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
app = Flask(__name__)
app.debug = True
cnx = mysql.connector.connect(user='root', password='dacjd156n.',host='some-mysql')
cursor = cnx.cursor()
create_database(cnx,cursor)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/Sub')
def sub_page():
    url = "http://35.198.152.126/myflix/videos"
    headers = {}
    payload = json.dumps({ })

    response = requests.get(url)
    #print (response)
    # exit if status code is not ok
    print (response)
    print (response.status_code)
    if response.status_code != 200:
      print("Unexpected response: {0}. Status: {1}. Message: {2}".format(response.reason, response.status, jResp['Exception']['Message']))
      return "Unexpected response: {0}. Status: {1}. Message: {2}".format(response.reason, response.status, jResp['Exception']['Message'])
    jResp = response.json()
    print (jResp)
    return 'Sub Page'+response.status_code

@app.route('/register', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username= request.form['username']
        password= request.form['password']

        cnx = mysql.connector.connect(user='root', password='dacjd156n.',host='some-mysql')
        cursor = cnx.cursor()
        insert_user(cnx,cursor,username,password)

        return redirect(url_for('login'))
    return render_template('login.html', error=error)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port="5000")
