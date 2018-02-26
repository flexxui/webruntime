from .util.config import Config

config = Config('webruntime', '~appdata/.flexx.cfg', '~appdata/.webruntime.cfg',

        # webruntime=('', str, 'The default web runtime to use. '
        #             'Default is "app or browser".'),
        firefox_exe=('', str, 'The location of the Firefox executable. '
                     'Auto-detect by default.'),
        chrome_exe=('', str, 'The location of the Chrome/Chromium executable. '
                    'Auto-detect by default.'),
        nw_exe=('', str, 'The location of the NW.js executable. '
                'Auto-install by default.'),
        )
