def parse(folder, source: str) -> dict:
    lines = source.splitlines()
    node = {"category": folder, "ui": [], "data": {}, "src": ""}

    for i in range(len(lines)):
        line = lines[i]

        if line.startswith("@"):
            _parse_data(node, line)
        elif line.startswith("exec"):
            _parse_exec(node, lines[i + 1 :])

    return node


def _parse_data(node, string):
    string = string.split("-")
    name = string[0].strip().replace("@", "")
    widget = string[1].strip()
    value = string[2].strip()

    if "String" in widget:
        node["data"][name] = value
        _parse_string_widget(node, name, widget)

    elif "Number" in widget:
        if "." in value:
            node["data"][name] = float(value)
        else:
            node["data"][name] = int(value)

        _parse_number_widget(node, name, widget)

    elif "Boolean" in widget:
        node["data"][name] = bool(value)
        _parse_boolean_widget(node, name, widget)

    elif "Dropdown" in widget:
        node["data"][name] = value
        _parse_dropdown_widget(node, name, widget)

    elif "Slider" in widget:
        node["data"][name] = float(value)
        _parse_slider_widget(node, name, widget)

    elif "Colorpicker" in widget:
        node["data"][name] = value
        _parse_colorpicker_widget(node, name, widget)


def _parse_exec(data, lines):
    def _del_newline_and_tab(line):
        if line.startswith("\n\t"):
            return line[2:]
        return line

    src = ""

    for line in lines:
        line = _del_newline_and_tab(line)
        src = f"{src}\n{line}"

    data["src"] = src


def _parse_string_widget(node, name, widget):
    node["ui"].append({"name": name, "widget": "String", })


def _parse_number_widget(node, name, widget):
    node["ui"].append({"name": name, "widget": "Number"})


def _parse_boolean_widget(node, name, widget):
    node["ui"].append({"name": name, "widget": "Boolean"})


def _parse_dropdown_widget(node, name, widget):
    items = widget.replace("Dropdown[", "").replace("]", "")
    items = [item.strip() for item in items.split(",")]

    node["ui"].append({"name": name, "widget": "Dropdown", "items": items})


def _parse_slider_widget(node, name, widget):
    values = widget.replace("Slider[", "").replace("]", "")
    values = [float(value.strip()) for value in values.split(",")]

    node["ui"].append(
        {"name": name, "widget": "Slider", "min": values[0], "max": values[1]}
    )


def _parse_colorpicker_widget(node, name, widget):
    node["ui"].append({"name": name, "widget": "Colorpicker"})
