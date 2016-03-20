from flask import Flask

app = Flask(__name__)

"""
SOME CONFIGURATIONS
"""

app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

"""
NOTE: have to make a file autoloader to get views from all subdirectories
in each version number
"""

# a working example, BUT static! (need to be more dynamic...)
from v1 import api as api_1_blueprint
app.register_blueprint(api_1_blueprint, url_prefix='/v1')
# app.register_blueprint(api_1_blueprint, subdomain='v1')
