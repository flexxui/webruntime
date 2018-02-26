"""
Webruntime CLI.
"""

import sys
import subprocess

import webruntime


def help():
    lines = ['webruntime [options] url runtime',
             '',
             '  -h          - show help text',
             '  --version   - show version number'
             ]
    print('\n'.join(lines))



def main():
    if len(sys.argv) == 1:
        help()
    elif len(sys.argv) == 2:
        if sys.argv[1] == '-h':
            help()
        elif sys.argv[1] == '--version':
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
