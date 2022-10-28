
from cmath import isnan


def find(soup, label_name, attrib=None):
    content = ""
    for label in soup.find_all(label_name):
        if attrib:
            result = label.get(attrib)
        else:
            result = label.content

        if result:
                content += result + "\n"

    return content
