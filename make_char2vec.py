import logging
from gensim.models import word2vec

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

sentences = word2vec.Text8Corpus('allWiki_1kugiri.txt')
model = word2vec.Word2Vec(sentences, size=60, window=60, min_count=50, hs=1, negative=15, iter=6)

model.save("mychar2vec_fromWikiALL.model")
print("model generation ended.")
