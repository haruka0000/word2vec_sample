from gensim.models import word2vec

## word1
word1  = input('Word 01 >')

## 演算記号
math = input('+ or - or e(End)>')

if math == '+' or math == '-':
  ## word2
  word2  = input('Word 02 >')


data = word2vec.Text8Corpus('data.txt')
model = word2vec.Word2Vec(data, size=200)

## 演算
if math == "+":   ## word1 + word2
  out=model.most_similar(positive=[word1,word2])
if math == "-":   ## word1 - word2
  out=model.most_similar(positive=[word1], negative=[word2])
if math == "e":   ## word1
  out=model.most_similar(positive=[word1])
  
for x in out:
  print(x[0],x[1])
