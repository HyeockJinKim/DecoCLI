from pycli.cmd import Command
from pycli.param import Param
from pycli.parser import Parser


class PyCLI:
    def __init__(self):
        self.parser = Parser()

    def set_cmd(self, name: str, _len=0):
        def _func(func):
            cmd = Command(func, _len)
            self.parser.set_cmd(name, cmd)
            return func
        return _func

    def set_param(self, name: str, key: str, _len=0):
        param = Param(key, _len)
        self.parser.set_param(name, param)

    def exec(self):
        funcs, params = self.parser.parse()

        for func in funcs:
            func.exec(params)
