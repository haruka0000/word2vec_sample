from xml.etree import ElementTree

XMLFILE = "jawiki-latest-pages-articles1.xml"

tree = ElementTree.parse(XMLFILE)  # ファイルから読み込み
root = tree.getroot()

f = open( "wiki_text.txt", "w" )
for e in root.getiterator():
  if 'text' in e.tag:
    print(e.text)
    f.write(str(e.text)) # textの書き出し
f.close()
