"""Test main.
"""
import pytest

import profile_examples.fibonacci_number.utils as TT

from . import ref_data


@pytest.mark.parametrize(
    ('fun',  'nmax', 'expected'),
    [(fun, 20, ref_data.REF_DATA) for _, fun in TT.list_fibs_functions()]
)
def test_fibs(fun, nmax, expected):
    assert fun(nmax) == expected
