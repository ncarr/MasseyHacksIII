from flask import Flask, render_template, request, url_for
from flask_mongoengine import MongoEngine
import datetime
app = Flask(__name__)
app.config.from_pyfile('cfg.py')
db = MongoEngine(app)

@app.route('/addProduct')
def addProduct():
    return render_template("form.html")

@app.route('/api/uploadfood', methods=['POST'])
def uploadfood():
    if request.method == 'POST':
        Food(name=request.form['name'], upc=request.form['upc'], expiry=datetime.datetime.strptime(request.form['expiry'], '%Y-%m-%d')).save()

class Food(db.Document):
    name = db.StringField(required=True)
    upc = db.StringField()
    expiry = db.DateTimeField()
    #fridge = db.ReferenceField(Fridge, reverse_delete_rule=CASCADE)

"""
class Fridge(db.Document):
    name = db.StringField(required=True)
    owner = db.ReferenceField(User, reverse_delete_rule=CASCADE)

class User(db.Document):
    name = db.StringField(required=True)
    fridges = db.List
"""
