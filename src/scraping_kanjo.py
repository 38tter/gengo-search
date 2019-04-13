import requests as web
import csv
import re
import codecs
import random
import bs4
from time import sleep
from sys import argv

datpath = 'gokanjo.dat'

sleep(1)
resp = web.get(str(argv[1]))
resp.raise_for_status()
soup = bs4.BeautifulSoup(resp.content, "html.parser")
link_elem01 = soup.find_all('td', class_='ctext')

text = str(link_elem01)
#text2 = text[34:46]
text = text.replace('、','')
text = text.replace('。','')
text = text.replace('△','')
text = text.replace('◯','')
text = text.replace('○','')
text = text.replace('･','')
text = text.replace('\n','')
text = text.replace('■','')
text = text.replace('（','')
text = text.replace('）','')
text = text.replace(' ','')
text = text.replace('.','')
text = text.replace('[','')
text = text.replace(']','')

#text = re.sub('size="2">[\u4E00-\u9FD0]*</font>','',text)
#text = re.sub('[あ-んア-ン]','',text)
text = re.sub('[a-zA-Z0-9]','',text)
text = re.sub('[&,;,‘,’,→,【,】,｢,｣,“,；,”,！,\，,〜,\?,：,\\,．,・,•,＜,＞,　,『,』,\+,\*,!,(,),_,「,」,_,%,《,》,:,\-,［,］,<,/,>,#,=,",\ ]','',text)

print("{0} \n".format(text))
with open(datpath, mode='a') as f:
    f.write('\n{0}'.format(text))
