from selenium import webdriver
from pyquery import PyQuery as pq
browser=webdriver.PhantomJS()
browser.get('http://www.baidu.com')

# print(browser.page_source)
# btn=browser.find_element_by_id('su')
# btn.click()

lis=browser.find_elements_by_css_selector('a')


print(lis)
browser.close()