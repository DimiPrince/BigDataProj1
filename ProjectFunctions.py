#functions needed for the project

import pymongo
import certifi
from urllib.parse import quote_plus

username = quote_plus("dprincipale")#change this y1our username
password = quote_plus("noHVUHjCW9iUKmSE")#change this to your password
cluster = "cluster0.hnstfom"

uri = f"mongodb+srv://{username}:{password}@{cluster}.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = pymongo.MongoClient(uri, tlsCAFile=certifi.where())
'''have to add second parameter of certificate, kept failing to establish connection without it
connection without it , "pip install certifi" in directory where your
python  is installed'''

db = client["BigData"]
collection = db["city_inspections"]

def check_business_violation():
    business_name = input("Enter a business name: ")
    document = collection.find_one({"business_name": business_name})
    if document is not None:
        if document['result'] == "No Violation Issued":
            print(f"The business '{business_name}' has no violations.")
        else:
            print(f"The business '{business_name}' has a violation.")
    else:
        print("Business Not found.")
