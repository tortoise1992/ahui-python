from urllib import request,parse,error
url='http://httpbin.org/get'
# headers={
#     "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
#     "Host":"httpbin.org"
# }
#
# dict={
#     "name":"ahui"
# }
#
# data=bytes(parse.urlencode(dict),encoding='utf-8')
# req=request.Request(url=url,data=data,headers=headers,method="POST")
# res=request.urlopen(req)
# print(res.read().decode('utf8'))


# proxy_handle=request.ProxyHandler({
#     'http': 'http://127.0.0.1:9743',
#     'https': 'https://127.0.0.1:9743'
# })
#
# opener=request.build_opener(proxy_handle)
# res=opener.open(url)
# print(res.read())

import requests