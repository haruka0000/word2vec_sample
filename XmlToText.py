from xml.etree import ElementTree

XMLFILE = "jawiki-latest-pages-articles2.xml"

tree = ElementTree.parse(XMLFILE)  # ファイルから読み込み
root = tree.getroot()

signs = ["[","]","*","{","}","=","|","-","<",">",":",";","'",]

for e in root.getiterator():
  if 'text' in e.tag:
    result = e.text
    for s in signs:
      try:
        result = result.replace(s,"")
      except:
        result = result
    print(result)
