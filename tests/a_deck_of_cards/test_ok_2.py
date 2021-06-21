"""Test ok_2.
"""
import profile_examples.a_deck_of_cards.ok_2 as TT

from . import ref_data


def test_cards():
    assert sorted(
        TT.cards(ref_data.SUITES, ref_data.NUMBERS)
    ) == ref_data.REF_DATA
