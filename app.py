# -*- coding: utf-8 -*-
"""
Created on Tue Oct 06 14:13:33 2015

@author: Nayak
"""

from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello! Welcome to the list of CSE Courses Website."
    
@app.route("/user/<username>")
def xxxxxx(username):
    return render_template('profile.html', name=username)
    
@app.route("/lotsofdata")
def people():
    CSE_Courses = {'Web_Data_Management': 5335, 'Data_Mining':5334, 'Databases': 5330, 'Software_Engg_2':5325,
    'Software_Metrics':6329, 'Machine_Learning':6363, 'Computer_Architecture':5350, 'Distributed_Systems':5306,
    'Algorithms':5311, 'Advanced_Topics_SE':5320, 'Computer_Networks':5344}
    #url = 'http://api.wunderground.com/api/8e89fd3aa8eea48f/geolookup/conditions/q/TX/Arlington.json'
    #f = urllib2.urlopen(url)
    #json_string = f.read()
    #parsed_json = json.loads(json_string)    
    #f.close()
    return jsonify(**CSE_Courses)
    
if __name__ == "__main__":
    app.run(debug=True)
    app.run(host = "127.0.0.1", port = 5000)
    