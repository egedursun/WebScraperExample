#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
EGE DOGAN DURSUN
WEB SCRAPING PROJECT

LANGUAGE: PYTHON 3.*

"""

#Import unit test module to use the test methods
import unit_tests as ut


#Testing the search with ID's
print("TESTING THE SEARCH WITH ID'S \n")
print(ut.test_id_search("1KAK06624EW999") , "\n")
print(ut.test_id_search("1KAK23090EW023") , "\n")
print(ut.test_id_search("1KAK06609EW001") , "\n")
print(ut.test_id_search("1KAK06624EW999") , "\n")
print(ut.test_id_search("dkjsfkjksskjsj") , "\n")

#Testing the search with Titles
print("TESTING THE SEARCH WITH TITLES \n")
print(ut.test_title_search("Düğmeli Cepli Kaban") , "\n")
print(ut.test_title_search("Kapüşonlu Uzun Şişme Mont") , "\n")
print(ut.test_title_search("Kapüşonlu Suni Kürk Detaylı Kapitoneli Şişme Mont") , "\n")
print(ut.test_title_search("Fermuarlı Kaşe Kaban") , "\n")
print(ut.test_title_search("Sonucsuz Title Denemesi") , "\n")

#Testing the search with Description
print("TESTING THE SEARCH WITH DESCRIPTION \n")
print(ut.test_description_search("Fermuarlı, Kaşe Kaban") , "\n")
print(ut.test_description_search("Cepli Kaban") , "\n")
print(ut.test_description_search("Düğmeli Shacket") , "\n")
print(ut.test_description_search("Suni Kürk Detaylı Kaban") , "\n")
print(ut.test_description_search("Sonucsuz Description Denemesi") , "\n")

#Testing the search with Category
print("TESTING THE SEARCH WITH CATEGORY \n")
print(ut.test_category_search("Koton Kadın Giyim Dış Giyim Kaban") , "\n")
print(ut.test_category_search("Sonucsuz Kategori Denemesi") , "\n")

#Testing the search with Colour
print("TESTING THE SEARCH WITH COLOUR \n")
print(ut.test_colour_search("Ekru"), "\n")
print(ut.test_colour_search("Siyah"), "\n")
print(ut.test_colour_search("Lacivert"), "\n")
print(ut.test_colour_search("Sonucsuz Renk Denemesi"), "\n")

#Testing the search with Price Range
print(ut.test_price_search(0, 199.99), "\n")
print(ut.test_price_search(200, 400), "\n")
print(ut.test_price_search(400, 1000), "\n")
print(ut.test_price_search(price_high=300), "\n")
print(ut.test_price_search(price_low=400), "\n")

#Testing the multiple search
print(ut.test_multiple_search("Cepli Kaban", 0, 1000, "Ekru"), "\n")
print(ut.test_multiple_search(price_low=0, price_high=1000, colour="Siyah"), "\n")
print(ut.test_multiple_search(description="Cepli Kaban", price_low=0, price_high=1000), "\n")
print(ut.test_multiple_search(description="Cepli Kaban", colour="Ekru"), "\n")


