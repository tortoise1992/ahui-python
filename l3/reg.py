import re
# s='hello worldwhlwfl'
# set=re.findall('w.l',s)
# print(set)

# s='ahuiisaaneg'
# # ss=re.match(r'b',s)
# ss=re.search(r'a',s)
# # print(ss.group())
# # print(ss.group())
# print(ss.group())

inputs='1+(30*20+(5/10-3*2)*10-20*(5-10/5))'

set=re.findall('\([^()]+\)',inputs)
print(set)
for i in set:
    str=eval(i)

# sss=re.sub('\([^()]+\)',str(eval(set.group())),inputs)
# print(sss)
# print(eval(set.group()))


print(inputs.replace('\([^()]\)','aaa',2))

a=[ x*x for x in range(10)]
print(a)


