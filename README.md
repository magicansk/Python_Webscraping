# Python WebScraping

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

## Before start:
Understanding the following:
 - HTML 
## Setting up the environment: 

Download from [Python](https://www.python.org/downloads/):

- Python version 3.8.0
- Pip version 19.3.1

### In command line:
Install beautifulsoap:
```cmd
python -m pip install --upgrade pip
pip3 install beautifulsoup4
```

## What is beautifulsoap?
[Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/) 是一個 Python 的函式庫模組，可以讓開發者僅須撰寫非常少量的程式碼，就可以快速解析網頁 HTML 碼，從中翠取出使用者有興趣的資料、去蕪存菁，降低網路爬蟲程式的開發門檻、加快程式撰寫速度。
- [Beautifulsoap Doc](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
### Beautifulsoap usage
Beautiful Soup 的運作方式就是讀取 HTML 原始碼，自動進行解析並產生一個 `BeautifulSoup` 物件，此物件中包含了整個 HTML 文件的結構樹，有了這個結構樹之後，就可以輕鬆找出任何有興趣的資料了。

以下是一個簡單的小程式，示範如何使用 Beautiful Soup 模組解析原始的 HTML 程式碼：


-------- 
#### Error: 
If you install in python interpreter:
```python 
>>> pip install selenium
              ^
SyntaxError: invalid syntax
```
pip is run from the command line, not the Python interpreter. It is a program that installs modules, so you can use them from Python. Once you have installed the module, then you can open the Python shell and do import BeautifulSoap4.
#### References: 
- [附範例與完整程式碼！手把手帶著你用 Python 做出爬蟲、抓取網頁資料](https://buzzorange.com/techorange/2017/08/04/python-scraping/)
- [Python 的 Beautiful Soup](https://blog.gtwang.org/programming/python-beautiful-soup-module-scrape-web-pages-tutorial/)
- [web scrapping tool](https://www.scraperapi.com/blog/the-10-best-web-scraping-tools) 
- [Web scraping with python](https://www.edureka.co/blog/web-scraping-with-python/)
- [Beautiful Soup: Build a Web Scraper With Python](https://realpython.com/beautiful-soup-web-scraper-python/)

error: 
- [Python3.X出现AttributeError: module 'urllib' has no attribute 'urlopen'错误](https://blog.csdn.net/john_bian/article/details/68059250)
- [python 3.3.2报错：No module named 'urllib2' 解决方法](https://blog.csdn.net/hacker_Lees/article/details/77866338) 
- [AttributeError: 'NoneType' object has no attribute 'text' - Python , BeautifulSoup Error](https://stackoverflow.com/questions/41318740/attributeerror-nonetype-object-has-no-attribute-text-python-beautifulso)
