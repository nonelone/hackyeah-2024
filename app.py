from flask import Flask, redirect, url_for, render_template

from flask_cors import CORS

from website import website_blueprint
from api import api_blueprint

from models import db, init_database

app = Flask(__name__, instance_relative_config=True)

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
cors = CORS(app, resources={r"/extension_api/*": {"origins": "*"}})

app.register_blueprint(api_blueprint)
app.register_blueprint(website_blueprint)

app.config.from_pyfile('secrets.py') # "secret" configurations in instance/secrets.py

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db'

db.init_app(app)

with app.app_context(): init_database()

if __name__ == "__main__":
    with app.app_context():
        init_database()
    app.run(debug=True)
