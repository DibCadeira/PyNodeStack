def parse(folder, source: str) -> dict:
    lines = source.splitlines()
    node = {"category": folder, "view": [], "data": {}, "compute": ""}

    for i in range(len(lines)):
        line = lines[i]

        if line.startswith("!"):
            _parse_data(node, line)
        elif line.startswith("compute"):
            _parse_compute(node, lines[i + 1 :])

    return node


def _parse_data(node, string):
    string = string.split("-")
    name = string[0].strip().replace("!", "")
    widget = string[1].strip()
    value = string[2].strip()

    if "String" in widget:
        node["data"][name] = value
        _parse_string_widget(node, widget)

    elif "Number" in widget:
        if "." in value:
            node["data"][name] = float(value)
        else:
            node["data"][name] = int(value)

        _parse_number_widget(node, widget)

    elif "Boolean" in widget:
        node["data"][name] = bool(value)
        _parse_boolean_widget(node, widget)

    elif "Dropdown" in widget:
        node["data"][name] = value
        _parse_dropdown_widget(node, widget)

    elif "Slider" in widget:
        node["data"][name] = float(value)
        _parse_slider_widget(node, widget)

    elif "Colorpicker" in widget:
        node["data"][name] = value
        _parse_colorpicker_widget(node, widget)


def _parse_compute(data, lines):
    def _del_newline_and_tab(line):
        if line.startswith("\n\t"):
            return line[2:]
        return line

    compute = ""

    for line in lines:
        line = _del_newline_and_tab(line)
        compute = f"{compute}\n{line}"

    data["compute"] = compute


def _parse_string_widget(node, widget):
    node["view"].append({"widget": "String"})


def _parse_number_widget(node, widget):
    node["view"].append({"widget": "Number"})


def _parse_boolean_widget(node, widget):
    node["view"].append({"widget": "Boolean"})


def _parse_dropdown_widget(node, widget):
    items = widget.replace("Dropdown[", "").replace("]", "")
    items = [item.strip() for item in items.split(",")]

    node["view"].append({"widget": "Dropdown", "items": items})


def _parse_slider_widget(node, widget):
    values = widget.replace("Slider[", "").replace("]", "")
    values = [float(value.strip()) for value in values.split(",")]

    node["view"].append({"widget": "Slider", "min": values[0], "max": values[1]})


def _parse_colorpicker_widget(node, widget):
    node["view"].append({"widget": "Colorpicker"})
