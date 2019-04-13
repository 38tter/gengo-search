import logging
from gensim.models import word2vec

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

#sentences = word2vec.Text8Corpus('shishogokyou_kugiri_shinji.txt')
sentences = word2vec.Text8Corpus('45_gokan_shinji_half_kugiri.txt')
#sentences = word2vec.Text8Corpus('nukidashi_corpus_kugiri.txt')
model = word2vec.Word2Vec(sentences, size=60, window=5, min_count=10, hs=1, negative=0, iter=10)
#model = word2vec.Word2Vec(sentences, size=60, window=8, min_count=50, hs=0, negative=0, iter=10)

model.save("mychar2vec_fromShishogokyou.model")
print("model generation ended.")
