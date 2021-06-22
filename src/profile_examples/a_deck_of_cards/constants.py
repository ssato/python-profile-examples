"""main.
"""
import pathlib
import re


CURDIR = pathlib.Path(__file__).parent
MOD_FILENAME_RE = re.compile(r'^(?:ok|ng).+.py')

SUITES = ['H', 'C', 'D', 'S']
NUMBERS = [
    'A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K'
]
SNS_MAP = dict(
    list=(SUITES, NUMBERS),
    tuple=(tuple(SUITES), tuple(NUMBERS)),
    frozenset=(frozenset(SUITES), frozenset(NUMBERS)),
)
