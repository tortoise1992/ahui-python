import shelve

f=shelve.open(r'shelve_text')
data=f.get('info')
print(data)