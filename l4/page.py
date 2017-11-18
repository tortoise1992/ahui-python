# 分页
class Foo:
    def __init__(self):
        pass

    def __str__(self):
        return 'ahui'
    def __call__(self, *args, **kwargs):
        return '123'
ahui=Foo()
print(ahui())
print(ahui)