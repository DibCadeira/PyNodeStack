from src.core.nstack import NodeStack

nstack = NodeStack()
# nstack.insert("LoadImage", {"path": "./assets/mask.jpg"})
# nstack.insert("LoadImage", {"path": "./assets/pug.jpg"})

nstack.insert("CellularNoise", {"num_points": 32, "scale": 3})
nstack.insert("PerlinNoise")
nstack.insert("Multiply")
nstack.insert("SaveImage", {"path": "noise_mul.jpg"})
# nstack.insert("EditableImage")

nstack.eval()
