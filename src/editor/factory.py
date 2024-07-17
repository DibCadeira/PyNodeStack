from PySide6.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QSlider, QComboBox


class Factory:
    @staticmethod
    def create(view):
        root = QWidget()
        layout = QVBoxLayout()
        root.setLayout(layout)

        for data in view:
            if data["widget"] == "String":
                layout.addWidget(QLineEdit())
            elif data["widget"] == "Number":
                layout.addWidget(QLineEdit())
            elif data["widget"] == "Boolean":
                print("Boolean Widget")

        return root
