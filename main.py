from src.core.nodestack import NodeStack
import numpy as np

nstack = NodeStack()
nstack.add("CellularNoise")# {"width": 256, "height": 256, "num_points": 13, "scale": 1})
#nstack.add("EditableImage")
nstack.eval()



image = nstack.stack[0]
height, width = image.shape

rgba_image = np.dstack((image, np.full((height, width), 255, dtype=np.uint8)))
linear_rgba_image = rgba_image.flatten()
print(linear_rgba_image.tolist())

print(nstack.stack)