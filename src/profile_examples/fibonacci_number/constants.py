"""main.
"""
import pathlib
import re


CURDIR = pathlib.Path(__file__).parent
MOD_FILENAME_RE = re.compile(r'^fib.+.py$')

FUN_NAME = 'fibs'
