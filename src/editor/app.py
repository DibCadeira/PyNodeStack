from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout
from src.core.nodestack import NodeStack
from src.editor.factory import Factory
import sys


class Window(QWidget):
    def __init__(self):
        self.node_stack = NodeStack()

        layout = QVBoxLayout()
        layout.addWidget(self.add("Add"))
        self.setLayout(layout)

    def add(self, node: str):
        n = self.node_stack.add(node)
        return Factory.create(n.view)


root = QApplication([])
window = Window()
window.show()
sys.exit(root.exec())
