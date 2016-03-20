#!/usr/bin/env python3
from tabulate import tabulate
from flask import url_for
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

    import urllib
    output = []
    longuest_meth = []

    for v in versions:

        for rule in app.url_map.iter_rules():
            methods = ', '.join(rule.methods)

            out = "{:<20s}|{:<10s}|{:<20s}"
            if rule.endpoint != 'static':
                """line = urllib.parse.unquote(out).format(rule.endpoint,
                                                        methods,
                                                        str(rule))"""
                line = [rule.endpoint, methods, rule]
                output.append(line)
                longuest_meth.append(len(methods))
    print('\n')
    print(tabulate(output, headers=['ENDPOINT', 'METHODS', 'URI']), end='\n\n')

    """meth_str = 'METHODS' + ' ' * min(longuest_meth)
    print("{:<20} {:<10s} {:<20s}".format('ENDPOINT',
                                          meth_str,
                                          'RULE'))
    print(sorted(longuest_meth, reverse=True))
    for line in sorted(output):
        print(line)"""


@manager.command
def bp():
    print(blueprints(), sep='\n')

def blueprints():
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
def root():
    print(app.config.__dict__['root_path'])

if __name__ == '__main__':
    manager.run()
