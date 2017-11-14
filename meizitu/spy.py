# -*- coding=UTF-8 -*-
from pyquery import PyQuery as pq
import requests
import time
import json
page=1
baseUrl='http://www.mzitu.com/page/'
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36'
}
urls=[]
def get_all_link(url,max):
    global page
    url = url + str(page)
    print('正在抓取第',page,'页')
    res = requests.get(url, headers=headers)
    res.encoding = "utf-8"
    doc=pq(res.text)
    temps=[]
    meizi = doc('#pins li a img')
    for i in meizi.items():
        urls.append({
            'title': i.attr('alt'),
            'link': i.parent().attr('href')
        })
        temps.append({
            'title': i.attr('alt'),
            'link': i.parent().attr('href')
        })
    print(temps)
    print('第',page,'页抓取完毕')
    page +=1
    if page <=max:
        time.sleep(0.5)
        get_all_link(baseUrl,100)
    else:
        print(max,'页数据抓取完毕!')

def write_in_file(data):
    data={
        'data':str(data)
    }
    with open('./meizitu.json','a',encoding='utf-8') as f:
        f.write(json.dumps(data))

# get_all_link(baseUrl,100)
# write_in_file(urls)

write_in_file(['周'])