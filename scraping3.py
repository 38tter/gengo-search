import requests as web
import bs4
import csv
import re
import codecs
from time import sleep
import random

#list = codecs.open('saishu_kumiawase2.dat', 'r', 'utf-8')
list = codecs.open('saishu_kouho.txt', 'r', 'utf-8')
datpath = 'saishu_kekka3.dat'

for word in list:
     word = word.replace('\n','')
     gengo = "\"" + word + "\""
     #gengo = gengo + " -site:b-name.jp -site:enamame.net -site:www.weiqiming.com -site:name.sijisuru.com -site:www.meiwen.org"
     #gengo = gengo + " -site:b-name.jp -site:www.meiwen.org"
     sleep(1)
     #resp = web.get('https://www.google.co.jp/search?hl=ja&lr=lang_ja&num=100000&q=' + ' '.join(gengo))
     resp = web.get('https://www.google.co.jp/search?hl=ja&start=10&num=1&q=' + ' '.join(gengo))
     #resp = web.get('https://www.google.com/search?as_q=' + ' '.join(gengo) + '&num=100&hl=ja&ie=UTF-8&oe=UTF-8&btnG=Google+検索&as_epq=&as_oq=&as_eq=&lr=lang_ja&as_ft=i&as_filetype=&as_qdr=all&as_occt=any&as_dt=i&as_sitesearch=')
     resp.raise_for_status()
     
     soup = bs4.BeautifulSoup(resp.text, "html.parser")
     #link_elem01 = soup.find_all(id='resultStats')
     link_elem01 = soup.find_all(id="resultStats")
     
     text = str(link_elem01)
     text2 = text[24:50]
     text2 = text2.replace(',','')
     print(text2)
     text3 = re.search(r"\s[0-9]*\s",text2)
     
     if text3:
         print("{0},{1}".format(gengo, text3.group(0)))
         with open(datpath, mode='a') as f:
             f.write('\n{0} {1}'.format(gengo, text3.group(0)))
