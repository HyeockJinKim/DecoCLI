
class Command:
    def __init__(self, _func):
        self.func = _func

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
