from PySide6.QtWidgets import QLineEdit


def TextInput(data, node):
    def set_value(value):
        node.data[data["name"]] = value

    widget = QLineEdit()
    widget.setPlaceholderText(data["name"])
    widget.textChanged.connect(set_value)

    return widget
