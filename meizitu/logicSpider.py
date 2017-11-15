# -*- coding=UTF-8 -*-
from pyquery import PyQuery as pq
import requests
import time
import json
import os
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36'
}
url = 'http://www.mzitu.com/26685'
res=requests.get(url,headers=headers).text
print(res)