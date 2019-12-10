# step 0 install the modules by pip
import requests
from bs4 import BeautifulSoup
url = "https://www.amazon.in/"
# step 1 get the HTML
r = requests.get(url)
htmlContent = r.content
# print(htmlContent)
# step2 Parse the HTML with beautiful soup
soup = BeautifulSoup(htmlContent,'html.parser')
# print(soup.prettify)
# step 3 html tree traversal
# get the title of html page
title = soup.title
# print(title)
# type of object 
# 1.tag
# 2 navigable string
# 3 beautifulsoup
# 4 comment
# get all the paragraph from page
paras = soup.find_all('p')
print(paras)
# get all the anchor tags
anchors = soup.find_all('a')
# print(anchors)
# get first element in html page
print(soup.find('p')) 
# get classes of any element
print(soup('p')['class'])

# find all the element with class lead
print(soup.find_all('p',class_='lead'))
# get the text from tags
print(soup.find('p').get_text())
