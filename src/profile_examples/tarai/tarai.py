# pylint: disable=invalid-name
"""Various tarai(x, y, z) implementations.
"""
import functools

try:
    from functools import cache  # python >= 3.9
except ImportError:
    cache = functools.partial(functools.lru_cache(None))


def tarai(x, y, z):
    """Simple implementation of tarai(x, y, z) as it is."""
    if x <= y:
        return y

    return tarai(tarai(x - 1, y, z), tarai(y - 1, z, x), tarai(z - 1, x, y))


def memoized_tarai(x, y, z, acc=None):
    """Self-made memoized version of tarai(x, y, z)"""
    if x <= y:
        return y

    if acc is None:
        acc = dict()
    else:
        val = acc.get((x, y, z), None)
        if val is not None:
            return val

    val = memoized_tarai(
        memoized_tarai(x - 1, y, z, acc=acc),
        memoized_tarai(y - 1, z, x, acc=acc),
        memoized_tarai(z - 1, x, y, acc=acc),
        acc=acc
    )
    acc[(x, y, z)] = val
    return val


@cache
def memoized_tarai_2(x, y, z):
    if x <= y:
        return y

    return memoized_tarai_2(
        memoized_tarai_2(x - 1, y, z), memoized_tarai_2(y - 1, z, x),
        memoized_tarai_2(z - 1, x, y)
    )


@functools.lru_cache()
def memoized_tarai_3(x, y, z):
    if x <= y:
        return y

    return memoized_tarai_3(
        memoized_tarai_3(x - 1, y, z), memoized_tarai_3(y - 1, z, x),
        memoized_tarai_3(z - 1, x, y)
    )


@functools.lru_cache(None)
def memoized_tarai_4(x, y, z):
    if x <= y:
        return y

    return memoized_tarai_4(
        memoized_tarai_4(x - 1, y, z), memoized_tarai_4(y - 1, z, x),
        memoized_tarai_4(z - 1, x, y)
    )


# Hacks.
setattr(
    memoized_tarai_2,
    '__doc__',
    'Memoized version of tarai(x, y, z) using functools.cache.'
)
setattr(
    memoized_tarai_3,
    '__doc__',
    'Memoized version of tarai(x, y, z) using functools.lru_cache.'
)
setattr(
    memoized_tarai_4,
    '__doc__',
    'Memoized version of tarai(x, y, z) using functools.lru_cache(None).'
)

CALLABLES = (
    tarai, memoized_tarai, memoized_tarai_2, memoized_tarai_3, memoized_tarai_4
)
