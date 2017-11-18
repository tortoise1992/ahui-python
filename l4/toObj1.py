class Person:
    def __init__(self,name):
        self.name=name

    @property
    def peer(self):
        return 1
    @peer.setter
    def peer(self,val):
        print(val)
    @peer.deleter
    def peer(self):
        print(self)

# p=Person('ahui')
# print(p.peer)
#
# p.peer=123
# # print(p.peer)
#
# del p.peer