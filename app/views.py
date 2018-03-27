# views.py

from flask import Flask, render_template, flash, request
from app import app

from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField

import os, sys

from datetime import datetime
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Now you can import your module
import projects

import ships

class ReusableForm(Form):
    name = TextField('Name:', validators=[validators.required()])

@app.route('/')
def index():
    return render_template("index.html")

# @app.route('/about')
# def about():
#     return render_template("about.html")
    
@app.route('/compsci', methods=['GET','POST'])
#@app.route('/', methods=['GET','POST'])
def project():
    
    selectedProject = request.args.get('project')
    
    #TODO: add in validation from here https://pythonspot.com/flask-web-forms/ or here https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iii-web-forms
    #form = ReusableForm(request.form)
   
    #print form.errors
    if request.method == 'POST':
        
        if selectedProject == 'collatz':
            limit=request.form['limit']
            #print limit
            #print(type(limit))
            #time.sleep(10)
            steps = projects.collatz(float(limit))
            
            return render_template("compsci.html", project = selectedProject, steps = steps)
            
        elif selectedProject == 'hoffman':
            string = request.form['string']
            encodedString = projects.hoffman(string)
            
            if encodedString:
                return render_template("compsci.html", project = selectedProject, encodedString = encodedString)
        
        elif selectedProject == 'fizzbuzz':
            limit = float(request.form['limit'])
            method = request.form['method']
            startTime = datetime.now()
            startTime = startTime.microsecond
            results = projects.fizzbuzz(method, limit)
            endTime = datetime.now()
            endTime = endTime.microsecond
            
            print(endTime-startTime)
            
            if type(results) is 'list':
                return render_template("compsci.html", project = selectedProject, results_list = results, time = (endTime-startTime))
            else:
                return render_template("compsci.html", project = selectedProject, results = results, time = (endTime-startTime))
 
        # if form.validate():
        #     # Save the comment here.
        #     flash('Hello ' + name)
        # else:
        #     flash('All the form fields are required. ')
    
    return render_template("compsci.html", project = selectedProject)
    
@app.route('/ships')
def list():
    listType = request.args.get('listType')
    
    if listType == 'pmvShips':
        listEntries = ships.getPMVShips()
    elif listType == 'pmvShipTypes': 
        listEntries = ships.getPMVShipTypes()
    # elif listType == 'pilotShips': 
    #     listEntries = ships.getPilotShips()
    else: 
        listType = 'pmvShips'
        listEntries = ships.getPMVShips()
    
    return render_template('ships.html', listEntries=listEntries, listType=listType)