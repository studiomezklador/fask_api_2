import os
import re
from glob import glob
from flask import Flask, Blueprint


forbidden_directories = ['env', '__pycache__']
forbidden_files = ['__init__.py', '__main__.py']
basedir = os.path.abspath(os.path.dirname(__file__))
directories = [directory for directory in os.listdir(basedir) if os.path.isdir(
os.path.join(basedir ,directory)) and directory not in forbidden_directories]

root = dict((key, os.path.join(basedir, key)) for key in directories)

"""
From HERE: file autoloader experiment - WIP!
"""
versions = [directory for directory in root.keys() if re.match('^v\d+$', directory)]

for version in versions:
        # subdirs = dict((k, []) for k in os.listdir(os.path.join('/', version)))
        sub_path = '{}/'.format(version)
        sub_files = glob(sub_path + './**/*.py', recursive=True)
        subfiles = [filename.split('/')[-1] for filename in sub_files if filename not in forbidden_files]
        blueprints = dict((k, [subfiles]) for k in os.listdir(sub_path))

# print(blueprints)
"""
for rts, drcs, files in os.walk(os.path.join('./', versions[0])):
    for drc in drcs:
        if drc not in forbidden_directories:
            print(drc)
        # print(drc)
    for filename in files:
        if filename not in forbidden_files:
            print(os.path.join(rts, filename))
"""
app = Flask(__name__)



"""
for version in versions:
    app.register_blueprint(version, url_prefix='/'+version)
"""
