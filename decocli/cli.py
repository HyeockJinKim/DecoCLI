import types

from decocli.mbr.cmd import Command
from decocli.mbr.param import Param
from decocli.mbr.parser import Parser


class CLI:
    parser = Parser()

    @staticmethod
    def clear():
        """
        Clear CLI
        :return: None
        """

        CLI.parser = Parser()

    @staticmethod
    def set_cmd(name=None, _len=0):
        """
        Set command for using in CLI function
        :param name: command name used in CLI
        :param _len: len of command
        :return: Command function
        """

        def _func(func):
            cmd = Command(func)
            if name:
                CLI.parser.set_cmd(name, cmd)
            else:
                CLI.parser.set_cmd(func.__name__, cmd)

            return func

        if isinstance(name, types.FunctionType):
            f, name = name, None
            return _func(f)

        return _func

    @staticmethod
    def set_param(name: str, key: str, _len=0):
        """
        Set param for using in CLI function
        :param name: command name used in CLI
        :param key: kwargs name used in CLI function
        :param _len: len of parameter
        :return: None
        """

        param = Param(key, _len)
        CLI.parser.set_param(name, param)

    @staticmethod
    def exec():
        """
        Execute command function
        :return: results of commands
        """

        funcs, params = CLI.parser.parse()
        results = []
        for func in funcs:
            results.append(func.exec(params))

        if len(results) == 1:
            return results[0]

        return results
