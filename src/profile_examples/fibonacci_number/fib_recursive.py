"""Recursive version.
"""


def fib(num):
    """Compute fibonacci number."""
    if num in (0, 1):  # fib(0) == 0, fib(1) == 1
        return num

    return fib(num - 2) + fib(num - 1)


def fibs(nmax):
    """Compute fibonacci numbers."""
    return [fib(n) for n in range(nmax + 1)]
