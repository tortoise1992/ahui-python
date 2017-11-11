from bs4 import BeautifulSoup
html = """
<html>
    <head>
        <title>The Dormouse's story</title>
    </head>
    <body>
        <p class="story">
            Once upon a time there were three little sisters; and their names were
            <a href="http://example.com/elsie" class="sister" id="link1">
                <span>Elsie</span>
            </a>
            <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
            and
            <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
            and they lived at the bottom of a well.
        </p>
        <p class="story">...</p>
"""

soup=BeautifulSoup(html,'lxml')

# print(soup.p.children)
# for k,v in enumerate(soup.p.children):
#     print(k)
#     print(v)

# print(soup.find_all(attrs={'id':"link2"}))

# print(soup.select('a'))
dom=soup.select('a')
for i in dom:
    print(i.get_text())