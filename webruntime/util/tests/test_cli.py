import sys
import subprocess
import webruntime

from webruntime.util.testing import run_tests_if_main, raises


def test_cli():
    cmd = [sys.executable, '-m', 'webruntime', '--version']
    v = subprocess.check_output(cmd, stderr=subprocess.STDOUT).decode().strip()
    assert v == webruntime.__version__

    
run_tests_if_main()
