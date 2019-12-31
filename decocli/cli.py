import types
from sys import argv

from decocli.mbr.cmd import Command
from decocli.mbr.param import Param
from decocli.mbr.parser import Parser
from decocli.mbr.subcli import SubCLI


def _cli():
    for cmd in argv[1:]:
        yield cmd


class CLI:

    parser = Parser(_cli())

    @staticmethod
    def add_sub_cli(sub_cli: SubCLI):
        """

        :return:
        """
        CLI.parser.add_sub(sub_cli)

    @staticmethod
    def clear():
        """
        Clear CLI
        :return: None
        """

        def _cli():
            for cmd in argv[1:]:
                yield cmd

        CLI.parser = Parser(_cli())

    @staticmethod
    def set_cmd(name=None, default=None):
        """
        Set command for using in CLI function
        :param name: command name used in CLI
        :param _len: len of command
        :return: Command function
        """

        def _func(func):
            cmd = Command(func, default)
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

        funcs, params, flag = CLI.parser.parse()
        if flag is 0:
            print('There is command that is not set in CLI')
            exit(-1)
        results = []

        for func in funcs:
            results.append(func.exec(params))

        if len(results) == 1:
            return results[0]

        return results
