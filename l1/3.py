# login
# print(user)
pages=['home','about','list','finance']
login_status=False


def login(auth_type='jd'):

    def wrapper(f):
        def inner():
            global login_status
            if not login_status:
                print('please login...')
                if auth_type == 'jd':
                    ff = open('login.txt', 'r')
                    user = eval(ff.readline())
                    # print(user)
                    name=input('input your name:')
                    pwd=input('input your pwd:')
                    if name == user['name'] and pwd == user['pwd']:
                        f()
                        login_status=True
                    else:
                        print('name or pwd is wrong')
                elif auth_type == 'wx':
                    print('wx')
                elif auth_type == 'github':
                    print('github')
            else:
                f()
        return inner
    return wrapper

@login()
def indexs():
    print('welcome to home page')

@login()
def abouts():
    print('welcome to about page')

@login()
def lists():
    print('welcome to list page')

@login()
def finance():
    print('welcome to finance page')

while True:
    print('------welcome to our site-------')
    for i,v in enumerate(pages):
        print(i,'---',v)
    while True:
        page=input('select a page:')
        if page.isdigit() and int(page)<=len(pages)-1 :
            page=int(page)
            if page == 0:
                indexs()
            elif page == 1:
                abouts()
            elif page == 2:
                lists()
            else:
                finance()