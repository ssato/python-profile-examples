"""Test main.
"""
import pathlib
import re

import pytest

import profile_examples.a_deck_of_cards.main as TT


CURDIR = pathlib.Path(__file__).parent


@pytest.mark.parametrize(
    ('curdir',  'pattern', 'expected'),
    (
     (TT.CURDIR, TT.MOD_FILENAME_RE, ['ng_1', 'ng_2', 'ok_1', 'ok_2']),
     (CURDIR, re.compile(r'__init__.py'), ['__init__']),
    )
)
def test_list_modules(curdir, pattern, expected):
    assert TT.list_modules(curdir, pattern) == expected
