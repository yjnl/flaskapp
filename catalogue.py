from datetime import *
import time
import sys

import json
import requests
# First we set our credentials

from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
app = Flask(__name__)
app.debug = True

@app.route('/Video/<video>')
def video_page(video):
    print (video)
    url = 'http://34.67.41.89/myflix/videos?filter={"video.uuid":"'+video+'"}'
    headers = {}
    payload = json.dumps({ })
    print (request.endpoint)
    response = requests.get(url)
    print (url)
    if response.status_code != 200:
      print("Unexpected response: {0}. Status: {1}. Message: {2}".format(response.reason, response.status, jResp['Exception']['Message']))
      return "Unexpected response: {0}. Status: {1}. Message: {2}".format(response.reason, response.status, jResp['Exception']['Message'])
    jResp = response.json()
    print (type(jResp))
    print (jResp)
    for index in jResp:
        for key in index:
           if (key !="_id"):
              print (index[key])
              for key2 in index[key]:
                  print (key2,index[key][key2])
                  if (key2=="Name"):
                      video=index[key][key2]
                  if (key2=="file"):
                      videofile=index[key][key2]
                  if (key2=="pic"):
                      pic=index[key][key2]
    return render_template('video.html', name=video,file=videofile,pic=pic)

@app.route('/')
def cat_page():
    url = "http://34.67.41.89/myflix/videos"
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
    print (type(jResp))
    
    # Getting the categories
    categories = []
    caturl = "http://34.67.41.89/myflix/categories"
    catresponse = requests.get(caturl)
    catjResp = catresponse.json()
    for catindex in catjResp:
        for catkey in catindex:
            if (catkey != "_id"):
                categories.append(catindex[catkey].capitalize())
    categories = sorted(categories)
   
    html="<h1>MyFlix</h1>"
    
    for categ in categories:
        # is this the first item being added for this category? if so, change the css style
        first = True
        
        html += '<h2 style="clear:both">' + categ + '</h2>'
        
        for index in jResp:
           #print (json.dumps(index))
           print ("----------------")
           for key in index:

               if (key !="_id"):
                  print (index[key])
                  for key2 in index[key]:
                      if (key2=="Name"):
                          name=index[key][key2]
                      if (key2=="thumb"):
                          thumb=index[key][key2]
                      if (key2=="uuid"):
                          uuid=index[key][key2]
                      if (key2=="category" and index[key][key2] == categ.lower()):
                          if first:
                            html += '<div style="clear:both; float: left">'
                            first = False
                          else:
                            html += '<div style="float: left">'
                          
                          html=html+'<h3>'+name+'</h3>'
                          ServerIP=request.host.split(':')[0]
                          html=html+'<a href="http://'+ServerIP+'/Video/'+uuid+'">'
                          html=html+'<img src="http://34.134.202.10/pics/'+thumb+'">'
                          html=html+"</a>"        
                          html += '</div>'
                          print("=======================")

    return html


if __name__ == '__main__':
    app.run(host='0.0.0.0',port="5000")
