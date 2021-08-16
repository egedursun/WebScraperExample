#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
EGE DOGAN DURSUN
WEB SCRAPING PROJECT

LANGUAGE: PYTHON 3.*

"""

from flask import Flask
app = Flask(__name__)

#Import Couch DB library to use it as a database
import couchdb  

#Launch Couch DB server
couch = couchdb.Server()  

#Admin credentials, normally, it shouldn't be hardcoded and used with authorisation
couch.resource.credentials = ("admin", "cosmos")

#Reach the created database
db = couch["db_web_scraping"]

#Tests for ID Search
def test_id_search(_id):
    results = []
    for doc in db.find({'selector': {'product_id': _id}}):
        results.append(dict(doc))
    if len(results) == 0:
        return "There is no data with the given ID."
    return results
        
    
#Tests for Title Search
def test_title_search(title):
    results = []
    for doc in db.find({'selector': {'title' : title}}):
        results.append(dict(doc))
    if len(results) == 0:
        return "There is no data with the given Title."
    return results
    

#Tests for Description Search
def test_description_search(description):
    results = []
    for doc in db.find({'selector': {'description' : description}}):
        results.append(dict(doc))
    if len(results) == 0:
        return "There is no data with the given Description."
    return results
    

#Tests for Product Category Search
def test_category_search(category):
    results = []
    for doc in db.find({'selector': {'product_category' : category}, 'limit': 9999}):
        results.append(dict(doc))
    if len(results) == 0:
        return "There is no data with the given Category."
    return results


#Tests for Colour Search
def test_colour_search(colour):
    results = []
    for doc in db.find({'selector': {'colour' : colour}, 'limit': 9999}):
        results.append(dict(doc))
    if len(results) == 0:
        return "There is no data with the given Colour."
    return results
    
    
#Tests for Price Range Search
def test_price_search(price_low=0, price_high=99999):
    results = []
    for doc in db.find(
            {'selector': 
                {'prices.price' : 
                    {'$gt' : price_low, 
                     '$lt' : price_high}
                }, 
                'limit': 9999}):
        results.append(dict(doc))
    if len(results) == 0:
        return "There is no data with the given Price Range."
    return results

#Tests for Multiple Parameter Search
def test_multiple_search(description=None, price_low=0, price_high=99999, colour=None):
    results = []
    if (description is not None) and (colour is not None):
        for doc in db.find(
                {'selector':
                    {'prices.price' :
                        {'$gt' : price_low,
                        '$lt' : price_high},
                     'description' : description,
                     'colour' : colour
                    },
                    'limit': 9999}):
            results.append(dict(doc))
    elif (description is not None) and (colour is None):
        for doc in db.find(
                {'selector':
                    {'prices.price' :
                        {'$gt' : price_low,
                        '$lt' : price_high},
                     'description' : description
                    },
                    'limit': 9999}):
            results.append(dict(doc))
    elif (description is None) and (colour is not None):
        for doc in db.find(
                {'selector':
                    {'prices.price' :
                        {'$gt' : price_low,
                        '$lt' : price_high},
                     'colour' : colour
                    },
                    'limit': 9999}):
            results.append(dict(doc))
    elif (description is None and colour is None):
        for doc in db.find(
                {'selector':
                    {'prices.price' :
                        {'$gt' : price_low,
                        '$lt' : price_high}
                    },
                    'limit': 9999}):
            results.append(dict(doc))
    if len(results) == 0:
        return "There is no data with the given Search Parameters."
    return results