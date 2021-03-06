from flask import Flask, render_template, request, url_for, redirect
import json
import datetime, requests, csv
app = Flask(__name__, static_folder='public', static_url_path='')
app.config.from_pyfile('cfg.py')

fruitlist = {}
with open('fruits.csv', newline='') as csvfile:
    fruitreader = csv.reader(csvfile)
    for row in fruitreader:
        fruitlist[row[0]] = row[1]

def getRecipe(query):
    r = requests.get('https://api.edamam.com/search?q=' + query + '&app_id=' + app.config.get('EDAMAM_RECIPE_ID') + '&app_key=' + app.config.get('EDAMAM_RECIPE_KEY'))
    return r.json()

def getFroots():
    with open('data.json', 'r') as f:
        return json.load(f)

def getRecipes():
    returnstatement = {}
    for fruit, _ in getFroots().items():
        returnstatement[fruit] = getRecipe(fruit).get('hits')[0].get('recipe')
    return returnstatement

@app.route('/')
def home():
    try:
        return render_template('index.html', recipes=getRecipes(), basket=getFroots(), fruits=fruitlist)
    except:
        return render_template('index.html')

@app.route('/fruits/eat', methods=['POST'])
def deletFroot():
    data = {}
    with open('data.json', 'r') as f:
        data = json.load(f)
        name = request.form['name']
        try:
            data[name]
        except:
            data[name] = 0
            with open('data.json', 'w') as f:
                json.dump(data, f)
            return redirect(url_for('home'), code=302)
        else:
            data[name] -= 1
            if data[name] <= 0:
                del data[name]
            with open('data.json', 'w') as f:
                json.dump(data, f)
            return redirect(url_for('home'), code=302)

@app.route('/fruits/add', methods=['POST'])
def addFroot():
    data = {}
    with open('data.json', 'r') as f:
        data = json.load(f)
        try:
            data[request.form['name']]
        except:
            data[request.form['name']] = 1
            with open('data.json', 'w') as f:
                json.dump(data, f)
            return redirect(url_for('froots'), code=302)
        else:
            data[request.form['name']] += 1
            with open('data.json', 'w') as f:
                json.dump(data, f)
            return redirect(url_for('froots'), code=302)

@app.route('/fruits')
def froots():
    return render_template('fruits.html', fruits=fruitlist)

@app.route('/fruitinfo/<name>')
def fruitInfo(name):
    appleInfo = Nutrition.getFruit(name)
    try:
        imageUrl = fruitlist[name]
    except IndexError:
        imageUrl = 'https://staticdelivery.nexusmods.com/mods/110/images/74627-0-1459502036.jpg'
    return render_template('fruitInfo.html', name=name, calories=appleInfo['calories'], imageUrl=imageUrl)

class Nutrition(object):
    def getFruit(ingredient):
        r = requests.get('https://api.edamam.com/api/nutrition-data?app_id=' + app.config.get('EDAMAM_APP_ID') + '&app_key=' + app.config.get('EDAMAM_APP_KEY') + '&ingr=1%20' + ingredient)
        return r.json()
