import os
import sys
from __init__ import app, basedir, root, versions
from flask.ext.sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(root['storage'], 'dev.db')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)


def create_app(config_name):
    # a working example
    from .v1 import api as api_1_0_blueprint
    app.register_blueprint(api_1_0_blueprint, url_prefix='/v1')

if __name__ == '__main__':
    # print(basedir, root, versions, sep='\n')
    # print(db)
    app.run(debug=True)
