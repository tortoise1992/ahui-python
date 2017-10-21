import urllib.request
import urllib.parse

page=1
url="http://www.qiushibaike.com/hot/page/"+str(page)
user_agent="Mozilla/5.0 (iPad; CPU OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1"
headers={"User-Agent":user_agent}
try:
    req=urllib.request.Request(url=url,headers=headers)
    response=urllib.request.urlopen(req)
    print(response.read().decode('utf8'))
except:
    print('error')