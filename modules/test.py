import logging

import sys
import os
def ask():
    logging.logger()

ask()

print(sys.path)


paths=os.path.abspath(os.path.dirname(__file__))
p=os.path.join(paths,'index.html')
print(p)