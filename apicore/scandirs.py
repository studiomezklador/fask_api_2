import os
from fnmatch import fnmatch
import re


basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
forbidden_directories = ['env', '__pycache__', '__init__.py', '.git', os.path.dirname(__file__)]
forbidden_files = ['__init__.py', '__main__.py']
directories = [directory for directory in os.listdir(basedir) if os.path.isdir(
    os.path.join(basedir,
                 directory)) and directory not in forbidden_directories]

root = dict((key, os.path.join(basedir, key)) for key in directories)

"""
From HERE: file autoloader experiment - WIP!
"""
versions = [directory for directory in root.keys() if re.match('^v\d+$',
                                                               directory)]
blueprints = {}
mem_result = None
for version in versions:
    tmp_dict = {}
    if version in root.keys():
        Path = root[version]
        pattern = "*.py"
        for anchor, subdirs, files in os.walk(Path):
            for filename in files:
                if fnmatch(filename,
                           pattern) and filename not in forbidden_files:
                    tmp = re.sub(Path, '', os.path.join(anchor,
                                                        filename)).split('/')
                    File = tmp.pop()
                    result = ".".join([x for x in tmp if x])
                    if result == mem_result:
                        first_file = tmp_dict[result]
                        tmp_dict[result] = [first_file, File]
                    else:
                        tmp_dict[result] = File

                    mem_result = result
    blueprints[version] = dict(tmp_dict)


if __name__ == '__main__':
    print('basedir: {}'.format(basedir),
          'root: {}'.format(root),
          'versions: {}'.format(versions),
          'blueprints: {}'.format(blueprints),
          sep='\n\n')
