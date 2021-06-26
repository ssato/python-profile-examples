"""Compute tarai(x, y, z).

tarai(x, y, z) =
    if x <= y:
        y
    else:
        tarai(tarai(x - 1, y, z), tarai(y - 1, z, x), tarai(z - 1, x, y))

.. seealso:: https://w.wiki/3YPE
"""
import warnings

import click

from .. import prof
from . import constants, tarai
# from . import constants, datatypes, tarai


DEFAULT_VALUES_AS_STR: str = ','.join(
    (f'{v!s}' for v in constants.DEFAULT_VALUES)
)


@click.command()
@click.option(
    '--values', default=DEFAULT_VALUES_AS_STR,
    help='x,y,z values separated with comma for tarai(x, y, z)'
)
@click.option(
    '--other-types', is_flag=True,
    help='Try various types other than in to store int and use '
         'it during computation [not implemented yet]'
)
@click.option(
    '--full', is_flag=True, help='Get full profiling data'
)
@click.option(
    '--show-results', is_flag=True, help='Show computed results also'
)
def main(
    values: str = DEFAULT_VALUES_AS_STR,
    other_types: bool = False,
    full: bool = False,
    show_results: bool = False
):
    """Compute and show the result of tarai(x, y, z).
    """
    if other_types:
        warnings.warn('Not implemented yet.')

    xyz = [int(i) for i in values.split(',')]
    assert len(xyz) == 3, f'Wrong argument was given for --value, {xyz}'

    runner = prof.ProfiledRunner(tarai.CALLABLES, full, show_results)
    runner.run(*xyz)
    # todo:
    # if other_types:
    #    for desc, mxyz in datatypes.make_values(xyz):
    #        print(f'####### {desc} #######')
    #        runner.run(*mxyz)
    # else:
    #     runner.run(*xyz)


if __name__ == '__main__':
    main()
