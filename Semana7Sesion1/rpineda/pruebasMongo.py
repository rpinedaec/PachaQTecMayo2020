import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["admin"]
mycol = mydb["sedes"]
mydoc = mycol.find().sort("Codigo",-1).limit(5)
for x in mydoc:
  print(x)