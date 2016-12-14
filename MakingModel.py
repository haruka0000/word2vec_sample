from gensim.models import word2vec
import logging

# 進捗表示用
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


data = word2vec.Text8Corpus("data.txt")
model = word2vec.Word2Vec(data, size=100, min_count=20, window=10)

# 学習結果を出力する
model.save("sample(size100_mc20_w10).model")

