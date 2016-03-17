from flask import Blueprint

api = Blueprint('api', __name__)
from v1.auth import views, errors
# from v1.auth.models import User
