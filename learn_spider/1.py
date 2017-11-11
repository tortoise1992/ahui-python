import requests

# response=requests.get('http://www.baidu.com')
# response.encoding='utf-8'
# print(type(response))
# print(response.status_code)
# print(response.text)
# print(response.cookies)
# print(response.content)
# print(response.content.decode('utf-8'))
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
}

# data={
#     'name':'ahui',
#     'age':26
# }
# response=requests.get('https://www.zhihu.com',headers=headers)

# response=requests.post('http://httpbin.org/post',data=data)
# print(response.text)
# print(response.json())

# files={
#     'files':open('text.txt',"rb")
# }
# response=requests.post('http://httpbin.org/post',files=files)
# print(response.text)

response=requests.get('http://www.baidu.com')
cookies=response.cookies
# print(type(cookies))
for i,v in cookies.items():
    print(i)
    print(v)