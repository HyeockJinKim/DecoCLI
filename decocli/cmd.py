
class Command:
    def __init__(self, _func, _len):
        self.func = _func
        self.len = _len

    def exec(self, params=None):
        try:
            return self.func(**params)
        except TypeError:
            pass
        try:
            return self.func()
        except TypeError:
            print('This Command has problem')
            exit(-1)
