from sys import argv

from decocli.cmd import Command
from decocli.param import Param


class Parser:
    def __init__(self):
        self.commands = {}
        self.params = {}

        def _cli():
            for cmd in argv[1:]:
                yield cmd

        self.cli = _cli()

    def set_cmd(self, name: str, cmd: Command):
        self.commands[name] = cmd

    def set_param(self, name: str, _param: Param):
        self.params[name] = _param

    def parse(self):
        funcs = []
        params = {}
        cli = self.cli
        while True:
            try:
                cmd = next(cli)
            except StopIteration:
                break

            try:
                funcs.append(self.commands[cmd])
            except KeyError:
                try:
                    param_len = self.params[cmd].len
                    param_name = self.params[cmd].name
                    if param_len > 1:
                        params[param_name] = []

                    for i in range(param_len):
                        try:
                            if param_len > 1:
                                params[param_name].append(next(cli))
                            else:
                                params[param_name] = next(cli)
                        except StopIteration:
                            print('This param ', cmd, " don't have enough param.")
                            exit(-1)
                except KeyError:
                    print('This keyword "', cmd, '" is not set for your CLI.')
                    exit(-1)

        return funcs, params
