#!/usr/bin/env python3
from flask import url_for
from flask.ext.script import Manager

from __init__ import app


manager = Manager(app)


@manager.command
def hello():
    """ JUST FOR TEST """
    print("hello!")


@manager.command
def routes():
    """ Not Working """
    import urllib
    output = []
    for rule in app.url_map.iter_rules():
        options = []
        for arg in rule.arguments:
            options.append("[{0}]".format(arg))

        print(options)
        methods = ', '.join(rule.methods)
        url = url_for(rule.endpoint, **options)
        line = urllib.parse.unquote("{:50s} {:20s} {}".format(rule.endpoint,
                                                              methods, url))
        output.append(line)

    for line in sorted(output):
        print(line)


if __name__ == '__main__':
    manager.run()
