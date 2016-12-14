from gensim.models import word2vec
import numpy as np
import matplotlib.pyplot as plt

def responce(goal, file_name):
  # 学習済みモデルのロード
  model = word2vec.Word2Vec.load(file_name)

  A = input()
  B = goal
  while True:
    intention_list = []

    # Aの類似語を集める　類似度順にソート
    similar_words = model.most_similar(positive=[A], negative=[])
    similar_words.sort(key=lambda x: float(x[1]), reverse=True)
    
    print(similar_words) 
    print("単語\t" + A + "との類似度")
    
    for s in similar_words:
      print(s[0] + "\t" + str(s[1]))

      # 各類似語とゴールとの類似度の比較
      intention_list.append((s[0],model.similarity(B,s[0])))
    
    intention_list.sort(key=lambda x: float(x[1]), reverse=True)
    #print(intention_list)
    
    print("\n単語\t" + B + "との類似度")
    for il in intention_list:
      print(il[0] + "\t" + str(il[1]))
    
    print("=======================================================")
    print("「" + intention_list[0][0] + "」")
    A = input()
  

if __name__=='__main__':
  goal = "徳島"
  file_name = "sample(size100_mc20_w10).model" 
  responce(goal, file_name)
