class Person():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def say(self):
        print('hello,%s'% self.name)

# ahui=Person('ahui',26)

class Common:
    def run(self):
        print('i am runing')

class Ani(Person,Common):
    def s1(self):
        print('s1')
    def s2(self):
        super(Ani,self).say()

# ahui.say()


a=Ani('ahui',20)
a.s2()
a.run()