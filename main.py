from src.core.nstack import NodeStack

nstack = NodeStack()
nstack.insert("CellularNoise", {"width": 256, "height": 256, "num_points": 32, "scale": 2})
nstack.insert("Image", { "path": "TexLabPro.jpg"})
#nstack.insert("EditableImage")

print(type(nstack.eval()[0]))