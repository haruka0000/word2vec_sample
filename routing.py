from gensim.models import word2vec
import numpy as np
import matplotlib.pyplot as plt

def plot(ary_dct):
	key_list = []
	key_list.append(ary_dct.keys())
	value_list = []
	value_list.append(ary_dct.keys())
	x = range(1,len(array))
	y = 
	fig = plt.figure()

	ax = fig.add_subplot(1,1,1)
	ax.scatter(x,y)
	
	ax.set_title('first scatter plot')
	ax.set_xlabel('x')
	ax.set_ylabel('y')

	fig.show() 

def getRoute(start,goal,fname):
	parray = []
  similarities = {}
  # 学習済みモデルのロード
  model = word2vec.Word2Vec.load(fname)

  print(start)

  out=model.most_similar(positive=[start], negative=[])
  for o in out:
    print(o)
  print()
  #out=model.most_similar(positive=[goal], negative=[])
  #for o in out:
    #print(o)
  #print()
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
  start = "アオミドロ"
  goal = "俊二"
  fname = "sample(size200_mc20_w15).model" 
  getRoute(start, goal, fname)
