

class Param:
    def __init__(self, name, _len, _types=None):
        self.name = name
        self.len = _len
        self.val = []
        self.types = []

    def add_val(self, _val):
        if len(self.val) >= self.len:
            return

        self.val.append(_val)

    def _type(self, _types):
        if not _types:
            self.types = []
            return

        for i in range(self.len):
            try:
                self.types.append(_types[i])
            except IndexError:
                self.types.append(None)
            except TypeError:
                self.types.append(_types)

