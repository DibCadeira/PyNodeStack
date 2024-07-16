class Node:
    def __init__(self, data, view, compute):
        self.data = data
        self.view = view
        self.compute = compute

    def eval(self, stack):
        exec(self.compute, globals(), {"data": self.data, "stack": stack})
