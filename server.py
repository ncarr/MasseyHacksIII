from flask import Flask, render_template, request, url_for
app = Flask(__name__)

@app.route('/', methods=['POST'])
def hello():
    name=request.form['name']
    return("Hello, %s!" % name)
