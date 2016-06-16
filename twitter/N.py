import MeCab
import sys

def collect(text):
  userdic_path="./wikipedia_title.dic"
  mt = MeCab.Tagger("-Ochasen -u " + userdic_path)
  mt.parse('')
  node = mt.parseToNode(text)
  n = []
  while node:
    word_class = node.feature.split(',')
    print (node.surface, word_class[0])
    if word_class[0] == "名詞":
      n.append(node.surface)
    node = node.next
  #n = n[1:-1]
  return n

if __name__ == '__main__':
  f = open('test.txt')
  text = f.read()
  f.close()
  
  n = list(set(collect(text)))

  f = open('text.txt', 'w')
  f.write(' '.join(n))
  f.close()
