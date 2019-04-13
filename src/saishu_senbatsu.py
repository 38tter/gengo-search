from gensim.models import Word2Vec
import codecs

JPChmodel_path = 'mychar2vec_fromWikiALL.model'
JPmodel = Word2Vec.load(JPChmodel_path)
kouho = codecs.open("saishu_kouho.txt", 'r', 'UTF-8')
datpath = 'saishu_kumiawase.dat'

mean = 0.26
std = 0.23
cutoff = 0.3

kouho_list = []
for line in kouho:
  kouho_list.append(line)

hodoyoikyorilist = []
for idx1 in range(0, len(kouho_list)):
  try:
    distance = JPmodel.similarity(kouho_list[idx1][0], kouho_list[idx1][1])
    #if(mean-std<distance and distance<mean+std):
    if(distance>cutoff):
      absval = abs(distance - mean)
      hodoyoikyorilist.append([kouho_list[idx1], distance, absval])
  except KeyError as error:
    print(error)

finalkouho = sorted(hodoyoikyorilist, key=lambda x:x[1], reverse=False)

for gengo in finalkouho:
  with open(datpath, mode='a') as f:
    name = gengo[0].replace('\n','')
    f.write('\n{0}'.format(name))
