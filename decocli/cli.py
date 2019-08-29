from decocli.cmd import Command
from decocli.param import Param
from decocli.parser import Parser


class CLI:
    parser = Parser()

    @staticmethod
    def clear():
        CLI.parser = Parser()

    @staticmethod
    def set_cmd(name=None, _len=0):
        def _func(func):
            cmd = Command(func, _len)
            if name:
                CLI.parser.set_cmd(name, cmd)
            else:
                CLI.parser.set_cmd(func.__name__, cmd)

            return func
        return _func

    @staticmethod
    def set_param(name: str, key: str, _len=0):
        param = Param(key, _len)
        CLI.parser.set_param(name, param)

    @staticmethod
    def exec():
        funcs, params = CLI.parser.parse()
        results = []
        for func in funcs:
            results.append(func.exec(params))

        if len(results) == 1:
            return results[0]

        return results
