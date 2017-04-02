from flask import Flask, render_template, request, url_for
from flask_mongoengine import MongoEngine
import datetime, requests
app = Flask(__name__)
app.config.from_pyfile('cfg.py')
db = MongoEngine(app)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return render_template('hello.html', name=request.args.get("name"))
    else:
        return render_template('hello.html', name=request.args.get("name"))

@app.route('/fruitinfo')
def fruitInfo():
    appleInfo = Nutrition.getFruit('1 large apple')
    return render_template('fruitInfo.html', name=appleInfo['ingredients'][0]['text'], calories=appleInfo['calories'], imageUrl='https://staticdelivery.nexusmods.com/mods/110/images/74627-0-1459502036.jpg')

@app.route('/api/fruits', methods=['POST'])
def uploadFruit():
    if request.method == 'POST':
        Fruit(name=request.form['name'], upc=request.form['upc'], expiry=datetime.datetime.strptime(request.form['expiry'], '%Y-%m-%d')).save()

class Fruit(db.Document):
    name = db.StringField(required=True)
    upc = db.StringField()
    expiry = db.DateTimeField()

class Nutrition(object):
    def getFruit(ingredient):
        r = requests.get('https://api.edamam.com/api/nutrition-data?app_id=' + app.config.get('EDAMAM_APP_ID') + '&app_key=' + app.config.get('EDAMAM_APP_KEY') + '&ingr=' + ingredient)
        return r.json()
