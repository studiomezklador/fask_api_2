from flask import Flask

app = Flask(__name__)

"""
SOME CONFIGURATIONS
"""

app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
