#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
EGE DOGAN DURSUN
WEB SCRAPING PROJECT

LANGUAGE: PYTHON 3.*
API FRAMEWORK: FLASK

"""

#Import Flask library for API design
from flask import Flask
from flask import request
app = Flask(__name__)

#Import Couch DB library to use it as a database
import couchdb  


#Launch Couch DB server
couch = couchdb.Server()  

#Admin credentials, normally, it shouldn't be hardcoded and used with authorisation
couch.resource.credentials = ("admin", "cosmos")

#Database connection
db = couch["db_web_scraping"]

#Search by ID
@app.route('/search/search_by_id/<query_id>')
def search_by_id(query_id):
    results = []
    for doc in db.find({'selector': {'product_id': query_id}}):
        results.append(dict(doc))
    return str(results)


#Search by Title
@app.route('/search/search_by_title/<query_title>')
def search_by_title(query_title):
    results = []
    for doc in db.find({'selector': {'title' : query_title}}):
        results.append(dict(doc))
    return str(results)


#Search by Description
@app.route('/search/search_by_description/<query_description>')
def search_by_description(query_description):
    results = []
    for doc in db.find({'selector': {'description' : query_description}}):
        results.append(dict(doc))
    return str(results)


#Search by Product Category
@app.route('/search/search_by_category/<query_category>')
def search_by_category(query_category):
    results = []
    for doc in db.find({'selector': {'product_category' : query_category}, 'limit': 9999}):
        results.append(dict(doc))
    return str(results)


#Search by Colour
@app.route('/search/search_by_colour/<query_colour>')
def search_by_colour(query_colour):
    results = []
    for doc in db.find({'selector': {'colour' : query_colour}, 'limit': 9999}):
        results.append(dict(doc))
    return str(results)


#Search by Price Range
@app.route('/search/search_by_price/<query_price_low>&<query_price_high>')
def search_by_price(query_price_low, query_price_high):
    results = []
    for doc in db.find(
            {'selector': 
                {'prices.price' : 
                    {'$gt' : float(query_price_low), 
                     '$lt' : float(query_price_high)}
                    }, 
                    'limit': 9999
                }):
        results.append(dict(doc))
    return str(results)

#Search by Multiple Parameters
@app.route('/search/multiple_search')
def search_by_multiple_parameters():
    description = request.args.get('description')
    price_low = request.args.get('price_low')
    price_high = request.args.get('price_high')
    colour = request.args.get('colour')
    
    if price_low == None:
        price_low = 0
    if price_high == None:
        price_high = 99999
    
    results = []
    if (description is not None) and (colour is not None):
        for doc in db.find(
                {'selector':
                    {'prices.price' :
                        {'$gt' : int(price_low),
                        '$lt' : int(price_high)},
                     'description' : description,
                     'colour' : colour
                    },
                    'limit': 9999}):
            results.append(dict(doc))
    elif (description is not None) and (colour is None):
        for doc in db.find(
                {'selector':
                    {'prices.price' :
                        {'$gt' : int(price_low),
                        '$lt' : int(price_high)},
                     'description' : description
                    },
                    'limit': 9999}):
            results.append(dict(doc))
    elif (description is None) and (colour is not None):
        for doc in db.find(
                {'selector':
                    {'prices.price' :
                        {'$gt' : int(price_low),
                        '$lt' : int(price_high)},
                     'colour' : colour
                    },
                    'limit': 9999}):
            results.append(dict(doc))
    elif (description is None and colour is None):
        for doc in db.find(
                {'selector':
                    {'prices.price' :
                        {'$gt' : int(price_low),
                        '$lt' : int(price_high)}
                    },
                    'limit': 9999}):
            results.append(dict(doc))
    return str(results)

#Run the api
if __name__ == '__main__':
   app.run()
