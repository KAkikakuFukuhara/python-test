""" 複雑なxmlファイルの作成
"""
import xml.etree.ElementTree as et


if __name__ == "__main__":
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

    # XMLファイルを作成する
    tree.write('example.xml', encoding='utf-8', xml_declaration=True)
