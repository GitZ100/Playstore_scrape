from google_play_scraper import app
from flask_pymongo import pymongo
from bs4 import BeautifulSoup
import requests
import os

MONGO_USERNAME = os.environ['MONGO_USERNAME']
MONGO_PASS = os.environ['MONGO_PASS']
client = pymongo.MongoClient(f"mongodb+srv://{MONGO_USERNAME}:{MONGO_PASS}@megamind.v6m4xku.mongodb.net/?retryWrites=true&w=majority")
db = client.get_database("megamind")
user_collection = pymongo.collection.Collection(db, 'user_collection')

URL = "https://play.google.com/store/games?hl=en&gl=US&pli=1"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
job_elements = soup.find_all("a", class_="Si6A0c Gy4nib")
appinfolst = []

print("Scraping Packages")
for result in job_elements:
    # print(result['href'][23:], end="\n" * 2)
    # print(type(result['href']))
    appinfo = app(result['href'][23:], lang= 'en', country='us')
    appinfolst.append(appinfo)
    
db.collection.insert_many(appinfolst)