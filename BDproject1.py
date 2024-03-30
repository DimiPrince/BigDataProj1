import pymongo

uri = "mongodb+srv://<dprincipale>:<noHVUHjCW9iUKmSE>@cluster0.hnstfom.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = pymongo.MongoClient(uri)

db = client["sample_mflix"]
collection = db["comments"]

for document in collection.find():
    print(document)