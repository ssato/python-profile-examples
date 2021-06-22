"""main.
"""
from .. import utils
from . import constants


def list_fibs_functions(fun_name=constants.FUN_NAME, curdir=constants.CURDIR,
                        pattern=constants.MOD_FILENAME_RE):
    """
    List 'fibs' fucntions in this module.

    :return: [(module_name: str, func: Callable)]
    """
    return [
        (m, utils.load_from_py(m, fun_name, curdir))
        for m in utils.list_modules(curdir, pattern)
    ]
