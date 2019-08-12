
class Param:
    def __init__(self, _type=None, _len=0):
        self.type = _type
        self.len = _len
        self.val = None

    def add_val(self, _val):
        if self.val:
            try:
                self.val.append(_val)
            except:
                self.val = list(self.val)
                self.val.append(_val)
        else:
            self.val = _val
