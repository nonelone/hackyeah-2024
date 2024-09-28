from flask import Blueprint, abort, request, redirect, render_template, flash
from models import db, SuspiciousUrl, verify_url


website_blueprint = Blueprint('website', __name__)

@website_blueprint.route("/", methods=["GET","POST"])
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
        if request.form['url'] != None:
            target_url=request.form['url']
            return render_template('protected.html', reason=reason, target_url=target_url)

        else: return render_template('protected.html', reason="bad_protocol") # no target specified, not my problem

@website_blueprint.route("/suspicious_url", methods=["GET"])
def suspicious_url():
    verify_url("")
    res = "<ul>"
    suslist = db.session.query(SuspiciousUrl).order_by(SuspiciousUrl.evil_factor.desc()).all()
    return render_template("suspicious.html", suslist=suslist)
