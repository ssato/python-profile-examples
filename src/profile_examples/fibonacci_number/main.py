"""Compute fibonacci number and print them.

- Fib(0) = 0
- Fib(1) = 1
- Fib(n) = Fib(n - 1) + Fib(n - 2)
"""
import pathlib

import click

from . import prof, utils


DEFAULT_MAX = 30
DEFAULT_TIMES = 5
CURDIR = pathlib.Path(__file__).parent


@click.command()
@click.option(
    '--nmax', default=DEFAULT_MAX,
    help='The max index number of Fibonacci number.'
)
@click.option(
    '--times', default=DEFAULT_TIMES,
    help='How many times to run target functions'
)
@click.option(
    '--print-results', is_flag=True, help='Print out computed results also'
)
def main(nmax=DEFAULT_MAX, times=DEFAULT_TIMES, print_results=False):
    """Compute and show the fiboonacci numbers.
    """
    profile_fns = prof.RUN_WITH_PROF_FNS
    fib_fns = utils.list_fibs_functions()

    for pfn in profile_fns:
        for mod_name, ffn in fib_fns:
            print(f'## module: {mod_name}')
            res = pfn(ffn, nmax, times)

    if print_results:
        print(f'{res!r}')


if __name__ == '__main__':
    main()
