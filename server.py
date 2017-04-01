from flask import Flask, render_template, request, url_for
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return render_template('hello.html', name=request.args.get("name"))
    else:
        return render_template('hello.html', name=request.args.get("name"))
