from flask import Flask, request, redirect, session
from flask.templating import render_template
import json
from mock_data import catalog


app = Flask('server')

@app.route("/")
def home():
    return "hello from flask"

@app.route("/me")
def about_me():
    return "Trey Schneider"

@app.route("/api/catalog", methods = ['get'])
def get_catalog():
    return json.dumps(catalog)

@app.route("/api/catalog", methods = ['post'])
def save_catalog():
    pass

@app.route("/api/catalog/count", methods = ['get'])
def count_catalog():
    return f'{len(catalog)}'

@app.route("/api/catalog/total", methods = ['get'])
def total_catalog():
    return json.dumps(sum([x['price'] for x in catalog]))

@app.route("/api/catalog/most_expensive", methods = ['get'])
def max_catalog():
    max_num = 0
    title = ''
    for x in catalog:
        if x['price']> max_num:
            title = x['title']
    return json.dumps(title)

@app.route("/api/catalog/<id>", methods = ['get'])
def get_by_id(id):
    try:
        return json.dumps([x for x in catalog if x['_id'] == id][0])
    except IndexError:
        return 'ID does not exist'

    
app.run(debug=True)