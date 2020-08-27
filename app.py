
import datetime as dt
import numpy as np
import pandas as pd
 

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, render_template, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import create_classes


#https://stackabuse.com/using-sqlalchemy-with-flask-and-postgresql/
app = Flask(__name__, static_url_path='/static',template_folder="templates")
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://postgres:Welcome102!@localhost:5432/meteorites_db'
db = SQLAlchemy(app)
meteorites = create_classes(db)
migrate = Migrate(app, db)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/bar")
def bar():
        return render_template('barchart.html')

@app.route("/bubble")
def bubble():
        return render_template('bubblechart.html')

@app.route("/map")
def map():
        return render_template('impactmap.html')

@app.route("/data-table")
def data():
        return render_template('data-table.html')

@app.route("/raw-data")
def data_pull():
        results = db.session.query(meteorites.id, meteorites.name, meteorites.recclass, meteorites.mass, meteorites.fall, meteorites.year, meteorites.reclat, meteorites.reclong, meteorites.maincategory).all()
        # initialize dictionary 
        data = []
        for result in results:
                d = {"id":result[0], "name":result[1], "recclass" : result[2], "mass" : result[3], "fall" : result[4], "year" : result[5], "reclat" : result[6], "reclong" : result[7], "maincategory" : result[8]} 
                data.append(d)
        json_data = jsonify(data)
        return json_data

if __name__ == '__main__':
    app.run()