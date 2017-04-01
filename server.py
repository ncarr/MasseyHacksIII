from flask import Flask, render_template, request, url_for
app = Flask(__name__)

@app.route('/<name>')
def hello(name):
    return("Hello, %s!" % name)
