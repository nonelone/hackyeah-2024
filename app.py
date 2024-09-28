from flask import Flask, redirect, url_for, render_template

from website import website_blueprint
from api import api_blueprint

app = Flask(__name__, instance_relative_config=True)

app.register_blueprint(api_blueprint)
app.register_blueprint(website_blueprint)

app.config.from_pyfile('secrets.py') # "secret" configurations in instance/secrets.py

if __name__ == "__main__":
    app.run(debug=True)
