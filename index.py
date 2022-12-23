import requests
from bs4 import BeautifulSoup
import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

from flask import Flask, render_template, request, make_response, jsonify
from datetime import datetime, timezone, timedelta
app = Flask(__name__)

@app.route("/")
def index():
    homepage = "<h1>樂法</h1>"
    homepage += "<a href=/webhook>webhook</a><br>"
    return homepage
 
@app.route("/webhook", methods=["POST"])
def webhook():
    # build a request object
    req = request.get_json(force=True)
    # fetch queryResult from json
    action =  req.get("queryResult").get("action")
    #msg =  req.get("queryResult").get("queryText")
    #info = "動作：" + action + "； 查詢內容：" + msg
    if (action == "kindChoice"):
        kind =  req.get("queryResult").get("parameters").get("kind")
        info = "您想查詢的飲料是：" + kind + "，相關飲品:\n"
    
#if __name__ == "__main__":
#    app.run()
    collection_ref = db.collection("drink")
    docs = collection_ref.get()
    result = ""
    info = ""
    for doc in docs:
        dict = doc.to_dict()
        if fange in dict["name"]:
            result += "種類:" + dict["name"] + "\n"
            result += "品項:" + dict["detail"] + "\n"
    info += result + "\n"
    return make_response(jsonify({"fulfillmentText": info}))