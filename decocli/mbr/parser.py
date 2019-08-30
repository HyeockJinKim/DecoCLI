from sys import argv

from decocli.mbr.cmd import Command
from decocli.mbr.param import Param


class Parser:
    def __init__(self):
        self.commands = {}
        self.params = {}

        def _cli():
            for cmd in argv[1:]:
                yield cmd

        self.cli = _cli()

    def set_cmd(self, name: str, cmd: Command):
        if name in self.commands.keys():
            print('This keyword "', name, '" is already set')
            exit(-1)
        self.commands[name] = cmd

    def set_param(self, name: str, _param: Param):
        self.params[name] = _param

    def parse(self):
        funcs = []
        params = {}
        while True:
            cmd = self._consume()
            if not cmd:
                break

            func = self._parse_command(cmd)
            if func:
                funcs.append(func)
                continue

            param_name = self.params[cmd].name
            params[param_name] = self._parse_param(cmd)

        return funcs, params

    def _parse_command(self, cmd):
        try:
            commands = self.commands
            return commands[cmd]
        except KeyError:
            return None

    def _parse_param(self, cmd):
        try:
            param_len = self.params[cmd].len
            return self._consume_param(param_len)
        except KeyError:
            print('This keyword "', cmd, '" is not set for your CLI.')
            exit(-1)

    def _consume(self):
        try:
            return next(self.cli)
        except StopIteration:
            return None

    def _consume_param(self, _len):
        if _len == 1:
            cmd = self._consume()
            return cmd

        params = []
        for i in range(_len):
            cmd = self._consume()
            if not cmd:
                print('This param ', cmd, " don't have enough param.")
                exit(-1)

            params.append(cmd)
        return params
