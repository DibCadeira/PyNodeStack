from src.core.factory import Factory


class NodeStack:
    def __init__(self):
        self.nodes = []
        self.stack = []

    def add(self, node: str):
        self.nodes.append(Factory.create(node))
        return self.nodes[-1]

    def set_node_data(self, index: int, data: dict):
        node = self.nodes[index]
        node.data = node.data | data

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        return self.stack.pop()

    def remove(self, index):
        self.nodes.pop(index)

    def eval(self):
        for node in self.nodes:
            print(f"Computing >> {node.name}")
            node.eval({"push": self.push, "pop": self.pop})

        return self.stack[0]
