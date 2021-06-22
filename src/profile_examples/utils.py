"""main.
"""
import importlib


def list_modules(curdir, pattern):
    """List names from files (*.py) in ``curdir`` match ``pattern``.
    """
    return sorted(
        m.name.replace('.py', '')
        for m in curdir.glob('*.py') if pattern.match(m.name)
    )


def load_from_py(mod_name, fun_name, mod_dir):
    """.. note:: It's not safe always.
    """
    py_path = mod_dir / f'{mod_name}.py'
    if not py_path.exists():
        raise ValueError(f'Module {mod_name} does not exists!')

    spec = importlib.util.spec_from_file_location('mod', py_path)
    mod = spec.loader.load_module()
    return getattr(mod, fun_name, None)
