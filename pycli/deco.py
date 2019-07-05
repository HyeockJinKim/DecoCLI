from functools import wraps
from pycli.struct import command_dict, param_dict


class SetCommand:
    def __init__(self, name):
        self.name = name

    def __call__(self, func, *args, **kwargs):
        @wraps(func)
        def _decorator(*args, **kwargs):
            return  func(*args, **kwargs)

        command_dict[self.name] = _decorator
        return _decorator


class AddParam:
    def __init__(self, name):
        self.name = name

    def __call__(self, func, *args, **kwargs):
        @wraps(func)
        def _decorator(*args, **kwargs):
            kwargs[self.name] = lambda: param_dict[self.name]
            return func(*args, **kwargs)

        for key, value in command_dict.items():
            if value is func:
                command_dict[key] = _decorator

        return _decorator


class AddParams:
    def __init__(self, names):
        self.names = names

    def __call__(self, func, *args, **kwargs):
        @wraps(func)
        def _decorator(*args, **kwargs):
            for name in self.names:
                kwargs[name] = lambda: param_dict[name]
            return func(*args, **kwargs)

        for key, value in command_dict.items():
            if value is func:
                command_dict[key] = _decorator

        return _decorator

