"""Test main.
"""
import pytest

import profile_examples.tarai.tarai as TT


FUNCS = (
    TT.tarai, TT.memoized_tarai, TT.memoized_tarai_2, TT.memoized_tarai_3
)


@pytest.mark.parametrize(
    ('fun',  'xyz', 'expected'),
    [(fun, (5, 3, 0), 5) for fun in FUNCS]
)
def test_tarai(fun, xyz, expected):
    assert fun(*xyz) == expected
