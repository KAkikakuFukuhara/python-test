import xml.etree.ElementTree as et

if __name__ == "__main__":
    # https://tech-hint.hatenablog.com/entry/2023/02/17/195735
    # ルート要素を作成する
    root = et.Element('root')

    # 子要素を作成する
    child = et.SubElement(root, 'child')
    child.text = 'Hello, World!'

    # 要素のツリーを作成する
    tree = et.ElementTree(root)

    # XMLファイルを作成する
    tree.write('example.xml', encoding='utf-8', xml_declaration=True)

    # きれいに出力したい場合は以下の`lxml`を参考にすること
    # https://stackoverflow.com/questions/749796/pretty-printing-xml-in-python