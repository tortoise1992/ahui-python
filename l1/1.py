# classMates=['ahui','xiaozhang','shanshan']
# print(len(classMates))
# classMates.append('admn')
# # classMates.pop()
# classMates.insert(1,'周青会')
# classMates.pop(0)
# print(classMates)

# def add():
# #
# return 'hello'
# import copy
# a=[1,'ahui',[1,2]]
# b=copy.deepcopy(a)
# b[2][1]='test'
# print(a)

# def print_info(name,age,sex='male'):
#     print('hello %s,you are %d years old,%s' % (name,age,sex))
#
#
# # print_info('ahui',25)
#
# def test(*args):
#     count=0
#     for x in args:
#         count +=x
#
#     print(count)
#
# test(1,2,3,4,6)

# bibao
# def func(x):
#
#     def add():
#         return x
#     return add
# print(func(20)())


import time
def countTime(f):
    def inner():
        start=time.time()
        f()
        end=time.time()
        a=end-start
        print('time is %s' % a)
    return inner


@countTime
def fol():
    print('fol')
    time.sleep(2)


# fol=countTime(fol)
# fol()

fol()