from gensim.models import word2vec

# 学習済みモデルのロード
model = word2vec.Word2Vec.load("sample.model")

while True:
  print("(word1)ENTER   OR   (word1) (+ or -) (word2)ENTER")
  words = input('>> ').split(" ")

  ## word1
  word1 = words[0]

  ## 演算
  if len(words) == 3:
  
    word2 = words[2]
    ## 演算記号
    math = words[1]
  
    if math == "+":   ## word1 + word2
      out=model.most_similar(positive=[word1,word2])
    if math == "-":   ## word1 - word2
      out=model.most_similar(positive=[word1], negative=[word2])
  else :   ## word1
    out=model.most_similar(positive=[word1])
  
  for x in out:
    print(x[0],x[1])
  print("\n")
