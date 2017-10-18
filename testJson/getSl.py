import shelve

# f=shelve.open(r'shelve_text')
# data=f.get('info')
# print(data)


f=shelve.open('test')
data=f.get('info')
for x in data:
    print(x)
