#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
EGE DOGAN DURSUN
WEB SCRAPING PROJECT

LANGUAGE: PYTHON 3.*
SCRAPING FRAMEWORK: BEAUTIFULSOUP

"""

#The library that will be used for information retrieval from the website
from requests import get

#Import BeautifulSoup library for scraping information from HTML documents
from bs4 import BeautifulSoup

#Import json library for list to json operations
import json


"""
SCRAPING THE PRODUCT LIST

"""

#Retrieve the HTML information from the website
response = get("https://www.koton.com/tr/kadin/giyim/dis-giyim/kaban/c/M01-C02-N01-AK104-K100071")
response.encoding = "utf-8"

#Instantiate the BeautifulSoup object
html_soup = BeautifulSoup(response.text, "html.parser")

#Retrieve all items with "div" tag as well as a class name that contains "product-item"
posts = html_soup.find_all("div", class_="product-item")

#Retrieve the links from the response and take the href values to achieve the links for different products
links = []
for post in posts:
    for a in post.find_all("a", href=True):
        if a["href"] not in links:
            links.append(a["href"])

#Remove the duplicate products from the list by removing the links with query parameters
concatenated_links = []
for link in links:
    if "productPosition" not in link:
        link = "https://www.koton.com" + link
        concatenated_links.append(link)

#Print the total amount of products retrieved
print("Total Number of Items Retrieved: ", len(concatenated_links))


"""
SCRAPING THE PRODUCT INFORMATION FROM THE PRODUCT PAGES BY USING THE LINKS
"""

#
products = []
for link in concatenated_links:
    product = {}
    response = get(link)
    response.encoding = "utf-8"
    soup = BeautifulSoup(response.text, "html.parser")
    
    #Retrieving product ID
    product_id = soup.find("span", class_="productNumber").contents[0]
    product["product_id"] = product_id.strip()
    
    #Retrieving product title
    title = soup.find("h1").contents[0]
    product["title"] = title.strip()
    
    #Retrieving product description
    description = soup.find("div", class_="product-details").find("p", class_="alt-text").contents[0]
    product["description"] = description.strip()
    
    #Retrieving product image URIs
    images = []
    image_div = soup.find("div", class_="detailShowcaseContainer").find_all("img", class_="current")
    
    for image_l in image_div:
        image_src = image_l.get("alt-src")
        image_src_dict = {"uri" : image_src}
        images.append(image_src_dict)
    
    product["images"] = images
    
    #Retrieving the publishing date of the product
    """
    Couldn't find any information about the publishing date of the products
    """
    
    #Retrieve product category
    category = soup.find("div", class_="product-content-wrap").find("input", {"id" : "pdpProductCategory"})["value"]
    product["product_category"] = category.strip()
    
    #Retrieve product colour
    colour = soup.find("div", class_="color").find("span", class_="title").contents[0].strip()[6:]
    product["colour"] = colour
    
    #Price and the currency of the product / status of discount
    discount = False
    price = soup.find("div", class_="price")
    
    prices_dict = {}
    if price.find("span", class_="insteadPrice") is not None:
        discount = True
        price_data = price.find("span", class_="insteadPrice").find("s").contents[0].strip()
    else:
        price_data = price.find("span", class_="normalPrice").contents[0].strip()
    
    prices_dict["price"] = float(price_data[1:].replace(",","."))
    prices_dict["currency"] = price_data[:1]
        
    product["prices"] = prices_dict
    
    
    #Status of any active discounts on the product
    product["discount"] = discount
    
    
    #Sizes for the product, the general status of the inventory, and the individual inventory status for different sizes
    sizes = []
    
    size_info = soup.find("ul", class_="size-items").find_all("li")
    
    general_stock_condition = True
    
    if len(size_info) != 0:
        for size_l in size_info:
            size_dict = {}
            size_l = size_l.contents
            size_name = size_l[1].get_text().strip()
            
            #If inventory is larger than 0, it will return true, otherwise false.
            stock_condition = (int(size_l[1].get("stocklevel")) > 0)
            
            size_dict["size_name"] = size_name
            size_dict["in_stock"] = stock_condition
            sizes.append(size_dict)
            
    else:
        general_stock_condition = False
        #print("no general stock!")
    
    product["sizes"] = sizes    
    
    product["in_stock"] = general_stock_condition
        
    
    #Add the product to the product list
    products.append(product)
    print(product)
    
"""
SAVE THE RETRIEVED DATA IN A .CSV FILE / FILE OUTPUT
"""

#Save the data in json format in a file named data_output. It will be used for retrieval and database operations later
json_data = json.dumps(products, ensure_ascii=False)
with open('data_output.json', 'w', encoding="utf-8") as f:
    f.write(json_data)
    
