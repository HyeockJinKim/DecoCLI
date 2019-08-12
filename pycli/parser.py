from sys import argv


class Parser:
    def __init__(self):
        self.commands = {}
        self.params = {}
        self.cli = argv[1:]
        self.func = None

    def parse(self):
        for cmd in self.cli:
            try:
                self.func = self.commands[cmd]
            except:
                pass

    def set_param(self, name, param):
        self.params[name] = param

    def set_cmd(self, name, cmd):
        self.commands[name] = cmd

    def add_param(self, name, param):
        try:
            self.params[name].append(param)
        except:
            self.params[name] = list(self.params[name])
            self.params[name].append(param)

    def add_params(self, name, params):
        if params is None:
            params = []

        for param in params:
            try:
                self.params[name].append(param)
            except:
                self.params[name] = list(self.params[name])
                self.params[name].append(param)
