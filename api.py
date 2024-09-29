from flask import Blueprint, abort, request, redirect, flash, url_for
from urllib.parse import urlparse, urlunparse

# requests library for checking availiability of HTTPS
import requests

from models import verify_url

# register blueprint
api_blueprint = Blueprint('api', __name__)


@api_blueprint.route("/api", methods=["POST"])
def api():
    if request.method == 'POST':
        if request.form['url'] is not None:
            requested_url = request.form['url']
            url = urlparse(requested_url)
            if url.scheme == "http": # if the protocol is http
                new_url = urlunparse(url._replace(scheme="https"))
                try:
                    with requests.get(new_url) as r: # try to connect over https
                        if r.status_code == 200: # if it is possible we replace the url
                            url = new_url
                except: pass
                return redirect(url_for('website.protected', reason="insecure"))
            if url.scheme != "https":
                return redirect(url_for('website.protected', reason="bad_protocol"))

            secure = verify_url(url.netloc)
            if secure:
                return redirect(url_for('website.protected', reason="success"),code=307)
            else:
                return redirect(url_for('website.protected', reason="dangerous"))
        else: abort(503)

    elif request.method == 'GET':
        return '<title>API</title><h1>For API usage, dummy!</h1>'
    abort(403)

def api():
    if request.method == 'POST':
        if request.form['url'] is not None: # if method is POST and specifies `url`
            requested_url = request.form['url']
            url = urlparse(requested_url) # parse URL
            try:
                with requests.get(requested_url) as r:
                    assert r.status_code == 200
            except: return "bad_protocol"

            if url.scheme == "": # if user has not specified the protocol
                url.scheme == "http" # assume its insecure and then try to connect to https

            if url.scheme == "http": # if the protocol is http
                new_url = urlunparse(url._replace(scheme="https"))
                try:
                    with requests.get(new_url) as r: # try to connect over https
                        if r.status_code == 200: # if it is possible we replace the url
                            url = new_url

                except: pass
                return "insecure" # otherwise block the connection

            if url.scheme != "https": # if the scheme is not https at this point it is neither http
                return "bad_protocol" # and we block custom protocols

            # if protocols are valid, check the security of URL
            return "success" if verify_url(url.netloc) else "dangerous"

        else: abort(503) # if no URL was provided throw 503 error
