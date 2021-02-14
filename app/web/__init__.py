import os

from flask import Flask, render_template, abort, redirect, url_for, request
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Email

from app.services.contact_service import ContactService

DATABASE_URL = os.environ.get("DATABASE_URL", "data/contacts.json")


app = Flask(__name__)
app.config[
    "SECRET_KEY"
] = "204f26b2c90fd38adb73d2b76b8c2769d51c1c7cf0c684d8b57b5365d3e106d7"

contact_service = ContactService(DATABASE_URL)


class ContactForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = EmailField("E-mail", validators=[DataRequired(), Email()])


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404


@app.route("/")
def index():
    contacts = contact_service.get_contacts()
    return render_template("index.html", contacts=contacts)


@app.route("/search")
def search():
    term = request.args.get("term", "")

    if not term:
        return redirect(url_for("index"))

    contacts = contact_service.find(term)

    return render_template("search.html", contacts=contacts, term=term)


@app.route("/about-us")
def about():
    return render_template("about.html")


@app.route("/contacts/add", methods=["GET", "POST"])
def add_contact():
    form = ContactForm()

    if form.validate_on_submit():
        contact = contact_service.create(form.name.data, form.email.data)

        return redirect(url_for("contact_details", name=contact.name))

    return render_template("add_contact.html", form=form)


@app.route("/contacts/<name>")
def contact_details(name):
    try:
        contact = contact_service.find(name)[0]
    except IndexError:
        return abort(404)

    return render_template("contact_details.html", contact=contact)


@app.route("/contacts/<name>/edit", methods=["GET", "POST"])
def edit_contact(name):
    try:
        contact = contact_service.find(name)[0]
    except IndexError:
        return abort(404)

    form = ContactForm(obj=contact)

    if form.validate_on_submit():
        form.populate_obj(contact)
        contact_service.save_contacts()

        return redirect(url_for("contact_details", name=contact.name))

    return render_template("edit_contact.html", contact=contact, form=form)


@app.route("/contacts/<name>/remove", methods=["POST"])
def remove_contact(name):
    try:
        contact = contact_service.find(name)[0]
    except IndexError:
        return abort(404)

    contact_service.remove(contact)

    return redirect(url_for("index"))
