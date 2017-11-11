# douban

import requests
import re

response=requests.get('https://book.douban.com/').text
pattern=re.compile('li.*?cover.*?href="(.*?)".*?alt="(.*?)".*?"author">(.*?)</p>',re.S)

result=re.findall(pattern,response)
for v in result:
    link,name,author = v
    name=re.sub('\s*','',name)
    author=re.sub('\s*','',author)
    print(name,'----',author,'----',link)