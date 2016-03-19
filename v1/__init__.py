from flask import Blueprint, request, g, Response
from apicore.scandirs import basedir, root, versions, blueprints
import simplejson as json

api = Blueprint('api', __name__)
from v1.auth import views, errors
# from v1.auth.models import User

"""
Here is how to implement a before_request on a Blueprint.
NOTE: this API must check if it's a browser-based navigation (or not)
on any single request (or maybe once?).
"""


def before_api():
    """
    JUST create a global in Flask App dict containing client's browsing
    interface.
    """
    userAgent = request.user_agent
    g.client = {'browser': userAgent.browser,
                'platform': userAgent.platform,
                'version': userAgent.version,
                'language': userAgent.language}


api.before_request(before_api)


@api.route('/')
def index():
    """
    if no browser and no platform: it's a CLI request.
    """
    if g.client['browser'] is None or g.client['platform'] is None:
        string = "hello from API {} -- in CLI Mode"
        msg = {'message': string.format(versions[0]),
               'status': 'OK',
               'mode': 200}
        r = Response(json.dumps(msg))
        r.headers['Content-type'] = 'application/json; charset=utf-8'
        return r, 200

    """
    ELSE: it's obviously on a web browser
    """
    string = "<h1>hello from API v1 | {} | {} | {} | {}</h1>"
    return string.format(g.client['browser'],
                         g.client['platform'],
                         g.client['version'],
                         g.client['language'])
