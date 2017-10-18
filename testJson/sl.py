import shelve

f=shelve.open(r'shelve_text.txt')
f['info']={'name':'ahui','age':'25'}

f.close()
