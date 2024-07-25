from src.core.node import Node
import json


class NodeStack:
    def __init__(self):
        self.nodes = []
        self.stack = []
        self.bundle = None

        self._preload("bundle.json")

    def insert(self, node: str, data=None):
        base = self.bundle[node]
        self.nodes.append(Node(base))

        if data:
            self.set_node_data(-1, data)

        return self.nodes[-1]

    def remove(self, index):
        self.nodes.pop(index)

    def set_node_data(self, index: int, data: dict):
        node = self.nodes[index]
        node.data = node.data | data

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        return self.stack.pop()

    def eval(self):
        for node in self.nodes:
            print(f">> {node.name}")
            node.eval({"push": self.push, "pop": self.pop})

        return self.stack

    def _preload(self, path):
        with open(path, "r") as file:
            self.bundle = json.load(file)
