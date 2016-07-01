from gensim.models import word2vec

if __name__=='__main__':
  start = "国"
  goal = "人"
  similarities = {}
  # 学習済みモデルのロード
  model = word2vec.Word2Vec.load("sample.model")
 
  out=model.most_similar(positive=[start], negative=[])
  for o in out:
    print(o)
  print()
  out=model.most_similar(positive=[goal], negative=[])
  for o in out:
    print(o)
  print()

  intention = start
  while intention[0] != goal:
    out=model.most_similar(positive=[intention], negative=[])
    for o in out:
      similarities[o[0]] = model.similarity(goal,o[0])
 
    most_similar = sorted(similarities.items(), key=lambda x: x[1], reverse=True)[0]
    if most_similar[0] == intention[0]:
      print("The word can no longer go near")
      break
    else:
      intention = most_similar
      print(intention)
