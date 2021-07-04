import os.path
import markdown


def openfile(filename):
    filepath = os.path.join("app/pages/", filename)
    with open(filepath, "r", encoding="utf-8") as input_file:
        content_md = input_file.read()

    md_to_html = markdown.markdown(content_md)
    data = {
        'content': md_to_html
    }
    return data