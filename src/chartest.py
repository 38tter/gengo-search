from gensim.models.word2vec import Word2Vec
import gensim
import sys

JPmodel = Word2Vec.load('mychar2vec_fromWikiALL.model') # Learned from Japanese character

out = JPmodel.most_similar(positive=["人"], negative=["王"])

for x in out:
  print(x)
