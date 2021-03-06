#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
EGE DOGAN DURSUN
WEB SCRAPING PROJECT

LANGUAGE: PYTHON 3.*
DB TECHNOLOGY: COUCH DB

"""

#Import Couch DB library to use it as a database
import couchdb  

#Import json for json operations
import json

#Launch Couch DB server
couch = couchdb.Server()  

#Admin credentials, normally, it shouldn't be hardcoded and used with authorisation
couch.resource.credentials = ("admin", "cosmos")
  
#Create the database as a storage for product information
db = couch.create('db_web_scraping')  
print("Database created");  

#Read the output data json file that was generated by the scraper module
with open('data_output.json', 'r') as myfile:
    data=json.load(myfile)

#Insert the data to the database
for i in range(0, len(data)):    
    db.save(data[i])
print("Products have been successfully inserted...")


  





