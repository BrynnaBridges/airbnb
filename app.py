
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
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://postgres:Welcome102!@localhost:5432/airbnb_db'
db = SQLAlchemy(app)
airbnb = create_classes(db)
migrate = Migrate(app, db)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/neighborhoods")
def neighborhoods():
        return render_template('neighborhoods.html')

@app.route("/heatmap")
def heatmap():
        return render_template('heatmap.html')

@app.route("/bedrooms")
def bedrooms():
        return render_template('bedrooms.html')

@app.route("/propertytype")
def propertytype():
        return render_template('propertytype.html')

@app.route("/members")
def members():
        return render_template('members.html')

@app.route("/data-table")
def data():
        return render_template('data-table.html')

@app.route("/raw-data")
def data_pull():
        results = db.session.query(airbnb.index, airbnb.id, airbnb.price, airbnb.host_response_rate, airbnb.neighbourhood_cleansed, airbnb.review_scores_rating, airbnb.cancellation_policy, airbnb.property_type, airbnb.bedrooms).all()
        # initialize dictionary 
        data = []
        for result in results:
                d = {"index":result[0], "id":result[1], "price" : result[2], "host_response_rate" : result[3], "neighbourhood_cleansed" : result[4], "review_scores_rating" : result[5], "cancellation_policy" : result[6], "property_type" : result[7], "bedrooms" : result[8]} 
                data.append(d)
        json_data = jsonify(data)
        return json_data

if __name__ == '__main__':
    app.run()