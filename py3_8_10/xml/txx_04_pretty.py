""" lxml.etree.parseを作成から保存まで一次ファイルを使用して実装
"""
import os
import xml.dom.minidom as md
import xml.etree.ElementTree as et
import tempfile


def make_etree():
    # ルート要素を作成する
    root = et.Element('root')

    # 子要素を作成する
    child1 = et.SubElement(root, 'child1')

    # 子要素を作成する
    child1_2 = et.SubElement(child1, 'child1_2')
    child1_2.text = 'Hello, World!'
    # 子要素を作成する
    child1_3 = et.SubElement(child1, 'child1_3')
    child1_3.text = 'Hello, World!'
    # 子要素を作成する
    child1_4 = et.SubElement(child1, 'child1_4')
    child1_4.text = 'Hello, World!'

    # 要素のツリーを作成する
    tree = et.ElementTree(root)

    return tree

    # XMLファイルを作成する


if __name__ == "__main__":
    ## 参考
    ## https://stackoverflow.com/questions/749796/pretty-printing-xml-in-python

    FILE_NAME = "example.xml"

    ## element tree の作成
    etree = make_etree()

    ## 一時ファイルに保存してdomでロードする
    with tempfile.NamedTemporaryFile(delete=True) as t:
        etree.write(t.name, encoding='utf-8', xml_declaration=True)

        dom = md.parse(t.name)

    ## 出力をきれいにする（インデントとか）
    # To parse string instead use: dom = md.parseString(xml_string)
    pretty_xml: str = dom.toprettyxml()
    # remove the weird newline issue:
    pretty_xml: str = os.linesep.join([s for s in pretty_xml.splitlines()
                                if s.strip()])

    ## 保存
    DST_FILE_NAME= "pretty_example.xml"
    with open(DST_FILE_NAME, "w") as f:
        f.write(pretty_xml)
