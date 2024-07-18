from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from src.editor.widgets.textinput import TextInput


class NodeWidget(QWidget):
    def __init__(self, title, node):
        super().__init__()
        layout = QVBoxLayout()
        label = QLabel(title)
        layout.addWidget(label)

        for data in node.view:
            if data["widget"] == "String":
                layout.addWidget(TextInput(data, node))

            elif data["widget"] == "Number":
                layout.addWidget(TextInput(data, node))

        self.setLayout(layout)
