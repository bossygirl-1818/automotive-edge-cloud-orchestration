def load_css(css_path):
    with open(css_path, "r", encoding="utf-8") as file:
        return file.read()