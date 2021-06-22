"""for loop version.

.. seealso:: https://en.wikipedia.org/wiki/Fibonacci_number
"""


def fib(num, fib_0_1=(0, 1)):
    """Compute fibonacci number for n > 1."""
    (fib_prev_prev, fib_prev) = fib_0_1  # fib(0), fib(1)

    for _ in range(num):
        fib_next, fib_prev = fib_prev, fib_prev_prev + fib_prev

    return fib_next


def fibs(nmax):
    """Compute fibonacci numbers."""
    return [0, 1] + [fib(n) for n in range(2, nmax + 1)]
