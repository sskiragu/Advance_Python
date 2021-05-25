import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017")
mydb = myclient["hr"] #Creating the database

mycol = mydb["details"] #Creating a collection

mydict = [
{"name" : "Sam", "county": "Nairobi"},
{"name" : "John", "county": "Mombasa"}
]

##Insert
# mycol.insert_one(mydict)
# mycol.insert_many(mydict)

##Find
# myrec = mycol.find_one()
# print(myrec)

# myresults = mycol.find()
# for myres in myresults:
# 	print(myres)

##Query specific record
# myquery = {"name":"Sam"}
# myresults = mycol.find(myquery)

# for myres in myresults:
# 	print(myres)

##Update
# myquery = {"name": "John"}
# newvalues = {"$set":{"name":"Peter"}}
# mycol.update_one(myquery,newvalues)

# myquery = {"county": "Nairobi"}
# newvalues = {"$set":{"county":"Kisumu"}}
# mycol.update_many(myquery,newvalues)

##Delete
# myquery = {"name":"Peter"}
# mycol.delete_one(myquery)

myquery = {"name":"Sam"}
mycol.delete_many(myquery)
