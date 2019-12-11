# import the library  
import urllib.request
from bs4 import BeautifulSoup  
#我們定義一個變量 (quote_page) 並賦值為網站的網址鏈接。
# 賦值網站鏈接
quote_page = 'https://www.bloomberg.com/quote/SPX:IND' 
# 利用 Python 的 urllib2 庫獲取方才定義的網址 quote_page 的 HTML 網頁信息
# 檢索網站並獲取 html 代碼，存入變量”page”中 
page = urllib.request.urlopen(quote_page) 
# 我們把網頁解析為 BeautifulSoup 格式，以便我們用 BeautifulSoup 庫來分析網頁。
# 用 beautifulSoup 解析 HTML 代碼並存入變量“soup”中` 
soup = BeautifulSoup(page,'html.parser')
# In beautifulsoap library the find() function can help us fetch different specific content
name_box = soup.find('h1', attrs={'class':'name'})
# 在我們得到標籤之後，我們可以用 name_box 的 text 屬性獲取相應值
name = name_box.text.strip()
print (name)
# strip() 函數用於去除前後空格
price_box = soup.find('div',attrs={'class':'price'})
price = price_box.text
print (price) 


# import Beautiful Soup Module 
from bs4 import BeautifulSoup 
#original HTML code 
html_doc = """ 
<html><head><title>Hello World</title></head>
<body><h2>Test Header</h2>
<p>This is a test.</p>
<a id="link1" href="/my_link1">Link 1</a>
<a id="link2" href="/my_link2">Link 2</a>
<p>Hello, <b class="boldtext">Bold Text</b></p>
</body></html>
""" 
# using Beautiful Soup parse the HTML code 
soup = BeautifulSoup(html_doc, 'html.parser')
# output the 排版後的 HTML 程式碼
print(soup.prettify())
#print the title tag 
title_tag = soup.title
print(title_tag)
print(title_tag.string) #just print the word in title not include the tag 


"""
Created on Wed Dec 11 23:43:50 2019

@author: Anna
"""

import requests
import bs4
from bs4 import BeautifulSoup

url = 'https://www.animal.com.tw/pages/BlueBuffalo%E8%97%8D%E9%A5%8C%E7%8B%97%E9%A3%BC%E6%96%99'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36','Connection': 'close'}
requests.adapters.DEFAULT_RETRIES = 5
webcontent = requests.get(url,headers=headers)
webcontent.encoding = 'UTF-8'
soup = BeautifulSoup(webcontent.text,'html.parser')
for i in soup.select('.meepshop-meep-ui__sidebar-index__root'):
    print(i.prettify())
    print('\n')
 
# import the library  
import urllib.request
from bs4 import BeautifulSoup  
#我們定義一個變量 (quote_page) 並賦值為網站的網址鏈接。
# 賦值網站鏈接
user_agent = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36','Connection': 'close'}
headers = {'User-Agent': user_agent}
quote_page = 'https://www.bloomberg.com/quote/SPX:IND' 
# 利用 Python 的 urllib2 庫獲取方才定義的網址 quote_page 的 HTML 網頁信息
# 檢索網站並獲取 html 代碼，存入變量”page”中 
page = urllib.request.urlopen(quote_page,headers=headers) 
# 我們把網頁解析為 BeautifulSoup 格式，以便我們用 BeautifulSoup 庫來分析網頁。
# 用 beautifulSoup 解析 HTML 代碼並存入變量“soup”中` 
soup = BeautifulSoup(page,'html.parser')
print(soup)

name_box = soup.find('h1', attrs={'class':'name'})
# 在我們得到標籤之後，我們可以用 name_box 的 text 屬性獲取相應值
name = str(name_box).strip()
print (name)
# strip() 函數用於去除前後空格
price_box = soup.find('div',attrs={'class':'price'})
price = price_box.text
print (price) 
