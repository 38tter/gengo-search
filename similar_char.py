import codecs
from gensim.models.word2vec import Word2Vec
JPChmodel_from_shishogokyou_path = 'mychar2vec_fromShishogokyou.model'
#JPChmodel_from_shishogokyou_path = 'mychar2vec_fromWikiALL.model'
JPmodel_from_shishogokyou = Word2Vec.load(JPChmodel_from_shishogokyou_path)

str = "永元天治応正長文和安延暦寛徳保承仁嘉平康宝久慶建享弘貞明禄大亀寿万化観喜神政中養雲護"
nnn = 100
mean = 0.10
std = 0.14
cutoff = 0.3

list1 = codecs.open('joyokanji.txt', 'r', 'utf-8')
list2 = codecs.open('kyoikukanji.txt', 'r', 'utf-8')
list_joyo = []
list_kyoiku = []

datpath = 'saishu_kouho.txt'
allresult = ""

for line in list1:
  list_joyo.append(line)

for line2 in list2:
  list_kyoiku.append(line2)

for idx in range(0, len(str)):
  try:
    out = JPmodel_from_shishogokyou.most_similar(positive = str[idx], topn=nnn)
    resulttext=""
    resulttext+=str[idx]+": "

    if list_kyoiku.count(str[idx]):
      allresult+=str[idx]

    for var in range(0, nnn):
      #if(out[var][1]>mean-std and out[var][1]<mean+std):
      if(out[var][1]>cutoff):
        if str.count(out[var][0]):
          resulttext+="("+out[var][0]+")"
          with open(datpath, mode='a') as f:
              f.write('\n{0}{1}'.format(str[idx], out[var][0]))
              f.write('\n{1}{0}'.format(str[idx], out[var][0]))
        else:
          if list_kyoiku[0].count(out[var][0]):
            resulttext+="【"+out[var][0]+"】"
            allresult+=out[var][0]
            with open(datpath, mode='a') as f:
                f.write('\n{0}{1}'.format(str[idx], out[var][0]))
                f.write('\n{1}{0}'.format(str[idx], out[var][0]))
          else:
            if list_joyo[0].count(out[var][0]):
              resulttext+="{"+out[var][0]+"}"
    print(resulttext)

  except KeyError as error:
    print(error)

lst = list(set(allresult))

#print(','.join(lst))
#print(len(lst))

resultlist = []
for lstidx in range(0, len(lst)):
  distance=0
  cnt=0
  for stridx in range(0, len(str)):
    if lst[lstidx] != str[stridx]:
      try:
        distance += JPmodel_from_shishogokyou.similarity(lst[lstidx], str[stridx])
        cnt+=1
      except KeyError as error:
        print(error)

  resultlist.append([lst[lstidx],distance/cnt])

ranking = sorted(resultlist, key=lambda x:x[1], reverse=True)

finalkouho=ranking[:30]
import pprint
pprint.pprint(finalkouho)
