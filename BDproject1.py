import pymongo
import json
from urllib.parse import quote_plus

username = quote_plus("dprincipale")
password = quote_plus("noHVUHjCW9iUKmSE")
cluster = "cluster0.hnstfom"

uri = f"mongodb+srv://{username}:{password}@{cluster}.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = pymongo.MongoClient(uri)

#mongoimport --uri mongodb+srv://<username>:<password>@cluster0.hnstfom.mongodb.net/<dbname> --collection <collectionname> --type json --file <yourfile.json>
#not working so going to just use regular file stream   

# Use the 'BigData' database
db = client["BigData"]

# Load the JSON data

data = []
with open('city_inspections.json') as f:
    for line in f:
        document = json.loads(line)
        # Replace the '_id' field with the value of the '$oid' field
        document['_id'] = document['_id']['$oid']
        data.append(document)

# Insert the data into the 'city_inspections' collection
db.city_inspections.insert_many(data)