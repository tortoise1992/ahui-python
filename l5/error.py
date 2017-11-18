try:
    # i=int('aaa')
    raise Exception('你出错了！！')
except Exception as e:
    print(e)
    i=1

print(i)