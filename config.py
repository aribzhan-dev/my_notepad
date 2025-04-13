from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client['notepad_db']
collection = db['notes']
