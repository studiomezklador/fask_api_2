import os
import sys
from __init__ import app
from apicore.scandirs import basedir, root, versions, blueprints
from flask.ext.sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(root['storage'], 'dev.db')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

"""
NOTE: have to make a file autoloader to get views from all subdirectories in each version number
"""

# a working example
from v1 import api as api_1_blueprint
app.register_blueprint(api_1_blueprint, url_prefix='/v1')

if __name__ == '__main__':
    """
    print('basedir: {}'.format(basedir),
          'root: {}'.format(root),
          'versions: {}'.format(versions),
          'blueprints: {}'.format(blueprints),
          sep='\n')
    """
    # print(db)
    app.run(debug=True)
