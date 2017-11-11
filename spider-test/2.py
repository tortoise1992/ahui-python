import urllib.request
import urllib.parse
# str=urllib.request.urlopen("http://www.baidu.com")
# print(str.read().decode('utf-8'))
data=bytes(urllib.parse.urlencode({"hello":"world"}),encoding='utf8')
print(data)
response=urllib.request.urlopen("http://httpbin.org/post",data=data)
print(response.read().decode('utf-8'))