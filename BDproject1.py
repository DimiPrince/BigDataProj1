import pymongo
from urllib.parse import quote_plus

username = quote_plus("dprincipale")
password = quote_plus("noHVUHjCW9iUKmSE")
cluster = "cluster0.hnstfom"

uri = f"mongodb+srv://{username}:{password}@{cluster}.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = pymongo.MongoClient(uri)

db = client["sample_mflix"]
collection = db["comments"]

for document in collection.find():
    print(document)