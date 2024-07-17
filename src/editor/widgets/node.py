from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel


class NodeWidget(QWidget):
    def __init__(self, title):
        super().__init__()
        layout = QVBoxLayout()
        label = QLabel(title)
        label.setStyleSheet("background-color: yellow; border: 1px solid black;") 
        layout.addWidget()

        self.setLayout(layout)
