from datetime import datetime
from flask import Flask, render_template, request, redirect
from bs4 import BeautifulSoup
import requests
from google_play_scraper import app
from flask_pymongo import pymongo
import os
from dotenv import load_dotenv

import os

# Load environment variables from the .env file
load_dotenv()

# Access the environment variables using the os module
USER = os.getenv('MONGO_USERNAME')
PASS = os.getenv('MONGO_PASS')

app1 = Flask(__name__)

client = pymongo.MongoClient(f"mongodb+srv://{USER}:{PASS}@megamind.v6m4xku.mongodb.net/?retryWrites=true&w=majority")
db = client.get_database("megamind")
user_collection = pymongo.collection.Collection(db, 'user_collection')
# megamind

@app1.route('/')
def index():
  appinfolst = db.collection.find({})
  print("___________________________________________________",appinfolst)
  return render_template('index.html', all_datas=appinfolst)

@app1.route('/details')
def details():
  return "details Page"
# @app1.route('/packages')
# def packages():
#   URL = "https://play.google.com/store/games?hl=en&gl=US&pli=1"
#   page = requests.get(URL)
#   soup = BeautifulSoup(page.content, "html.parser")
#   job_elements = soup.find_all("a", class_="Si6A0c Gy4nib")
#   appinfolst = []

#   for result in job_elements:
#     # print(result['href'][23:], end="\n" * 2)
#     # print(type(result['href']))
#     appinfo = app(result['href'][23:], lang= 'en', country='us')
#     appinfolst.append(appinfo)
#     print(appinfo, end='\n'*2)
#   db.collection.insert_many(appinfolst)
#     # 
#   return "soup.prettify()"


if __name__ == "__main__":
  with app1.app_context():
    # db.create_all()
    app1.run(debug=True, port=8001, host='0.0.0.0')
