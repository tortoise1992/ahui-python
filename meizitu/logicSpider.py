# -*- coding=UTF-8 -*-
from pyquery import PyQuery as pq
import requests
import time
import json
import os
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36'
}

url = 'http://www.mzitu.com/26685'
res=requests.get(url,headers=headers).text
doc=pq(res)
# print(doc)
span=doc('.pagenavi span')
length=int(span.eq(6).text())
title=doc('.main-image a img').attr('alt')

# print(span.eq(6).text())

for i in range(1,length+1):
    href=url+'/'+str(i)
    # print(href)
    headers={
        'Referer': url
    }
    data=requests.get(href,headers=headers).text
    html=pq(data)
    img_path = html('.main-image a img').attr('src')
    filename=img_path.split(r'/')[-1]
    data=requests.get(img_path,headers=headers).content

    if not os.path.exists(title.strip()):
        os.makedirs(title.strip())
    with open(title.strip()+'\\'+filename,'wb') as f:
        f.write(data)

