"""効率的な方法 (2).
"""
import itertools


def cards(suites, numbers):
    """Cards generator."""
    return [f'{s} {n}' for s, n in itertools.product(suites, numbers)]
