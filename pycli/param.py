
class Param:
    def __init__(self, _type=None, _len=1):
        self.type = _type
        self.len = _len
        self.val = []

    def add_val(self, _val):
        if len(self.val) >= self.len:
            return

        self.val.append(_val)
