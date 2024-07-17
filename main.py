from src.core.nodestack import NodeStack

nstack = NodeStack()
nstack.add("CellularNoise")
nstack.set_node_data(0, {"width": 1024, "height": 1024, "num_points": 36, "scale": 2})
nstack.add("Image")
nstack.eval()
