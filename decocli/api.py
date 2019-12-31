import types

from decocli.cli import CLI
from decocli.mbr.cmd import Command


def cli_class(cls):
    """

    """
    for name in cls.__dict__.keys():
        if name.startswith('_'):
            continue

        func = cls.__dict__[name]
        params = func.__code__.co_varnames
        default = None
        if len(params) > 0:
            default = {params[0]: cls()}
        CLI.set_cmd(func, default)

    return cls
