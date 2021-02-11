from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about-us")
def about():
    return render_template("about.html")


@app.route("/contacts/<name>")
def contact_details(name):
    return f"Contact details for {name}"
