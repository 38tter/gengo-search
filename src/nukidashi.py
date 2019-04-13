import re
import codecs
import numpy as np
import matplotlib.pyplot as plt
from gensim.models.word2vec import Word2Vec
import gensim
from statistics import mean, stdev
import random
import sys, io

list = codecs.open('45_gokan_shinji.txt', 'r', 'utf-8')
str = "永元天治応正長文和安延暦寛徳保承仁嘉平康宝久慶建享弘貞明禄大亀寿万化観喜神政中養雲護"

list2 = []
genbun = ""
for line in list:
  list2.append(line)
  genbun+=line

for char in str:
  pattern = ".{5}" + char + ".{5}"
  #print(pattern)
  result_list = re.findall(pattern, genbun)
  for pat in result_list:
    with codecs.open(sys.argv[1], "a", "utf-8") as f:
      f.write(pat)
