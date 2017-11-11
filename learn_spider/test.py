import requests
from pyquery import PyQuery as pq
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
}
baseUrl='http://list.youku.com/category/show/c_97_s_1_d_1_g_%E5%8F%A4%E8%A3%85.html?spm=a2htv.20009910.m_86809.5~5~5!2~1~3~A'
response=requests.get(baseUrl,headers=headers).text
doc=pq(response)
items=doc('.yk-pack')
for i in items.items():
    print(i.find('a').attr('title'))
# print(doc('.yk-pack'))