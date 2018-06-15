from functools import wraps
from flask import request, Response
from app import app


def failed_auth():
    """
    Sends a 401 response that enables basic auth
    """
    return Response(
        "Could not verify your access level for that URL.\nYou have to login with proper credentials",
        401,
        {"WWW-Authenticate": 'Basic realm="Login Required"'},
    )


def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.headers.get("authorization")
        if not auth or auth != app.config["API_KEY"]:
            return failed_auth()
        return f(*args, **kwargs)

    return decorated
