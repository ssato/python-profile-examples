"""main.
"""
import click

from . import prof, utils


DEFAULT_TIMES = 10000
PROF_NAMES = sorted(prof.PROF_MAP.keys())


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
@click.option(
    '--profiler', type=click.Choice(PROF_NAMES),
    help='Get profile data using it'
)
@click.option(
    '--print-results', is_flag=True, help='Print out computed results also'
)
def show_cards(times=DEFAULT_TIMES, module='', collection_type='frozenset',
               profiler='cProfile', print_results=False):
    """Show cards in various ways.
    """
    sns = utils.get_suites_and_numbers(collection_type)
    if module:
        cards_fn = utils.load_from_py(module)
        print(f'## module: {module}')
        prof.show(
            times, cards_fn, *sns, profiler=profiler,
            print_results=print_results
        )
    else:
        for mod_name in utils.list_modules():
            cards_fn = utils.load_from_py(mod_name)
            print(f'## module: {mod_name}')
            prof.show(
                times, cards_fn, *sns, profiler=profiler,
                print_results=print_results
            )


if __name__ == '__main__':
    show_cards()
