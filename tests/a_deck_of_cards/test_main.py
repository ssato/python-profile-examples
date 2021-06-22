"""Test main.
"""
import pathlib
import re

import pytest

import profile_examples.a_deck_of_cards.utils as TT
import profile_examples.a_deck_of_cards.constants as C


CURDIR = pathlib.Path(__file__).parent


@pytest.mark.parametrize(
    ('curdir',  'pattern', 'expected'),
    (
     (C.CURDIR, C.MOD_FILENAME_RE, ['ng_1', 'ng_2', 'ok_1', 'ok_2', 'ok_3']),
     (CURDIR, re.compile(r'__init__.py'), ['__init__']),
    )
)
def test_list_modules(curdir, pattern, expected):
    assert TT.list_modules(curdir, pattern) == expected
