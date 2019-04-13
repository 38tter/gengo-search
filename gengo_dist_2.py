import codecs
import numpy as np
import matplotlib.pyplot as plt
from gensim.models.word2vec import Word2Vec
import gensim
from statistics import mean, stdev
import random

JPChmodel_path = 'mychar2vec_fromWikiALL.model'
JPChmodel_from_shishogokyou_path = 'mychar2vec_fromShishogokyou.model'
JPmodel = Word2Vec.load(JPChmodel_path)
JPmodel_from_shishogokyou = Word2Vec.load(JPChmodel_from_shishogokyou_path)

list1 = codecs.open('gengo_ichiran2.txt', 'r', 'utf-8')
list2 = []
list3 = codecs.open('miyata_gengo2.txt', 'r', 'utf-8')
list4 = []
list5 = codecs.open('shishogokyou_shinji.txt', 'r', 'utf-8')
list6 = []

distancelist = []
distancelist_m = []
distancelist_r = []

for line in list1:
  list2.append(line)

for line2 in list3:
  list4.append(line2)

for line3 in list5:
  list6.append(line3)

for idx in range(0, len(list2)):
  try:
    distance = JPmodel_from_shishogokyou.similarity(list2[idx][0], list2[idx][1])
    distancelist.append(distance)
  except KeyError as error:
    print(error)

left = np.array(range(0, len(distancelist)))
height = np.array(distancelist)

for idx2 in range(0, len(list4)):
  try:
    distance_m = JPmodel_from_shishogokyou.similarity(list4[idx2][0], list4[idx2][1])
    distancelist_m.append(distance_m)
  except KeyError as error:
    print(error)

index2word = JPmodel_from_shishogokyou.wv.index2word
for idx3 in range(0, len(list2)):
  try:
    #distance_r = JPmodel_from_shishogokyou.similarity(random.choice(list6), random.choice(list6))
    distance_r = JPmodel_from_shishogokyou.similarity(random.choice(list6[0]), random.choice(list6[0]))
    distancelist_r.append(distance_r)
  except KeyError as error:
    print(error)

hili = []
for idx4 in range(0, 100000):
  try:
    hili.append(JPmodel_from_shishogokyou.similarity(random.choice(list6[0]), random.choice(list6[0])))
  except KeyError as error:
    print(error)

left2 = np.array(range(0, len(distancelist_m)))
height2 = np.array(distancelist_m)

left3 = np.array(range(0, len(distancelist_r)))
height3 = np.array(distancelist_r)

mean = np.mean(distancelist)
std = np.std(distancelist)
var = np.var(distancelist)
sem = np.std(distancelist)/np.sqrt(252)

mean_m = np.mean(distancelist_m)
std_m = np.std(distancelist_m)
var_m = np.var(distancelist_m)
sem_m = np.std(distancelist_m)/np.sqrt(32)

mean_r = np.mean(distancelist_r)
std_r = np.std(distancelist_r)
var_r = np.var(distancelist_r)
sem_r = np.std(distancelist_r)/np.sqrt(252)

mean_rc = np.mean(hili)
std_rc = np.std(hili)
var_rc = np.var(hili)
plt.xlabel("gengo")
plt.ylabel("cosine similarity")
plt.ylim(-0.6, 1.)
plt.annotate("Learned from Shisho-gokyo (except for Raiki),\npast,\nmean: {0:.2f}±{1:.2f} std: {2:.2f} var: {3:.2f}".format(mean, sem, std, var), xy=(50., 0.7), color='royalblue')
plt.annotate("Learned from Shisho-gokyo (except for Raiki),\nprediction,\nmean: {0:.2f}±{1:.2f} std: {2:.2f} var: {3:.2f}".format(mean_m, sem_m, std_m, var_m), xy=(0., -0.4), color='limegreen')
plt.annotate("Learned from Shisho-gokyo (except for Raiki),\nrandom choice,\nmean: {0:.2f}±{1:.2f} std: {2:.2f} var: {3:.2f}".format(mean_r, sem_r, std_r, var_r), xy=(50., 0.4), color='orangered')
plt.plot(left, height, color='royalblue')
plt.plot(left2, height2, color='limegreen')
plt.plot(left3, height3, color='orangered')
plt.savefig("pdf/gengo_dist.png")

#plt.annotate("Learned from Shisho-gokyo\n(except for Raiki),\nrandom choice, \nmean: {0:.2f} std: {1:.2f} var: {2:.2f}".format(mean_rc, std_rc, var_rc), xy=(0.3, 1000))
#plt.hist(hili, bins=200)
#plt.savefig("pdf/gengo_random.png")
