from bson.objectid import ObjectId
from config import MONGO_URL
import pymongo
from pymongo import MongoClient
from hall import *


cluster = MongoClient(MONGO_URL)
db = cluster["events"]
halls_colection = db["halls"]
contacts_colection = db["contacts"]

def save_hall(hall): #void func. get dict o sent. saving the email in sent table and deleting the mail from sending table.
    if type(hall) != dict:
        hall = hall.__dict__
    halls_colection.insert_one(hall)

def save_contact(contact): #void func. get dict o sent. saving the email in sent table and deleting the mail from sending table.
    contacts_colection.insert_one(contact)

def get_all_contacts():
    return contacts_colection.find({})

def get_hall_by_id(hall_id):
    hall = halls_colection.find_one({"_id":ObjectId(hall_id)})
    return hall

def get_all_halls():
    halls = halls_colection.find({})
    # halls_list = []
    # for hall in halls:
    #     halls_list.append(get_hall_from_dict(hall))
    return list(halls)

def get_halls_by_filter(filters):
    if filters.get("price"):
        filters["price"] = {"$lte" : filters["price"]}
    if filters.get("several_places"):
        filters["several_places"] = {"$gte" : filters["several_places"]}
    halls = halls_colection.find(filters)
    # halls_list = []
    # for hall in halls:
    #     halls_list.append(get_hall_from_dict(hall))
    return list(halls)

def delete_hall(title):
    halls_colection.delete_one({"title":title})

def delete_all_halls():
    halls_colection.delete_many({})


# hall = Hall("Shmomomo", "Jerusalem", "Hazofim 14", "vila", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcST6UHYRKveU7BsY131zPmPqETWEy-hNMaswg&usqp=CAU", "Tamar", "0556268895", "beutyull, and fjghd lkejlkwejf jairjksj jehruwaeh jkkahsudhs jgyhdjkhiuhikuhiuhi", 250, 5000)
# hall = Hall("tfofofo", "Tel aviv", "Alenbi", "vila", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRZ2tp6Nq7fECN9pKGR2PqvFfKtS49kmLx5Mw&usqp=CAU", "Tamar", "0556268895", "beutyull, and fjghd lkejlkwejf jairjksj jehruwaeh jkkahsudhs jgyhdjkhiuhikuhiuhi", 400, 20000)
# save_hall(hall)
# for i in get_all_halls():
#     print(i.__dict__)


# print(len(get_all_halls()))
# delete_hall("Hasharon")
# print(len(get_all_halls()))
# delete_all_halls()
# print(len(get_all_halls()))
# print(get_hall_by_id("5ffec6cfa2673a61f7064e81"))
# print(len(get_halls_by_filter({"city":"Jerusalem", "category":"vila", "price":100000})))

