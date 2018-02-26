"""
Config and definitions specific to Webruntime.
"""

import os.path as op

from . import ROOT_DIR, THIS_DIR  # noqa

NAME = 'webruntime'
DOC_DIR = op.join(ROOT_DIR, 'docs')
DOC_BUILD_DIR = op.join(DOC_DIR, '_build')
