import json

dic={
    "name":"ahui",
    "age":25,
    "job":"webfe"
}
#
# f=open('./data.json','w')
# f.write(json.dumps(dic))
# print('success')

# f=open('./data.txt','r')
# str=f.read()
# data=json.loads(str)
# print(data['name'])

f=open('./data.json','a')
# data=json.load(f)
# print(data)
json.dump(dic,f)

