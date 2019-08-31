
from decocli.mbr.cmd import Command
from decocli.mbr.param import Param


class Parser:
    def __init__(self, cli=None):
        self.sub = {}
        self.commands = {}
        self.params = {}
        self.cli = cli

    def add_sub(self, _sub):
        if _sub.name in self.sub.keys():
            print('This keyword "', _sub.name, '" is already set')
            exit(-1)

        self.sub[_sub.name] = _sub

    def set_cmd(self, name: str, cmd: Command):
        if name in self.commands.keys():
            print('This keyword "', name, '" is already set')
            exit(-1)

        self.commands[name] = cmd

    def set_param(self, name: str, _param: Param):
        self.params[name] = _param

    def parse(self):
        """
        Parse CLI
        :return: func, params, flag
        """
        funcs = []
        params = {}
        while True:
            cmd = self._consume()
            if not cmd:
                break
            func, param, flag = self._parse_sub_cli(cmd)
            if flag >= 0:
                funcs += func
                params.update(param)
                continue

            func = self._parse_command(cmd)
            if func:
                funcs.append(func)
                continue

            name, param = self._parse_param(cmd)
            if param:
                params[name] = param
            else:
                return funcs, params, 0

        return funcs, params, 1

    def _parse_sub_cli(self, cmd):
        try:
            return self.sub[cmd].parse(self.cli)
        except KeyError:
            return None, None, -1

    def _parse_command(self, cmd):
        try:
            return self.commands[cmd]
        except KeyError:
            return None

    def _parse_param(self, cmd):
        try:
            param_len = self.params[cmd].len
            param_name = self.params[cmd].name
            return param_name, self._consume_param(param_len)
        except KeyError:
            print('This keyword "', cmd, '" is not set for your CLI.')
            return None, None

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
