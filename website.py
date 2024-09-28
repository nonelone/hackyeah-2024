from flask import Blueprint, abort, request, redirect


website_blueprint = Blueprint('website', __name__)

@website_blueprint.route("/", methods=["GET"])
def home():
    if request.method == 'POST':
        return '404'
    else:
        return "Welcome home!"

@website_blueprint.route("/protected", methods=["GET", "POST"])
def protected():
    if request.method == 'GET':
        return redirect("/")
    else:
        return "AMOGUS"
