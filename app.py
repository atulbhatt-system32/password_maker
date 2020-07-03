from flask import Flask, render_template, redirect, url_for, request


app = Flask(__name__)
app.debug = True

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/list",methods = ['POST', 'GET'])
def list():
    if request.method == 'POST':
        username = request.form['username'] 
        website = request.form['site']
        prefix = "AB"
        suffix = "SS"
        symbol = "@"
        number = "98"
        password = prefix + website[0].lower() + username[0].lower() \
            + username[-1].lower() + website[-1].lower() + number + symbol + suffix

    return render_template('index.html', password = password, page = username)