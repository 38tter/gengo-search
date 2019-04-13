import requests as web
import csv
import re
import codecs
import random
import bs4
from time import sleep

datpath = 'joyokanji.dat'

sleep(1)
resp = web.get('https://ja.wikipedia.org/wiki/%E5%B8%B8%E7%94%A8%E6%BC%A2%E5%AD%97%E4%B8%80%E8%A6%A7')
#resp = web.get('http://www.1-em.net/sampo/sisyogokyo/gokyo/syokyo/syokyo2.htm')
resp.raise_for_status()
soup = bs4.BeautifulSoup(resp.content, "html.parser")
link_elem01 = soup.find_all("a",class_="extiw")

text = str(link_elem01)
#text2 = text[34:46]
#text = text.replace('、','')
#text = text.replace('。','')
#text = text.replace('△','')
#text = text.replace('◯','')
#text = text.replace('○','')
#text = text.replace('･','')
#text = text.replace('\n','')
#text = text.replace('■','')
#text = text.replace('（','')
#text = text.replace('）','')
#text = text.replace(' ','')
#text = text.replace('.','')
#text = text.replace('[','')
#text = text.replace(']','')

#text = re.sub('size="2">*</font>','',text)
text = re.sub('[あ-んア-ン]','',text)
text = re.sub('[a-zA-Z0-9]','',text)
text = re.sub('[\[,ー,\],\',\.,&,;,‘,’,→,【,】,｢,｣,“,；,”,！,\，,〜,\?,：,\\,．,・,•,＜,＞,　,『,』,\+,\*,!,(,),_,「,」,_,%,《,》,:,\-,［,］,<,/,>,#,=,",\ ]','',text)

print("{0} \n".format(text))
with open(datpath, mode='a') as f:
    f.write('\n{0}'.format(text))
