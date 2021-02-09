from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>Welcome to the Contacts App!</h1>"


@app.route("/about")
def about():
    return """
<h1>About</h1>
<p>This is a small and simple contacts management application.</p>
    """
