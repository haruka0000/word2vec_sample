import MeCab
import sys
from collections import Counter


def collect(t):
  userdic_path="./wikipedia_title.dic"
  mt = MeCab.Tagger("-Ochasen -u " + userdic_path)
  mt.parse('')
  #print(type(t))
  node = mt.parseToNode(t)
  n = []
  while node:
    word_class = node.feature.split(',')
    #print (node.surface, word_class[0], word_class[1])
    if word_class[0] == "名詞":
      if word_class[1] == "一般" or word_class[1] == "固有名詞":
        n.append(node.surface)
    node = node.next
  #n = n[1:-1]
  return n


def count(words):
  counter = Counter(words)
  # 上位50個の単語と個数を返す
  return counter.most_common(50)



if __name__ == '__main__':
  count(['aaa','bbb','aaa','ccc'])
