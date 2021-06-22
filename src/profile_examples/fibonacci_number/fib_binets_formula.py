"""Closed form expression, Binet's formula.

.. seealso:: https://en.wikipedia.org/wiki/Fibonacci_number
"""
import math


SQRT_5 = math.sqrt(5)


def fib(nmax, sqrt_5=SQRT_5):
    """Compute a fibonacci number, Fib(n)."""
    kvar = 1 / sqrt_5
    return kvar * (((1 + sqrt_5) / 2) ** nmax - ((1 - sqrt_5) / 2) ** nmax)


def fibs(nmax):
    """Compute fibonacci number."""
    acc = [0, 1]  # Fib(0), Fib(1)
    return acc + [int(fib(n)) for n in range(2, nmax + 1)]
