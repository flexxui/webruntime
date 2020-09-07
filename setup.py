# -*- coding: utf-8 -*-

"""
Webruntime setup script.
"""

import os
import sys
import shutil

try:
    import setuptools  # noqa, analysis:ignore
except ImportError:
    pass  # setuptools allows for "develop", but it's not essential

from distutils.core import setup


## Function we need

def get_version_and_doc(filename):
    NS = dict(__version__='', __doc__='')
    docStatus = 0  # Not started, in progress, done
    for line in open(filename, 'rb').read().decode().splitlines():
        if line.startswith('__version__'):
            exec(line.strip(), NS, NS)
        elif line.startswith('"""'):
            if docStatus == 0:
                docStatus = 1
                line = line.lstrip('"')
            elif docStatus == 1:
                docStatus = 2
        if docStatus == 1:
            NS['__doc__'] += line.rstrip() + '\n'
    if not NS['__version__']:
        raise RuntimeError('Could not find __version__')
    return NS['__version__'], NS['__doc__']


def package_tree(pkgroot):
    subdirs = [os.path.relpath(i[0], THIS_DIR).replace(os.path.sep, '.')
               for i in os.walk(os.path.join(THIS_DIR, pkgroot))
               if '__init__.py' in i[2]]
    return subdirs


## Collect info for setup()

THIS_DIR = os.path.dirname(__file__)

# Define name and description
name = 'webruntime'
description = "Launch HTML5 apps in the browser or a desktop-like runtime."

# Get version and docstring (i.e. long description)
version, doc = get_version_and_doc(os.path.join(THIS_DIR, name, '__init__.py'))


## Setup

setup(
    name=name,
    version=version,
    author='Almar Klein and contributors',
    author_email='almar.klein@gmail.com',
    license='(new) BSD',
    url='http://webruntime.readthedocs.io',
    download_url='https://pypi.python.org/pypi/webruntime',
    keywords="GUI, web, runtime, XUL, nwjs",
    description=description,
    long_description=doc,
    platforms='any',
    provides=[name],
    install_requires=['dialite'],
    packages=package_tree(name),
    package_dir={name: name},
    package_data={},
    entry_points={'console_scripts': ['webruntime = webruntime.__main__:main'], },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
