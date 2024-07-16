class NodeStack:
    def __init__(self):
        self.nodes = []
        self.stack = []

    def eval(self):
        for node in self.nodes:
            node.eval(self.stack)

        return self.stack[0]
