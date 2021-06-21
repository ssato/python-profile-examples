"""main.
"""
import datetime
import importlib
import pathlib
import re
import timeit

import click


CURDIR = pathlib.Path(__file__).parent
MOD_FILENAME_RE = re.compile(r'^(?:ok|ng).+.py')

DEFAULT_TIMES = 10000
SUITES = ['H', 'C', 'D', 'S']
NUMBERS = [
    'A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K'
]
SNS_MAP = dict(
    list=(SUITES, NUMBERS),
    tuple=(tuple(SUITES), tuple(NUMBERS)),
    frozenset=(frozenset(SUITES), frozenset(NUMBERS)),
)


def list_modules(curdir=CURDIR, pattern=MOD_FILENAME_RE):
    """List names from {ok,ng}*.py.
    """
    return sorted(
        m.name.replace('.py', '')
        for m in curdir.glob('*.py') if pattern.match(m.name)
    )


def load_from_py(mod_name, fun_name='cards'):
    """.. note:: It's not safe always.
    """
    py_path = CURDIR / f'{mod_name}.py'
    if not py_path.exists():
        raise ValueError(f'Module {mod_name} does not exists!')

    spec = importlib.util.spec_from_file_location('mod', py_path)
    mod = spec.loader.load_module()
    return getattr(mod, fun_name, None)


def show_with_time(times, cards_fn, suites, numbers):
    """A decorator to show reuslts and time elapsed.
    """
    start = timeit.default_timer()
    for _i in range(times):
        cards = cards_fn(suites, numbers)
    end = timeit.default_timer()
    print(datetime.timedelta(seconds=(end - start)))
    print(f'cards: {cards!r}')


@click.command()
@click.option(
    '--times', default=DEFAULT_TIMES,
    help='How many times to run target functions'
)
@click.option(
    '--module', default='', help='Select the name of the module to use'
)
@click.option(
    '--collection-type', type=click.Choice(['list', 'tuple', 'frozenset']),
    default='frozenset'
)
def show_cards(times=DEFAULT_TIMES, module='', collection_type='frozenset'):
    """Show cards in various ways.
    """
    sns = SNS_MAP[collection_type]
    if module:
        cards_fn = load_from_py(module)
        print(f'## module: {module}')
        show_with_time(times, cards_fn, *sns)
    else:
        for mod_name in list_modules():
            cards_fn = load_from_py(mod_name)
            print(f'## module: {mod_name}')
            show_with_time(times, cards_fn, *sns)


if __name__ == '__main__':
    show_cards()
