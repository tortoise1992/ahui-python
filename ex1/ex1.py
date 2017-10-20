# a=[1,2,3,4,5,6,7,8,9]
# b=a.pop(0)
# a.append(b)
# print(a)
#
#
# class Test:
#     @staticmethod
#     def add(x,y):
#         return x**y
#     @classmethod
#     def lose(cls):
#         print(cls.add)
#
# print(Test.add(2,4))
#
#
# Test.lose()


class Ahui:
    test='this is a text'
    def __init__(self):
        self.name='ahui'
        self.__pwd='123456'
        self.aaa='hello i am a test'
    def tell(self):
        print(self.name)
    def talk(self):
        print(self.__pwd)
    # get pwd self
    @property
    def pwd(self):
        return self.__pwd

a=Ahui()
# a.tell()
# print(a.pwd)
# print(a.__pwd)

print(Ahui.__dict__)
print(a.__dict__)
a.test='233333'
print(a.__dict__)
print(Ahui.__dict__)