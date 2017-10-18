import shelve

f=shelve.open(r'test')
f['info']=[{'name':'ahui','age':'25'},{'name':'ahui','age':'26'},{'name':'ahui','age':'27'}]

f.close()
