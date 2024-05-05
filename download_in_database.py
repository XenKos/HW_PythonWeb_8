import pymongo
import json


client = pymongo.MongoClient("mongodb+srv://XenKos:<kseni4ka78>@cluster0.02433gx.mongodb.net/")
db = client["XenKos"] 
collection = db["authors"]  

with open('C:/Users/Денег на комп нету/OneDrive/Робочий стіл/HW_PythonWeb_8/authors.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    collection.insert_many(data)


collection = db["quotes"]  

with open('C:/Users/Денег на комп нету/OneDrive/Робочий стіл/HW_PythonWeb_8/quotes.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    collection.insert_many(data)