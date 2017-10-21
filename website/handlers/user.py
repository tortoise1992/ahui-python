import tornado.web
import website.methods.readdb as mrd
class UserHandler(tornado.web.RequestHandler):
    def get(self):
        username = self.get_argument("user")
        user_info = mrd.select_table(col="*",table="user",  condition="username", value=username)
        self.render("user.html", users=user_info)