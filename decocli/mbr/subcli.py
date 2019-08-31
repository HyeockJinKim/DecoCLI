import types

from decocli.mbr.cmd import Command
from decocli.mbr.param import Param
from decocli.mbr.parser import Parser


class SubCLI:
    def __init__(self, name):
        self.name = name
        self.parser = Parser()

    def clear(self):
        """
        Clear CLI
        :return: None
        """

        self.parser = Parser()

    def set_cmd(self, name=None, _len=0):
        """
        Set command for using in CLI function
        :param name: command name used in CLI
        :param _len: len of command
        :return: Command function
        """

        def _func(func):
            cmd = Command(func)
            if name:
                self.parser.set_cmd(name, cmd)
            else:
                self.parser.set_cmd(func.__name__, cmd)

            return func

        if isinstance(name, types.FunctionType):
            f, name = name, None
            return _func(f)

        return _func

    def set_param(self, name: str, key: str, _len=0):
        """
        Set param for using in CLI function
        :param name: command name used in CLI
        :param key: kwargs name used in CLI function
        :param _len: len of parameter
        :return: None
        """

        param = Param(key, _len)
        self.parser.set_param(name, param)

    def parse(self, cli):
        """
        Parse sub CLI
        :param cli: cli
        :return: funcs, params, flag
        """

        self.parser.cli = cli
        return self.parser.parse()
