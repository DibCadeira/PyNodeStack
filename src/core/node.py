class Node:
    def __init__(self, base):
        self.name = base["name"]
        self.data = base["data"]
        self.src = base["src"]
        self.ui = base["ui"]
        

    def eval(self, stack):
        _locals = self.data | stack
        exec(self.src, globals(), _locals)
