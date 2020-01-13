from decocli.cli import CLI


def cli_class(cls):
    """
    Set CLI class
    """
    for name in cls.__dict__.keys():
        if name.startswith('_'):
            continue

        func = cls.__dict__[name]
        params = func.__code__.co_varnames
        default = None
        length = len(params)

        if length > 0:
            default = {params[0]: cls()}
            for i in range(1, length):
                CLI.set_param('--'+params[i], params[i], 1)

        CLI.set_cmd(func, default)

    return cls
