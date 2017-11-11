from urllib import request
from http import cookiejar

cookie=cookiejar.CookieJar()
handler=request.HTTPCookieProcessor(cookie)

opener=request.build_opener(handler)

opener.open('http://www.baidu.com')

for item in cookie:
    print(item.name)