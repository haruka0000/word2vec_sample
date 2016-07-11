from gensim.models import word2vec
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
fp = FontProperties(fname = '/usr/share/fonts/truetype/fonts-japanese-gothic.ttf');

def plot(ary):
  key_list = []
  value_list = []
  for num in ary:
    kl = []
    vl = []
    print("__________________________________________")
    for items in num: 
      print(items) 
      kl.append(items[0])
      vl.append(items[1])
    key_list.append(kl)
    value_list.append(vl)

  # 新規のウィンドウを描画
  fig = plt.figure()
  
  ax = fig.add_subplot(1,1,1)
  ax.set_title('first scatter plot')
  ax.set_xlabel('話題転換回数', fontproperties = fp)
  ax.set_ylabel('類似度', fontproperties = fp)
  #plt.ylim(0,1.0)
  plt.xlim(0,len(ary)+1)
  mkl = []
  for i in range(0,len(value_list)):
    for j in range(0,len(value_list[i])):
      if j == 0:
        mkl.append(value_list[i][j])
      else:
        plt.plot(i, value_list[i][j], 'k.')
      # 指定した座標の上にテキストを追加
      plt.text(i, value_list[i][j], key_list[i][j], ha = 'center', va = 'top', fontproperties = fp)

  plt.plot(mkl, '-o')
  plt.show()



def getRoute(start, goal, file_name):
  similarities = {}
  parray = []

  # 学習済みモデルのロード
  model = word2vec.Word2Vec.load(file_name)

  parray.append([(start, model.similarity(goal,start))])

  print(start)

  out=model.most_similar(positive=[start], negative=[])
  for o in out:
    print(o)
  print()
  
  
  intention = (start,model.similarity(goal,start))
  print("==========================================")
  while True:
    print(intention[0],"\t\t",str(int(intention[1]*100)),"% <=")
    near_words = model.most_similar(positive=[intention[0]], negative=[])
    for nw in near_words:
      similarities[nw[0]] = model.similarity(goal,nw[0])    # 付近のワードとゴールのワードの類似度を取得
      print("\t",nw[0],"\t\t",str(int(similarities[nw[0]] * 100)),"%")
 
    nr_rslts = sorted(similarities.items(), key=lambda x: x[1], reverse=True)
    parray.append(nr_rslts)
    most_similar = nr_rslts[0]

    if most_similar[0] == intention[0]:
      print("The word can no longer go near")
      break
    else:
      intention = most_similar
      #print(intention[0])
      
  plot(parray)

if __name__=='__main__':
  start = "高専"
  goal = "美人"
  file_name = "sample(size200_mc20_w15).model" 
  getRoute(start, goal, file_name)
