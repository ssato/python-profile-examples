"""Some data types alternates int object.
"""
import typing


class IntNamedTuple(typing.NamedTuple):
    """A namedtuple class mimics int object.
    """
    val: int = 0

    def __le__(self, other):
        return self.val <= other.val

    def __sub__(self, other: int):
        return self.val - other

    def __repr__(self):
        return f'{self.val!s}'


class IntObject:
    """A class mimics int object.
    """
    def __init__(self, val):
        self.val = val

    def __le__(self, other):
        return self.val <= other.val

    def __sub__(self, other: int):
        return self.val - other

    def __repr__(self):
        return f'{self.val!s}'


def make_values(ints: typing.Iterable[int]):
    """Make datasets.
    """
    return [
        ('int', ints),
        ('namedtuple', [IntNamedTuple(i) for i in ints]),
        ('class', [IntObject(i) for i in ints]),
    ]
