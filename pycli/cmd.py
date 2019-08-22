
class Command:
    def __init__(self, _func, _len):
        self.func = _func
        self.len = _len

    def exec(self, params):
        try:
            self.func(kwargs=params)
        except TypeError:
            print('This Command has problem')
            exit(-1)
