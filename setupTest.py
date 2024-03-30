#BigData project 1
#/usr/local/bin/python3 -m pip install pymongo
#interpreter bottom right in VS code, some libraries can be installed in one interpreter but not another

#can test if you are being connected to the database by using the following code

import pymongo
from urllib.parse import quote_plus

username = quote_plus("dprincipale")#change this y1our username
password = quote_plus("noHVUHjCW9iUKmSE")#change this to your password
cluster = "cluster0.hnstfom"

uri = f"mongodb+srv://{username}:{password}@{cluster}.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = pymongo.MongoClient(uri)

db = client["sample_mflix"]
collection = db["comments"]

for document in collection.find():
    print(document)


#should print all the sample data in the comments collection
