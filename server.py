from flask import Flask, render_template, request, url_for
from flask_mongoengine import MongoEngine
import datetime
app = Flask(__name__)
app.config.from_pyfile('cfg.py')
db = MongoEngine(app)

@app.route('/addProduct')
def addProduct():
    return render_template("form.html")

@app.route('/test')
def test():
    theSalad = Food(name='Caesar Salad', upc='Ross', expiry=datetime.date(2017, 5, 1)).save()
    return "It probably worked"

class Food(db.Document):
    name = db.StringField(required=True)
    upc = db.StringField()
    expiry = db.DateTimeField()
