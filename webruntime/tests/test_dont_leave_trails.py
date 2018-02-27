"""
Verify that the app runtimes do not leave profile directories around. We've
had firefox-app spam the  user directory before, and we want to make sure that does not
happen again.
"""

import os
import time
import tempfile

import webruntime
from webruntime.util.testing import run_tests_if_main, skip

userdir = os.path.expanduser('~')


def index():
    """ Get a set of filenames for the current user directory.
    """
    filenames = set()
    for root, dirs, files in os.walk(userdir):
        for fname in dirs:
            # if 'temp' in fname.lower():
            #     continue  # exception for FF, which seems to clean up itself
            filenames.add(os.path.join(root, fname))
        for fname in files:
            if len(fname) < 15:  # only simple names, not uids
                if 'fontconfig' in root:
                    continue  # CI
            filenames.add(os.path.join(root, fname))
    return filenames


def notrailtester(runtime, n=4):
    
    html_filename = os.path.join(tempfile.gettempdir(), 'webruntime_empty_page.html')
    with open(html_filename, 'wb') as f:
        f.write('<html><body>test page</body></html>'.encode())
    
    # Give a chance for common stuff to init
    x = webruntime.launch(html_filename, runtime)
    time.sleep(1.5)
    x.close()
    time.sleep(0.5)
    
    before = index()
    
    # Apparently, CI needs some more time for FF init its file system
    # It seems that even ~/Desktop is not there initially, which we use to
    # detect when we're good to go.
    desktop = os.path.normpath(os.path.expanduser('~/Desktop'))
    etime = time.time() + 8  # dont get stuck
    while time.time() < etime and desktop not in before:
        time.sleep(0.2)
        before = index()
    
    for i in range(n):
        x = webruntime.launch(html_filename, runtime)
        time.sleep(1.5)
        x.close()
        time.sleep(0.5)
    
    after = index()
    
    extra_files = after.difference(before)
    extra_files2 = [f for f in extra_files
                    if not f.startswith((webruntime.TEMP_APP_DIR,
                                         webruntime.RUNTIME_DIR))]
    
    print('has desktop:', desktop in before)
    print(extra_files2)
    assert len(extra_files2) < n


def test_notrail_firefox():
    if not webruntime.FirefoxRuntime().is_available():
        skip('no firefox')
    notrailtester('firefox-app')


def test_notrail_nw():
    if not webruntime.NWRuntime().is_available():
        skip('no nw')
    notrailtester('nw-app')


if __name__ == '__main__':
    test_notrail_firefox()
    test_notrail_nw()
    # run_tests_if_main()
