from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton
from src.core import NodeStack
from src.editor.widgets.node import NodeWidget


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.nstack = NodeStack()
        self.button = QPushButton("Run")
        self.button.clicked.connect(self.eval)

        layout = QVBoxLayout()
        layout.addWidget(self.button)
        self.setLayout(layout)

    def add(self, name: str):
        node = self.nstack.add(name)
        self.layout().addWidget(NodeWidget(name, node))

    def eval(self):
        self.nstack.eval()
