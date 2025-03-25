""" lxml.etree.parseの代替
"""
import os
import xml.dom.minidom as md

if __name__ == "__main__":
    ## 参考
    ## https://stackoverflow.com/questions/749796/pretty-printing-xml-in-python

    FILE_NAME = "example.xml"

    dom = md.parse(FILE_NAME)
    # To parse string instead use: dom = md.parseString(xml_string)
    pretty_xml = dom.toprettyxml()
    # remove the weird newline issue:
    pretty_xml = os.linesep.join([s for s in pretty_xml.splitlines()
                                if s.strip()])
    DST_FILE_NAME= "pretty_example.xml"
    with open(DST_FILE_NAME, "w") as f:
        f.write(pretty_xml)
