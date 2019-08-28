from decocli.cmd import Command
from decocli.param import Param
from decocli.parser import Parser


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
        results = []
        for func in funcs:
            results.append(func.exec(params))

        if len(results) == 1:
            return results[0]

        return results
