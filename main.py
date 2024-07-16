from src.core.builder import build
from src.core.factory import Factory

#build("nodes.json")
node = Factory.create("Add")
node.eval([])
