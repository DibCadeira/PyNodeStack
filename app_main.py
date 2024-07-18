from PySide6.QtWidgets import QApplication
from src.editor.app import Window
import sys


root = QApplication([])

window = Window()
window.add("CellularNoise")
window.add("Image")
window.show()

sys.exit(root.exec())