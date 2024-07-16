from src.core.factory import Factory


class NodeStack:
    def __init__(self):
        self.nodes = []
        self.stack = []

    def add(self, node: str):
        self.nodes.append(Factory.create(node))

    def set_data(self, index: int, data: list):
        self.nodes[index].data = data

    def remove(self, index):
        self.nodes.pop(index)

    def eval(self):
        for node in self.nodes:
            node.eval(self.stack)

        return self.stack[0]
