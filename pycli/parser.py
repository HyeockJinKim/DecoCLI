from sys import argv


class Parser:
    def __init__(self):
        self.commands = {}
        self.params = {}
        self.cli = argv

    def set_param(self, name, param):
        self.params[name] = param

    def set_cmd(self, name, cmd):
        self.commands[name] = cmd

    def add_param(self, name, param):
        if self.params[name]:
            self.params[name] = param
        else:
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

