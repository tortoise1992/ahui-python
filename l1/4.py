
def readFile(path):
    with open(path, 'a+') as f:
        # print(f.read())
        f.write('hello world')
        # print(f.read())
readFile('login.txt')


