"""
.. code-block:: none

    Webruntime CLI
    
    Usage:
      webruntime url runtime  launch the url in the given runtime
      webruntime --help       show this help text
      webruntime --version    show webruntime version number
"""

import sys

import webruntime


def help():
    print(__doc__.split('.. code-block:: none')[-1].lstrip().replace('    ', ''))


def main():
    if len(sys.argv) == 1:
        help()
    elif len(sys.argv) == 2:
        if sys.argv[1] in ('-h', '--help'):
            help()
        elif sys.argv[1] in ('--version', 'version'):
            print(webruntime.__version__)
        else:
            sys.exit('Invalid use of webruntime CLI.')
    elif len(sys.argv) == 3:
        rt = webruntime.launch(sys.argv[1], sys.argv[2])
        rt._proc = None  # don't close it when Python exits
    else:
        sys.exit('Invalid use of webruntime CLI.')


if __name__ == '__main__':
    main()
