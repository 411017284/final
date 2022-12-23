import requests
from bs4 import BeautifulSoup

import firebase_admin
from firebase_admin import credentials, firestore
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

url = "https://twcoupon.com/bmenu-%E6%A8%82%E6%B3%95%E5%B0%8F%E8%88%96-menu%E8%8F%9C%E5%96%AE%E5%83%B9%E6%A0%BC.html"
Data = requests.get(url)
Data.encoding = "utf-8"
sp = BeautifulSoup(Data.text, "html.parser")
result=sp.select(".store_menu ul")
#info = ""
info = ""
for item in result:
    name = item.find("div").text
    drinks = item.select("li")
    detail = ""
    for d in drinks:
      detail+=d.find("p").text + ":"
      for p in d.select("em"):
        detail += p.text + ";"
      detail += "\n"
    #info += name + "\n" + detail + "\n"
#print(info)
    docs = [
    {
    "name": name,
    "detail": detail,
    }
    ]
    collection_ref = db.collection("drink")
    for doc in docs:
      collection_ref.add(doc)




