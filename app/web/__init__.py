import os

from flask import Flask, render_template, abort

from app.services.contact_service import ContactService

DATABASE_URL = os.environ.get("DATABASE_URL", "data/contacts.json")


app = Flask(__name__)

contact_service = ContactService(DATABASE_URL)


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404


@app.route("/")
def index():
    contacts = contact_service.get_contacts()
    return render_template("index.html", contacts=contacts)


@app.route("/about-us")
def about():
    return render_template("about.html")


@app.route("/contacts/<name>")
def contact_details(name):
    try:
        contact = contact_service.find(name)[0]
    except IndexError:
        return abort(404)

    return render_template("contact_details.html", contact=contact)
