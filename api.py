from flask import Blueprint, abort, request, redirect
from urllib.parse import urlparse

api_blueprint = Blueprint('api', __name__)

@api_blueprint.route("/api", methods=["GET", "POST"])
def api():
    if request.method == 'POST':
        if request.form['url'] is not None:
            requested_url = request.form['url']
            print(requested_url)
            url = urlparse(requested_url)
            if url.path == "amazin.cum":
                return "SUS" #redirect("/protected")
            return str(url)
        else: abort(503)
    elif request.method == 'GET':
        return '<title>API</title><h1>For API usage, dummy!</h1>'
    abort(403)
