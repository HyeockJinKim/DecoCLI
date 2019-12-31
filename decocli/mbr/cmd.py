import types


class Command:
    def __init__(self, _func: types.FunctionType, default: dict=None):
        if default is None:
            default = dict()
        self.func = _func
        self.param_names = _func.__code__.co_varnames
        self.default_param = default
        self.check_default_param()

    def check_default_param(self):
        for param in self.param_names:
            if param not in self.default_param.keys():
                self.default_param[param] = None

    def exec(self, params: dict=None):
        if params is None:
            params = self.default_param

        for param in self.default_param.keys():
            params.setdefault(param, self.default_param[param])

        try:
            return self.func(**params)
        except TypeError:
            pass
        try:
            return self.func()
        except TypeError:
            print('This Command has problem')
            exit(-1)
