from flask import Blueprint, abort, request, redirect, flash, url_for
from urllib.parse import urlparse, urlunparse

import requests

from models import verify_url

api_blueprint = Blueprint('api', __name__)

@api_blueprint.route("/api", methods=["GET", "POST"])
def api():
    if request.method == 'POST':
        if request.form['url'] is not None:
            requested_url = request.form['url']
            url = urlparse(requested_url)
            if url.scheme == "http":
                new_url = urlunparse(url._replace(scheme="https"))
                try:
                    with requests.get(new_url) as r:
                        if r.status_code == 200:
                            return redirect((new_url))
                except: pass
                return redirect(url_for('website.protected', reason="insecure"))
            elif url.scheme != "https":
                return redirect(url_for('website.protected', reason="bad_protocol"))
            else:
                secure = verify_url(url.netloc)
                if secure:
                    return redirect(url_for('website.protected', reason="success"),code=307)
                else:
                    return redirect(url_for('website.protected', reason="dangerous"))
        else: abort(503)
    elif request.method == 'GET':
        return '<title>API</title><h1>For API usage, dummy!</h1>'
    abort(403)

@api_blueprint.route("/extension_api", methods=["POST"])
def extension_api():
    if request.method == 'POST':
        if request.form['url'] is not None:
            requested_url = request.form['url']
            url = urlparse(requested_url)
            if url.scheme == "http":
                new_url = urlunparse(url._replace(scheme="https"))
                try:
                    with requests.get(new_url) as r:
                        if r.status_code == 200:
                            return redirect((new_url))
                except: pass
                return "insecure" #redirect(url_for('website.protected', reason="insecure"))
            elif url.scheme != "https":
                return "bad_protocol" #redirect(url_for('website.protected', reason="bad_protocol"))
            else:
                secure = verify_url(url.netloc)
                if secure:
                    return "success" #redirect(url_for('website.protected', reason="success"),code=307)
                else:
                    return "dangerous" #redirect(url_for('website.protected', reason="dangerous"))
        else: abort(503)
    elif request.method == 'GET':
        return '<title>API</title><h1>For API usage, dummy!</h1>'
