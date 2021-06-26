"""Test main.
"""
import pytest

import profile_examples.tarai.tarai as TT


@pytest.mark.parametrize(
    ('fun',  'xyz', 'expected'),
    [(fun, (5, 3, 0), 5) for fun in TT.CALLABLES]
)
def test_tarai(fun, xyz, expected):
    assert fun(*xyz) == expected
