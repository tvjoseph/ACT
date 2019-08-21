import pymongo

client = pymongo.MongoClient("mongodb://ssethu:Gyt*R3^h@10.235.220.241:24017/alignment") # defaults to port 27017

db = client['alignment']

# print the number of documents in a collection
#print db.cool_collection.count()
print(db.list_collection_names())

article = {"author": "Derrick Mwiti",
            "about": "Introduction to MongoDB and Python",
            "tags":
                ["mongodb", "python", "pymongo"]}
#articles = db.articles
#result = articles.insert_one(article)
print(db.list_collection_names())
collection = db['reviews2']
#print(check)
cursor = collection.find({})
#print(len(cursor))
for document in cursor:
      print(document)

   

	
       
