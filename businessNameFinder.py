#BigData project 1
#/usr/local/bin/python3 -m pip install pymongo
#interpreter bottom right in VS code, some libraries can be installed in one interpreter but not another

#can test if you are being connected to the database by using the following code

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

#use "ATLIXCO DELI GROCERY INC." as a test business name
def BusinessFinder():
    business_name = input("Enter a business name: ")
    document = collection.find_one({"business_name": business_name})
    if document is not None:
        print(f"Business found: {document}")
    else:
        print("No business found with that name.")

BusinessFinder()

#should prompt user then print business if document exist
