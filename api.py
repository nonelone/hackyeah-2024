from flask import Blueprint, abort, request, redirect, flash, url_for
from urllib.parse import urlparse

api_blueprint = Blueprint('api', __name__)

@api_blueprint.route("/api", methods=["GET", "POST"])
def api():
    if request.method == 'POST':
        if request.form['url'] is not None:
            requested_url = request.form['url']
            print(requested_url)
            url = urlparse(requested_url)
            if url.scheme == "http":
                return redirect(url_for('website.protected', reason="insecure"))
            elif url.scheme != "https":
                return redirect(url_for('website.protected', reason="bad_protocol"))
            else:
                return f" {url.netloc} by {url.scheme}"
        else: abort(503)
    elif request.method == 'GET':
        return '<title>API</title><h1>For API usage, dummy!</h1>'
    abort(403)
