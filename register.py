from ApiCloud import ApiCloud
from CSVDump import *
from db import *
from datetime import *
import time
import sys
import mysql.connector
# First we set our credentials

from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
app = Flask(__name__)
app.debug = True
cnx = mysql.connector.connect(user='root', password='my-secret-pw',
                              host='mysql',)
cursor = cnx.cursor()
create_database(cnx,cursor)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/Sub')
def sub_page():
    return 'Sub Page'    

@app.route('/register', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username= request.form['username']
        password= request.form['password']
# From the developer portal
        client_id = 'aecobley@dundee.ac.uk'
        client_secret = 'jFYfw3jQZOrAWZ675nhV4JMNapN5WCEZAG5fyN0rPA7sTz3x'

        api = ApiCloud(client_id, client_secret)
        api.login(username, password)
        print api
        cnx = mysql.connector.connect(user='root', password='my-secret-pw',host='mysql',)
        cursor = cnx.cursor()
        insert_user(cnx,cursor,username,api["access_token"])
        print api["access_token"]
        return api["access_token"]
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)

if __name__ == '__main__':
    app.run(host='0.0.0.0')


