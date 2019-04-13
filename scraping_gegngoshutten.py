import requests as web
import csv
import re
import codecs
import random
import bs4
from time import sleep

datpath = 'gengo_shutten.dat'

#def get_tables(content, is_talkative=True):
#  bs = bs4.BeautifulSoup(content, "lxml")
#  tables = bs.find_all("table")
#  return tables
#
#def parse_table(table):
#  thead = table.find("thead")
#
#  if thead:
#    tr = thead.find("tr")
#    ths = tr.find_all("th")
#    columns = [th.text for th in ths]
#  else:
#    columns = []
#
#  tbody = table.find("tbody")
#  trs = tbody.find("tr")
#  rows = [columns]
#
#  for tr in trs:
#    row = [td.text for td in tr.find_all(["td", "th"])]
#    rows.append(row)
#
#  return rows

sleep(1)
resp = web.get('https://anond.hatelabo.jp/20180819134409')
#resp = web.get('http://www.1-em.net/sampo/sisyogokyo/gokyo/syokyo/syokyo2.htm')
resp.raise_for_status()
soup = bs4.BeautifulSoup(resp.content, "html.parser")
link_elem01 = soup.find_all("a", class_="keyword")
#tables = get_tables(resp.text)
#table = tables[0]
#rows = parse_table(table)

#print(rows)
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
text = re.sub('[あ-んア-ン]','',text)
text = re.sub('[a-zA-Z0-9]','',text)
text = re.sub('[&,;,‘,’,→,【,】,｢,｣,“,；,”,！,\，,〜,\?,：,\\,．,・,•,＜,＞,　,\+,\*,!,(,),_,「,」,_,%,《,》,:,\-,［,］,<,/,>,#,=,",\ ]','',text)

print("{0} \n".format(text))
with open(datpath, mode='a') as f:
    f.write('\n{0}'.format(text))
