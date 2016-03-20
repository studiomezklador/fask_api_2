from flask import Blueprint, request, g, Response
from apicore.scandirs import basedir, root, versions, blueprints
# import simplejson as json
from apicore.jsonmatter import Json

api = Blueprint('api', __name__)
from . import routes
from v1.auth import views, errors
# from v1.auth.models import User

"""
Here is how to implement a before_request on a Blueprint.
NOTE: this API must check if it's a browser-based navigation (or not)
on any single request (or maybe once?).
"""


@api.before_app_request
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


# api.before_request(before_api)
