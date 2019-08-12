from pycli.parser import Parser


class PyCLI:
    def __init__(self):
        self.parser = Parser()

    def set_param(self, name, default=None):
        self.parser.set_param(name, default)

    def set_cmd(self, name=None):
        def _func(func):
            return func

        self.parser.set_cmd(name, _func)
        return _func

    def add_param(self, name=None, param=None):
        def _func(func):
            return func

        self.parser.add_param(name, param)
        return _func

    def add_params(self, name=None, params=None):
        def _func(func):
            return func

        self.parser.add_params(name, params)
        return _func
