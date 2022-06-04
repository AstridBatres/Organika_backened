from crypt import methods
import json
from flask import Flask, abort
from about_me import me
from mock_data import catalog

app= Flask('organika')

@app.route("/", methods=['GET']) #root
def home():
    return "This is the home page!"
    
@app.route("/about")
def about():
  
    #return me["first"] + " " + me["last"]
    return f"{me['first']}{me['last']}"

@app.route("/myaddress")
def address():
    return f'{me["address"]["street"]} {me["address"]["city"]}'

#############################################
##################API ENDPOINTs ##############
##############################################

@app.route("/api/catalog", methods=["GET"])
def get_catalog():
    return json.dumps(catalog)

@app.route("/api/catalog/count", methods=["GET"])
def get_count():
    counts= len(catalog)
    return json.dumps(counts) #return the value

@app.route("/api/product/<id>", methods=["GET"])
def get_product(id):
    for prod in catalog:
        if prod["_id"] ==id:
            return json.dumps(prod)

    return abort(404, "Id does not match any product :(")

#@app.route("/api/catalog/total", methods=["GET"])
@app.get("/api/catalog/total")
def get_total():

    total=0
    for prod in catalog:
        total += prod["price"]

    return json.dumps(total)


@app.get("/api/catalog/<category>")
def get_category(category):
    clothing = []
    for prod in catalog:
            if prod["category"].lower() == category.lower():
                clothing.append(prod)

    return json.dumps(clothing)

@app.get("/api/categories")
def get_categories():
    results=[]
    for prod in catalog:
        cat=prod["category"]
        if not cat in results:
            results.append(cat)


    return json.dumps (results)

@app.get("/api/lowest")
def get_lowprice():
    solution = catalog[0]
    for prod in catalog:
        if prod["price"] < solution["price"]:
            solution=prod

    return json.dumps(solution)

@app.get("/api/exercise1")
def get_exe1():
    nums = [123,123,654,124,8865,532,4768,8476,45762,345,-1,234,0,-12,-456,-123,-865,532,4768]
    solution = {}

    # A: find the lowest number
    solution["a"] = 1
    for prod in catalog: 
        if prod[]


    # B: find how many numbers are lower than 500
    solution["b"] = 1

    # C: sum all the negatives
    solution["c"] = 1


    # D: find the sum of numbers except negatives
    solution["d"] = 1


    return json.dumps(solution)


app.run(debug=True)


