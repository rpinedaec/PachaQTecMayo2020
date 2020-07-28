import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

my_db = myclient["admin"]

colec = my_db["mi primera coleccion"]

for x in colec.find():
    print(x) 

