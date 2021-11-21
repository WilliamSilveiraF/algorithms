# from urllib import urlopen
# from xml.etree.ElementTree import parse

# var_url = urlopen("https://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml?5105e8233f9433cf70ac379d6ccc5775")
# xmldoc = parse(var_url)

# for item in xmldoc.iterfind('channel/item'):
#    print(item)

import xml.dom.minidom


def main():
    doc = xml.dom.minidom.parse("Myxml.xml");

    print(doc.nodeName)
    print(doc.firstChild.tagName)

    expertise = doc.getElementsByTagName("expertise")
    print(f"expertise: {expertise.length}")
    for skill in expertise:
        print("{}".format(skill.getAttribute("name")))


if __name__ == "__main__":
    main();