class Node:
    def __init__(self, name, data, view, compute):
        self.name = name
        self.data = data
        self.view = view
        self.compute = compute

    def eval(self, stack_operations):
        _locals = self.data | stack_operations
        exec(self.compute, globals(), _locals)
