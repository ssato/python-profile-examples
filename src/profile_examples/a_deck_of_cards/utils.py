"""main.
"""
import importlib.util

from .constants import CURDIR, MOD_FILENAME_RE, SNS_MAP


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


def get_suites_and_numbers(collection_type='frozenset'):
    """Suites and numbers.
    """
    return SNS_MAP[collection_type]
