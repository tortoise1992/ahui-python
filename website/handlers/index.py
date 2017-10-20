import tornado.web
import website.methods.readdb as mrd
class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        user_person=mrd.select_cols(table="user",col="*")
        print(user_person)
        self.render('index.html',user=user_person[0][0])

    def post(self, *args, **kwargs):
        username=self.get_argument('username')
        password=self.get_argument('password')
        # self.write({"code":200,"msg":"success"})
        user_info=mrd.select_table(col="*",table="user",condition="username",value=username)
        # print(user_info)
        if user_info:
            print(111)
            db_pwd=user_info[0][1]
            if db_pwd == password:
                self.write('welcome')
            else:
                self.write('password is wrong')
        else:
            mrd.insert_table(table="user", username=username, password=password)

