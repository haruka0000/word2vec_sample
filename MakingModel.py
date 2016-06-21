from gensim.models import word2vec
import logging

# 進捗表示用
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

data = word2vec.Text8Corpus('tweets.txt')
model = word2vec.Word2Vec(data, size=200)

# 学習結果を出力する
model.save("sample.model")

