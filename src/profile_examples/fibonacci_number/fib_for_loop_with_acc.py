"""accumulator を使う方法.
"""


def fibs(nmax):
    """Compute fibonacci number."""
    acc = [0, 1]  # Fib(0), Fib(1)

    if nmax < 2:
        return acc[:nmax + 1]

    for n in range(2, nmax + 1):
        fib_n_1 = acc[n - 1]
        fib_n_2 = acc[n - 2]
        fib_n = fib_n_1 + fib_n_2
        acc.append(fib_n)

    return acc
