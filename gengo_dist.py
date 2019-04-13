import codecs
import numpy as np
import matplotlib.pyplot as plt
from gensim.models.word2vec import Word2Vec
import gensim
from statistics import mean, stdev

JPChmodel_path = 'mychar2vec_fromWikiALL.model'
JPChmodel_from_shishogokyou_path = 'mychar2vec_from_shishogokyou.model'
JPmodel = Word2Vec.load(JPChmodel_path)
JPmodel_from_shishogokyou = Word2Vec.load(JPChmodel_path_from_shishogokyou)

list1 = codecs.open('gengo_ichiran2.txt', 'r', 'utf-8')
list2 = []
list3 = codecs.open('miyata_gengo.txt', 'r', 'utf-8')
list4 = []

distancelist = []
distancelist_m = []

for line in list1:
  list2.append(line)

for line2 in list3:
  list4.append(line2)

for idx in range(0, len(list2)):
  distance = JPmodel.similarity(list2[idx][0], list2[idx][1])
  distancelist.append(distance)

left = np.array(range(0, len(distancelist)))
height = np.array(distancelist)

for idx2 in range(0, len(list4)):
  distance_m = JPmodel.similarity(list4[idx2][0], list4[idx2][1])
  distancelist_m.append(distance_m)

left2 = np.array(range(0, len(distancelist_m)))
height2 = np.array(distancelist_m)

mean = np.mean(distancelist)
std = np.std(distancelist)
var = np.var(distancelist)

mean_m = np.mean(distancelist_m)
std_m = np.std(distancelist_m)
var_m = np.var(distancelist_m)

plt.xlabel("gengo")
plt.ylabel("cosine similarity")
plt.annotate("mean: {0:.2f} std: {1:.2f} var: {2:.2f}".format(mean, std, var), xy=(125., 0.8), color='royalblue')
plt.annotate("mean: {0:.2f} std: {1:.2f} var: {2:.2f}".format(mean_m, std_m, var_m), xy=(0., -0.3), color='orangered')
plt.plot(left, height, color='royalblue')
plt.plot(left2, height2, color='orangered')
plt.savefig("pdf/gengo_dist.png")
