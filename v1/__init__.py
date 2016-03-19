from flask import Blueprint, request, g, Response
from apicore.scandirs import basedir, root, versions, blueprints
import simplejson as json

api = Blueprint('api', __name__)
from v1.auth import views, errors
# from v1.auth.models import User


def before_api():
    userAgent = request.user_agent
    g.client = {'browser': userAgent.browser,
                'platform': userAgent.platform,
                'version': userAgent.version,
                'language': userAgent.language}


api.before_request(before_api)


@api.route('/')
def index():
    if g.client['browser'] is None or g.client['platform'] is None:
        msg = {'message': "hello from API {} -- in CLI Mode".format(versions[0]), 'status': 200}
        r = Response(json.dumps(msg))
        r.headers['Content-type'] = 'application/json; charset=utf-8'
        return r, 200

    string = "<h1>hello from API v1 | {} | {} | {} | {}</h1>"
    return string.format(g.client['browser'],
                         g.client['platform'],
                         g.client['version'],
                         g.client['language'])
