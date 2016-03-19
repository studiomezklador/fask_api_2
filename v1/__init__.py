from flask import Blueprint, request

api = Blueprint('api', __name__)
from v1.auth import views, errors
# from v1.auth.models import User

"""browser = request.user_agent.browser
version = request.user_agent.version and int(request.user_agent.version.split('.')[0])
platform = request.user_agent.platform
uas = request.user_agent.string"""

@api.route('/')
def index():
    userAgent = request.user_agent
    browser = userAgent.browser
    return "hello from API v1 | {}".format(browser)
