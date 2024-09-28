from flask import Blueprint, abort, request

api_blueprint = Blueprint('api', __name__)

@api_blueprint.route("/api", methods=["GET", "POST"])
def api():
    if request.method == 'POST':
        return '404'
    elif request.method == 'GET':
        return '<title>API</title><h1>For API usage, dummy!</h1>'
    abort(403)
