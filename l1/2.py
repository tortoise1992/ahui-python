import time
def test(flag=''):
    def log(f):
        def wrapper(*args,**kwargs):
            print('logging...')
            f(*args,**kwargs)
            if flag == 'true':
                times()
        return wrapper
    return log
def times():
    print('time %s' % time.time())
# print(@test())
@test('true')
def add(*args,**kwargs):
    count=0
    for i in args:
        count +=i
    print(count)

add(20,30,40,100)
