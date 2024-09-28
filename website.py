from flask import Blueprint, abort, request, redirect, render_template, flash
from models import db, SuspiciousUrl


website_blueprint = Blueprint('website', __name__)

@website_blueprint.route("/", methods=["GET"])
def home():
    if request.method == 'POST':
        return '404'
    else:
        return render_template('home.html')

@website_blueprint.route("/protected/<reason>", methods=["GET", "POST"])
def protected(reason):
    if request.method == 'GET':
        return render_template('protected.html', reason=reason)
    else:
        return "AMOGUS"

@website_blueprint.route("/suspicious_url", methods=["GET"])
def suspicious_url():
    res = "<ul>"
    suslist = db.session.query(SuspiciousUrl).all()
    return render_template("suspicious.html", suslist=suslist)
