from flask import Blueprint, abort, render_template, request

website_blueprint = Blueprint('website', __name__)

@website_blueprint.route("/", methods=["GET"])
def home():
    if request.method == 'POST':
        return '404'
    else:
        return render_template('home.html')
