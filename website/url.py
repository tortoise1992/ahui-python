
import sys

from website.handlers.index import IndexHandler
from website.handlers.user import UserHandler

# IndexHandler().test()
url=[
    (r'/',IndexHandler),
    (r"/user",UserHandler)
]