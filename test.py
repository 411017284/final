import requests
from bs4 import BeautifulSoup
url = "https://twcoupon.com/bmenu-%E6%A8%82%E6%B3%95%E5%B0%8F%E8%88%96-menu%E8%8F%9C%E5%96%AE%E5%83%B9%E6%A0%BC.html"
Data = requests.get(url)
Data.encoding = "utf-8"
sp = BeautifulSoup(Data.text, "html.parser")
result=sp.select(".wrapper")
info = ""
for item in result:
    name = item.find("div").text
    #drinks = item.find("p")
    #price = item.select("em")
    info += name + "\n" #+ drinks + "\n" + price + "\n\n"
print(info)
