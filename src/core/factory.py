from src.core.node import Node
import json

NODES = None


class Factory:
    @staticmethod
    def create(name: str):
        base_node = NODES[name]
        return Node(base_node["data"], base_node["view"], base_node["compute"])

    @staticmethod
    def preload(path):
        global NODES
        with open(path, "r") as file:
            NODES = json.load(file)


Factory.preload("nodes.json")
