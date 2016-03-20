#!/usr/bin/env python3
from tabulate import tabulate
# from flask import url_for
from flask.ext.script import Manager

from __init__ import app
from apicore.scandirs import basedir, root, versions, blueprints, directories


manager = Manager(app)


@manager.command
def hello():
    """ JUST FOR TEST """
    print("hello!")


@manager.command
def paths():
    print("basedir: {}".format(basedir),
          "root: {}".format(root),
          "versions: {}".format(versions),
          "directories: {}".format(directories),
          "blueprints: {}".format(blueprints),
          sep='\n\n')


@manager.command
def routes():
    output = []

    for v in versions:

        for rule in app.url_map.iter_rules():
            methods = ', '.join(rule.methods)

            if rule.endpoint != 'static':
                line = [rule.endpoint, methods, rule]
                output.append(line)

    print('\n')
    print(tabulate(output, headers=['ENDPOINT', 'METHODS', 'URI']), end='\n\n')


@manager.command
def bp():
    print(fl_blueprints(), sep='\n')


def fl_blueprints():
    p = []
    for k, v in app.blueprints.items():
        # vars: get all attributes from class / instance
        p.append(vars(v))
    return p


@manager.command
def config():
    print(app.config)
    """for k, v in app.config.__dict__:
        print("{}: {}".format(k, v), sep='\n')"""


@manager.command
def fl_root():
    print(app.config.__dict__['root_path'])

if __name__ == '__main__':
    manager.run()
