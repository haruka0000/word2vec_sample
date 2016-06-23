from xml.etree import ElementTree

XMLFILE = "jawiki-latest-abstract.xml"

tree = ElementTree.parse(XMLFILE)  # ファイルから読み込み
root = tree.getroot()
#print (root.tag)# feedと出力
e = root.find('text')
print(e.text)
