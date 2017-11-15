# -*- coding=UTF-8 -*-
from pyquery import PyQuery as pq
import requests
import time
import json
import os
class MeiziSpider():
    def __init__(self):
        self.headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36',
            'Host': 'www.mzitu.com',
            'Referer':'http://www.mzitu.com'

        }
        self.page=1
        self.baseUrl='http://www.mzitu.com/page/'
        self.dir='\images'

    def get_page(self,url):
        response=requests.get(url,headers=self.headers)
        response.encoding = "utf-8"
        return response.text

    def get_html(self,res):
        return pq(res)

    def get_enters(self):
        urls=[]
        url=self.baseUrl+str(self.page)
        page=self.get_page(url)
        html=self.get_html(page)
        for i in html('#pins li a img').items():
            urls.append({
                'title': i.attr('alt'),
                'link': i.parent().attr('href')
            })
        return urls

    def make_dir(self,name):
        path=os.path.abspath(os.path.dirname(__file__))+self.dir+'\\'+name
        # print(path)
        isExist=os.path.exists(path)
        if not isExist :
            #makedirs可以创建父级目录
            os.makedirs(path)

    def saveImg(self,name,path,refer):
        #反盗链
        img=requests.get(path,headers={
            'Referer': refer
        }).content
        # print(path)
        with open(os.path.abspath(os.path.dirname(__file__))+self.dir+'\\'+name+'\\'+name+'.jpg','wb') as f:
            f.write(img)

    def get_detail_page(self):
        urls=self.get_enters()
        for i in urls:
            url=i['link']
            detail_page=self.get_page(url)
            detail_html=self.get_html(detail_page)
            img_path=detail_html('.main-image').find('img').attr('src')
            next_img=detail_html('.main-image').find('a').attr('href')
            # print(img_path)
            self.make_dir(i['title'][:5].strip())
            self.saveImg(i['title'][:5].strip(),img_path,url)

spider=MeiziSpider()
# spider.make_dir('ahui')
# print(spider.get_enters())
spider.get_detail_page()